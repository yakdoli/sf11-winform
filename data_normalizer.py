"""
WinForms_Docs 데이터 정규화 모듈
"""

import json
import re
import logging
import time
import multiprocessing as mp
from pathlib import Path
from typing import Dict, List, Set, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime
import unicodedata
from collections import defaultdict, Counter
import hashlib
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import traceback
import psutil
import gc

from config import (
    OUTPUT_DIR, CATEGORY_MAPPING, SUBCATEGORY_MAPPING,
    DOCUMENT_METADATA_FIELDS, CODE_SNIPPET_METADATA_FIELDS,
    VALIDATION_RULES, OUTPUT_FORMATS
)

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class NormalizedDocument:
    """정규화된 문서 데이터 클래스"""
    id: str
    file_path: str
    normalized_filename: str
    category: str
    subcategory: str
    title: str
    normalized_title: str
    description: str
    tags: List[str]
    normalized_tags: List[str]
    content: str
    normalized_content: str
    word_count: int
    char_count: int
    reading_time: float
    language: str
    code_snippets: List[Dict[str, Any]]
    normalized_code_snippets: List[Dict[str, Any]]
    metadata: Dict[str, Any]
    relationships: List[Dict[str, Any]]
    quality_score: float
    created_date: str
    updated_date: str

@dataclass
class NormalizationStats:
    """정규화 통계 데이터 클래스"""
    total_documents: int = 0
    normalized_documents: int = 0
    failed_documents: int = 0
    total_words: int = 0
    total_chars: int = 0
    total_tags: int = 0
    total_code_snippets: int = 0
    normalized_categories: int = 0
    normalized_subcategories: int = 0
    normalized_titles: int = 0
    normalized_tags_count: int = 0
    processing_time: float = 0.0

class DataNormalizer:
    """데이터 정규화 클래스 - 병렬 처리 최적화"""
    
    def __init__(self):
        self.stats = NormalizationStats()
        self.normalized_docs: List[NormalizedDocument] = []
        self.category_hierarchy: Dict[str, List[str]] = {}
        self.tag_vocabulary: Set[str] = set()
        self.code_language_stats: Dict[str, int] = defaultdict(int)
        
        # 병렬 처리 설정
        self.max_workers = min(mp.cpu_count(), 8)  # 최대 8개 워커
        self.chunk_size = 50  # 문서 청크 크기
        
        # 성능 모니터링
        self.process = psutil.Process()
        self.start_memory = self.process.memory_info().rss / 1024 / 1024  # MB
        self.peak_memory = self.start_memory
        
        # 컴파일된 정규식 캐시
        self.compiled_patterns = self._compile_patterns()
        
        # 정규식 패턴 미리 컴파일
        self.text_pattern = re.compile(r'[^\w\s가-힣\.\,\!\?\;\:\-\(\)\[\]\{\}\<\>\=\+\*\/\\\@\#\$\%\&\|]')
        self.space_pattern = re.compile(r'\s+')
        
    def _compile_patterns(self) -> Dict[str, re.Pattern]:
        """정규식 패턴 미리 컴파일"""
        patterns = {
            'html_tags': re.compile(r'<[^>]+>'),
            'html_entities': re.compile(r'&[^;]+;'),
            'extra_spaces': re.compile(r'[ \t]+'),
            'empty_lines': re.compile(r'\n\s*\n'),
            'special_chars': re.compile(r'[^\w\s가-힣]'),
            'multiple_spaces': re.compile(r'\s+'),
            'leading_trailing_spaces': re.compile(r'^\s+|\s+$'),
        }
        return patterns
    
    def _update_memory_usage(self):
        """메모리 사용량 업데이트"""
        current_memory = self.process.memory_info().rss / 1024 / 1024  # MB
        self.peak_memory = max(self.peak_memory, current_memory)
        return current_memory
        
    def normalize_document(self, doc_data: Dict[str, Any]) -> Optional[NormalizedDocument]:
        """단일 문서 정규화"""
        try:
            start_time = datetime.now()
            
            # 기본 정보 추출
            file_path = doc_data.get('file_path', '')
            content = doc_data.get('cleaned_content', doc_data.get('content', ''))
            metadata = doc_data.get('metadata', {})
            code_snippets = doc_data.get('code_snippets', [])
            
            # ID 생성
            doc_id = self._generate_document_id(file_path)
            
            # 카테고리 정규화
            category = self._normalize_category(metadata.get('category', ''))
            subcategory = self._normalize_subcategory(metadata.get('subcategory', ''))
            
            # 제목 정규화
            title = metadata.get('title', 'Untitled')
            normalized_title = self._normalize_text(title)
            
            # 설명 정규화
            description = metadata.get('description', '')
            normalized_description = self._normalize_text(description)
            
            # 태그 정규화
            tags = metadata.get('tags', [])
            normalized_tags = self._normalize_tags(tags)
            
            # 내용 정규화
            normalized_content = self._normalize_content(content)
            
            # 코드 스니펫 정규화
            normalized_code_snippets = self._normalize_code_snippets(code_snippets)
            
            # 관계 매핑 생성
            relationships = self._create_relationships(doc_data, category, subcategory)
            
            # 품질 점수 계산
            quality_score = self._calculate_quality_score(doc_data)
            
            # 읽기 시간 계산
            reading_time = self._calculate_reading_time(len(normalized_content.split()))
            
            # 언어 감지
            language = self._detect_language(content)
            
            # 정규화된 문서 생성
            normalized_doc = NormalizedDocument(
                id=doc_id,
                file_path=file_path,
                normalized_filename=self._normalize_filename(Path(file_path).name),
                category=category,
                subcategory=subcategory,
                title=title,
                normalized_title=normalized_title,
                description=description,
                tags=tags,
                normalized_tags=normalized_tags,
                content=content,
                normalized_content=normalized_content,
                word_count=len(normalized_content.split()),
                char_count=len(normalized_content),
                reading_time=reading_time,
                language=language,
                code_snippets=code_snippets,
                normalized_code_snippets=normalized_code_snippets,
                metadata=metadata,
                relationships=relationships,
                quality_score=quality_score,
                created_date=metadata.get('created_date', ''),
                updated_date=metadata.get('modified_date', '')
            )
            
            # 통계 업데이트
            self.stats.normalized_documents += 1
            self.stats.total_words += normalized_doc.word_count
            self.stats.total_chars += normalized_doc.char_count
            self.stats.total_tags += len(normalized_tags)
            self.stats.total_code_snippets += len(normalized_code_snippets)
            
            # 태그 어휘 업데이트
            self.tag_vocabulary.update(normalized_tags)
            
            # 코드 언어 통계 업데이트
            for snippet in normalized_code_snippets:
                lang = snippet.get('language', 'unknown')
                self.code_language_stats[lang] += 1
            
            # 처리 시간 계산
            processing_time = (datetime.now() - start_time).total_seconds()
            self.stats.processing_time += processing_time
            
            logger.info(f"문서 정규화 완료: {Path(file_path).name} (품질 점수: {quality_score:.2f})")
            
            return normalized_doc
            
        except Exception as e:
            logger.error(f"문서 정규화 오류: {file_path} - {str(e)}")
            self.stats.failed_documents += 1
            return None
    
    def _generate_document_id(self, file_path: str) -> str:
        """문서 ID 생성"""
        return hashlib.md5(file_path.encode('utf-8')).hexdigest()
    
    def _normalize_category(self, category: str) -> str:
        """카테고리 정규화"""
        normalized = CATEGORY_MAPPING.get(category, category.lower().replace('_', '-'))
        if normalized != category:
            self.stats.normalized_categories += 1
        return normalized
    
    def _normalize_subcategory(self, subcategory: str) -> str:
        """서브 카테고리 정규화"""
        if not subcategory:
            return ''
        normalized = SUBCATEGORY_MAPPING.get(subcategory, subcategory.lower().replace('_', '-'))
        if normalized != subcategory:
            self.stats.normalized_subcategories += 1
        return normalized
    
    def _normalize_text(self, text: str) -> str:
        """텍스트 정규화 - 병렬 처리 최적화"""
        if not text:
            return ''
        
        # 유니코드 정규화
        text = unicodedata.normalize('NFKC', text)
        
        # 병렬 처리를 위한 작업 분할
        tasks = [
            ('whitespace_normalization', lambda t: self._normalize_whitespace_parallel(t)),
            ('special_char_removal', lambda t: self._remove_special_chars_parallel(t)),
            ('final_cleanup', lambda t: self._final_cleanup_parallel(t)),
        ]
        
        # 순차적 처리 (의존성 때문)
        processed_text = text
        
        for task_name, task_func in tasks:
            processed_text = task_func(processed_text)
        
        return processed_text
    
    def _normalize_whitespace_parallel(self, text: str) -> str:
        """병렬 공백 정규화"""
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    def _remove_special_chars_parallel(self, text: str) -> str:
        """병렬 특수 문자 제거"""
        return re.sub(r'[^\w\s가-힣\.\,\!\?\;\:\-\(\)\[\]\{\}\<\>\=\+\*\/\\\@\#\$\%\&\|]', ' ', text)
    
    def _final_cleanup_parallel(self, text: str) -> str:
        """병렬 최종 정리"""
        return re.sub(r'\s+', ' ', text).strip()
    
    def _normalize_tags(self, tags: List[str]) -> List[str]:
        """태그 정규화"""
        normalized_tags = []
        
        for tag in tags:
            normalized_tag = self._normalize_text(tag)
            if normalized_tag and len(normalized_tag) > 1:
                normalized_tags.append(normalized_tag.lower())
        
        # 중복 제거
        unique_tags = list(set(normalized_tags))
        if len(unique_tags) != len(normalized_tags):
            self.stats.normalized_tags_count += 1
        
        return unique_tags
    
    def _normalize_content(self, content: str) -> str:
        """내용 정규화"""
        if not content:
            return ''
        
        # 유니코드 정규화
        content = unicodedata.normalize('NFKC', content)
        
        # 여러 줄바꿈 정리
        content = re.sub(r'\n\s*\n', '\n\n', content)
        
        # 여러 공백 정리
        content = re.sub(r'[ \t]+', ' ', content)
        
        # 불필요한 공백 제거
        content = content.strip()
        
        return content
    
    def _normalize_code_snippets(self, code_snippets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """코드 스니펫 정규화"""
        normalized_snippets = []
        
        for snippet in code_snippets:
            normalized_snippet = {
                'language': self._normalize_language(snippet.get('language', 'unknown')),
                'code': self._normalize_code(snippet.get('code', '')),
                'normalized_code': self._normalize_code_content(snippet.get('code', '')),
                'description': self._normalize_text(snippet.get('description', '')),
                'line_start': snippet.get('line_start', 0),
                'line_end': snippet.get('line_end', 0),
                'hash': snippet.get('hash', ''),
                'normalized_hash': self._generate_hash(snippet.get('code', ''))
            }
            normalized_snippets.append(normalized_snippet)
        
        return normalized_snippets
    
    def _normalize_language(self, language: str) -> str:
        """프로그래밍 언어 정규화"""
        language_map = {
            'csharp': 'csharp',
            'c#': 'csharp',
            'cs': 'csharp',
            'vb': 'vb.net',
            'vb.net': 'vb.net',
            'vb.net': 'vb.net',
            'asp': 'asp.net',
            'aspx': 'asp.net',
            'xml': 'xml',
            'html': 'html',
            'css': 'css',
            'js': 'javascript',
            'javascript': 'javascript',
            'sql': 'sql',
            'json': 'json',
            'plain': 'plaintext',
            'text': 'plaintext',
            'unknown': 'unknown'
        }
        
        return language_map.get(language.lower(), 'unknown')
    
    def _normalize_code(self, code: str) -> str:
        """코드 정규화"""
        if not code:
            return ''
        
        # 줄바꿈 정리
        code = re.sub(r'\r\n', '\n', code)
        code = re.sub(r'\n+', '\n', code)
        
        # 불필요한 공백 제거
        lines = code.split('\n')
        normalized_lines = []
        
        for line in lines:
            # 앞뒤 공백 제거
            line = line.rstrip()
            if line:  # 빈 줄이 아닌 경우만 추가
                normalized_lines.append(line)
        
        return '\n'.join(normalized_lines)
    
    def _normalize_code_content(self, code: str) -> str:
        """코드 내용 정규화 (비교용)"""
        normalized = self._normalize_code(code)
        # 주석 제거
        normalized = re.sub(r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"', '', normalized, flags=re.MULTILINE | re.DOTALL)
        return normalized
    
    def _generate_hash(self, content: str) -> str:
        """해시 생성"""
        return hashlib.md5(content.encode('utf-8')).hexdigest()
    
    def _create_relationships(self, doc_data: Dict[str, Any], category: str, subcategory: str) -> List[Dict[str, Any]]:
        """문서 관계 생성"""
        relationships = []
        
        # 카테고리 관계
        if category:
            relationships.append({
                'type': 'category',
                'target': category,
                'strength': 'strong'
            })
        
        # 서브 카테고리 관계
        if subcategory:
            relationships.append({
                'type': 'subcategory',
                'target': subcategory,
                'strength': 'strong'
            })
        
        # 태그 관계
        tags = doc_data.get('metadata', {}).get('tags', [])
        for tag in tags:
            relationships.append({
                'type': 'tag',
                'target': tag.lower(),
                'strength': 'medium'
            })
        
        # 코드 스니펫 관계
        code_snippets = doc_data.get('code_snippets', [])
        for snippet in code_snippets:
            language = snippet.get('language', 'unknown')
            relationships.append({
                'type': 'code_language',
                'target': language,
                'strength': 'weak'
            })
        
        return relationships
    
    def _calculate_quality_score(self, doc_data: Dict[str, Any]) -> float:
        """품질 점수 계산"""
        score = 0.0
        max_score = 100.0
        
        # 제품 점수 (20점)
        title = doc_data.get('metadata', {}).get('title', '')
        if title and len(title) > 5:
            score += 20.0
        else:
            score += 5.0
        
        # 내용 점수 (30점)
        content = doc_data.get('cleaned_content', '')
        word_count = len(content.split())
        if word_count > 100:
            score += 30.0
        elif word_count > 50:
            score += 20.0
        elif word_count > 10:
            score += 10.0
        
        # 메타데이터 점수 (25점)
        metadata = doc_data.get('metadata', {})
        required_fields = ['category', 'title', 'description']
        present_fields = sum(1 for field in required_fields if metadata.get(field))
        score += (present_fields / len(required_fields)) * 25.0
        
        # 코드 스니펫 점수 (15점)
        code_snippets = doc_data.get('code_snippets', [])
        if code_snippets:
            score += 15.0
        elif word_count > 200:  # 긴 문서는 코드가 없어도 괜찮음
            score += 10.0
        
        # 구조 점수 (10점)
        if '```' in content:
            score += 5.0
        if '# ' in content or '## ' in content:
            score += 5.0
        
        return min(score, max_score)
    
    def _calculate_reading_time(self, word_count: int) -> float:
        """읽기 시간 계산 (분)"""
        # 평균 분당 200단어 가정
        return max(1.0, word_count / 200.0)
    
    def _detect_language(self, content: str) -> str:
        """언어 감지"""
        # 간단한 언어 감지 로직
        if not content:
            return 'unknown'
        
        # 영어 비율 계산
        english_chars = sum(1 for c in content if c.isascii())
        total_chars = len(content)
        
        if total_chars == 0:
            return 'unknown'
        
        english_ratio = english_chars / total_chars
        
        if english_ratio > 0.7:
            return 'en'
        elif english_ratio > 0.3:
            return 'mixed'
        else:
            return 'ko'
    
    def _normalize_filename(self, filename: str) -> str:
        """파일명 정규화"""
        # 확장자 제거
        name = Path(filename).stem
        
        # 특수 문자 제거
        name = re.sub(r'[^\w\s가-힣\-]', '', name)
        
        # 여러 공백 제거
        name = re.sub(r'\s+', '_', name)
        
        return name.lower()
    
    def build_category_hierarchy(self, normalized_docs: List[NormalizedDocument]):
        """카테고리 계층 구조 구축"""
        hierarchy = defaultdict(list)
        
        for doc in normalized_docs:
            category = doc.category
            subcategory = doc.subcategory
            
            if subcategory:
                hierarchy[category].append(subcategory)
        
        # 중복 제거
        for category in hierarchy:
            hierarchy[category] = list(set(hierarchy[category]))
        
        self.category_hierarchy = dict(hierarchy)
    
    def build_tag_vocabulary(self, normalized_docs: List[NormalizedDocument]):
        """태그 어휘 구축"""
        all_tags = set()
        
        for doc in normalized_docs:
            all_tags.update(doc.normalized_tags)
        
        self.tag_vocabulary = all_tags
    
    def normalize_dataset_parallel(self, input_file: Path, output_dir: Path = None) -> List[NormalizedDocument]:
        """병렬 데이터셋 정규화 - 성능 최적화"""
        if output_dir is None:
            output_dir = OUTPUT_DIR / 'normalized_data'
        
        logger.info(f"병렬 데이터셋 정규화 시작: {input_file}")
        
        start_time = time.time()
        
        # 입력 파일 읽기
        with open(input_file, 'r', encoding='utf-8') as f:
            docs_data = json.load(f)
        
        self.stats.total_documents = len(docs_data)
        logger.info(f"처리할 문서 수: {self.stats.total_documents}")
        
        # 동적 작업 분할
        optimal_chunk_size = self._calculate_optimal_chunk_size(len(docs_data))
        doc_chunks = self._create_document_chunks(docs_data, optimal_chunk_size)
        
        normalized_docs = []
        
        # 프로세스 풀을 이용한 병렬 처리
        with ProcessPoolExecutor(max_workers=self.max_workers) as executor:
            # 청크별로 작업 제출
            future_to_chunk = {
                executor.submit(self.process_document_chunk, chunk): chunk
                for chunk in doc_chunks
            }
            
            # 결과 수집
            for future in as_completed(future_to_chunk):
                try:
                    chunk_results = future.result()
                    normalized_docs.extend([doc for doc in chunk_results if doc is not None])
                except Exception as e:
                    logger.error(f"문서 청크 처리 오류: {str(e)}")
                    logger.error(traceback.format_exc())
        
        # 카테고리 계층 구조 구축
        self.build_category_hierarchy(normalized_docs)
        
        # 태그 어휘 구축
        self.build_tag_vocabulary(normalized_docs)
        
        # 통계 업데이트
        self.stats.processing_time = time.time() - start_time
        self.stats.peak_memory_usage = self.peak_memory
        
        logger.info(f"병렬 데이터셋 정규화 완료: {len(normalized_docs)}개 문서 처리")
        logger.info(f"처리 시간: {self.stats.processing_time:.2f}초")
        logger.info(f"평균 처리 속도: {len(normalized_docs)/self.stats.processing_time:.2f} 문서/초")
        
        return normalized_docs
    
    def process_document_chunk(self, doc_chunk: List[Dict[str, Any]]) -> List[Optional[NormalizedDocument]]:
        """문서 청크 처리 - 병렬용"""
        results = []
        
        for doc_data in doc_chunk:
            try:
                # 메모리 사용량 측정
                memory_before = self.process.memory_info().rss / 1024 / 1024
                
                # 문서 정규화
                normalized_doc = self.normalize_document(doc_data)
                
                if normalized_doc:
                    results.append(normalized_doc)
                
                # 메모리 사용량 측정
                memory_after = self.process.memory_info().rss / 1024 / 1024
                memory_usage = memory_after - memory_before
                
                # 통계 업데이트
                self.stats.processed_documents += 1
                self.stats.total_words += normalized_doc.word_count
                self.stats.total_chars += normalized_doc.char_count
                
                # 메모리 정리
                del doc_data, normalized_doc
                gc.collect()
                
            except Exception as e:
                logger.error(f"문서 처리 오류: {doc_data.get('file_path', 'unknown')} - {str(e)}")
                logger.error(traceback.format_exc())
                results.append(None)
        
        return results
    
    def _calculate_optimal_chunk_size(self, total_docs: int) -> int:
        """최적 청크 크기 계산 - CPU 코어 수 기반"""
        cpu_count = mp.cpu_count()
        
        if total_docs <= cpu_count:
            return 1
        
        # 문서 수와 CPU 코어 수에 따른 동적 청크 크기
        base_chunk = max(1, total_docs // (cpu_count * 2))
        
        # 메모리 제한 고려
        available_memory = psutil.virtual_memory().available / (1024 * 1024)  # MB
        memory_factor = min(1.0, available_memory / 2048)  # 2GB 이상이면 정상
        
        return max(1, int(base_chunk * memory_factor))
    
    def _create_document_chunks(self, docs_data: List[Dict[str, Any]], chunk_size: int) -> List[List[Dict[str, Any]]]:
        """문서 청크 생성 - 크기 기반 최적화"""
        # 문서 크기 정보 수집 (추정)
        doc_sizes = []
        for doc_data in docs_data:
            # 문서 크기 추정 (content 길이 기반)
            content_size = len(doc_data.get('content', ''))
            doc_sizes.append((doc_data, content_size))
        
        # 크기 기준 정렬
        doc_sizes.sort(key=lambda x: x[1], reverse=True)
        
        # 동적 청크 생성
        chunks = []
        current_chunk = []
        current_size = 0
        
        for doc_data, size in doc_sizes:
            # 현재 청크에 추가
            current_chunk.append(doc_data)
            current_size += size
            
            # 청크 크기 또는 크기 제한 도달 시 분할
            if len(current_chunk) >= chunk_size or current_size >= 100 * 1024:  # 100KB
                chunks.append(current_chunk)
                current_chunk = []
                current_size = 0
        
        # 남은 문서 추가
        if current_chunk:
            chunks.append(current_chunk)
        
        return chunks
        self.build_category_hierarchy(normalized_docs)
        
        # 태그 어휘 구축
        self.build_tag_vocabulary(normalized_docs)
        
        self.normalized_docs = normalized_docs
        
        # 결과 저장
        self.save_normalized_data(output_dir)
        
        logger.info(f"데이터셋 정규화 완료: {len(normalized_docs)}개 문서")
        
        return normalized_docs
    
    def save_normalized_data(self, output_dir: Path):
        """정규화된 데이터 저장"""
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # 정규화된 문서 저장
        normalized_docs_data = [asdict(doc) for doc in self.normalized_docs]
        with open(output_dir / 'normalized_documents.json', 'w', encoding='utf-8') as f:
            json.dump(normalized_docs_data, f, ensure_ascii=False, indent=2)
        
        # 통계 정보 저장
        stats_data = asdict(self.stats)
        with open(output_dir / 'normalization_stats.json', 'w', encoding='utf-8') as f:
            json.dump(stats_data, f, ensure_ascii=False, indent=2)
        
        # 카테고리 계층 구조 저장
        with open(output_dir / 'category_hierarchy.json', 'w', encoding='utf-8') as f:
            json.dump(self.category_hierarchy, f, ensure_ascii=False, indent=2)
        
        # 태그 어휘 저장
        tag_vocabulary_data = {
            'total_tags': len(self.tag_vocabulary),
            'tags': sorted(list(self.tag_vocabulary))
        }
        with open(output_dir / 'tag_vocabulary.json', 'w', encoding='utf-8') as f:
            json.dump(tag_vocabulary_data, f, ensure_ascii=False, indent=2)
        
        # 코드 언어 통계 저장
        with open(output_dir / 'code_language_stats.json', 'w', encoding='utf-8') as f:
            json.dump(dict(self.code_language_stats), f, ensure_ascii=False, indent=2)
        
        logger.info(f"정규화된 데이터 저장 완료: {output_dir}")
    
    def generate_normalization_report(self, output_dir: Path = None):
        """정규화 보고서 생성"""
        if output_dir is None:
            output_dir = OUTPUT_DIR / 'reports'
        
        report_dir = output_dir / 'normalization_reports'
        report_dir.mkdir(parents=True, exist_ok=True)
        
        # 텍스트 보고서
        report_content = f"""
WinForms_Docs 데이터 정규화 보고서
==================================

정규화 일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

기본 통계:
- 총 문서 수: {self.stats.total_documents}
- 성공 정규화: {self.stats.normalized_documents}
- 실패 정규화: {self.stats.failed_documents}
- 성공률: {(self.stats.normalized_documents / self.stats.total_documents * 100):.1f}%

내용 통계:
- 총 단어 수: {self.stats.total_words:,}
- 총 문자 수: {self.stats.total_chars:,}
- 총 태그 수: {self.stats.total_tags:,}
- 총 코드 스니펫 수: {self.stats.total_code_snippets:,}
- 평균 단어 수: {self.stats.total_words / max(self.stats.normalized_documents, 1):.0f}
- 평균 태그 수: {self.stats.total_tags / max(self.stats.normalized_documents, 1):.1f}

정규화 통계:
- 정규화된 카테고리: {self.stats.normalized_categories}
- 정규화된 서브 카테고리: {self.stats.normalized_subcategories}
- 정규화된 제목: {self.stats.normalized_titles}
- 정규화된 태그: {self.stats.normalized_tags_count}

카테고리 계층 구조:
"""
        
        for category, subcategories in self.category_hierarchy.items():
            report_content += f"- {category}: {len(subcategories)}개 서브 카테고리\n"
            for subcategory in subcategories:
                report_content += f"  - {subcategory}\n"
        
        # 태그 통계
        report_content += f"\n태그 통계 (총 {len(self.tag_vocabulary)}개):\n"
        tag_counter = Counter()
        for doc in self.normalized_docs:
            tag_counter.update(doc.normalized_tags)
        
        for tag, count in tag_counter.most_common(20):
            report_content += f"- {tag}: {count}회\n"
        
        # 코드 언어 통계
        report_content += f"\n코드 언어 통계:\n"
        for language, count in sorted(self.code_language_stats.items(), key=lambda x: x[1], reverse=True):
            report_content += f"- {language}: {count}개 스니펫\n"
        
        # 보고서 파일 저장
        with open(report_dir / 'normalization_report.txt', 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        logger.info(f"정규화 보고서 생성 완료: {report_dir / 'normalization_report.txt'}")

def main():
    """메인 실행 함수"""
    logger.info("WinForms_Docs 데이터 정규화 시작")
    
    # 데이터 정규화기 초기화
    normalizer = DataNormalizer()
    
    # 정규화된 데이터 파일 경로
    input_file = OUTPUT_DIR / 'json_data' / 'processed_documents.json'
    
    if not input_file.exists():
        logger.error(f"입력 파일을 찾을 수 없습니다: {input_file}")
        return
    
    # 데이터셋 정규화
    normalized_docs = normalizer.normalize_dataset(input_file)
    
    # 정규화 보고서 생성
    normalizer.generate_normalization_report()
    
    # 최종 로그
    logger.info(f"데이터 정규화 완료. 성공: {normalizer.stats.normalized_documents}, 실패: {normalizer.stats.failed_documents}")

if __name__ == "__main__":
    main()