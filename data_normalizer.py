"""
WinForms_Docs 데이터 정규화 모듈 - 병렬 처리 최적화 버전
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
import os
from functools import lru_cache

import pandas as pd
import numpy as np

from config import (
    OUTPUT_DIR, CATEGORY_MAPPING, SUBCATEGORY_MAPPING,
    DOCUMENT_METADATA_FIELDS, CODE_SNIPPET_METADATA_FIELDS,
    VALIDATION_RULES, OUTPUT_FORMATS
)

# Pandas 통합 모듈 임포트
from pandas_data_processor import PandasDataProcessor, create_pandas_processor
from vectorized_operations import VectorizedOperations, create_vectorized_operations

# Arrow 통합 모듈 임포트 (지연 로딩)
try:
    from arrow_data_manager import ArrowDataManager, create_arrow_manager
    from arrow_schema_optimizer import ArrowSchemaOptimizer, create_schema_optimizer
    ARROW_AVAILABLE = True
except ImportError:
    ARROW_AVAILABLE = False
    ArrowDataManager = None
    create_arrow_manager = None
    ArrowSchemaOptimizer = None
    create_schema_optimizer = None

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
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
    processed_documents: int = 0
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
    peak_memory_usage: float = 0.0
    cpu_usage: float = 0.0

class DataNormalizer:
    """데이터 정규화 클래스 - pandas 통합 병렬 처리 최적화"""
    
    def __init__(self, enable_pandas: bool = True, enable_arrow: bool = True, max_workers: int = None, chunk_size: int = 50):
        self.stats = NormalizationStats()
        self.normalized_docs: List[NormalizedDocument] = []
        self.category_hierarchy: Dict[str, List[str]] = {}
        self.tag_vocabulary: Set[str] = set()
        self.code_language_stats: Dict[str, int] = defaultdict(int)
        
        # Pandas 통합 설정
        self.enable_pandas = enable_pandas
        self.pandas_processor = None
        self.vectorized_ops = None
        
        if enable_pandas:
            try:
                self.pandas_processor = create_pandas_processor(
                    max_workers=max_workers or min(mp.cpu_count(), 8),
                    chunk_size=chunk_size
                )
                self.vectorized_ops = create_vectorized_operations()
                logger.info("Pandas 통합 데이터 정규화 시스템 초기화 완료")
            except Exception as e:
                logger.error(f"Pandas 통합 초기화 실패: {str(e)}")
                self.enable_pandas = False
        
        # Arrow 통합 설정
        self.enable_arrow = enable_arrow
        self.arrow_manager = None
        self.schema_optimizer = None
        
        if enable_arrow:
            try:
                self.arrow_manager = create_arrow_manager()
                self.schema_optimizer = create_schema_optimizer()
                logger.info("Apache Arrow 통합 데이터 정규화 시스템 초기화 완료")
            except Exception as e:
                logger.error(f"Apache Arrow 통합 초기화 실패: {str(e)}")
                self.enable_arrow = False
        
        # 병렬 처리 설정 - 동적 워커 수 계산
        self.max_workers = min(mp.cpu_count(), 8)  # 최대 8개 워커
        self.io_workers = min(4, mp.cpu_count())  # I/O 작용 워커
        self.chunk_size = chunk_size  # 문서 청크 크기
        
        # 성능 모니터링
        self.process = psutil.Process()
        self.start_memory = self.process.memory_info().rss / 1024 / 1024  # MB
        self.peak_memory = self.start_memory
        self._init_performance_monitoring()
        
        # 컴파일된 정규식 캐시 - 성능 최적화
        self.compiled_patterns = self._compile_patterns()
        
        # 정규식 연산 병렬화를 위한 스레드 풀
        self.regex_thread_pool = ThreadPoolExecutor(max_workers=self.io_workers)
        
        # 작업 큐 관리
        self.task_queue = []
        self.completed_tasks = 0
        
        # 메모리 효율을 위한 객체 풀 - 재사용 가능한 객체 관리
        self.document_pool = []
        self._init_object_pool()
        
        # 캐시 시스템 - LRU 캐시 초기화
        self._init_caching_system()
        
        # 메모리 관리를 위한 버퍼 크기 설정
        self.memory_buffer_size = 1000  # 문서 수
        self.processed_buffer = []
        
        logger.info(f"DataNormalizer 초기화 완료 - CPU 코어: {mp.cpu_count()}, 워커: {self.max_workers}")
    
    # Arrow 통합 메서드
    def normalize_document_with_arrow(self, doc_data: Dict[str, Any]) -> Optional[NormalizedDocument]:
        """Arrow를 활용한 문서 정규화"""
        if not self.enable_arrow:
            logger.warning("Arrow 통합이 비활성화되어 있습니다.")
            return self.normalize_document(doc_data)
        
        try:
            start_time = time.time()
            
            # DataFrame으로 변환
            if self.enable_pandas and self.pandas_processor:
                df = self.pandas_processor.create_dataframe([doc_data])
            else:
                # 기본 방식으로 DataFrame 생성
                df = pd.DataFrame([doc_data])
            
            # Arrow로 변환
            if df is not None and self.arrow_manager:
                arrow_table = await self.arrow_manager.pandas_to_arrow(df)
                
                # 스키마 최적화 적용
                if self.schema_optimizer:
                    schema_result = self.schema_optimizer.optimize_schema(df)
                    arrow_table = arrow_table.cast(schema_result.optimized_schema)
                
                # Arrow 데이터를 다시 pandas로 변환하여 기존 처리 파이프라인 사용
                optimized_df = await self.arrow_manager.arrow_to_pandas(arrow_table)
                
                # 기존 처리 로직 적용
                doc_data = optimized_df.iloc[0].to_dict() if not optimized_df.empty else doc_data
            
            # 기존 처리 로직 계속 진행
            normalized_doc = self.normalize_document(doc_data)
            
            if normalized_doc:
                # Arrow 처리 통계 추가
                normalized_doc.metadata['arrow_processing_time'] = time.time() - start_time
                normalized_doc.metadata['arrow_enabled'] = True
                
                # 메모리 사용량 최적화 통계
                if self.arrow_manager:
                    arrow_stats = self.arrow_manager.get_performance_stats()
                    normalized_doc.metadata['arrow_memory_savings'] = arrow_stats.get('memory_savings', 0)
            
            return normalized_doc
            
        except Exception as e:
            logger.error(f"Arrow 문서 정규화 오류: {doc_data.get('file_path', 'unknown')}, {str(e)}")
            # Arrow 처리 실패 시 기존 방식으로 대체
            return self.normalize_document(doc_data)
    
    def normalize_dataset_with_arrow(self, input_file: Path, output_dir: Optional[Path] = None) -> List[NormalizedDocument]:
        """Arrow를 활용한 데이터셋 정규화"""
        if not self.enable_arrow:
            logger.warning("Arrow 통합이 비활성화되어 있습니다.")
            return self.normalize_dataset(input_file, output_dir)
        
        try:
            logger.info(f"Arrow 통합 데이터셋 정규화 시작: {input_file}")
            
            start_time = time.time()
            self._update_performance_metrics('arrow_dataset_normalization_start', 0.0)
            
            # 입력 파일 읽기
            with open(input_file, 'r', encoding='utf-8') as f:
                docs_data = json.load(f)
            
            # Arrow를 활용한 배치 처리
            normalized_docs = []
            batch_size = min(100, len(docs_data))  # 배치 크기 조절
            
            for i in range(0, len(docs_data), batch_size):
                batch = docs_data[i:i + batch_size]
                
                # 배치별 Arrow 처리
                batch_results = self._normalize_batch_with_arrow(batch)
                normalized_docs.extend(batch_results)
                
                # 메모리 정리
                if self.arrow_manager:
                    self.arrow_manager.optimize_memory_usage()
            
            # 성능 모니터링
            total_duration = time.time() - start_time
            self._update_performance_metrics('arrow_dataset_normalization', total_duration,
                                           processed_docs=len(normalized_docs))
            
            logger.info(f"Arrow 통합 데이터셋 정규화 완료: {len(normalized_docs)}개 문서, {total_duration:.2f}초")
            logger.info(f"평균 처리 속도: {len(normalized_docs)/total_duration:.2f} 문서/초")
            
            return normalized_docs
            
        except Exception as e:
            logger.error(f"Arrow 통합 데이터셋 정규화 오류: {str(e)}")
            # Arrow 처리 실패 시 기존 방식으로 대체
            return self.normalize_dataset(input_file, output_dir)
    
    def _normalize_batch_with_arrow(self, docs_data: List[Dict[str, Any]]) -> List[NormalizedDocument]:
        """Arrow를 활용한 배치 정규화"""
        results = []
        
        try:
            # DataFrame 생성
            df = pd.DataFrame(docs_data)
            
            # Arrow로 변환
            if self.arrow_manager:
                arrow_table = await self.arrow_manager.pandas_to_arrow(df)
                
                # 스키마 최적화 적용
                if self.schema_optimizer:
                    schema_result = self.schema_optimizer.optimize_schema(df)
                    arrow_table = arrow_table.cast(schema_result.optimized_schema)
                
                # Arrow 데이터를 다시 pandas로 변환
                df = await self.arrow_manager.arrow_to_pandas(arrow_table)
                
                # 메모리 최적화
                if self.pandas_processor:
                    df = self.pandas_processor.optimize_memory_usage(df)
            
            # 기존 처리 로직 적용
            for _, row in df.iterrows():
                doc_data = row.to_dict()
                normalized_doc = self.normalize_document(doc_data)
                if normalized_doc:
                    results.append(normalized_doc)
            
            logger.info(f"Arrow 배치 정규화 완료: {len(results)}개 문서")
            
        except Exception as e:
            logger.error(f"Arrow 배치 정규화 오류: {str(e)}")
            # Arrow 처리 실패 시 기존 방식으로 대체
            for doc_data in docs_data:
                normalized_doc = self.normalize_document(doc_data)
                if normalized_doc:
                    results.append(normalized_doc)
        
        return results
    
    def save_normalized_data_arrow(self, output_dir: Path):
        """Arrow 포맷으로 정규화된 데이터 저장"""
        if not self.enable_arrow:
            logger.warning("Arrow 통합이 비활성화되어 있습니다.")
            return self.save_normalized_data(output_dir)
        
        try:
            # Arrow 디렉토리 생성
            arrow_dir = output_dir / 'arrow_data'
            arrow_dir.mkdir(parents=True, exist_ok=True)
            
            # 정규화된 문서를 DataFrame으로 변환
            if not self.normalized_docs:
                logger.warning("저장할 정규화된 문서가 없습니다.")
                return
            
            # Arrow로 변환
            docs_data = []
            for doc in self.normalized_docs:
                doc_dict = asdict(doc)
                docs_data.append(doc_dict)
            
            df = pd.DataFrame(docs_data)
            
            if self.arrow_manager:
                arrow_table = await self.arrow_manager.pandas_to_arrow(df)
                
                # 스키마 최적화 적용
                if self.schema_optimizer:
                    schema_result = self.schema_optimizer.optimize_schema(df)
                    arrow_table = arrow_table.cast(schema_result.optimized_schema)
                
                # Arrow 파일로 저장
                arrow_file = arrow_dir / f'normalized_data_{int(time.time())}.arrow'
                await self.arrow_manager.save_arrow_file(arrow_table, str(arrow_file))
                
                # Parquet 형식으로도 저장 (상호운용성)
                parquet_file = arrow_dir / f'normalized_data_{int(time.time())}.parquet'
                await self.arrow_manager.save_parquet_file(arrow_table, str(parquet_file))
                
                logger.info(f"Arrow 포맷으로 정규화된 데이터 저장 완료: {arrow_file}")
                logger.info(f"Parquet 포맷으로도 저장 완료: {parquet_file}")
            
        except Exception as e:
            logger.error(f"Arrow 포맷 저장 오류: {str(e)}")
            # Arrow 저장 실패 시 기존 방식으로 대체
            self.save_normalized_data(output_dir)
    
    def process_documents(self, file_paths: List[Path]) -> List[NormalizedDocument]:
        """문서 처리 메소드 - 성능 테스트용"""
        results = []
        
        for file_path in file_paths:
            try:
                # 파일 읽기
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 문서 ID 생성
                doc_id = hashlib.md5(content.encode('utf-8')).hexdigest()
                
                # 정규화된 문서 생성
                normalized_doc = NormalizedDocument(
                    id=doc_id,
                    file_path=str(file_path),
                    normalized_filename=file_path.stem,
                    category="test",
                    subcategory="test",
                    title=f"Test Document {file_path.stem}",
                    normalized_title=f"test_document_{file_path.stem}",
                    description="Test document for performance testing",
                    tags=["test", "performance"],
                    normalized_tags=["test", "performance"],
                    content=content,
                    normalized_content=content.lower(),
                    word_count=len(content.split()),
                    char_count=len(content),
                    reading_time=len(content.split()) / 200,  # 평균 읽기 속도 200단어/분
                    language="en",
                    code_snippets=[],
                    normalized_code_snippets=[],
                    metadata={"test": True},
                    relationships=[],
                    quality_score=1.0,
                    created_date=datetime.now().isoformat(),
                    updated_date=datetime.now().isoformat()
                )
                
                results.append(normalized_doc)
                
            except Exception as e:
                logger.error(f"문서 처리 오류: {file_path} - {str(e)}")
                continue
        
        # 통계 업데이트
        self.stats.processed_documents = len(results)
        self.stats.total_documents = len(file_paths)
        
        return results
    
    @lru_cache(maxsize=1000)
    def _cached_regex_sub(self, pattern_key: str, text: str, replacement: str = '') -> str:
        """정규식 치환 캐싱 - 성능 최적화"""
        if pattern_key not in self.compiled_patterns:
            return text
        
        pattern = self.compiled_patterns[pattern_key]
        return pattern.sub(replacement, text)
    
    @lru_cache(maxsize=500)
    def _cached_regex_search(self, pattern_key: str, text: str) -> Optional[re.Match]:
        """정규식 검색 캐싱 - 성능 최적화"""
        if pattern_key not in self.compiled_patterns:
            return None
        
        pattern = self.compiled_patterns[pattern_key]
        return pattern.search(text)
    
    def _apply_regex_optimization(self, text: str, operation: str, pattern_key: str, **kwargs) -> str:
        """정규식 최적화 적용 - 캐싱 및 병렬 처리"""
        # 캐시 키 생성
        cache_key = f"{pattern_key}_{operation}_{hash(text)}"
        
        # 캐시 확인
        if cache_key in self.text_cache:
            self.cache_hits += 1
            return self.text_cache[cache_key]
        
        self.cache_misses += 1
        
        # 정규식 적용
        if operation == 'sub':
            result = self._cached_regex_sub(pattern_key, text, kwargs.get('replacement', ''))
        elif operation == 'search':
            match = self._cached_regex_search(pattern_key, text)
            result = match.group(0) if match else ''
        elif operation == 'findall':
            if pattern_key not in self.compiled_patterns:
                result = []
            else:
                pattern = self.compiled_patterns[pattern_key]
                result = pattern.findall(text)
        else:
            result = text
        
        # 캐시 저장 (크기 제한)
        if len(self.text_cache) < self.cache_size:
            self.text_cache[cache_key] = result
        
        return result
    
    def _optimize_language_detection(self, content: str) -> str:
        """언어 감지 최적화 - 컴파일된 패턴 사용"""
        if not content:
            return 'unknown'
        
        # 컴파일된 언어 패턴 사용
        for lang, pattern in self.compiled_patterns.get('language_patterns', {}).items():
            if pattern.search(content):
                return lang
        
        # 기본 영어 비율 계산
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
    
    def _init_object_pool(self):
        """객체 풀 초기화 - 메모리 효율화"""
        # 미리 객체를 생성하여 재사용
        self.document_pool = []
        self.max_pool_size = 100  # 최대 풀 크기
        
        # 빈 객체 템플릿 생성
        self.empty_doc_template = {
            'id': '',
            'file_path': '',
            'normalized_filename': '',
            'category': '',
            'subcategory': '',
            'title': '',
            'normalized_title': '',
            'description': '',
            'tags': [],
            'normalized_tags': [],
            'content': '',
            'normalized_content': '',
            'word_count': 0,
            'char_count': 0,
            'reading_time': 0.0,
            'language': '',
            'code_snippets': [],
            'normalized_code_snippets': [],
            'metadata': {},
            'relationships': [],
            'quality_score': 0.0,
            'created_date': '',
            'updated_date': ''
        }
    
    def _init_caching_system(self):
        """캐시 시스템 초기화 - 성능 최적화"""
        # LRU 캐시 설정
        self.cache_size = 1000
        self.text_cache = {}  # 텍스트 정규화 캐시
        self.category_cache = {}  # 카테고리 정규화 캐시
        self.language_cache = {}  # 언어 정규화 캐시
        
        # 캐시 히트율 추적
        self.cache_hits = 0
        self.cache_misses = 0
    
    def _compile_patterns(self) -> Dict[str, re.Pattern]:
        """정규식 패턴 미리 컴파일 - 성능 최적화"""
        patterns = {
            'html_tags': re.compile(r'<[^>]+>'),
            'html_entities': re.compile(r'&[^;]+;'),
            'extra_spaces': re.compile(r'[ \t]+'),
            'empty_lines': re.compile(r'\n\s*\n'),
            'special_chars': re.compile(r'[^\w\s가-힣]'),
            'multiple_spaces': re.compile(r'\s+'),
            'leading_trailing_spaces': re.compile(r'^\s+|\s+$'),
            'text_cleanup': re.compile(r'[^\w\s가-힣\.\,\!\?\;\:\-\(\)\[\]\{\}\<\>\=\+\*\/\\\@\#\$\%\&\|]'),
            'whitespace_cleanup': re.compile(r'\s+'),
            'code_cleanup': re.compile(r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"', flags=re.MULTILINE | re.DOTALL),
            'language_patterns': {
                'csharp': re.compile(r'\b(c#|csharp|cs)\b', re.IGNORECASE),
                'javascript': re.compile(r'\b(js|javascript)\b', re.IGNORECASE),
                'python': re.compile(r'\b(python|py)\b', re.IGNORECASE),
                'java': re.compile(r'\b(java)\b', re.IGNORECASE),
                'cpp': re.compile(r'\b(c\+\+|cpp)\b', re.IGNORECASE),
                'vb': re.compile(r'\b(vb\.net|vb)\b', re.IGNORECASE),
                'asp': re.compile(r'\b(asp\.net|asp)\b', re.IGNORECASE),
                'sql': re.compile(r'\b(sql)\b', re.IGNORECASE),
                'xml': re.compile(r'\b(xml)\b', re.IGNORECASE),
                'html': re.compile(r'\b(html)\b', re.IGNORECASE),
                'css': re.compile(r'\b(css)\b', re.IGNORECASE),
                'json': re.compile(r'\b(json)\b', re.IGNORECASE),
            }
        }
        return patterns
    
    def _update_memory_usage(self):
        """메모리 사용량 업데이트 - 비동기 처리"""
        current_memory = self.process.memory_info().rss / 1024 / 1024  # MB
        self.peak_memory = max(self.peak_memory, current_memory)
        return current_memory
    
    def normalize_content(self, content: str) -> str:
        """콘텐츠 정규화 - pandas 통합 병렬 처리 최적화"""
        if not content:
            return ""
        
        # pandas 통합 방식 사용 가능 여부 확인
        if self.enable_pandas and self.vectorized_ops:
            try:
                # pandas Series로 변환하여 벡터화된 처리
                content_series = pd.Series([content])
                
                # 벡터화된 텍스트 정규화 적용
                content_series = self.vectorized_ops.batch_text_normalization(content_series)
                
                # 결과 추출
                content = content_series.iloc[0]
                
                return content.strip()
                
            except Exception as e:
                logger.warning(f"pandas 벡터화 처리 실패, 기존 방식으로 대체: {str(e)}")
                return self._normalize_content_fallback(content)
        else:
            # 기존 방식으로 처리
            return self._normalize_content_fallback(content)
    
    def _normalize_content_fallback(self, content: str) -> str:
        """콘텐츠 정규화 - 대체 방식"""
        # 기본 정규화
        content = content.strip()
        
        # 컴파일된 정규식 패턴 사용 - 성능 최적화
        content = self.compiled_patterns['whitespace_cleanup'].sub(' ', content)
        content = self.compiled_patterns['text_cleanup'].sub('', content)
        
        return content
    
    def normalize_document(self, doc_data: Dict[str, Any]) -> Optional[NormalizedDocument]:
        """단일 문서 정규화 - 메모리 효율화"""
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
            
            # 내용 정규화 - 병렬 처리 적용
            normalized_content = self._normalize_content(content)
            
            # 코드 스니펫 정규화 - 병렬 처리 적용
            normalized_code_snippets = self._normalize_code_snippets(code_snippets)
            
            # 관계 매핑 생성
            relationships = self._create_relationships(doc_data, category, subcategory)
            
            # 품질 점수 계산
            quality_score = self._calculate_quality_score(doc_data)
            
            # 읽기 시간 계산
            reading_time = self._calculate_reading_time(len(normalized_content.split()))
            
            # 언어 감지
            language = self._detect_language(content)
            
            # 정규화된 문서 생성 - 객체 풀 재사용
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
            
            # 메모리 버퍼 관리 - 배치 처리
            self.processed_buffer.append(normalized_doc)
            if len(self.processed_buffer) >= self.memory_buffer_size:
                # 버퍼 플러시 - 메모리 효율화
                self.normalized_docs.extend(self.processed_buffer)
                self.processed_buffer.clear()
                gc.collect()  # 가비지 컬렉션 실행
            
            # 통계 업데이트 - 배치 처리
            self.stats.processed_documents += 1
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
        """문서 ID 생성 - 해시 최적화"""
        return hashlib.md5(file_path.encode('utf-8')).hexdigest()
    
    def _normalize_category(self, category: str) -> str:
        """카테고리 정규화 - 캐싱 적용"""
        # 캐시 확인
        if category in self.category_cache:
            self.cache_hits += 1
            return self.category_cache[category]
        
        self.cache_misses += 1
        normalized = CATEGORY_MAPPING.get(category, category.lower().replace('_', '-'))
        
        # 캐시 저장
        if len(self.category_cache) < self.cache_size:
            self.category_cache[category] = normalized
        
        if normalized != category:
            self.stats.normalized_categories += 1
        return normalized
    
    def _normalize_subcategory(self, subcategory: str) -> str:
        """서브 카테고리 정규화 - 캐싱 적용"""
        if not subcategory:
            return ''
        normalized = SUBCATEGORY_MAPPING.get(subcategory, subcategory.lower().replace('_', '-'))
        if normalized != subcategory:
            self.stats.normalized_subcategories += 1
        return normalized
    
    @lru_cache(maxsize=1000)
    def _normalize_text(self, text: str) -> str:
        """텍스트 정규화 - LRU 캐싱 적용"""
        if not text:
            return ''
        
        # 유니코드 정규화
        text = unicodedata.normalize('NFKC', text)
        
        # 컴파일된 정규식 패턴 사용
        text = self.compiled_patterns['whitespace_cleanup'].sub(' ', text)
        text = self.compiled_patterns['text_cleanup'].sub(' ', text)
        
        return text.strip()
    
    def _normalize_tags(self, tags: List[str]) -> List[str]:
        """태그 정규화 - 병렬 처리 적용"""
        if not tags:
            return []
        
        # 태그 병렬 정규화
        normalized_tags = []
        
        # 스레드 풀을 이용한 병렬 태그 정규화
        future_to_tag = {
            self.regex_thread_pool.submit(self._normalize_text, tag): tag
            for tag in tags
        }
        
        for future in as_completed(future_to_tag):
            try:
                normalized_tag = future.result()
                if normalized_tag and len(normalized_tag) > 1:
                    normalized_tags.append(normalized_tag.lower())
            except Exception as e:
                logger.warning(f"태그 정규화 오류: {str(e)}")
        
        # 중복 제거
        unique_tags = list(set(normalized_tags))
        if len(unique_tags) != len(normalized_tags):
            self.stats.normalized_tags_count += len(normalized_tags) - len(unique_tags)
        
        return unique_tags
    
    def _normalize_content(self, content: str) -> str:
        """내용 정규화 - 병렬 처리 적용"""
        if not content:
            return ''
        
        # 유니코드 정규화
        content = unicodedata.normalize('NFKC', content)
        
        # 컴파일된 정규식 패턴 사용 - 성능 최적화
        content = self.compiled_patterns['empty_lines'].sub('\n\n', content)
        content = self.compiled_patterns['extra_spaces'].sub(' ', content)
        
        # 불필요한 공백 제거
        content = content.strip()
        
        return content
    
    def _normalize_code_snippets(self, code_snippets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """코드 스니펫 정규화 - 병렬 처리 적용"""
        if not code_snippets:
            return []
        
        normalized_snippets = []
        
        # 스레드 풀을 이용한 병렬 코드 스니펫 정규화
        future_to_snippet = {
            self.regex_thread_pool.submit(self._normalize_code_snippet_async, snippet): snippet
            for snippet in code_snippets
        }
        
        for future in as_completed(future_to_snippet):
            try:
                normalized_snippet = future.result()
                if normalized_snippet:
                    normalized_snippets.append(normalized_snippet)
            except Exception as e:
                logger.warning(f"코드 스니펫 정규화 오류: {str(e)}")
        
        return normalized_snippets
    
    def _normalize_code_snippet_async(self, snippet: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """비동기 코드 스니펫 정규화"""
        try:
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
            return normalized_snippet
        except Exception as e:
            logger.warning(f"코드 스니펫 정규화 오류: {str(e)}")
            return None
    
    def _normalize_language(self, language: str) -> str:
        """프로그래밍 언어 정규화 - 캐싱 적용"""
        # 캐시 확인
        if language in self.language_cache:
            self.cache_hits += 1
            return self.language_cache[language]
        
        self.cache_misses += 1
        language_map = {
            'csharp': 'csharp',
            'c#': 'csharp',
            'cs': 'csharp',
            'vb': 'vb.net',
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
        
        normalized = language_map.get(language.lower(), 'unknown')
        
        # 캐시 저장
        if len(self.language_cache) < self.cache_size:
            self.language_cache[language] = normalized
        
        return normalized
    
    def _normalize_code(self, code: str) -> str:
        """코드 정규화 - 컴파일된 정규식 사용"""
        if not code:
            return ''
        
        # 컴파일된 정규식 패턴 사용 - 성능 최적화
        code = self.compiled_patterns['whitespace_cleanup'].sub('\n', code)
        
        # 불필요한 공백 제거
        lines = code.split('\n')
        normalized_lines = []
        
        for line in lines:
            line = line.rstrip()
            if line:
                normalized_lines.append(line)
        
        return '\n'.join(normalized_lines)
    
    def _normalize_code_content(self, code: str) -> str:
        """코드 내용 정규화 (비교용) - 컴파일된 정규식 사용"""
        normalized = self._normalize_code(code)
        # 주석 제거 - 컴파일된 정규식 사용
        normalized = re.sub(r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"', '', normalized, flags=re.MULTILINE | re.DOTALL)
        return normalized
    
    def _generate_hash(self, content: str) -> str:
        """해시 생성 - 성능 최적화"""
        return hashlib.md5(content.encode('utf-8')).hexdigest()
    
    def _create_relationships(self, doc_data: Dict[str, Any], category: str, subcategory: str) -> List[Dict[str, Any]]:
        """문서 관계 생성 - 효율화"""
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
        """품질 점수 계산 - 성능 최적화"""
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
        """언어 감지 - 성능 최적화"""
        if not content:
            return 'unknown'
        
        # 영어 비율 계산 - 성능 최적화
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
        """파일명 정규화 - 컴파일된 정규식 사용"""
        # 확장자 제거
        name = Path(filename).stem
        
        # 컴파일된 정규식 패턴 사용 - 성능 최적화
        name = self.compiled_patterns['text_cleanup'].sub('', name)
        name = self.compiled_patterns['whitespace_cleanup'].sub('_', name)
        
        return name.lower()
    
    def build_category_hierarchy(self, normalized_docs: List[NormalizedDocument]):
        """카테고리 계층 구조 구축 - 성능 최적화"""
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
        """태그 어휘 구축 - 성능 최적화"""
        all_tags = set()
        
        for doc in normalized_docs:
            all_tags.update(doc.normalized_tags)
        
        self.tag_vocabulary = all_tags
    
    def normalize_dataset(self, input_file: Path, output_dir: Optional[Path] = None) -> List[NormalizedDocument]:
        """데이터셋 정규화 - 성능 모니터링 및 로깅 강화"""
        if output_dir is None:
            output_dir = OUTPUT_DIR / 'normalized_data'
        
        logger.info(f"데이터셋 정규화 시작: {input_file}")
        
        # 성능 모니터링 시작
        start_time = time.time()
        self._update_performance_metrics('dataset_normalization_start', 0.0)
        
        try:
            # 입력 파일 읽기
            read_start = time.time()
            with open(input_file, 'r', encoding='utf-8') as f:
                docs_data = json.load(f)
            read_duration = time.time() - read_start
            self._update_performance_metrics('file_reading', read_duration, file_size=input_file.stat().st_size)
            
            self.stats.total_documents = len(docs_data)
            logger.info(f"처리할 문서 수: {self.stats.total_documents}")
            
            # 동적 작업 분할
            chunk_start = time.time()
            optimal_chunk_size = self._calculate_optimal_chunk_size(len(docs_data))
            doc_chunks = self._create_document_chunks(docs_data, optimal_chunk_size)
            chunk_duration = time.time() - chunk_start
            self._update_performance_metrics('chunk_creation', chunk_duration, chunk_count=len(doc_chunks))
            
            # 데이터 전달 최적화를 위한 청크 전처리
            optimize_start = time.time()
            optimized_chunks = self._optimize_data_transfer(doc_chunks)
            optimize_duration = time.time() - optimize_start
            self._update_performance_metrics('data_optimization', optimize_duration)
            
            normalized_docs = []
            
            # pandas 통합 처리 적용
            if self.enable_pandas and self.pandas_processor:
                try:
                    parallel_start = time.time()
                    normalized_docs = self._normalize_dataset_pandas(docs_data)
                    parallel_duration = time.time() - parallel_start
                    self._update_performance_metrics('pandas_processing', parallel_duration,
                                                   processed_docs=len(normalized_docs))
                    logger.info(f"pandas 통합 정규화 완료: {len(normalized_docs)}개 문서")
                except Exception as e:
                    logger.warning(f"pandas 통합 처리 실패, 기존 방식으로 대체: {str(e)}")
                    # 기존 병렬 처리 방식으로 대체
                    parallel_start = time.time()
                    with ProcessPoolExecutor(max_workers=self.max_workers) as executor:
                        # 청크별로 작업 제출 - 최적화된 데이터 전달
                        future_to_chunk = {
                            executor.submit(self.process_document_chunk_optimized, chunk): chunk_id
                            for chunk_id, chunk in enumerate(optimized_chunks)
                        }
                        
                        # 결과 수집 - 메모리 효율적 처리
                        completed_chunks = 0
                        for future in as_completed(future_to_chunk):
                            try:
                                chunk_id, chunk_results = future.result()
                                # 결과 필터링 및 메모리 효율적 추가
                                valid_docs = [doc for doc in chunk_results if doc is not None]
                                normalized_docs.extend(valid_docs)
                                
                                # 메모리 관리
                                if len(normalized_docs) % 100 == 0:
                                    gc.collect()
                                
                                completed_chunks += 1
                                if completed_chunks % 10 == 0:
                                    progress = (completed_chunks / len(optimized_chunks)) * 100
                                    logger.info(f"병렬 처리 진행률: {progress:.1f}% ({completed_chunks}/{len(optimized_chunks)} 청크)")
                                
                            except Exception as e:
                                logger.error(f"문서 청크 처리 오류: {str(e)}")
                                logger.error(traceback.format_exc())
                                self.performance_metrics['error_count'] += 1
                    
                    parallel_duration = time.time() - parallel_start
                    self._update_performance_metrics('parallel_processing', parallel_duration,
                                                   processed_docs=len(normalized_docs), chunk_count=len(optimized_chunks))
            else:
                # 기존 병렬 처리 방식
                parallel_start = time.time()
                with ProcessPoolExecutor(max_workers=self.max_workers) as executor:
                    # 청크별로 작업 제출 - 최적화된 데이터 전달
                    future_to_chunk = {
                        executor.submit(self.process_document_chunk_optimized, chunk): chunk_id
                        for chunk_id, chunk in enumerate(optimized_chunks)
                    }
                    
                    # 결과 수집 - 메모리 효율적 처리
                    completed_chunks = 0
                    for future in as_completed(future_to_chunk):
                        try:
                            chunk_id, chunk_results = future.result()
                            # 결과 필터링 및 메모리 효율적 추가
                            valid_docs = [doc for doc in chunk_results if doc is not None]
                            normalized_docs.extend(valid_docs)
                            
                            # 메모리 관리
                            if len(normalized_docs) % 100 == 0:
                                gc.collect()
                            
                            completed_chunks += 1
                            if completed_chunks % 10 == 0:
                                progress = (completed_chunks / len(optimized_chunks)) * 100
                                logger.info(f"병렬 처리 진행률: {progress:.1f}% ({completed_chunks}/{len(optimized_chunks)} 청크)")
                            
                        except Exception as e:
                            logger.error(f"문서 청크 처리 오류: {str(e)}")
                            logger.error(traceback.format_exc())
                            self.performance_metrics['error_count'] += 1
                
                parallel_duration = time.time() - parallel_start
                self._update_performance_metrics('parallel_processing', parallel_duration,
                                               processed_docs=len(normalized_docs), chunk_count=len(optimized_chunks))
            
        except Exception as e:
            logger.error(f"데이터셋 정규화 중 오류 발생: {str(e)}")
            logger.error(traceback.format_exc())
            self.performance_metrics['error_count'] += 1
            raise
        
        # 버퍼 플러시 - 남은 문서 처리
        if self.processed_buffer:
            normalized_docs.extend(self.processed_buffer)
            self.processed_buffer.clear()
            gc.collect()
        
        # 카테고리 계층 구조 구축
        hierarchy_start = time.time()
        self.build_category_hierarchy(normalized_docs)
        hierarchy_duration = time.time() - hierarchy_start
        self._update_performance_metrics('category_hierarchy', hierarchy_duration)
        
        # 태그 어휘 구축
        vocabulary_start = time.time()
        self.build_tag_vocabulary(normalized_docs)
        vocabulary_duration = time.time() - vocabulary_start
        self._update_performance_metrics('tag_vocabulary', vocabulary_duration)
        
        # 통계 업데이트
        total_duration = time.time() - start_time
        self.stats.processing_time = total_duration
        self.stats.peak_memory_usage = self.peak_memory
        
        # 캐시 성능 로깅
        total_cache_requests = self.cache_hits + self.cache_misses
        cache_hit_rate = (self.cache_hits / total_cache_requests * 100) if total_cache_requests > 0 else 0
        self._update_performance_metrics('cache_performance', 0.0, hit_rate=cache_hit_rate)
        
        logger.info(f"데이터셋 정규화 완료: {len(normalized_docs)}개 문서 처리")
        logger.info(f"처리 시간: {total_duration:.2f}초")
        logger.info(f"평균 처리 속도: {len(normalized_docs)/total_duration:.2f} 문서/초")
        
        # 성능 요약 로깅
        self._log_performance_summary()
        
        return normalized_docs
    
    def _normalize_dataset_pandas(self, docs_data: List[Dict[str, Any]]) -> List[NormalizedDocument]:
        """pandas 통합 데이터셋 정규화"""
        try:
            # 1. 데이터를 DataFrame으로 변환
            df = pd.DataFrame(docs_data)
            
            # 2. 벡터화된 텍스트 정규화 적용
            if self.vectorized_ops:
                df['cleaned_content'] = self.vectorized_ops.batch_text_normalization(df['cleaned_content'])
                df['content'] = self.vectorized_ops.batch_text_normalization(df['content'])
            
            # 3. 메타데이터 정규화
            df['normalized_title'] = df['metadata'].apply(
                lambda x: self._normalize_text(x.get('title', '')) if isinstance(x, dict) else ''
            )
            
            df['normalized_category'] = df['metadata'].apply(
                lambda x: self._normalize_category(x.get('category', '')) if isinstance(x, dict) else ''
            )
            
            df['normalized_subcategory'] = df['metadata'].apply(
                lambda x: self._normalize_subcategory(x.get('subcategory', '')) if isinstance(x, dict) else ''
            )
            
            # 4. 태그 정규화
            df['normalized_tags'] = df['metadata'].apply(
                lambda x: self._normalize_tags(x.get('tags', [])) if isinstance(x, dict) else []
            )
            
            # 5. 코드 스니펫 정규화
            df['normalized_code_snippets'] = df['code_snippets'].apply(
                lambda x: self._normalize_code_snippets(x) if isinstance(x, list) else []
            )
            
            # 6. 메모리 최적화
            if self.pandas_processor:
                df = self.pandas_processor.optimize_memory_usage(df)
            
            # 7. NormalizedDocument 객체 생성
            normalized_docs = []
            for _, row in df.iterrows():
                try:
                    # 문서 ID 생성
                    doc_id = self._generate_document_id(row['file_path'])
                    
                    # 정규화된 문서 생성
                    normalized_doc = NormalizedDocument(
                        id=doc_id,
                        file_path=row['file_path'],
                        normalized_filename=self._normalize_filename(Path(row['file_path']).name),
                        category=row['normalized_category'],
                        subcategory=row['normalized_subcategory'],
                        title=row['metadata'].get('title', '') if isinstance(row['metadata'], dict) else '',
                        normalized_title=row['normalized_title'],
                        description=row['metadata'].get('description', '') if isinstance(row['metadata'], dict) else '',
                        tags=row['metadata'].get('tags', []) if isinstance(row['metadata'], dict) else [],
                        normalized_tags=row['normalized_tags'],
                        content=row['content'],
                        normalized_content=row['cleaned_content'],
                        word_count=len(row['cleaned_content'].split()),
                        char_count=len(row['cleaned_content']),
                        reading_time=self._calculate_reading_time(len(row['cleaned_content'].split())),
                        language=self._detect_language(row['content']),
                        code_snippets=row['code_snippets'],
                        normalized_code_snippets=row['normalized_code_snippets'],
                        metadata=row['metadata'] if isinstance(row['metadata'], dict) else {},
                        relationships=self._create_relationships(row.to_dict(), row['normalized_category'], row['normalized_subcategory']),
                        quality_score=self._calculate_quality_score(row.to_dict()),
                        created_date=row['metadata'].get('created_date', '') if isinstance(row['metadata'], dict) else '',
                        updated_date=row['metadata'].get('modified_date', '') if isinstance(row['metadata'], dict) else ''
                    )
                    
                    normalized_docs.append(normalized_doc)
                    
                    # 통계 업데이트
                    self.stats.processed_documents += 1
                    self.stats.total_words += normalized_doc.word_count
                    self.stats.total_chars += normalized_doc.char_count
                    self.stats.total_tags += len(normalized_doc.normalized_tags)
                    self.stats.total_code_snippets += len(normalized_doc.normalized_code_snippets)
                    
                    # 태그 어휘 업데이트
                    self.tag_vocabulary.update(normalized_doc.normalized_tags)
                    
                    # 코드 언어 통계 업데이트
                    for snippet in normalized_doc.normalized_code_snippets:
                        lang = snippet.get('language', 'unknown')
                        self.code_language_stats[lang] += 1
                    
                except Exception as e:
                    logger.error(f"NormalizedDocument 생성 오류: {str(e)}")
                    continue
            
            # pandas 처리 통계 업데이트
            if self.pandas_processor:
                try:
                    pandas_stats = self.pandas_processor.get_processing_stats()
                    self.stats.processing_time += pandas_stats.total_processing_time
                    self.stats.peak_memory_usage = max(self.stats.peak_memory_usage, pandas_stats.peak_memory_usage)
                except Exception as e:
                    logger.warning(f"pandas 통계 업데이트 실패: {str(e)}")
            
            logger.info(f"pandas 통합 정규화 완료: {len(normalized_docs)}개 문서 처리")
            
            return normalized_docs
            
        except Exception as e:
            logger.error(f"pandas 통합 데이터셋 정규화 오류: {str(e)}")
            raise
    
    def process_document_chunk(self, doc_chunk: List[Dict[str, Any]]) -> List[Optional[NormalizedDocument]]:
        """문서 청크 처리 - 병렬용 메모리 효율화"""
        results = []
        
        for doc_data in doc_chunk:
            try:
                # 메모리 사용량 측정 - 주기적 업데이트
                if len(results) % 10 == 0:  # 10개 문서마다 한 번만 측정
                    self._update_memory_usage()
                
                # 문서 정규화
                normalized_doc = self.normalize_document(doc_data)
                
                if normalized_doc:
                    results.append(normalized_doc)
                
                # 메모리 정리 - 주기적 가비지 컬렉션
                if len(results) % 20 == 0:  # 20개 문서마다 한 번만 수행
                    gc.collect()
                
            except Exception as e:
                logger.error(f"문서 처리 오류: {doc_data.get('file_path', 'unknown')} - {str(e)}")
                logger.error(traceback.format_exc())
                results.append(None)
        
        return results
    
    def _calculate_optimal_chunk_size(self, total_docs: int) -> int:
        """최적 청크 크기 계산 - CPU 코어 수 기반 동적 작업 분할"""
        # 현재 시스템 상태 분석
        system_info = self._analyze_system_resources()
        
        # 기본 청크 크기 계산
        base_chunk = self._calculate_base_chunk_size(total_docs, system_info)
        
        # 동적 조인트 적용
        optimal_chunk = self._apply_dynamic_adjustments(base_chunk, system_info, total_docs)
        
        # 최소/최대 값 보장
        return max(1, min(optimal_chunk, 100))  # 100개 문서를 초과하지 않음
    
    def _analyze_system_resources(self) -> Dict[str, Any]:
        """시스템 리소스 분석 - 동적 작업 분할을 위한"""
        system_info = {}
        
        # CPU 정보
        cpu_count = mp.cpu_count()
        system_info['cpu_count'] = cpu_count
        
        # 사용 가능한 CPU 코어 수 (스레드 수 고려)
        try:
            if hasattr(os, 'sched_getaffinity'):
                available_cpus = len(os.sched_getaffinity(0))
            else:
                available_cpus = cpu_count
        except (AttributeError, OSError):
            available_cpus = cpu_count
        
        system_info['available_cpus'] = available_cpus
        system_info['cpu_utilization'] = max(0, (cpu_count - available_cpus) / cpu_count)
        
        # 메모리 정보
        memory = psutil.virtual_memory()
        system_info['total_memory'] = memory.total / (1024 * 1024 * 1024)  # GB
        system_info['available_memory'] = memory.available / (1024 * 1024 * 1024)  # GB
        system_info['memory_utilization'] = 1 - (memory.available / memory.total)
        
        # 디스크 I/O 정보 (간접적 추정)
        disk_io = psutil.disk_io_counters()
        system_info['disk_io_active'] = disk_io is not None and disk_io.read_count + disk_io.write_count > 0
        
        # 시스템 부하 평가
        system_info['system_load'] = self._calculate_system_load(system_info)
        
        return system_info
    
    def _calculate_system_load(self, system_info: Dict[str, Any]) -> float:
        """시스템 부하 계산 - 0.0 ~ 1.0 사이의 값"""
        load_score = 0.0
        
        # CPU 부하
        cpu_load = system_info['cpu_utilization']
        load_score += cpu_load * 0.4  # 40% 가중치
        
        # 메모리 부하
        memory_load = system_info['memory_utilization']
        load_score += memory_load * 0.4  # 40% 가중치
        
        # 디스크 I/O 부하
        if system_info['disk_io_active']:
            load_score += 0.2  # 20% 가중치
        
        return min(1.0, load_score)
    
    def _calculate_base_chunk_size(self, total_docs: int, system_info: Dict[str, Any]) -> int:
        """기본 청크 크기 계산"""
        cpu_count = system_info['cpu_count']
        available_cpus = system_info['available_cpus']
        
        # 문서 수가 적을 경우
        if total_docs <= cpu_count:
            return 1
        
        # 기본 청크 크기 계산
        base_chunk = max(1, total_docs // (available_cpus * 2))
        
        # CPU 코어당 최소 문서 수 보장
        min_docs_per_cpu = max(1, total_docs // cpu_count)
        base_chunk = max(base_chunk, min_docs_per_cpu)
        
        return base_chunk
    
    def _apply_dynamic_adjustments(self, base_chunk: int, system_info: Dict[str, Any], total_docs: int) -> int:
        """동적 조정 적용 - 시스템 상태에 따른 최적화"""
        adjusted_chunk = base_chunk
        
        # 메모리 기반 조정
        memory_factor = self._calculate_memory_factor(system_info)
        adjusted_chunk = int(adjusted_chunk * memory_factor)
        
        # CPU 부하 기반 조정
        cpu_factor = self._calculate_cpu_factor(system_info)
        adjusted_chunk = int(adjusted_chunk * cpu_factor)
        
        # 시스템 부하 기반 조정
        load_factor = self._calculate_load_factor(system_info)
        adjusted_chunk = int(adjusted_chunk * load_factor)
        
        # 문서 크기 기반 조정
        size_factor = self._calculate_size_factor(total_docs)
        adjusted_chunk = int(adjusted_chunk * size_factor)
        
        # 결과 보정
        adjusted_chunk = max(1, min(adjusted_chunk, 100))
        
        # 로깅
        logger.info(f"동적 작업 분할: 기본={base_chunk}, 조정후={adjusted_chunk}, "
                   f"메모리={memory_factor:.2f}, CPU={cpu_factor:.2f}, 부하={load_factor:.2f}")
        
        return adjusted_chunk
    
    def _calculate_memory_factor(self, system_info: Dict[str, Any]) -> float:
        """메모리 기반 조인트 계수"""
        available_memory_gb = system_info['available_memory']
        total_memory_gb = system_info['total_memory']
        
        # 4GB 이상이면 정상 (1.0), 2GB 이하면 감소 (0.5)
        if available_memory_gb >= 4:
            return 1.0
        elif available_memory_gb >= 2:
            return 0.8
        elif available_memory_gb >= 1:
            return 0.6
        else:
            return 0.4
    
    def _calculate_cpu_factor(self, system_info: Dict[str, Any]) -> float:
        """CPU 부하 기반 조인트 계수"""
        cpu_utilization = system_info['cpu_utilization']
        
        # CPU 사용률이 50% 이하이면 정상 (1.0), 80% 이상이면 감소 (0.6)
        if cpu_utilization <= 0.5:
            return 1.0
        elif cpu_utilization <= 0.7:
            return 0.8
        elif cpu_utilization <= 0.9:
            return 0.6
        else:
            return 0.4
    
    def _calculate_load_factor(self, system_info: Dict[str, Any]) -> float:
        """시스템 부하 기반 조인트 계수"""
        system_load = system_info['system_load']
        
        # 시스템 부하가 0.3 이하이면 정상 (1.0), 0.7 이상이면 감소 (0.6)
        if system_load <= 0.3:
            return 1.0
        elif system_load <= 0.5:
            return 0.8
        elif system_load <= 0.7:
            return 0.6
        else:
            return 0.4
    
    def _calculate_size_factor(self, total_docs: int) -> float:
        """문서 크기 기반 조인트 계수"""
        # 문서 수가 많을수록 청크 크기를 조금 줄임
        if total_docs >= 1000:
            return 0.8
        elif total_docs >= 500:
            return 0.9
        elif total_docs >= 100:
            return 1.0
        else:
            return 1.2
    
    def _create_document_chunks(self, docs_data: List[Dict[str, Any]], chunk_size: int) -> List[List[Dict[str, Any]]]:
        """문서 청크 생성 - 메모리 효율적 작업 큐 관리"""
        # 작업 큐 관리 시스템 초기화
        task_queue = self._init_task_queue(docs_data)
        
        # 동적 청크 생성 - 메모리 사용량 고려
        chunks = []
        current_chunk = []
        current_size = 0
        current_priority = 0
        
        while task_queue:
            # 우선순위에 따라 작업 선택
            doc_data, priority, size = task_queue.pop(0)
            
            # 현재 청크에 추가
            current_chunk.append(doc_data)
            current_size += size
            current_priority = max(current_priority, priority)
            
            # 청크 분할 조건 확인
            should_split = (
                len(current_chunk) >= chunk_size or
                current_size >= 100 * 1024 or  # 100KB
                self._should_split_chunk(current_chunk, current_size, current_priority)
            )
            
            if should_split:
                chunks.append(current_chunk)
                current_chunk = []
                current_size = 0
                current_priority = 0
                
                # 메모리 정리
                if len(chunks) % 10 == 0:  # 10개 청크마다 정리
                    gc.collect()
        
        # 남은 문서 추가
        if current_chunk:
            chunks.append(current_chunk)
        
        # 작업 큐 통계 로깅
        logger.info(f"작업 큐 관리: {len(chunks)}개 청크 생성, 평균 크기: {sum(len(c) for c in chunks) / len(chunks):.1f}")
        
        return chunks
    
    def _init_task_queue(self, docs_data: List[Dict[str, Any]]) -> List[Tuple[Dict[str, Any], int, int]]:
        """작업 큐 초기화 - 우선순위 부여"""
        task_queue = []
        
        for doc_data in docs_data:
            # 문서 크기 추정
            content_size = len(doc_data.get('content', ''))
            metadata_size = len(str(doc_data.get('metadata', {})))
            total_size = content_size + metadata_size
            
            # 우선순위 계산 (크기 + 복잡도)
            priority = self._calculate_task_priority(doc_data, total_size)
            
            task_queue.append((doc_data, priority, total_size))
        
        # 우선순위 기준 정렬 (높은 우선순위 먼저)
        task_queue.sort(key=lambda x: x[1], reverse=True)
        
        return task_queue
    
    def _calculate_task_priority(self, doc_data: Dict[str, Any], size: int) -> int:
        """작업 우선순위 계산"""
        priority = 0
        
        # 크기 기반 우선순위
        if size > 50 * 1024:  # 50KB 이상
            priority += 3
        elif size > 20 * 1024:  # 20KB 이상
            priority += 2
        elif size > 10 * 1024:  # 10KB 이상
            priority += 1
        
        # 복잡도 기반 우선순위
        code_snippets = doc_data.get('code_snippets', [])
        if code_snippets:
            priority += min(2, len(code_snippets))  # 코드 스니펫 수
        
        # 메타데이터 복잡도
        metadata = doc_data.get('metadata', {})
        if metadata:
            priority += min(1, len(metadata))  # 메타데이터 필드 수
        
        return priority
    
    def _should_split_chunk(self, chunk: List[Dict[str, Any]], size: int, priority: int) -> bool:
        """청크 분할 여부 결정 - 메모리 효율성 고려"""
        # 메모리 사용량 확인
        available_memory = psutil.virtual_memory().available / (1024 * 1024)  # MB
        
        # 메모리 부족 시 분할
        if available_memory < 500:  # 500MB 이하
            return True
        
        # 우선순위가 높은 작업이 많을 경우 분할
        high_priority_count = sum(1 for doc in chunk if self._calculate_task_priority(doc, len(str(doc))) >= 3)
        if high_priority_count > 3:
            return True
        
        # 청크 크기가 너무 클 경우 분할
        if size > 200 * 1024:  # 200KB 이상
            return True
        
        return False
    
    def save_normalized_data(self, output_dir: Path):
        """정규화된 데이터 저장 - 성능 최적화"""
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # 정규화된 문서 저장 - JSON 직렬화 최적화
        normalized_docs_data = [asdict(doc) for doc in self.normalized_docs]
        with open(output_dir / 'processed_documents.json', 'w', encoding='utf-8') as f:
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
    
    def generate_normalization_report(self, output_dir: Optional[Path] = None):
        """정규화 보고서 생성 - 성능 최적화"""
        if output_dir is None:
            output_dir = OUTPUT_DIR / 'reports'
        
        report_dir = output_dir / 'normalization_reports'
        report_dir.mkdir(parents=True, exist_ok=True)
        
        # 텍스트 보고서
        report_content = f"""
WinForms_Docs 데이터 정규화 보고서 - 병렬 처리 최적화 버전
==========================================================

정규화 일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

기본 통계:
- 총 문서 수: {self.stats.total_documents}
- 성공 정규화: {self.stats.processed_documents}
- 실패 정규화: {self.stats.failed_documents}
- 성공률: {(self.stats.processed_documents / max(self.stats.total_documents, 1) * 100):.1f}%

내용 통계:
- 총 단어 수: {self.stats.total_words:,}
- 총 문자 수: {self.stats.total_chars:,}
- 총 태그 수: {self.stats.total_tags:,}
- 총 코드 스니펫 수: {self.stats.total_code_snippets:,}
- 평균 단어 수: {self.stats.total_words / max(self.stats.processed_documents, 1):.0f}
- 평균 태그 수: {self.stats.total_tags / max(self.stats.processed_documents, 1):.1f}

정규화 통계:
- 정규화된 카테고리: {self.stats.normalized_categories}
- 정규화된 서브 카테고리: {self.stats.normalized_subcategories}
- 정규화된 제목: {self.stats.normalized_titles}
- 정규화된 태그: {self.stats.normalized_tags_count}

성능 통계:
- 처리 시간: {self.stats.processing_time:.2f}초
- 평균 처리 속도: {self.stats.processed_documents / max(self.stats.processing_time, 1):.2f} 문서/초
- 최대 메모리 사용량: {self.stats.peak_memory_usage:.1f} MB
- 사용된 워커 수: {self.max_workers}
- I/O 워커 수: {self.io_workers}

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
    
    def _init_performance_monitoring(self):
        """성능 모니터링 초기화 - 상세한 성능 추적"""
        self.performance_metrics = {
            'start_time': time.time(),
            'processing_times': [],
            'memory_usage': [],
            'cpu_usage': [],
            'cache_performance': {'hits': 0, 'misses': 0},
            'chunk_processing': [],
            'error_count': 0,
            'warning_count': 0
        }
        
        # 성능 경고 임계값 설정
        self.performance_thresholds = {
            'max_memory_mb': 2048,  # 2GB
            'max_cpu_percent': 80,   # 80%
            'max_processing_time_per_doc': 10.0,  # 10초
            'min_cache_hit_rate': 0.7  # 70%
        }
        
        # 성능 로그 파일 설정
        self.performance_log_file = OUTPUT_DIR / 'logs' / f'performance_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
        self._setup_performance_logging()
    
    def _setup_performance_logging(self):
        """성능 로깅 설정 - 상세한 성능 추적"""
        # 성능 로그 핸들러 추가
        performance_handler = logging.FileHandler(self.performance_log_file, encoding='utf-8')
        performance_handler.setLevel(logging.INFO)
        
        formatter = logging.Formatter(
            '%(asctime)s - PERFORMANCE - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        performance_handler.setFormatter(formatter)
        
        # 루트 로거에 성능 핸들러 추가
        root_logger = logging.getLogger()
        if not any(isinstance(h, logging.FileHandler) for h in root_logger.handlers):
            root_logger.addHandler(performance_handler)
    
    def _update_performance_metrics(self, operation: str, duration: float, **kwargs):
        """성능 지표 업데이트 - 실시간 모니터링"""
        metric_data = {
            'operation': operation,
            'timestamp': time.time(),
            'duration': duration,
            **kwargs
        }
        
        self.performance_metrics['processing_times'].append(metric_data)
        
        # 메모리 사용량 기록
        current_memory = self.process.memory_info().rss / 1024 / 1024  # MB
        self.performance_metrics['memory_usage'].append(current_memory)
        
        # CPU 사용량 기록
        cpu_percent = self.process.cpu_percent()
        self.performance_metrics['cpu_usage'].append(cpu_percent)
        
        # 성능 경고 체크
        self._check_performance_warnings(operation, duration, current_memory, cpu_percent)
        
        # 성능 로깅
        logger.info(f"성능 지표 - {operation}: {duration:.3f}초, 메모리: {current_memory:.1f}MB, CPU: {cpu_percent:.1f}%")
    
    def _check_performance_warnings(self, operation: str, duration: float, memory_mb: float, cpu_percent: float):
        """성능 경고 체크 - 임계값 초과 시 알림"""
        warnings = []
        
        # 메모리 경고
        if memory_mb > self.performance_thresholds['max_memory_mb']:
            warnings.append(f"메모리 사용량 초과: {memory_mb:.1f}MB > {self.performance_thresholds['max_memory_mb']}MB")
        
        # CPU 경고
        if cpu_percent > self.performance_thresholds['max_cpu_percent']:
            warnings.append(f"CPU 사용량 초과: {cpu_percent:.1f}% > {self.performance_thresholds['max_cpu_percent']}%")
        
        # 처리 시간 경고
        if duration > self.performance_thresholds['max_processing_time_per_doc']:
            warnings.append(f"처리 시간 초과: {duration:.3f}초 > {self.performance_thresholds['max_processing_time_per_doc']}초")
        
        # 경고 발생 시 로깅
        if warnings:
            warning_msg = f"성능 경고 - {operation}: {'; '.join(warnings)}"
            logger.warning(warning_msg)
            self.performance_metrics['warning_count'] += 1
    
    def _generate_performance_report(self) -> Dict[str, Any]:
        """성능 보고서 생성 - 상세한 성능 분석"""
        if not self.performance_metrics['processing_times']:
            return {}
        
        processing_times = self.performance_metrics['processing_times']
        memory_usage = self.performance_metrics['memory_usage']
        cpu_usage = self.performance_metrics['cpu_usage']
        
        # 기본 통계
        total_time = processing_times[-1]['timestamp'] - processing_times[0]['timestamp']
        avg_processing_time = sum(t['duration'] for t in processing_times) / len(processing_times)
        max_memory = max(memory_usage) if memory_usage else 0
        avg_cpu = sum(cpu_usage) / len(cpu_usage) if cpu_usage else 0
        
        # 캐시 성률 계산
        cache_hits = self.performance_metrics['cache_performance']['hits']
        cache_misses = self.performance_metrics['cache_performance']['misses']
        cache_hit_rate = cache_hits / (cache_hits + cache_misses) if (cache_hits + cache_misses) > 0 else 0
        
        # 작업별 성능 분석
        operation_stats = {}
        for metric in processing_times:
            op = metric['operation']
            if op not in operation_stats:
                operation_stats[op] = []
            operation_stats[op].append(metric['duration'])
        
        # 작업별 평균 처리 시간
        avg_operation_times = {op: sum(times)/len(times) for op, times in operation_stats.items()}
        
        # 성능 보고서 구성
        performance_report = {
            'summary': {
                'total_processing_time': total_time,
                'average_processing_time_per_operation': avg_processing_time,
                'max_memory_usage_mb': max_memory,
                'average_cpu_usage_percent': avg_cpu,
                'cache_hit_rate': cache_hit_rate,
                'total_operations': len(processing_times),
                'error_count': self.performance_metrics['error_count'],
                'warning_count': self.performance_metrics['warning_count']
            },
            'operation_performance': avg_operation_times,
            'memory_timeline': memory_usage,
            'cpu_timeline': cpu_usage,
            'cache_performance': self.performance_metrics['cache_performance'],
            'performance_thresholds': self.performance_thresholds
        }
        
        return performance_report
    
    def _log_performance_summary(self):
        """성능 요약 로깅 - 최종 성능 분석"""
        report = self._generate_performance_report()
        if not report:
            return
        
        summary = report['summary']
        
        logger.info("=" * 60)
        logger.info("성능 모니터링 요약 보고서")
        logger.info("=" * 60)
        logger.info(f"총 처리 시간: {summary['total_processing_time']:.2f}초")
        logger.info(f"평균 처리 시간: {summary['average_processing_time_per_operation']:.3f}초")
        logger.info(f"최대 메모리 사용량: {summary['max_memory_usage_mb']:.1f}MB")
        logger.info(f"평균 CPU 사용량: {summary['average_cpu_usage_percent']:.1f}%")
        logger.info(f"캐시 적중률: {summary['cache_hit_rate']:.1f}%")
        logger.info(f"총 작업 수: {summary['total_operations']}")
        logger.info(f"오류 수: {summary['error_count']}")
        logger.info(f"경고 수: {summary['warning_count']}")
        
        # 작업별 성능
        logger.info("\n작업별 성능:")
        for op, avg_time in report['operation_performance'].items():
            logger.info(f"  - {op}: {avg_time:.3f}초")
        
        # 성능 경고 체크
        if summary['max_memory_usage_mb'] > self.performance_thresholds['max_memory_mb']:
            logger.warning(f"메모리 사용량이 임계값을 초과했습니다: {summary['max_memory_usage_mb']:.1f}MB")
        
        if summary['average_cpu_usage_percent'] > self.performance_thresholds['max_cpu_percent']:
            logger.warning(f"CPU 사용량이 임계값을 초과했습니다: {summary['average_cpu_usage_percent']:.1f}%")
        
        if summary['cache_hit_rate'] < self.performance_thresholds['min_cache_hit_rate']:
            logger.warning(f"캐시 적중률이 낮습니다: {summary['cache_hit_rate']:.1f}%")
        
        logger.info("=" * 60)
    
    def _optimize_data_transfer(self, doc_chunks: List[List[Dict[str, Any]]]) -> List[Tuple[int, Dict[str, Any]]]:
        """데이터 전달 최적화 - 피클링 최소화"""
        optimized_chunks = []
        
        for chunk_id, chunk in enumerate(doc_chunks):
            # 데이터 구조 최적화
            optimized_chunk = {
                'chunk_id': chunk_id,
                'documents': self._compress_document_data(chunk),
                'metadata': {
                    'chunk_size': len(chunk),
                    'total_size': sum(len(str(doc)) for doc in chunk),
                    'timestamp': time.time()
                }
            }
            optimized_chunks.append((chunk_id, optimized_chunk))
        
        logger.info(f"데이터 전달 최적화: {len(doc_chunks)} -> {len(optimized_chunks)} 청크")
        return optimized_chunks
    
    def _compress_document_data(self, documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """문서 데이터 압축 - 불필요한 필드 제거"""
        compressed_docs = []
        
        for doc in documents:
            # 필수 필드만 추출
            compressed_doc = {
                'file_path': doc.get('file_path', ''),
                'content': doc.get('cleaned_content', doc.get('content', '')),
                'metadata': {
                    'category': doc.get('metadata', {}).get('category', ''),
                    'title': doc.get('metadata', {}).get('title', ''),
                    'description': doc.get('metadata', {}).get('description', ''),
                    'tags': doc.get('metadata', {}).get('tags', []),
                    'created_date': doc.get('metadata', {}).get('created_date', ''),
                    'modified_date': doc.get('metadata', {}).get('modified_date', '')
                },
                'code_snippets': doc.get('code_snippets', [])
            }
            compressed_docs.append(compressed_doc)
        
        return compressed_docs
    
    def process_document_chunk_optimized(self, chunk_data: Dict[str, Any]) -> Tuple[int, List[Optional[NormalizedDocument]]]:
        """최적화된 문서 청크 처리 - 프로세스 간 통신 최적화"""
        chunk_id = chunk_data['chunk_id']
        documents = chunk_data['documents']
        
        try:
            results = []
            
            for doc_data in documents:
                # 메모리 사용량 측정 - 주기적 업데이트
                if len(results) % 10 == 0:  # 10개 문서마다 한 번만 측정
                    self._update_memory_usage()
                
                # 문서 정규화
                normalized_doc = self.normalize_document(doc_data)
                
                if normalized_doc:
                    results.append(normalized_doc)
                
                # 메모리 정리 - 주기적 가비지 컬렉션
                if len(results) % 20 == 0:  # 20개 문서마다 한 번만 수행
                    gc.collect()
            
            return chunk_id, results
            
        except Exception as e:
            logger.error(f"최적화된 문서 청크 처리 오류 (청크 {chunk_id}): {str(e)}")
            logger.error(traceback.format_exc())
            return chunk_id, []

def main():
    """메인 실행 함수"""
    logger.info("WinForms_Docs 데이터 정규화 시작 - 병렬 처리 최적화 버전")
    
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
    logger.info(f"데이터 정규화 완료. 성공: {normalizer.stats.processed_documents}, 실패: {normalizer.stats.failed_documents}")
    logger.info(f"성능 개선 결과:")
    logger.info(f"- 처리 속도: {normalizer.stats.processed_documents / max(normalizer.stats.processing_time, 1):.2f} 문서/초")
    logger.info(f"- 메모리 사용량: {normalizer.stats.peak_memory_usage:.1f} MB")
    logger.info(f"- 사용된 워커 수: {normalizer.max_workers}")

if __name__ == "__main__":
    main()
