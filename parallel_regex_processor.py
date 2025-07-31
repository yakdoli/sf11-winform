"""
WinForms_Docs 병렬 정규식 처리 모듈

반복적 정규식 연산의 성능을 개선하기 위한 병렬 처리 모듈입니다.
정규식 패턴 컴파일 캐시, 벡터화된 정규식 처리, 병렬 패턴 매칭을 제공합니다.
"""

import re
import time
import logging
import multiprocessing as mp
from typing import Dict, List, Set, Optional, Any, Tuple, Pattern
from dataclasses import dataclass, asdict
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import traceback
from functools import lru_cache

from parallel_config import ParallelProcessor, ParallelConfig

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class RegexPattern:
    """정규식 패턴 데이터 클래스"""
    name: str
    pattern: str
    flags: int = 0
    description: str = ""
    compiled_pattern: Optional[Pattern] = None
    
    def __post_init__(self):
        """패턴 컴파일"""
        if self.compiled_pattern is None:
            self.compiled_pattern = re.compile(self.pattern, self.flags)

@dataclass
class RegexProcessingResult:
    """정규식 처리 결과 데이터 클래스"""
    pattern_name: str
    matches: List[Tuple[int, int, str]]  # (start, end, matched_text)
    replacements: List[Tuple[int, int, str]]  # (start, end, replacement_text)
    processing_time: float
    input_text: str
    output_text: str

class RegexPatternManager:
    """정규식 패턴 관리 클래스"""
    
    def __init__(self):
        self.patterns: Dict[str, RegexPattern] = {}
        self.pattern_stats: Dict[str, Dict[str, Any]] = {}
        self._initialize_common_patterns()
    
    def _initialize_common_patterns(self):
        """일반적인 정규식 패턴 초기화"""
        # HTML 태그 제거 패턴
        self.add_pattern("html_tags", r'<[^>]+>', 0, "HTML 태그 제거")
        self.add_pattern("html_tags_multiline", r'<[^>]+>', re.MULTILINE | re.DOTALL, "HTML 태그 제거 (다중 라인)")
        
        # 특수 문자 정제 패턴
        self.add_pattern("special_chars", r'[^\w\s가-힣]', 0, "특수 문자 제거")
        self.add_pattern("whitespace", r'\s+', 0, "여러 공백 문자 정리")
        self.add_pattern("empty_lines", r'\n\s*\n', 0, "빈 줄 제거")
        
        # 코드 블록 패턴
        self.add_pattern("code_blocks", r'```([a-zA-Z0-9+]*)\s*\n(.*?)\n```', re.DOTALL, "코드 블록 추출")
        self.add_pattern("inline_code", r'`([^`]+)`', 0, "인라인 코드 추출")
        
        # URL 패턴
        self.add_pattern("urls", r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', 0, "URL 추출")
        
        # 이메일 패턴
        self.add_pattern("emails", r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 0, "이메일 추출")
        
        # 숫자 패턴
        self.add_pattern("numbers", r'\d+', 0, "숫자 추출")
        self.add_pattern("float_numbers", r'\d+\.\d+', 0, "실수 추출")
        
        # 날짜 패턴
        self.add_pattern("dates", r'\d{4}-\d{2}-\d{2}', 0, "날짜 추출")
        self.add_pattern("times", r'\d{2}:\d{2}:\d{2}', 0, "시간 추출")
        
        # 불필요한 키워드 패턴
        self.add_pattern("unwanted_keywords", r'\b(?:TODO|FIXME|NOTE|WARNING|ERROR)\b', 0, "불필요한 키워드 제거")
        
        # 주석 패턴
        self.add_pattern("line_comments", r'//.*$', re.MULTILINE, "한 줄 주석 제거")
        self.add_pattern("block_comments", r'/\*.*?\*/', re.DOTALL, "블록 주석 제거")
        
        # 테이블 관련 패턴
        self.add_pattern("table_borders", r'\|[-+]+\|', 0, "테이블 테두기 제거")
        self.add_pattern("table_cells", r'\|\s*(.*?)\s*\|', 0, "테이블 셀 추출")
        
        # D2H 관련 패턴
        self.add_pattern("d2h_prefixes", r'\[D2H\][^\n]*\n?', 0, "D2H 접두사 제거")
        self.add_pattern("d2h_links", r'\[D2H\][^\]]*\]', 0, "D2H 링크 제거")
        
        # MS XHelp 관련 패턴
        self.add_pattern("ms_xhelp_links", r'ms-xhelp:.*?\]', 0, "MS XHelp 링크 제거")
        self.add_pattern("package_url", r'package:[^\]]*\]', 0, "패키지 URL 제거")
        
        # 추가 공백 패턴
        self.add_pattern("extra_spaces", r'[ \t]+', 0, "추가 공백 정리")
        self.add_pattern("leading_spaces", r'^[ \t]+', re.MULTILINE, "선두 공백 제거")
        self.add_pattern("trailing_spaces", r'[ \t]+$', re.MULTILINE, "후행 공백 제거")
    
    def add_pattern(self, name: str, pattern: str, flags: int = 0, description: str = ""):
        """정규식 패턴 추가"""
        regex_pattern = RegexPattern(name, pattern, flags, description)
        self.patterns[name] = regex_pattern
        
        # 통계 초기화
        self.pattern_stats[name] = {
            'usage_count': 0,
            'total_processing_time': 0.0,
            'average_processing_time': 0.0,
            'match_count': 0,
            'replacement_count': 0
        }
    
    def get_pattern(self, name: str) -> Optional[RegexPattern]:
        """패턴 가져오기"""
        pattern = self.patterns.get(name)
        if pattern:
            self.pattern_stats[name]['usage_count'] += 1
        return pattern
    
    def get_all_patterns(self) -> Dict[str, RegexPattern]:
        """모든 패턴 가져오기"""
        return self.patterns.copy()
    
    def update_pattern_stats(self, pattern_name: str, processing_time: float, 
                           match_count: int, replacement_count: int):
        """패턴 통계 업데이트"""
        if pattern_name in self.pattern_stats:
            stats = self.pattern_stats[pattern_name]
            stats['total_processing_time'] += processing_time
            stats['match_count'] += match_count
            stats['replacement_count'] += replacement_count
            stats['average_processing_time'] = stats['total_processing_time'] / stats['usage_count']
    
    def get_pattern_stats(self) -> Dict[str, Dict[str, Any]]:
        """패턴 통계 반환"""
        return self.pattern_stats.copy()

class ParallelRegexProcessor:
    """병렬 정규식 처리 클래스"""
    
    def __init__(self, processor: Optional[ParallelProcessor] = None):
        self.pattern_manager = RegexPatternManager()
        self.processor = processor or ParallelProcessor()
        self.compiled_patterns_cache: Dict[str, Pattern] = {}
        
        # 성능 모니터링
        self.total_processed = 0
        self.total_processing_time = 0.0
        self.cache_hits = 0
        self.cache_misses = 0
    
    @lru_cache(maxsize=1000)
    def _compile_pattern_cached(self, pattern: str, flags: int = 0) -> Pattern:
        """패턴 컴파일 캐싱"""
        key = f"{pattern}_{flags}"
        if key not in self.compiled_patterns_cache:
            self.compiled_patterns_cache[key] = re.compile(pattern, flags)
        else:
            self.cache_hits += 1
        self.cache_misses += 1
        return self.compiled_patterns_cache[key]
    
    def process_text_parallel(self, texts: List[str], pattern_names: List[str], 
                            operation: str = "findall") -> List[RegexProcessingResult]:
        """텍스트 병렬 정규식 처리"""
        start_time = time.time()
        
        # 작업 청크 생성
        chunk_size = self.processor.calculate_optimal_chunk_size(len(texts))
        text_chunks = self.processor.create_work_chunks(texts, chunk_size)
        
        results = []
        
        try:
            # 병렬 처리
            with ProcessPoolExecutor(max_workers=self.processor.get_optimal_workers()) as executor:
                future_to_chunk = {
                    executor.submit(self._process_text_chunk, chunk, pattern_names, operation): chunk 
                    for chunk in text_chunks
                }
                
                for future in as_completed(future_to_chunk):
                    try:
                        chunk_results = future.result()
                        results.extend(chunk_results)
                    except Exception as e:
                        logger.error(f"텍스트 청크 처리 오류: {str(e)}")
                        logger.error(traceback.format_exc())
        
        except Exception as e:
            logger.error(f"병렬 정규식 처리 오류: {str(e)}")
            logger.error(traceback.format_exc())
        
        # 성능 통계 업데이트
        processing_time = time.time() - start_time
        self.total_processed += len(texts)
        self.total_processing_time += processing_time
        
        logger.info(f"병렬 정규식 처리 완료: {len(texts)}개 텍스트, "
                   f"처리 시간: {processing_time:.2f}초, "
                   f"평균 속도: {len(texts)/processing_time:.2f} 텍스트/초")
        
        return results
    
    def _process_text_chunk(self, text_chunk: List[str], pattern_names: List[str], 
                           operation: str = "findall") -> List[RegexProcessingResult]:
        """텍스트 청크 처리"""
        results = []
        
        for text in text_chunk:
            result = self._process_single_text(text, pattern_names, operation)
            if result:
                results.append(result)
        
        return results
    
    def _process_single_text(self, text: str, pattern_names: List[str], 
                           operation: str = "findall") -> Optional[RegexProcessingResult]:
        """단일 텍스트 처리"""
        if not text:
            return None
        
        start_time = time.time()
        output_text = text
        matches = []
        replacements = []
        
        for pattern_name in pattern_names:
            pattern = self.pattern_manager.get_pattern(pattern_name)
            if not pattern:
                continue
            
            try:
                # 컴파일된 패턴 사용
                compiled_pattern = pattern.compiled_pattern
                
                if operation == "findall":
                    # 패턴 찾기
                    for match in compiled_pattern.finditer(text):
                        matches.append((match.start(), match.end(), match.group()))
                
                elif operation == "sub":
                    # 패턴 치환
                    def replace_func(match):
                        replacement = f"[{pattern_name}:{match.group()}]"
                        replacements.append((match.start(), match.end(), replacement))
                        return replacement
                    
                    output_text = compiled_pattern.sub(replace_func, output_text)
                
                elif operation == "remove":
                    # 패턴 제거
                    def remove_func(match):
                        replacements.append((match.start(), match.end(), ""))
                        return ""
                    
                    output_text = compiled_pattern.sub(remove_func, output_text)
                
                # 통계 업데이트
                processing_time = time.time() - start_time
                self.pattern_manager.update_pattern_stats(
                    pattern_name, processing_time, len(matches), len(replacements)
                )
                
            except Exception as e:
                logger.error(f"패턴 처리 오류 ({pattern_name}): {str(e)}")
                continue
        
        return RegexProcessingResult(
            pattern_name="_".join(pattern_names),
            matches=matches,
            replacements=replacements,
            processing_time=time.time() - start_time,
            input_text=text,
            output_text=output_text
        )
    
    def clean_text_vectorized(self, text: str, cleaning_rules: List[str]) -> str:
        """벡터화된 텍스트 정제"""
        if not text:
            return ""
        
        # 정제 규칙 그룹화
        html_patterns = [p for p in cleaning_rules if 'html' in p.lower()]
        special_patterns = [p for p in cleaning_rules if 'special' in p.lower() or 'whitespace' in p.lower()]
        code_patterns = [p for p in cleaning_rules if 'code' in p.lower()]
        unwanted_patterns = [p for p in cleaning_rules if 'unwanted' in p.lower() or 'd2h' in p.lower() or 'ms_xhelp' in p.lower()]
        
        cleaned_text = text
        
        # HTML 태그 제거
        for pattern_name in html_patterns:
            pattern = self.pattern_manager.get_pattern(pattern_name)
            if pattern:
                cleaned_text = pattern.compiled_pattern.sub('', cleaned_text)
        
        # D2H 및 MS XHelp 관련 패턴 제거
        for pattern_name in unwanted_patterns:
            pattern = self.pattern_manager.get_pattern(pattern_name)
            if pattern:
                cleaned_text = pattern.compiled_pattern.sub('', cleaned_text)
        
        # 테이블 테두기 제거
        table_pattern = self.pattern_manager.get_pattern("table_borders")
        if table_pattern:
            cleaned_text = table_pattern.compiled_pattern.sub('', cleaned_text)
        
        # 불필요한 키워드 제거
        for pattern_name in unwanted_patterns:
            if 'unwanted' in pattern_name:
                pattern = self.pattern_manager.get_pattern(pattern_name)
                if pattern:
                    cleaned_text = pattern.compiled_pattern.sub('', cleaned_text)
        
        # 특수 문자 및 공백 정리
        for pattern_name in special_patterns:
            pattern = self.pattern_manager.get_pattern(pattern_name)
            if pattern:
                cleaned_text = pattern.compiled_pattern.sub(' ', cleaned_text)
        
        # 코드 블록 처리
        for pattern_name in code_patterns:
            pattern = self.pattern_manager.get_pattern(pattern_name)
            if pattern:
                # 코드 블록을 [CODE_BLOCK] 태그로 대체
                def replace_code(match):
                    return f'[CODE_BLOCK:{match.group(1) or "unknown"}]'
                cleaned_text = pattern.compiled_pattern.sub(replace_code, cleaned_text)
        
        # 최종 정리
        extra_spaces_pattern = self.pattern_manager.get_pattern("extra_spaces")
        if extra_spaces_pattern:
            cleaned_text = extra_spaces_pattern.compiled_pattern.sub(' ', cleaned_text)
        
        empty_lines_pattern = self.pattern_manager.get_pattern("empty_lines")
        if empty_lines_pattern:
            cleaned_text = empty_lines_pattern.compiled_pattern.sub('\n\n', cleaned_text)
        
        # 줄바꿈 정리
        cleaned_text = '\n'.join(line.strip() for line in cleaned_text.split('\n') if line.strip())
        
        return cleaned_text.strip()
    
    def extract_code_blocks_parallel(self, texts: List[str]) -> List[Tuple[str, List[Dict[str, Any]]]]:
        """병렬 코드 블록 추출"""
        pattern_name = "code_blocks"
        pattern = self.pattern_manager.get_pattern(pattern_name)
        
        if not pattern:
            return []
        
        results = []
        
        for text in texts:
            code_snippets = []
            cleaned_text = text
            
            # 모든 코드 블록 찾기
            matches = list(pattern.compiled_pattern.finditer(text))
            
            # 역순으로 처리하여 위치 문제 방지
            for match in reversed(matches):
                language = match.group(1) or 'unknown'
                code = match.group(2)
                
                # 코드 스니펫 생성
                code_snippet = {
                    'language': language.lower(),
                    'code': code,
                    'normalized_code': self._normalize_code_content(code),
                    'line_start': text[:match.start()].count('\n') + 1,
                    'line_end': text[:match.end()].count('\n') - 1,
                    'hash': self._generate_hash(code)
                }
                code_snippets.append(code_snippet)
                
                # 원본 내용에서 코드 블록 제거
                start_pos, end_pos = match.span()
                cleaned_text = cleaned_text[:start_pos] + f'[CODE_BLOCK:{len(code_snippets)-1}]' + cleaned_text[end_pos:]
            
            results.append((cleaned_text, code_snippets))
        
        return results
    
    def _normalize_code_content(self, code: str) -> str:
        """코드 내용 정규화"""
        if not code:
            return ''
        
        # 줄바꿈 정리
        code = re.sub(r'\r\n', '\n', code)
        code = re.sub(r'\n+', '\n', code)
        
        # 주석 제거 (간소화된 버전)
        line_comment_pattern = self.pattern_manager.get_pattern("line_comments")
        block_comment_pattern = self.pattern_manager.get_pattern("block_comments")
        
        if line_comment_pattern:
            code = line_comment_pattern.compiled_pattern.sub('', code)
        
        if block_comment_pattern:
            code = block_comment_pattern.compiled_pattern.sub('', code)
        
        # 불필요한 공백 정리
        lines = code.split('\n')
        normalized_lines = []
        
        for line in lines:
            stripped_line = line.strip()
            if stripped_line:
                normalized_lines.append(stripped_line)
        
        return '\n'.join(normalized_lines)
    
    def _generate_hash(self, text: str) -> str:
        """텍스트 해시 생성"""
        import hashlib
        return hashlib.md5(text.encode('utf-8')).hexdigest()
    
    def get_performance_stats(self) -> Dict[str, Any]:
        """성능 통계 반환"""
        cache_hit_rate = self.cache_hits / (self.cache_hits + self.cache_misses) * 100 if (self.cache_hits + self.cache_misses) > 0 else 0
        
        return {
            'total_processed': self.total_processed,
            'total_processing_time': self.total_processing_time,
            'average_processing_time': self.total_processing_time / self.total_processed if self.total_processed > 0 else 0,
            'cache_hits': self.cache_hits,
            'cache_misses': self.cache_misses,
            'cache_hit_rate': cache_hit_rate,
            'pattern_stats': self.pattern_manager.get_pattern_stats()
        }

# 전역 인스턴스
_default_regex_processor = None

def get_default_regex_processor() -> ParallelRegexProcessor:
    """기본 병렬 정규식 처리기 인스턴스 반환"""
    global _default_regex_processor
    if _default_regex_processor is None:
        _default_regex_processor = ParallelRegexProcessor()
    return _default_regex_processor