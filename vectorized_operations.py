"""
WinForms_Docs 벡터화된 연산 클래스 - 정규식 및 텍스트 처리 최적화

주요 기능:
==========
1. 정규식 패턴 벡터화
   - 컴파일된 정규식 패턴을 pandas Series.str 메서드로 변환
   - 배치 처리를 통한 정규식 성능 최적화
   - 캐시된 정규식 패턴 관리

2. 텍스트 정규화 배치 처리
   - 벡터화된 텍스트 정규화 작업
   - 다국어 텍스트 처리 지원
   - 효율적인 문자열 변환

3. 중복 검출 최적화
   - pandas 기반 고속 중복 검출
   - 벡터화된 유사도 계산
   - 메모리 효율적인 중복 그룹화

4. 함수 캐시 관리
   - 컴파일된 함수 캐시 시스템
   - LRU 캐시를 통한 중복 계산 방지
   - 메모리 사용량 최적화

성능 향상 목표:
=============
- 정규식 처리 속도: 기존 대비 200-300% 향상
- 텍스트 정규화 속도: 기존 대비 150-200% 향상
- 중복 검출 속도: 기존 대비 400-500% 향상
- 메모리 사용량: 30-50% 감소

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0 (벡터화된 연산 시스템)
"""

import pandas as pd
import numpy as np
import re
import logging
import time
import hashlib
import gc
import psutil
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any, Generator, Union, Callable
from dataclasses import dataclass, asdict
from datetime import datetime
from functools import lru_cache
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor, as_completed
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from config import (
    WINFORMS_DOCS_DIR, OUTPUT_DIR, BACKUP_DIR,
    PROCESSING_OPTIONS, LOGGING_CONFIG
)

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
class VectorizationStats:
    """벡터화 통계 데이터 클래스"""
    total_operations: int = 0
    successful_operations: int = 0
    failed_operations: int = 0
    total_processing_time: float = 0.0
    average_processing_time: float = 0.0
    memory_usage: float = 0.0
    cache_hits: int = 0
    cache_misses: int = 0
    speedup_factor: float = 0.0

class RegexPatternCache:
    """정규식 패턴 캐시 클래스"""
    
    def __init__(self, max_size: int = 1000):
        self.patterns: Dict[str, re.Pattern] = {}
        self.max_size = max_size
        self.access_count: Dict[str, int] = {}
        self.hit_count = 0
        self.miss_count = 0
        
    def get_pattern(self, pattern_name: str, pattern_str: str) -> re.Pattern:
        """정규식 패턴 가져오기 (캐시 활용)"""
        cache_key = f"{pattern_name}:{hashlib.md5(pattern_str.encode()).hexdigest()}"
        
        # 캐시 확인
        if cache_key in self.patterns:
            self.hit_count += 1
            self.access_count[cache_key] = self.access_count.get(cache_key, 0) + 1
            return self.patterns[cache_key]
        
        # 캐시 미스 - 새 패턴 생성
        self.miss_count += 1
        
        # LRU 정책에 따른 캐시 정리
        if len(self.patterns) >= self.max_size:
            self._cleanup_cache()
        
        # 패턴 컴파일
        try:
            compiled_pattern = re.compile(pattern_str, re.IGNORECASE | re.UNICODE)
            self.patterns[cache_key] = compiled_pattern
            self.access_count[cache_key] = 1
            return compiled_pattern
        except Exception as e:
            logger.error(f"정규식 패턴 컴파일 오류: {pattern_name}, {str(e)}")
            raise
    
    def _cleanup_cache(self) -> None:
        """캐시 정리 (LRU 정책)"""
        # 접근 횟수가 가장 적은 항목 제거
        if self.patterns:
            least_used = min(self.access_count.items(), key=lambda x: x[1])[0]
            del self.patterns[least_used]
            del self.access_count[least_used]
    
    def get_stats(self) -> Dict[str, Any]:
        """캐시 통계 반환"""
        total_requests = self.hit_count + self.miss_count
        hit_rate = (self.hit_count / total_requests * 100) if total_requests > 0 else 0
        
        return {
            'cache_size': len(self.patterns),
            'max_size': self.max_size,
            'hit_count': self.hit_count,
            'miss_count': self.miss_count,
            'hit_rate': hit_rate,
            'most_used': max(self.access_count.items(), key=lambda x: x[1]) if self.access_count else (0, 0)
        }

class CompiledFunctionCache:
    """컴파일된 함수 캐시 클래스"""
    
    def __init__(self, max_size: int = 500):
        self.functions: Dict[str, Callable] = {}
        self.max_size = max_size
        self.call_count: Dict[str, int] = {}
        self.hit_count = 0
        self.miss_count = 0
        
    def get_function(self, func_name: str, func: Callable) -> Callable:
        """컴파일된 함수 가져오기 (캐시 활용)"""
        cache_key = f"{func_name}:{hash(func.__code__)}"
        
        # 캐시 확인
        if cache_key in self.functions:
            self.hit_count += 1
            self.call_count[cache_key] = self.call_count.get(cache_key, 0) + 1
            return self.functions[cache_key]
        
        # 캐시 미스 - 새 함수 등록
        self.miss_count += 1
        
        # LRU 정책에 따른 캐시 정리
        if len(self.functions) >= self.max_size:
            self._cleanup_cache()
        
        # 함수 등록
        self.functions[cache_key] = func
        self.call_count[cache_key] = 1
        return func
    
    def _cleanup_cache(self) -> None:
        """캐시 정리 (LRU 정책)"""
        # 호출 횟수가 가장 적은 항목 제거
        if self.functions:
            least_used = min(self.call_count.items(), key=lambda x: x[1])[0]
            del self.functions[least_used]
            del self.call_count[least_used]
    
    def get_stats(self) -> Dict[str, Any]:
        """캐시 통계 반환"""
        total_calls = self.hit_count + self.miss_count
        hit_rate = (self.hit_count / total_calls * 100) if total_calls > 0 else 0
        
        return {
            'cache_size': len(self.functions),
            'max_size': self.max_size,
            'hit_count': self.hit_count,
            'miss_count': self.miss_count,
            'hit_rate': hit_rate,
            'most_called': max(self.call_count.items(), key=lambda x: x[1]) if self.call_count else (0, 0)
        }

class VectorizedOperations:
    """벡터화된 연산 클래스 - 핵심 텍스트 처리 시스템"""
    
    def __init__(self, max_cache_size: int = 1000):
        self.regex_cache = RegexPatternCache(max_cache_size)
        self.function_cache = CompiledFunctionCache(max_cache_size // 2)
        self.stats = VectorizationStats()
        self.process = psutil.Process()
        
        # 컴파일된 정규식 패턴
        self.regex_patterns = self._compile_regex_patterns()
        
        # 컴파일된 함수
        self.compiled_functions = self._compile_functions()
        
        # 성능 모니터링
        self.start_time = time.time()
        
        logger.info("벡터화된 연산 시스템 초기화 완료")
    
    def _compile_regex_patterns(self) -> Dict[str, re.Pattern]:
        """정규식 패턴 컴파일"""
        patterns = {
            # HTML 관련
            'html_tags': r'<[^>]+>',
            'html_entities': r'&[a-zA-Z0-9#]+;',
            'html_comments': r'<!--.*?-->',
            
            # 마크다운 관련
            'markdown_headers': r'^#{1,6}\s+(.+)$',
            'markdown_links': r'\[([^\]]+)\]\(([^)]+)\)',
            'markdown_images': r'!\[([^\]]*)\]\(([^)]+)\)',
            'markdown_code': r'```([a-zA-Z0-9+]*)\s*\n(.*?)\n```',
            'markdown_inline_code': r'`([^`]+)`',
            'markdown_lists': r'^\s*[-*+]\s+(.+)$',
            'markdown_tables': r'\|(.+)\|',
            
            # 코드 관련
            'code_blocks': r'```[a-zA-Z0-9+]*\s*\n(.*?)\n```',
            'code_inline': r'`([^`]+)`',
            'code_comments': r'//.*?$|/\*.*?\*/',
            'code_strings': r'["\'][^"\']*["\']',
            
            # 텍스트 정규화
            'extra_spaces': r'\s+',
            'empty_lines': r'\n\s*\n',
            'leading_trailing_spaces': r'^\s+|\s+$',
            'special_chars': r'[^\w\s가-힣.,!?;:()\[\]{}"\'-]',
            'urls': r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'phone': r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
            'numbers': r'\b\d+(?:\.\d+)?\b',
            
            # 문서 구조
            'section_headers': r'^#+\s+(.+)$',
            'code_language': r'```([a-zA-Z0-9+]+)',
            'file_extensions': r'\.([a-zA-Z0-9]+)$',
            
            # 언어 특화
            'korean_jamo': r'[ㄱ-ㅎㅏ-ㅣ]',
            'korean_chars': r'[가-힣]',
            'english_words': r'\b[a-zA-Z]+\b',
            'whitespace': r'\s'
        }
        
        compiled_patterns = {}
        for name, pattern in patterns.items():
            try:
                compiled_patterns[name] = self.regex_cache.get_pattern(name, pattern)
            except Exception as e:
                logger.error(f"정규식 패턴 컴파일 실패: {name}, {str(e)}")
                compiled_patterns[name] = None
        
        return compiled_patterns
    
    def _compile_functions(self) -> Dict[str, Callable]:
        """컴파일된 함수 생성"""
        functions = {
            'text_normalizer': self._vectorized_text_normalization,
            'html_cleaner': self._vectorized_html_cleaning,
            'code_extractor': self._vectorized_code_extraction,
            'metadata_extractor': self._vectorized_metadata_extraction,
            'duplicate_detector': self._vectorized_duplicate_detection,
            'similarity_calculator': self._vectorized_similarity_calculation
        }
        
        compiled_functions = {}
        for name, func in functions.items():
            try:
                compiled_functions[name] = self.function_cache.get_function(name, func)
            except Exception as e:
                logger.error(f"함수 컴파일 실패: {name}, {str(e)}")
                compiled_functions[name] = None
        
        return compiled_functions
    
    def vectorized_regex_replace(self, series: pd.Series, pattern_name: str, replacement: str = '') -> pd.Series:
        """벡터화된 정규식 치환"""
        try:
            start_time = time.time()
            
            # 패턴 가져오기
            pattern = self.regex_patterns.get(pattern_name)
            if pattern is None:
                logger.error(f"정규식 패턴을 찾을 수 없음: {pattern_name}")
                return series
            
            # 벡터화된 치환
            result = series.str.replace(pattern, replacement, regex=True)
            
            # 통계 업데이트
            processing_time = time.time() - start_time
            self.stats.total_operations += 1
            self.stats.successful_operations += 1
            self.stats.total_processing_time += processing_time
            
            logger.debug(f"벡터화된 정규식 치환 완료: {pattern_name}, {processing_time:.3f}s")
            
            return result
            
        except Exception as e:
            logger.error(f"벡터화된 정규식 치환 오류: {pattern_name}, {str(e)}")
            self.stats.total_operations += 1
            self.stats.failed_operations += 1
            return series
    
    def batch_text_normalization(self, series: pd.Series) -> pd.Series:
        """배치 텍스트 정규화"""
        try:
            start_time = time.time()
            
            # 1. HTML 태그 제거
            result = self.vectorized_regex_replace(series, 'html_tags', '')
            
            # 2. HTML 엔티티 제거
            result = self.vectorized_regex_replace(result, 'html_entities', '')
            
            # 3. 여러 공백 정리
            result = self.vectorized_regex_replace(result, 'extra_spaces', ' ')
            
            # 4. 앞뒤 공백 제거
            result = self.vectorized_regex_replace(result, 'leading_trailing_spaces', '')
            
            # 5. 빈 줄 정리
            result = self.vectorized_regex_replace(result, 'empty_lines', '\n')
            
            # 6. 특수 문자 정리
            result = self.vectorized_regex_replace(result, 'special_chars', ' ')
            
            # 7. 텍스트 정규화 함수 적용
            result = self.compiled_functions['text_normalizer'](result)
            
            # 통계 업데이트
            processing_time = time.time() - start_time
            self.stats.total_operations += 1
            self.stats.successful_operations += 1
            self.stats.total_processing_time += processing_time
            
            logger.info(f"배치 텍스트 정규화 완료: {processing_time:.3f}s")
            
            return result
            
        except Exception as e:
            logger.error(f"배치 텍스트 정규화 오류: {str(e)}")
            self.stats.total_operations += 1
            self.stats.failed_operations += 1
            return series
    
    def parallel_duplicate_detection(self, df1: pd.DataFrame, df2: pd.DataFrame, 
                                   threshold: float = 0.85) -> pd.DataFrame:
        """병렬 중복 검출"""
        try:
            start_time = time.time()
            
            # 데이터프레임 병합을 위한 준비
            df1 = df1.copy()
            df2 = df2.copy()
            df1['source'] = 'df1'
            df2['source'] = 'df2'
            
            # 콘텐츠 기준으로 중복 검출
            duplicates = []
            
            # 청크 단위로 처리
            chunk_size = 1000
            df1_chunks = [df1[i:i + chunk_size] for i in range(0, len(df1), chunk_size)]
            
            # 병렬 처리
            with ThreadPoolExecutor(max_workers=min(mp.cpu_count(), 8)) as executor:
                future_to_chunk = {
                    executor.submit(self._process_duplicate_chunk, chunk, df2, threshold): chunk
                    for chunk in df1_chunks
                }
                
                for future in as_completed(future_to_chunk):
                    try:
                        chunk_duplicates = future.result()
                        duplicates.extend(chunk_duplicates)
                    except Exception as e:
                        logger.error(f"중복 검출 청크 처리 오류: {str(e)}")
                        continue
            
            # 결과 데이터프레임 생성
            if duplicates:
                result_df = pd.DataFrame(duplicates)
            else:
                result_df = pd.DataFrame(columns=['id1', 'id2', 'similarity', 'content1', 'content2'])
            
            # 통계 업데이트
            processing_time = time.time() - start_time
            self.stats.total_operations += 1
            self.stats.successful_operations += 1
            self.stats.total_processing_time += processing_time
            
            logger.info(f"병렬 중복 검출 완료: {len(duplicates)}개 중복 발견, {processing_time:.3f}s")
            
            return result_df
            
        except Exception as e:
            logger.error(f"병렬 중복 검출 오류: {str(e)}")
            self.stats.total_operations += 1
            self.stats.failed_operations += 1
            return pd.DataFrame()
    
    def _process_duplicate_chunk(self, chunk: pd.DataFrame, df2: pd.DataFrame, threshold: float) -> List[Dict]:
        """중복 검출 청크 처리"""
        duplicates = []
        
        for _, row1 in chunk.iterrows():
            content1 = row1.get('content', '')
            
            # df2와 비교
            for _, row2 in df2.iterrows():
                content2 = row2.get('content', '')
                
                # 유사도 계산
                similarity = self._calculate_text_similarity(content1, content2)
                
                if similarity >= threshold:
                    duplicates.append({
                        'id1': row1.get('id', ''),
                        'id2': row2.get('id', ''),
                        'similarity': similarity,
                        'content1': content1[:100] + '...' if len(content1) > 100 else content1,
                        'content2': content2[:100] + '...' if len(content2) > 100 else content2
                    })
        
        return duplicates
    
    def _calculate_text_similarity(self, text1: str, text2: str) -> float:
        """텍스트 유사도 계산"""
        if not text1 or not text2:
            return 0.0
        
        # 간단한 유사도 계산 (실제 구현에서는 더 정교한 알고리즘 사용)
        if text1 == text2:
            return 1.0
        
        # SequenceMatcher를 사용한 유사도 계산
        similarity = difflib.SequenceMatcher(None, text1, text2).ratio()
        
        return similarity
    
    def _vectorized_text_normalization(self, series: pd.Series) -> pd.Series:
        """벡터화된 텍스트 정규화"""
        # 소문자 변환
        result = series.str.lower()
        
        # 여러 공백 정리
        result = result.str.replace(r'\s+', ' ', regex=True)
        
        # 앞뒤 공백 제거
        result = result.str.strip()
        
        # 빈 문자열 처리
        result = result.replace('', 'EMPTY')
        
        return result
    
    def _vectorized_html_cleaning(self, series: pd.Series) -> pd.Series:
        """벡터화된 HTML 정리"""
        # HTML 태그 제거
        result = self.vectorized_regex_replace(series, 'html_tags', '')
        
        # HTML 엔티티 제거
        result = self.vectorized_regex_replace(result, 'html_entities', '')
        
        # HTML 주석 제거
        result = self.vectorized_regex_replace(result, 'html_comments', '')
        
        return result
    
    def _vectorized_code_extraction(self, series: pd.Series) -> Tuple[pd.Series, pd.Series]:
        """벡터화된 코드 추출"""
        # 코드 블록 추출
        code_blocks = series.str.extractall(self.regex_patterns['code_blocks'])[0]
        
        # 코드 블록 제거
        cleaned_content = series.str.replace(self.regex_patterns['code_blocks'], '[CODE_BLOCK]', regex=True)
        
        return cleaned_content, code_blocks
    
    def _vectorized_metadata_extraction(self, series: pd.Series) -> pd.DataFrame:
        """벡터화된 메타데이터 추출"""
        # 제목 추출
        titles = series.str.extract(self.regex_patterns['markdown_headers'])[0]
        
        # 링크 추출
        links = series.str.extractall(self.regex_patterns['markdown_links'])[1]
        
        # 이미지 추출
        images = series.str.extractall(self.regex_patterns['markdown_images'])[1]
        
        # 코드 언어 추출
        code_languages = series.str.extract(self.regex_patterns['code_language'])[0]
        
        # 메타데이터 데이터프레임 생성
        metadata_df = pd.DataFrame({
            'title': titles.fillna(''),
            'links': links.fillna('').groupby(level=0).apply(lambda x: ', '.join(x)),
            'images': images.fillna('').groupby(level=0).apply(lambda x: ', '.join(x)),
            'code_languages': code_languages.fillna('')
        })
        
        return metadata_df
    
    def _vectorized_duplicate_detection(self, df: pd.DataFrame) -> pd.DataFrame:
        """벡터화된 중복 검출"""
        # 콘텐츠 기준으로 중복 그룹화
        duplicates = df[df.duplicated(subset=['content'], keep=False)]
        
        # 중복 그룹 생성
        duplicate_groups = duplicates.groupby('content').apply(lambda x: {
            'content': x['content'].iloc[0],
            'count': len(x),
            'files': x['file_path'].tolist()
        }).reset_index()
        
        return duplicate_groups
    
    def _vectorized_similarity_calculation(self, df: pd.DataFrame) -> pd.DataFrame:
        """벡터화된 유사도 계산"""
        try:
            # TF-IDF 벡터라이저 생성
            vectorizer = TfidfVectorizer(max_features=1000)
            
            # 콘텐츠 벡터화
            tfidf_matrix = vectorizer.fit_transform(df['content'].fillna(''))
            
            # 코사인 유사도 계산
            cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
            
            # 유사도 데이터프레임 생성
            similarity_df = pd.DataFrame(
                cosine_sim,
                index=df.index,
                columns=df.index
            )
            
            return similarity_df
            
        except Exception as e:
            logger.error(f"벡터화된 유사도 계산 오류: {str(e)}")
            return pd.DataFrame()
    
    def get_cache_stats(self) -> Dict[str, Any]:
        """캐시 통계 반환"""
        regex_stats = self.regex_cache.get_stats()
        function_stats = self.function_cache.get_stats()
        
        return {
            'regex_cache': regex_stats,
            'function_cache': function_stats,
            'total_cache_hits': regex_stats['hit_count'] + function_stats['hit_count'],
            'total_cache_misses': regex_stats['miss_count'] + function_stats['miss_count']
        }
    
    def get_stats(self) -> VectorizationStats:
        """벡터화 통계 반환"""
        if self.stats.total_operations > 0:
            self.stats.average_processing_time = (
                self.stats.total_processing_time / self.stats.total_operations
            )
        
        # 메모리 사용량
        self.stats.memory_usage = self.process.memory_info().rss / 1024 / 1024  # MB
        
        # 캐시 통계
        cache_stats = self.get_cache_stats()
        total_requests = cache_stats['total_cache_hits'] + cache_stats['total_cache_misses']
        if total_requests > 0:
            cache_hit_rate = cache_stats['total_cache_hits'] / total_requests * 100
            self.stats.cache_hits = cache_stats['total_cache_hits']
            self.stats.cache_misses = cache_stats['total_cache_misses']
        
        return self.stats
    
    def clear_cache(self) -> None:
        """캐시 정리"""
        self.regex_cache.patterns.clear()
        self.regex_cache.access_count.clear()
        self.function_cache.functions.clear()
        self.function_cache.call_count.clear()
        
        gc.collect()
        logger.info("벡터화 연산 캐시 정리 완료")
    
    def __del__(self):
        """소멸자"""
        try:
            self.clear_cache()
        except:
            pass

# 유틸리티 함수
def create_vectorized_operations(max_cache_size: int = 1000) -> VectorizedOperations:
    """VectorizedOperations 인스턴스 생성"""
    return VectorizedOperations(max_cache_size)

def apply_vectorized_operations(df: pd.DataFrame, operations: List[str]) -> pd.DataFrame:
    """벡터화된 연산 적용"""
    vectorized_ops = create_vectorized_operations()
    
    try:
        for operation in operations:
            if operation == 'text_normalization':
                df['content'] = vectorized_ops.batch_text_normalization(df['content'])
            elif operation == 'html_cleaning':
                df['content'] = vectorized_ops._vectorized_html_cleaning(df['content'])
            elif operation == 'duplicate_detection':
                duplicates = vectorized_ops._vectorized_duplicate_detection(df)
                logger.info(f"중복 검출 완료: {len(duplicates)}개 중복 그룹")
            elif operation == 'similarity_calculation':
                similarity_df = vectorized_ops._vectorized_similarity_calculation(df)
                logger.info(f"유사도 계산 완료: {similarity_df.shape}")
        
        return df
        
    except Exception as e:
        logger.error(f"벡터화된 연산 적용 오류: {str(e)}")
        raise

if __name__ == "__main__":
    # 테스트 코드
    def test_vectorized_operations():
        """VectorizedOperations 테스트"""
        # 테스트 데이터 생성
        test_data = {
            'file_path': ['test1.md', 'test2.md', 'test3.md'],
            'content': [
                '# 제목 1\n\n이것은 첫 번째 테스트 문서입니다.\n\n```python\nprint("Hello, World!")\n```',
                '# 제목 2\n\n이것은 두 번째 테스트 문서입니다.\n\n```javascript\nconsole.log("Hello, World!");\n```',
                '# 제목 1\n\n이것은 첫 번째 테스트 문서와 동일합니다.\n\n```python\nprint("Hello, World!")\n```'
            ]
        }
        
        df = pd.DataFrame(test_data)
        
        try:
            # VectorizedOperations 테스트
            vectorized_ops = create_vectorized_operations()
            
            print("원본 데이터:")
            print(df[['file_path', 'content']].head())
            
            # 텍스트 정규화 적용
            df['normalized_content'] = vectorized_ops.batch_text_normalization(df['content'])
            
            print("\n정규화된 데이터:")
            print(df[['file_path', 'normalized_content']].head())
            
            # 중복 검출
            duplicates = vectorized_ops._vectorized_duplicate_detection(df)
            print(f"\n중복 검출 결과: {len(duplicates)}개 중복 그룹")
            
            # 통계 정보
            stats = vectorized_ops.get_stats()
            print(f"\n통계 정보:")
            print(f"총 연산 수: {stats.total_operations}")
            print(f"성공 연산 수: {stats.successful_operations}")
            print(f"실패 연산 수: {stats.failed_operations}")
            print(f"평균 처리 시간: {stats.average_processing_time:.3f}s")
            print(f"메모리 사용량: {stats.memory_usage:.2f}MB")
            
            # 캐시 통계
            cache_stats = vectorized_ops.get_cache_stats()
            print(f"\n캐시 통계:")
            print(f"정규식 캐시 적중률: {cache_stats['regex_cache']['hit_rate']:.1f}%")
            print(f"함수 캐시 적중률: {cache_stats['function_cache']['hit_rate']:.1f}%")
            
        except Exception as e:
            logger.error(f"테스트 오류: {str(e)}")
    
    # 테스트 실행
    test_vectorized_operations()