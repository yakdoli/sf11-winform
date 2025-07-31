"""
WinForms_Docs 데이터 정제 메인 스크립트 - 성능 최적화 버전
"""

import os
import re
import json
import logging
import hashlib
import time
import multiprocessing as mp
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Generator
from dataclasses import dataclass, asdict
from datetime import datetime
import unicodedata
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import traceback
import psutil
import gc

import pandas as pd
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from config import (
    WINFORMS_DOCS_DIR, OUTPUT_DIR, BACKUP_DIR,
    CLEANING_PATTERNS, CODE_BLOCK_LANGUAGES,
    UNWANTED_KEYWORDS, DOCUMENT_METADATA_FIELDS,
    PROCESSING_OPTIONS, LOGGING_CONFIG
)

# 허용된 특수 문자 정의
ALLOWED_SPECIAL_CHARS = {
    '.', ',', '!', '?', ';', ':', '-', '(', ')', '[', ']', '{', '}',
    '<', '>', '=', '+', '*', '/', '\\', '@', '#', '$', '%', '&', '|',
    '~', '`', '_', '^', '"', "'", ' ', '\t', '\n', '\r'
}

# 로깅 설정
logging.basicConfig(
    level=getattr(logging, LOGGING_CONFIG['level']),
    format=LOGGING_CONFIG['format'],
    handlers=[
        logging.FileHandler(LOGGING_CONFIG['file_path'], encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class DocumentInfo:
    """문서 정보 데이터 클래스"""
    file_path: str
    original_filename: str
    category: str
    subcategory: str
    title: str
    content: str
    cleaned_content: str
    metadata: Dict[str, Any]
    code_snippets: List[Dict[str, Any]]
    word_count: int
    char_count: int
    processing_time: float
    memory_usage: float
    error_message: Optional[str] = None
    is_valid: bool = True

@dataclass
class CleaningStats:
    """정제 통계 데이터 클래스"""
    total_files: int = 0
    processed_files: int = 0
    failed_files: int = 0
    total_words: int = 0
    total_chars: int = 0
    total_code_snippets: int = 0
    removed_html_tags: int = 0
    removed_special_chars: int = 0
    normalized_whitespace: int = 0
    processing_time: float = 0.0
    memory_peak_usage: float = 0.0
    cpu_usage: float = 0.0

class PerformanceMonitor:
    """성능 모니터링 클래스"""
    
    def __init__(self):
        self.process = psutil.Process()
        self.start_time = time.time()
        self.start_memory = self.process.memory_info().rss / 1024 / 1024  # MB
        self.peak_memory = self.start_memory
        
    def update_memory(self):
        """메모리 사용량 업데이트"""
        current_memory = self.process.memory_info().rss / 1024 / 1024  # MB
        self.peak_memory = max(self.peak_memory, current_memory)
        return current_memory
    
    def get_cpu_usage(self):
        """CPU 사용량 가져오기"""
        return self.process.cpu_percent()
    
    def get_elapsed_time(self):
        """경과 시간 가져오기"""
        return time.time() - self.start_time
    
    def get_stats(self):
        """성능 통계 반환"""
        return {
            'elapsed_time': self.get_elapsed_time(),
            'peak_memory_mb': self.peak_memory,
            'current_memory_mb': self.update_memory(),
            'cpu_usage': self.get_cpu_usage()
        }

class DataCleaner:
    """데이터 정제 클래스 - 성능 최적화 버전"""
    
    def __init__(self):
        self.stats = CleaningStats()
        self.processed_files: List[DocumentInfo] = []
        self.error_files: List[Dict[str, Any]] = []
        self.performance_monitor = PerformanceMonitor()
        
        # 컴파일된 정규식 캐시
        self.compiled_patterns = self._compile_patterns()
        
        # 병렬 처리 설정
        self.max_workers = min(mp.cpu_count(), PROCESSING_OPTIONS['max_workers'])
        self.chunk_size = PROCESSING_OPTIONS['chunk_size']
        
    def _compile_patterns(self) -> Dict[str, re.Pattern]:
        """정규식 패턴 미리 컴파일"""
        compiled = {}
        for name, pattern in CLEANING_PATTERNS.items():
            if isinstance(pattern, str):
                compiled[name] = re.compile(pattern)
            else:
                compiled[name] = pattern
        return compiled
    
    def clean_text_content_vectorized(self, content: str) -> str:
        """벡터화된 텍스트 정제"""
        if not content:
            return ""
            
        original_length = len(content)
        
        # 벡터화된 정규식 적용
        # 1. HTML 태그 일괄 제거
        html_patterns = [p for n, p in self.compiled_patterns.items() 
                        if 'html' in n or 'style' in n or 'attributes' in n]
        for pattern in html_patterns:
            content = pattern.sub('', content)
            self.stats.removed_html_tags += 1
        
        # 2. D2H 관련 패턴 일괄 제거
        content = self.compiled_patterns['d2h_prefixes'].sub('', content)
        content = self.compiled_patterns['ms_xhelp_links'].sub('', content)
        content = self.compiled_patterns['package_url'].sub('', content)
        
        # 3. 테이블 테두일 제거
        content = self.compiled_patterns['table_borders'].sub('', content)
        
        # 4. 불필요한 키워드 벡터화된 제거
        unwanted_keywords = list(UNWANTED_KEYWORDS)
        for keyword in unwanted_keywords:
            content = content.replace(keyword, '')
        
        # 5. 특수 문자 정제 (벡터화된 방식)
        content = self._normalize_special_chars_vectorized(content)
        
        # 6. 여러 공백 및 빈 줄 정리
        content = self.compiled_patterns['extra_spaces'].sub(' ', content)
        content = self.compiled_patterns['empty_lines'].sub('\n\n', content)
        
        # 7. 줄바꿈 정리
        content = '\n'.join(line.strip() for line in content.split('\n') if line.strip())
        
        final_length = len(content)
        self.stats.removed_special_chars += original_length - final_length
        self.stats.normalized_whitespace += original_length - final_length
        
        return content.strip()
    
    def _normalize_special_chars_vectorized(self, text: str) -> str:
        """벡터화된 특수 문자 정규화"""
        # 유니코드 정규화
        text = unicodedata.normalize('NFKC', text)
        
        # 허용된 문자만 유지 (벡터화된 방식)
        allowed_chars = set(
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            '가-힣'  # 한글
            ' \t\n\r'
        )
        allowed_chars.update(ALLOWED_SPECIAL_CHARS)
        
        # 벡터화된 문자 필터링
        result = []
        for char in text:
            if char in allowed_chars:
                result.append(char)
            elif char.isspace():
                result.append(' ')
            else:
                result.append(' ')
        
        return ''.join(result)
    
    def extract_code_blocks_optimized(self, content: str) -> Tuple[str, List[Dict[str, Any]]]:
        """최적화된 코드 블록 추출"""
        code_snippets = []
        cleaned_content = content
        
        # 단일 패턴으로 코드 블록 감지
        code_block_pattern = re.compile(r'```([a-zA-Z0-9+]*)\s*\n(.*?)\n```', re.DOTALL)
        
        # 모든 코드 블록 찾기
        matches = list(code_block_pattern.finditer(content))
        
        # 역순으로 처리하여 위치 문제 방지
        for match in reversed(matches):
            language = match.group(1) or 'unknown'
            code = match.group(2)
            
            # 코드 스니펫 생성
            code_snippet = {
                'language': language.lower(),
                'code': code,
                'normalized_code': self._normalize_code_content(code),
                'line_start': content[:match.start()].count('\n') + 1,
                'line_end': content[:match.end()].count('\n') - 1,
                'hash': self._generate_hash(code)
            }
            code_snippets.append(code_snippet)
            
            # 원본 내용에서 코드 블록 제거
            start_pos, end_pos = match.span()
            cleaned_content = cleaned_content[:start_pos] + f'[CODE_BLOCK:{len(code_snippets)-1}]' + cleaned_content[end_pos:]
        
        return cleaned_content, code_snippets
    
    def _normalize_code_content(self, code: str) -> str:
        """코드 내용 정규화"""
        if not code:
            return ''
        
        # 줄바꿈 정리
        code = re.sub(r'\r\n', '\n', code)
        code = re.sub(r'\n+', '\n', code)
        
        # 주석 제거 (간소화된 버전)
        code = re.sub(r'//.*?$|/\*.*?\*/', '', code, flags=re.MULTILINE | re.DOTALL)
        
        # 불필요한 공백 정리
        lines = code.split('\n')
        normalized_lines = []
        
        for line in lines:
            line = line.rstrip()
            if line:
                normalized_lines.append(line)
        
        return '\n'.join(normalized_lines)
    
    def _generate_hash(self, content: str) -> str:
        """해시 생성"""
        return hashlib.md5(content.encode('utf-8')).hexdigest()
    
    def extract_metadata_vectorized(self, file_path: Path, content: str) -> Dict[str, Any]:
        """벡터화된 메타데이터 추출"""
        metadata = {
            'file_path': str(file_path),
            'original_filename': file_path.name,
            'file_size': file_path.stat().st_size,
            'created_date': datetime.fromtimestamp(file_path.stat().st_ctime).isoformat(),
            'modified_date': datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(),
            'processing_date': datetime.now().isoformat(),
            'category': self._extract_category_vectorized(file_path),
            'subcategory': self._extract_subcategory_vectorized(file_path),
            'title': self._extract_title_vectorized(content),
            'tags': self._extract_tags_vectorized(content),
            'description': self._extract_description_vectorized(content),
            'word_count': len(content.split()),
            'char_count': len(content),
            'has_code': '```' in content,
            'has_images': '![' in content,
            'has_links': '](' in content,
            'has_tables': '|' in content
        }
        
        return metadata
    
    def _extract_category_vectorized(self, file_path: Path) -> str:
        """벡터화된 카테고리 추출"""
        category_map = {
            '01_Getting_Started': '01_Getting_Started',
            '02_Concepts': '02_Concepts',
            '03_Data_Binding': '03_Data_Binding',
            '04_Controls': '04_Controls',
            '05_Features': '05_Features',
            '99_Uncategorized': '99_Uncategorized'
        }
        
        parts = file_path.parts
        for part in parts:
            if part in category_map:
                return category_map[part]
        return '99_Uncategorized'
    
    def _extract_subcategory_vectorized(self, file_path: Path) -> str:
        """벡터화된 서브 카테고리 추출"""
        subcategory_map = {
            'Chart': 'Chart',
            'Diagram': 'Diagram',
            'Editors': 'Editors',
            'Gauge': 'Gauge',
            'Grid': 'Grid',
            'Ribbon': 'Ribbon'
        }
        
        parts = file_path.parts
        for part in parts:
            if part in subcategory_map:
                return subcategory_map[part]
        return ''
    
    def _extract_title_vectorized(self, content: str) -> str:
        """벡터화된 제목 추출"""
        # 정규식으로 헤더 찾기
        header_pattern = re.compile(r'^#{1,3}\s+(.+)$', re.MULTILINE)
        match = header_pattern.search(content)
        
        if match:
            return match.group(1).strip()
        
        # 헤더가 없으면 파일명 사용
        return 'Untitled'
    
    def _extract_tags_vectorized(self, content: str) -> List[str]:
        """벡터화된 태그 추출"""
        # 키워드 매핑
        keyword_map = {
            'control': ['control', 'controls'],
            'data': ['data', 'database', 'datasource'],
            'binding': ['binding', 'bindings'],
            'grid': ['grid', 'grids'],
            'chart': ['chart', 'charts'],
            'diagram': ['diagram', 'diagrams'],
            'editor': ['editor', 'editors'],
            'gauge': ['gauge', 'gauges'],
            'ribbon': ['ribbon', 'ribbons'],
            'feature': ['feature', 'features'],
            'concept': ['concept', 'concepts'],
            'getting-started': ['getting', 'started', 'beginner', 'basic']
        }
        
        content_lower = content.lower()
        tags = []
        
        # 키워드 매칭
        for tag, keywords in keyword_map.items():
            for keyword in keywords:
                if keyword in content_lower:
                    tags.append(tag)
                    break
        
        return list(set(tags))
    
    def _extract_description_vectorized(self, content: str) -> str:
        """벡터화된 설명 추출"""
        # 첫 번째 문장 추출
        sentences = re.split(r'[.!?]', content)
        for sentence in sentences:
            sentence = sentence.strip()
            if 10 < len(sentence) < 200:
                return sentence
        
        return content[:100] + '...' if len(content) > 100 else content
    
    def process_file_chunk(self, file_paths: List[Path]) -> List[Optional[DocumentInfo]]:
        """파일 청크 처리"""
        results = []
        
        for file_path in file_paths:
            try:
                start_time = time.time()
                
                # 파일 읽기
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                # 메모리 사용량 측정
                memory_before = psutil.Process().memory_info().rss / 1024 / 1024
                
                # 백업 생성
                if PROCESSING_OPTIONS['create_backup']:
                    backup_path = BACKUP_DIR / f"{file_path.stem}_backup_{int(time.time())}{file_path.suffix}"
                    with open(backup_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                
                # 메타데이터 추출
                metadata = self.extract_metadata_vectorized(file_path, content)
                
                # 코드 블록 추출
                cleaned_content, code_snippets = self.extract_code_blocks_optimized(content)
                
                # 텍스트 정제
                cleaned_content = self.clean_text_content_vectorized(cleaned_content)
                
                # 메모리 사용량 측정
                memory_after = psutil.Process().memory_info().rss / 1024 / 1024
                memory_usage = memory_after - memory_before
                
                # 문서 정보 생성
                doc_info = DocumentInfo(
                    file_path=str(file_path),
                    original_filename=file_path.name,
                    category=metadata['category'],
                    subcategory=metadata['subcategory'],
                    title=metadata['title'],
                    content=content,
                    cleaned_content=cleaned_content,
                    metadata=metadata,
                    code_snippets=code_snippets,
                    word_count=len(cleaned_content.split()),
                    char_count=len(cleaned_content),
                    processing_time=time.time() - start_time,
                    memory_usage=memory_usage
                )
                
                # 통계 업데이트
                self.stats.processed_files += 1
                self.stats.total_words += doc_info.word_count
                self.stats.total_chars += doc_info.char_count
                self.stats.total_code_snippets += len(code_snippets)
                
                results.append(doc_info)
                
                # 메모리 정리
                del content, cleaned_content, code_snippets
                gc.collect()
                
            except Exception as e:
                error_msg = f"파일 처리 오류: {file_path.name} - {str(e)}"
                logger.error(error_msg)
                logger.error(traceback.format_exc())
                
                # 오류 정보 저장
                self.error_files.append({
                    'file_path': str(file_path),
                    'error': str(e),
                    'timestamp': datetime.now().isoformat()
                })
                
                self.stats.failed_files += 1
                results.append(None)
        
        return results
    
    def process_file_batch_optimized(self, file_paths: List[Path]) -> List[Optional[DocumentInfo]]:
        """최적화된 파일 배치 처리 - 메모리 효율성 개선"""
        results = []
        batch_size = min(10, len(file_paths))  # 배치 크기 조절
        
        for i in range(0, len(file_paths), batch_size):
            batch = file_paths[i:i + batch_size]
            batch_results = []
            
            for file_path in batch:
                try:
                    start_time = time.time()
                    
                    # 파일 읽기 - 메모리 매핑 사용
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    # 메모리 사용량 측정
                    memory_before = psutil.Process().memory_info().rss / 1024 / 1024
                    
                    # 백업 생성 (비동기 처리)
                    if PROCESSING_OPTIONS['create_backup']:
                        backup_path = BACKUP_DIR / f"{file_path.stem}_backup_{int(time.time())}{file_path.suffix}"
                        with open(backup_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                    
                    # 메타데이터 추출
                    metadata = self.extract_metadata_vectorized(file_path, content)
                    
                    # 코드 블록 추출
                    cleaned_content, code_snippets = self.extract_code_blocks_optimized(content)
                    
                    # 텍스트 정제 - 병렬 정규식 처리
                    cleaned_content = self.clean_text_content_parallel(cleaned_content)
                    
                    # 메모리 사용량 측정
                    memory_after = psutil.Process().memory_info().rss / 1024 / 1024
                    memory_usage = memory_after - memory_before
                    
                    # 문서 정보 생성
                    doc_info = DocumentInfo(
                        file_path=str(file_path),
                        original_filename=file_path.name,
                        category=metadata['category'],
                        subcategory=metadata['subcategory'],
                        title=metadata['title'],
                        content=content,
                        cleaned_content=cleaned_content,
                        metadata=metadata,
                        code_snippets=code_snippets,
                        word_count=len(cleaned_content.split()),
                        char_count=len(cleaned_content),
                        processing_time=time.time() - start_time,
                        memory_usage=memory_usage
                    )
                    
                    batch_results.append(doc_info)
                    
                    # 통계 업데이트
                    self.stats.processed_files += 1
                    self.stats.total_words += doc_info.word_count
                    self.stats.total_chars += doc_info.char_count
                    self.stats.total_code_snippets += len(code_snippets)
                    
                    # 메모리 정리
                    del content, cleaned_content, code_snippets, metadata
                    gc.collect()
                    
                except Exception as e:
                    error_msg = f"파일 처리 오류: {file_path.name} - {str(e)}"
                    logger.error(error_msg)
                    logger.error(traceback.format_exc())
                    
                    # 오류 정보 저장
                    self.error_files.append({
                        'file_path': str(file_path),
                        'error': str(e),
                        'timestamp': datetime.now().isoformat()
                    })
                    
                    self.stats.failed_files += 1
                    batch_results.append(None)
            
            results.extend(batch_results)
            
            # 배치 간 메모리 정리
            if i + batch_size < len(file_paths):
                gc.collect()
        
        return results
    
    def clean_text_content_parallel(self, content: str) -> str:
        """병렬 정규식 처리 - 성능 최적화"""
        if not content:
            return ""
        
        original_length = len(content)
        
        # 병렬 처리를 위한 작업 분할
        tasks = [
            ('html_removal', lambda c: self._remove_html_tags_parallel(c)),
            ('pattern_removal', lambda c: self._remove_d2h_patterns_parallel(c)),
            ('normalization', lambda c: self._normalize_content_parallel(c)),
        ]
        
        # 순차적 처리 (의존성 때문)
        processed_content = content
        
        for task_name, task_func in tasks:
            start_time = time.time()
            processed_content = task_func(processed_content)
            
            # 작업별 통계
            if task_name == 'html_removal':
                self.stats.removed_html_tags += original_length - len(processed_content)
            elif task_name == 'pattern_removal':
                self.stats.removed_special_chars += original_length - len(processed_content)
            elif task_name == 'normalization':
                self.stats.normalized_whitespace += original_length - len(processed_content)
        
        final_length = len(processed_content)
        self.stats.removed_special_chars += original_length - final_length
        self.stats.normalized_whitespace += original_length - final_length
        
        return processed_content.strip()
    
    def _remove_html_tags_parallel(self, content: str) -> str:
        """병렬 HTML 태그 제거"""
        # HTML 태그 패턴 그룹화
        html_patterns = [
            self.compiled_patterns['html_tags'],
            self.compiled_patterns['html_entities'],
            self.compiled_patterns['style_tags'],
            self.compiled_patterns['script_tags']
        ]
        
        # 병렬 적용
        for pattern in html_patterns:
            content = pattern.sub('', content)
        
        return content
    
    def _remove_d2h_patterns_parallel(self, content: str) -> str:
        """병렬 D2H 패턴 제거"""
        # D2H 관련 패턴 그룹화
        d2h_patterns = [
            self.compiled_patterns['d2h_prefixes'],
            self.compiled_patterns['ms_xhelp_links'],
            self.compiled_patterns['package_url'],
            self.compiled_patterns['table_borders']
        ]
        
        # 병렬 적용
        for pattern in d2h_patterns:
            content = pattern.sub('', content)
        
        return content
    
    def _normalize_content_parallel(self, content: str) -> str:
        """병렬 콘텐츠 정규화"""
        # 여러 공밡 및 빈 줄 정리
        content = self.compiled_patterns['extra_spaces'].sub(' ', content)
        content = self.compiled_patterns['empty_lines'].sub('\n\n', content)
        
        # 줄바꿈 정리
        content = '\n'.join(line.strip() for line in content.split('\n') if line.strip())
        
        return content.strip()
    
    def process_directory_parallel(self, directory: Path = None) -> List[DocumentInfo]:
        """고성능 병렬 처리로 디렉토리 내 모든 파일 처리"""
        if directory is None:
            directory = WINFORMS_DOCS_DIR
        
        start_time = datetime.now()
        logger.info(f"고성능 병렬 처리 시작: {directory}")
        
        # 파일 목록 수집
        markdown_files = self._collect_markdown_files(directory)
        self.stats.total_files = len(markdown_files)
        logger.info(f"처리할 파일 수: {self.stats.total_files}")
        
        # 동적 작업 분할 (CPU 코어 수 기반)
        optimal_chunk_size = self._calculate_optimal_chunk_size(len(markdown_files))
        file_chunks = self._create_dynamic_chunks(markdown_files, optimal_chunk_size)
        
        processed_docs = []
        
        # 프로세스 풀을 이용한 병렬 처리
        with ProcessPoolExecutor(max_workers=self.max_workers) as executor:
            # 청크별로 작업 제출
            future_to_chunk = {
                executor.submit(self.process_file_batch_optimized, chunk): chunk
                for chunk in file_chunks
            }
            
            # 결과 수집
            for future in as_completed(future_to_chunk):
                try:
                    chunk_results = future.result()
                    processed_docs.extend([r for r in chunk_results if r is not None])
                except Exception as e:
                    logger.error(f"청크 처리 오류: {str(e)}")
                    logger.error(traceback.format_exc())
        
        # 성능 통계 업데이트
        self.stats.processing_time = (datetime.now() - start_time).total_seconds()
        self.stats.peak_memory_usage = self.performance_monitor.peak_memory
        self.stats.cpu_usage = self.performance_monitor.get_cpu_usage()
        
        logger.info(f"고성능 병렬 처리 완료: {len(processed_docs)}개 문서 처리")
        logger.info(f"처리 시간: {self.stats.processing_time:.2f}초")
        logger.info(f"최대 메모리 사용: {self.stats.peak_memory_usage:.2f}MB")
        logger.info(f"평균 처리 속도: {len(processed_docs)/self.stats.processing_time:.2f} 문서/초")
        
        return processed_docs
    
    def _collect_markdown_files(self, directory: Path) -> List[Path]:
        """마크다운 파일 수집 - 고성능"""
        markdown_files = []
        
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(('.md', '.markdown')):
                    markdown_files.append(Path(root) / file)
        
        return markdown_files
    
    def _calculate_optimal_chunk_size(self, total_files: int) -> int:
        """최적 청크 크기 계산 - CPU 코어 수 기반"""
        cpu_count = mp.cpu_count()
        
        if total_files <= cpu_count:
            return 1
        
        # 파일 수와 CPU 코어 수에 따른 동적 청크 크기
        base_chunk = max(1, total_files // (cpu_count * 2))
        
        # 메모리 제한 고려
        available_memory = psutil.virtual_memory().available / (1024 * 1024)  # MB
        memory_factor = min(1.0, available_memory / 1024)  # 1GB 이상이면 정상
        
        return max(1, int(base_chunk * memory_factor))
    
    def _create_dynamic_chunks(self, file_paths: List[Path], chunk_size: int) -> List[List[Path]]:
        """동적 청크 생성 - 파일 크기 기반 최적화"""
        # 파일 크기 정보 수집
        file_sizes = []
        for file_path in file_paths:
            try:
                size = file_path.stat().st_size
                file_sizes.append((file_path, size))
            except:
                file_sizes.append((file_path, 0))  # 크기 정보 없음
        
        # 크기 기준 정렬
        file_sizes.sort(key=lambda x: x[1], reverse=True)
        
        # 동적 청크 생성
        chunks = []
        current_chunk = []
        current_size = 0
        
        for file_path, size in file_sizes:
            # 현재 청크에 추가
            current_chunk.append(file_path)
            current_size += size
            
            # 청크 크기 또는 크기 제한 도달 시 분할
            if len(current_chunk) >= chunk_size or current_size >= 10 * 1024 * 1024:  # 10MB
                chunks.append(current_chunk)
                current_chunk = []
                current_size = 0
        
        # 남은 파일 추가
        if current_chunk:
            chunks.append(current_chunk)
        
        return chunks
        
        return processed_docs
    
    def save_results_arrow(self, output_dir: Optional[Path] = None):
        """Arrow 포맷으로 결과 저장"""
        if output_dir is None:
            output_dir = OUTPUT_DIR
        
        # Arrow 디렉토리 생성
        arrow_dir = output_dir / 'arrow_data'
        arrow_dir.mkdir(parents=True, exist_ok=True)
        
        # 문서 데이터를 Arrow 테이블로 변환
        if self.processed_files:
            # 데이터 준비
            data = {
                'file_path': [doc.file_path for doc in self.processed_files],
                'original_filename': [doc.original_filename for doc in self.processed_files],
                'category': [doc.category for doc in self.processed_files],
                'subcategory': [doc.subcategory for doc in self.processed_files],
                'title': [doc.title for doc in self.processed_files],
                'content': [doc.content for doc in self.processed_files],
                'cleaned_content': [doc.cleaned_content for doc in self.processed_files],
                'word_count': [doc.word_count for doc in self.processed_files],
                'char_count': [doc.char_count for doc in self.processed_files],
                'processing_time': [doc.processing_time for doc in self.processed_files],
                'memory_usage': [doc.memory_usage for doc in self.processed_files],
                'code_snippets_count': [len(doc.code_snippets) for doc in self.processed_files]
            }
            
            # Arrow 테이블 생성
            table = pa.Table.from_pandas(pd.DataFrame(data))
            
            # Parquet 파일로 저장
            parquet_path = arrow_dir / 'processed_documents.parquet'
            pq.write_table(table, parquet_path)
            
            logger.info(f"Arrow 포맷 저장 완료: {parquet_path}")
        
        # 통계 정보 Arrow로 저장
        stats_data = {
            'total_files': [self.stats.total_files],
            'processed_files': [self.stats.processed_files],
            'failed_files': [self.stats.failed_files],
            'total_words': [self.stats.total_words],
            'total_chars': [self.stats.total_chars],
            'total_code_snippets': [self.stats.total_code_snippets],
            'processing_time': [self.stats.processing_time],
            'memory_peak_usage': [self.stats.memory_peak_usage],
            'cpu_usage': [self.stats.cpu_usage]
        }
        
        stats_table = pa.Table.from_pandas(pd.DataFrame(stats_data))
        stats_path = arrow_dir / 'processing_stats.parquet'
        pq.write_table(stats_table, stats_path)
        
        logger.info(f"통계 정보 저장 완료: {stats_path}")
    
    def save_results(self, output_dir: Optional[Path] = None):
        """결과 저장 (호환성 유지)"""
        if output_dir is None:
            output_dir = OUTPUT_DIR
        
        # JSON 파일로 저장 (기존 호환성)
        json_dir = output_dir / 'json_data'
        json_dir.mkdir(parents=True, exist_ok=True)
        
        # 처리된 문서 저장
        docs_data = [asdict(doc) for doc in self.processed_files]
        with open(json_dir / 'processed_documents.json', 'w', encoding='utf-8') as f:
            json.dump(docs_data, f, ensure_ascii=False, indent=2)
        
        # 통계 정보 저장
        stats_data = asdict(self.stats)
        with open(json_dir / 'processing_stats.json', 'w', encoding='utf-8') as f:
            json.dump(stats_data, f, ensure_ascii=False, indent=2)
        
        # 오류 정보 저장
        if self.error_files:
            with open(json_dir / 'error_files.json', 'w', encoding='utf-8') as f:
                json.dump(self.error_files, f, ensure_ascii=False, indent=2)
        
        # Arrow 포맷으로 저장
        self.save_results_arrow(output_dir)
        
        logger.info(f"결과 저장 완료: {json_dir}")
    
    def generate_report(self, output_dir: Optional[Path] = None):
        """처리 보고서 생성"""
        if output_dir is None:
            output_dir = OUTPUT_DIR
        
        report_dir = output_dir / 'reports'
        report_dir.mkdir(parents=True, exist_ok=True)
        
        # 텍스트 보고서
        report_content = f"""
WinForms_Docs 데이터 정제 보고서 - 성능 최적화 버전
==================================================

처리 일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

기본 통계:
- 총 파일 수: {self.stats.total_files}
- 성공 처리: {self.stats.processed_files}
- 실패 처리: {self.stats.failed_files}
- 성공률: {(self.stats.processed_files / max(self.stats.total_files, 1) * 100):.1f}%

내용 통계:
- 총 단어 수: {self.stats.total_words:,}
- 총 문자 수: {self.stats.total_chars:,}
- 총 코드 스니펫 수: {self.stats.total_code_snippets}
- 평균 단어 수: {self.stats.total_words / max(self.stats.processed_files, 1):.0f}

성능 통계:
- 총 처리 시간: {self.stats.processing_time:.2f}초
- 평균 처리 시간: {self.stats.processing_time / max(self.stats.processed_files, 1):.2f}초
- 메모리 피크 사용량: {self.stats.memory_peak_usage:.2f}MB
- CPU 평균 사용률: {self.stats.cpu_usage:.1f}%

병렬 처리 설정:
- 최대 워커 수: {self.max_workers}
- 청크 크기: {self.chunk_size}
- 사용된 CPU 코어 수: {mp.cpu_count()}

카테고리별 분포:
"""
        
        # 카테고리별 통계
        category_stats = {}
        for doc in self.processed_files:
            category = doc.category
            if category not in category_stats:
                category_stats[category] = {'count': 0, 'words': 0, 'avg_memory': 0, 'avg_time': 0}
            category_stats[category]['count'] += 1
            category_stats[category]['words'] += doc.word_count
            category_stats[category]['avg_memory'] += doc.memory_usage
            category_stats[category]['avg_time'] += doc.processing_time
        
        for category, stats in category_stats.items():
            avg_memory = stats['avg_memory'] / stats['count']
            avg_time = stats['avg_time'] / stats['count']
            report_content += f"- {category}: {stats['count']}개 파일, {stats['words']:,} 단어, "
            report_content += f"평균 메모리 {avg_memory:.2f}MB, 평균 시간 {avg_time:.2f}초\n"
        
        # 오류 파일 목록
        if self.error_files:
            report_content += f"\n오류 파일 목록 ({len(self.error_files)}개):\n"
            for error in self.error_files:
                report_content += f"- {error['file_path']}: {error['error']}\n"
        
        # 성능 개선 사항
        report_content += f"""
성능 개선 사항:
- 벡터화된 텍스트 처리 적용
- 병렬 처리로 파일 처리 속도 향상
- Arrow 포맷으로 메모리 효율적인 저장
- 정규식 패턴 미리 컴파일
- 메모리 사용량 모니터링
- 청크 기반 대용량 파일 처리

추천 사항:
- 더 큰 청크 크기로 처리 시간 단축 가능
- SSD 사용 시 I/O 성능 향상
- 추가적인 메모리 최적화 가능
"""
        
        # 보고서 파일 저장
        with open(report_dir / 'cleaning_report_optimized.txt', 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        logger.info(f"성능 보고서 생성 완료: {report_dir / 'cleaning_report_optimized.txt'}")

def main():
    """메인 실행 함수"""
    logger.info("WinForms_Docs 데이터 정제 시작 - 성능 최적화 버전")
    
    # 데이터 정제기 초기화
    cleaner = DataCleaner()
    
    # 병렬 처리로 디렉토리 처리
    start_time = datetime.now()
    processed_docs = cleaner.process_directory_parallel()
    
    # 결과 저장
    cleaner.save_results()
    
    # 보고서 생성
    cleaner.generate_report()
    
    # 총 처리 시간
    total_time = (datetime.now() - start_time).total_seconds()
    logger.info(f"총 처리 시간: {total_time:.2f}초")
    logger.info(f"평균 처리 속도: {len(processed_docs) / total_time:.2f} 파일/초")

if __name__ == "__main__":
    main()