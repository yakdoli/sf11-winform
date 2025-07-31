"""
WinForms_Docs 해시 기반 중복 검사 모듈

O(n²) 복잡도의 중복 검사를 해시 기반으로 최적화하여 성능을 개선합니다.
해시 캐싱, 병렬 해시 계산, 중복 그룹 관리를 제공합니다.
"""

import hashlib
import time
import logging
import multiprocessing as mp
from typing import Dict, List, Set, Optional, Any, Tuple, Union
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import traceback
import json

from parallel_config import ParallelProcessor, ParallelConfig

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class HashResult:
    """해시 결과 데이터 클래스"""
    content_hash: str
    file_path: str
    file_name: str
    file_size: int
    content_preview: str
    hash_type: str
    created_at: str

@dataclass
class DuplicateHashGroup:
    """중복 해시 그룹 데이터 클래스"""
    hash_value: str
    files: List[HashResult]
    similarity_score: float
    duplicate_type: str
    created_at: str

class HashGenerator:
    """해시 생성기 클래스"""
    
    def __init__(self):
        self.hash_algorithms = {
            'md5': hashlib.md5,
            'sha1': hashlib.sha1,
            'sha256': hashlib.sha256,
            'sha512': hashlib.sha512
        }
        self.default_algorithm = 'md5'
    
    def generate_hash(self, content: str, algorithm: str = None) -> str:
        """텍스트 해시 생성"""
        if not content:
            return ""
        
        algorithm = algorithm or self.default_algorithm
        hash_func = self.hash_algorithms.get(algorithm)
        
        if not hash_func:
            raise ValueError(f"지원되지 않는 해시 알고리즘: {algorithm}")
        
        return hash_func(content.encode('utf-8')).hexdigest()
    
    def generate_file_hash(self, file_path: Path, algorithm: str = None) -> str:
        """파일 해시 생성"""
        if not file_path.exists():
            return ""
        
        algorithm = algorithm or self.default_algorithm
        hash_func = self.hash_algorithms.get(algorithm)
        
        if not hash_func:
            raise ValueError(f"지원되지 않는 해시 알고리즘: {algorithm}")
        
        # 파일 크기가 큰 경우 청크 단위로 처리
        chunk_size = 8192  # 8KB
        hash_func = hash_func()
        
        try:
            with open(file_path, 'rb') as f:
                while chunk := f.read(chunk_size):
                    hash_func.update(chunk)
            
            return hash_func.hexdigest()
        
        except Exception as e:
            logger.error(f"파일 해시 생성 오류 ({file_path}): {str(e)}")
            return ""
    
    def generate_content_hash(self, content: str, file_path: str = "", 
                            algorithm: str = None) -> HashResult:
        """콘텐츠 해시 결과 생성"""
        if not content and not file_path:
            return None
        
        # 콘텐츠 해시 생성
        content_hash = self.generate_hash(content, algorithm)
        
        # 파일 정보 수집
        file_size = len(content.encode('utf-8')) if content else 0
        file_name = Path(file_path).name if file_path else ""
        
        # 콘텐츠 미리보기 생성
        content_preview = content[:100] + "..." if len(content) > 100 else content
        
        return HashResult(
            content_hash=content_hash,
            file_path=file_path,
            file_name=file_name,
            file_size=file_size,
            content_preview=content_preview,
            hash_type=algorithm or self.default_algorithm,
            created_at=datetime.now().isoformat()
        )

class HashCache:
    """해시 캐시 클래스"""
    
    def __init__(self, max_size: int = 10000):
        self.max_size = max_size
        self.content_cache: Dict[str, HashResult] = {}
        self.file_cache: Dict[str, HashResult] = {}
        self.stats = {
            'cache_hits': 0,
            'cache_misses': 0,
            'total_requests': 0
        }
    
    def get_content_hash(self, content: str) -> Optional[HashResult]:
        """콘텐츠 해시 가져오기"""
        self.stats['total_requests'] += 1
        
        # 콘텐츠 해시 생성
        content_hash = hashlib.md5(content.encode('utf-8')).hexdigest()
        
        if content_hash in self.content_cache:
            self.stats['cache_hits'] += 1
            return self.content_cache[content_hash]
        
        self.stats['cache_misses'] += 1
        return None
    
    def set_content_hash(self, hash_result: HashResult):
        """콘텐츠 해시 설정"""
        if len(self.content_cache) >= self.max_size:
            # 가장 오래된 항목 제거 (간소화된 버전)
            oldest_key = next(iter(self.content_cache))
            del self.content_cache[oldest_key]
        
        self.content_cache[hash_result.content_hash] = hash_result
    
    def get_file_hash(self, file_path: str) -> Optional[HashResult]:
        """파일 해시 가져오기"""
        self.stats['total_requests'] += 1
        
        if file_path in self.file_cache:
            self.stats['cache_hits'] += 1
            return self.file_cache[file_path]
        
        self.stats['cache_misses'] += 1
        return None
    
    def set_file_hash(self, file_path: str, hash_result: HashResult):
        """파일 해시 설정"""
        if len(self.file_cache) >= self.max_size:
            # 가장 오래된 항목 제거 (간소화된 버전)
            oldest_key = next(iter(self.file_cache))
            del self.file_cache[oldest_key]
        
        self.file_cache[file_path] = hash_result
    
    def get_stats(self) -> Dict[str, Any]:
        """캐시 통계 반환"""
        hit_rate = self.stats['cache_hits'] / self.stats['total_requests'] * 100 if self.stats['total_requests'] > 0 else 0
        
        return {
            'cache_hits': self.stats['cache_hits'],
            'cache_misses': self.stats['cache_misses'],
            'total_requests': self.stats['total_requests'],
            'hit_rate': hit_rate,
            'content_cache_size': len(self.content_cache),
            'file_cache_size': len(self.file_cache)
        }
    
    def clear_cache(self):
        """캐시 비우기"""
        self.content_cache.clear()
        self.file_cache.clear()
        self.stats = {
            'cache_hits': 0,
            'cache_misses': 0,
            'total_requests': 0
        }

class ParallelHashDeduplicator:
    """병렬 해시 중복 검사 클래스"""
    
    def __init__(self, processor: Optional[ParallelProcessor] = None):
        self.hash_generator = HashGenerator()
        self.cache = HashCache()
        self.processor = processor or ParallelProcessor()
        
        # 중복 그룹 관리
        self.duplicate_groups: List[DuplicateHashGroup] = []
        self.unique_hashes: Set[str] = set()
        
        # 성능 통계
        self.total_files = 0
        self.total_hashes = 0
        self.duplicate_files = 0
        self.processing_time = 0.0
        
        # 로깅
        self.logger = logging.getLogger(__name__)
    
    def find_duplicates_parallel(self, file_paths: List[Path], 
                               content_based: bool = True) -> List[DuplicateHashGroup]:
        """병렬 중복 검사"""
        start_time = time.time()
        self.total_files = len(file_paths)
        
        self.logger.info(f"병렬 중복 검사 시작: {self.total_files}개 파일")
        
        # 파일 그룹화 (파일 크기 기반)
        size_groups = self._group_files_by_size(file_paths)
        
        # 각 크기 그룹별로 병렬 처리
        all_duplicate_groups = []
        
        for size, files in size_groups.items():
            if len(files) <= 1:
                continue  # 중복 가능성 없음
            
            group_duplicates = self._process_size_group(files, content_based)
            all_duplicate_groups.extend(group_duplicates)
        
        # 중복 그룹 후처리
        self.duplicate_groups = self._post_process_duplicate_groups(all_duplicate_groups)
        
        # 통계 업데이트
        self.processing_time = time.time() - start_time
        self.duplicate_files = sum(len(group.files) for group in self.duplicate_groups)
        
        self.logger.info(f"병렬 중복 검사 완료: {len(self.duplicate_groups)}개 중복 그룹, "
                        f"중복 파일: {self.duplicate_files}개, "
                        f"처리 시간: {self.processing_time:.2f}초")
        
        return self.duplicate_groups
    
    def _group_files_by_size(self, file_paths: List[Path]) -> Dict[int, List[Path]]:
        """파일 크기 기반 그룹화"""
        size_groups = {}
        
        for file_path in file_paths:
            try:
                file_size = file_path.stat().st_size
                if file_size not in size_groups:
                    size_groups[file_size] = []
                size_groups[file_size].append(file_path)
            except Exception as e:
                self.logger.error(f"파일 크기 확인 오류 ({file_path}): {str(e)}")
                continue
        
        return size_groups
    
    def _process_size_group(self, file_paths: List[Path], content_based: bool) -> List[DuplicateHashGroup]:
        """크기 그룹 처리"""
        if len(file_paths) <= 1:
            return []
        
        duplicate_groups = []
        
        if content_based:
            # 콘텐츠 기반 중복 검사
            duplicate_groups = self._find_content_duplicates(file_paths)
        else:
            # 파일 해시 기반 중복 검사
            duplicate_groups = self._find_file_hash_duplicates(file_paths)
        
        return duplicate_groups
    
    def _find_content_duplicates(self, file_paths: List[Path]) -> List[DuplicateHashGroup]:
        """콘텐츠 기반 중복 검사"""
        # 파일 내용 읽기
        file_contents = []
        for file_path in file_paths:
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    file_contents.append((file_path, content))
            except Exception as e:
                self.logger.error(f"파일 읽기 오류 ({file_path}): {str(e)}")
                continue
        
        if not file_contents:
            return []
        
        # 병렬 해시 계산
        hash_results = self._calculate_content_hashes_parallel(file_contents)
        
        # 중복 그룹 생성
        duplicate_groups = self._create_duplicate_groups_from_hashes(hash_results)
        
        return duplicate_groups
    
    def _find_file_hash_duplicates(self, file_paths: List[Path]) -> List[DuplicateHashGroup]:
        """파일 해시 기반 중복 검사"""
        # 병렬 파일 해시 계산
        hash_results = self._calculate_file_hashes_parallel(file_paths)
        
        # 중복 그룹 생성
        duplicate_groups = self._create_duplicate_groups_from_hashes(hash_results)
        
        return duplicate_groups
    
    def _calculate_content_hashes_parallel(self, file_contents: List[Tuple[Path, str]]) -> List[HashResult]:
        """병렬 콘텐츠 해시 계산"""
        # 작업 청크 생성
        chunk_size = self.processor.calculate_optimal_chunk_size(len(file_contents))
        content_chunks = self.processor.create_work_chunks(file_contents, chunk_size)
        
        hash_results = []
        
        try:
            # 병렬 처리
            with ProcessPoolExecutor(max_workers=self.processor.get_optimal_workers()) as executor:
                future_to_chunk = {
                    executor.submit(self._calculate_content_hashes_chunk, chunk): chunk 
                    for chunk in content_chunks
                }
                
                for future in as_completed(future_to_chunk):
                    try:
                        chunk_results = future.result()
                        hash_results.extend(chunk_results)
                    except Exception as e:
                        self.logger.error(f"콘텐츠 해시 계산 오류: {str(e)}")
                        self.logger.error(traceback.format_exc())
        
        except Exception as e:
            self.logger.error(f"병렬 콘텐츠 해시 계산 오류: {str(e)}")
            self.logger.error(traceback.format_exc())
        
        return hash_results
    
    def _calculate_content_hashes_chunk(self, content_chunk: List[Tuple[Path, str]]) -> List[HashResult]:
        """콘텐츠 해시 계산 청크"""
        results = []
        
        for file_path, content in content_chunk:
            # 캐시 확인
            cached_result = self.cache.get_content_hash(content)
            if cached_result:
                # 파일 경로 업데이트
                cached_result.file_path = str(file_path)
                cached_result.file_name = file_path.name
                results.append(cached_result)
                continue
            
            # 해시 생성
            hash_result = self.hash_generator.generate_content_hash(
                content, str(file_path)
            )
            
            if hash_result:
                # 캐시 저장
                self.cache.set_content_hash(hash_result)
                results.append(hash_result)
        
        return results
    
    def _calculate_file_hashes_parallel(self, file_paths: List[Path]) -> List[HashResult]:
        """병렬 파일 해시 계산"""
        # 작업 청크 생성
        chunk_size = self.processor.calculate_optimal_chunk_size(len(file_paths))
        file_chunks = self.processor.create_work_chunks(file_paths, chunk_size)
        
        hash_results = []
        
        try:
            # 병렬 처리
            with ProcessPoolExecutor(max_workers=self.processor.get_optimal_workers()) as executor:
                future_to_chunk = {
                    executor.submit(self._calculate_file_hashes_chunk, chunk): chunk 
                    for chunk in file_chunks
                }
                
                for future in as_completed(future_to_chunk):
                    try:
                        chunk_results = future.result()
                        hash_results.extend(chunk_results)
                    except Exception as e:
                        self.logger.error(f"파일 해시 계산 오류: {str(e)}")
                        self.logger.error(traceback.format_exc())
        
        except Exception as e:
            self.logger.error(f"병렬 파일 해시 계산 오류: {str(e)}")
            self.logger.error(traceback.format_exc())
        
        return hash_results
    
    def _calculate_file_hashes_chunk(self, file_chunk: List[Path]) -> List[HashResult]:
        """파일 해시 계산 청크"""
        results = []
        
        for file_path in file_chunk:
            # 캐시 확인
            cached_result = self.cache.get_file_hash(str(file_path))
            if cached_result:
                results.append(cached_result)
                continue
            
            # 해시 생성
            file_hash = self.hash_generator.generate_file_hash(file_path)
            
            if file_hash:
                hash_result = HashResult(
                    content_hash=file_hash,
                    file_path=str(file_path),
                    file_name=file_path.name,
                    file_size=file_path.stat().st_size,
                    content_preview="",
                    hash_type="md5",
                    created_at=datetime.now().isoformat()
                )
                
                # 캐시 저장
                self.cache.set_file_hash(str(file_path), hash_result)
                results.append(hash_result)
        
        return results
    
    def _create_duplicate_groups_from_hashes(self, hash_results: List[HashResult]) -> List[DuplicateHashGroup]:
        """해시 결과로 중복 그룹 생성"""
        hash_groups = {}
        
        # 해시 그룹화
        for hash_result in hash_results:
            if hash_result.content_hash not in hash_groups:
                hash_groups[hash_result.content_hash] = []
            hash_groups[hash_result.content_hash].append(hash_result)
        
        # 중복 그룹 생성
        duplicate_groups = []
        
        for hash_value, files in hash_groups.items():
            if len(files) > 1:  # 중복된 파일만
                duplicate_group = DuplicateHashGroup(
                    hash_value=hash_value,
                    files=files,
                    similarity_score=1.0,  # 완전 중복
                    duplicate_type="content" if any(f.content_preview for f in files) else "file_hash",
                    created_at=datetime.now().isoformat()
                )
                duplicate_groups.append(duplicate_group)
        
        return duplicate_groups
    
    def _post_process_duplicate_groups(self, duplicate_groups: List[DuplicateHashGroup]) -> List[DuplicateHashGroup]:
        """중복 그룹 후처리"""
        # 파일 수 기반 정렬
        duplicate_groups.sort(key=lambda x: len(x.files), reverse=True)
        
        # 유일한 해시만 유지
        unique_groups = []
        seen_hashes = set()
        
        for group in duplicate_groups:
            if group.hash_value not in seen_hashes:
                unique_groups.append(group)
                seen_hashes.add(group.hash_value)
        
        return unique_groups
    
    def resolve_duplicates(self, strategy: str = "keep_first") -> Dict[str, Any]:
        """중복 해결"""
        resolved_files = []
        removed_files = []
        
        for group in self.duplicate_groups:
            # 중복 그룹 내 파일 선택
            if strategy == "keep_first":
                kept_file = group.files[0]
                removed_files = group.files[1:]
            elif strategy == "keep_largest":
                kept_file = max(group.files, key=lambda x: x.file_size)
                removed_files = [f for f in group.files if f != kept_file]
            elif strategy == "keep_smallest":
                kept_file = min(group.files, key=lambda x: x.file_size)
                removed_files = [f for f in group.files if f != kept_file]
            else:
                kept_file = group.files[0]
                removed_files = group.files[1:]
            
            resolved_files.append({
                'kept_file': kept_file,
                'removed_files': removed_files,
                'duplicate_type': group.duplicate_type
            })
        
        return {
            'resolved_files': resolved_files,
            'total_duplicates': len(resolved_files),
            'total_removed_files': len(removed_files),
            'space_saved': sum(f.file_size for f in removed_files)
        }
    
    def generate_deduplication_report(self, output_path: Path = None) -> Dict[str, Any]:
        """중복 검사 보고서 생성"""
        report = {
            'summary': {
                'total_files': self.total_files,
                'duplicate_groups': len(self.duplicate_groups),
                'duplicate_files': self.duplicate_files,
                'unique_files': self.total_files - self.duplicate_files,
                'processing_time': self.processing_time,
                'space_saved': sum(f.file_size for group in self.duplicate_groups for f in group.files[1:])
            },
            'duplicate_groups': [
                {
                    'hash_value': group.hash_value,
                    'file_count': len(group.files),
                    'duplicate_type': group.duplicate_type,
                    'files': [
                        {
                            'file_path': f.file_path,
                            'file_name': f.file_name,
                            'file_size': f.file_size,
                            'content_preview': f.content_preview
                        } for f in group.files
                    ]
                } for group in self.duplicate_groups
            ],
            'cache_stats': self.cache.get_stats(),
            'performance_stats': self.processor.get_performance_stats()
        }
        
        # 보고서 파일 저장
        if output_path:
            try:
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(report, f, indent=2, ensure_ascii=False)
                self.logger.info(f"중복 검사 보고서 저장 완료: {output_path}")
            except Exception as e:
                self.logger.error(f"보고서 저장 오류: {str(e)}")
        
        return report
    
    def get_performance_stats(self) -> Dict[str, Any]:
        """성능 통계 반환"""
        return {
            'total_files': self.total_files,
            'total_hashes': self.total_hashes,
            'duplicate_files': self.duplicate_files,
            'processing_time': self.processing_time,
            'duplicate_rate': self.duplicate_files / self.total_files * 100 if self.total_files > 0 else 0,
            'cache_stats': self.cache.get_stats(),
            'processor_stats': self.processor.get_performance_stats()
        }

# 전역 인스턴스
_default_hash_deduplicator = None

def get_default_hash_deduplicator() -> ParallelHashDeduplicator:
    """기본 해시 중복 검사기 인스턴스 반환"""
    global _default_hash_deduplicator
    if _default_hash_deduplicator is None:
        _default_hash_deduplicator = ParallelHashDeduplicator()
    return _default_hash_deduplicator