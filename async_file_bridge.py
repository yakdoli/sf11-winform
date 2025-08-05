"""
WinForms_Docs 비동기 파일 관리자 - 기존 시스템 통합 브리지

주요 기능:
==========
1. 기존 data_cleaner.py와의 호환성 유지
2. AsyncFileManager를 통한 점진적 마이그레이션 지원
3. 성능 모니터링 통합
4. 오류 처리 및 복구 메커니즘

통전략:
=======
- 기존 API 인터페이스 유지
- 내부적으로 AsyncFileManager 사용
- 성능 비교를 위한 측정 포인트 추가
- 점진적 마이그레이션을 위한 전환 모드

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0 (통합 브리지)
"""

import asyncio
import logging
import time
import psutil
import gc
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, asdict, field
from datetime import datetime
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

from async_file_manager import AsyncFileManager, FileStats, QueueStats
from data_cleaner import DataCleaner, DocumentInfo, CleaningStats

# 로깅 설정
logger = logging.getLogger(__name__)

@dataclass
class MigrationStats:
    """마이그레이션 통계 정보"""
    total_files: int = 0
    migrated_files: int = 0
    fallback_files: int = 0
    performance_improvement: float = 0.0
    memory_usage_comparison: Dict[str, float] = field(default_factory=dict)

class AsyncFileBridge:
    """비동기 파일 관리자 - 기존 시스템 통합 브리지"""
    
    def __init__(self, 
                 use_async: bool = True,
                 max_concurrent: int = 10,
                 io_workers: int = 4,
                 enable_migration_stats: bool = True):
        """
        통합 브리지 초기화
        
        Args:
            use_async: AsyncFileManager 사용 여부
            max_concurrent: 최대 동시 처리 수
            io_workers: I/O 워커 수
            enable_migration_stats: 마이그레이션 통계 활성화
        """
        self.use_async = use_async
        self.max_concurrent = max_concurrent
        self.io_workers = io_workers
        self.enable_migration_stats = enable_migration_stats
        
        # AsyncFileManager 인스턴스
        self.async_manager = None
        if use_async:
            self.async_manager = AsyncFileManager(max_concurrent, io_workers)
        
        # 기존 DataCleaner 인스턴스 (백업용)
        self.fallback_cleaner = DataCleaner()
        
        # 마이그레이션 통계
        self.migration_stats = MigrationStats()
        
        # 성능 측정을 위한 변수
        self.performance_metrics = {
            'async_times': [],
            'sync_times': [],
            'memory_usage': []
        }
        
        # 스레드 안전성을 위한 락
        self.bridge_lock = threading.Lock()
        
        logger.info(f"AsyncFileBridge 초기화 완료 - Async 사용: {use_async}")
    
    async def process_files_async(self, file_paths: List[Path]) -> List[DocumentInfo]:
        """비동기 파일 처리 (AsyncFileManager 사용)"""
        if not self.use_async or not self.async_manager:
            logger.warning("AsyncFileManager가 활성화되지 않음 - 동기 처리로 전환")
            return await self._process_files_sync_fallback(file_paths)
        
        try:
            start_time = time.time()
            
            # AsyncFileManager 시작
            await self.async_manager.start_processing()
            
            # 파일 경로 문자열로 변환
            str_file_paths = [str(fp) for fp in file_paths]
            
            # 비동기 처리
            results = await self.async_manager.process_file_batch(str_file_paths)
            
            # 결과 변환
            document_infos = []
            for result in results:
                if result and 'content' in result:
                    doc_info = DocumentInfo(
                        file_path=result.get('file_path', ''),
                        original_filename=result.get('original_filename', ''),
                        category=result.get('category', ''),
                        subcategory=result.get('subcategory', ''),
                        title=result.get('title', ''),
                        content=result.get('content', ''),
                        cleaned_content=result.get('cleaned_content', ''),
                        metadata=result.get('metadata', {}),
                        code_snippets=result.get('code_snippets', []),
                        word_count=result.get('word_count', 0),
                        char_count=result.get('char_count', 0),
                        processing_time=result.get('processing_time', 0.0),
                        memory_usage=result.get('memory_usage', 0.0)
                    )
                    document_infos.append(doc_info)
            
            processing_time = time.time() - start_time
            self.performance_metrics['async_times'].append(processing_time)
            
            # 마이그레이션 통계 업데이트
            if self.enable_migration_stats:
                with self.bridge_lock:
                    self.migration_stats.migrated_files += len(document_infos)
                    self.migration_stats.total_files += len(file_paths)
            
            logger.info(f"비동기 처리 완료: {len(document_infos)}개 파일, {processing_time:.2f}초")
            return document_infos
            
        except Exception as e:
            logger.error(f"비동기 처리 오류: {str(e)}")
            # 동기 처리로 폴백
            return await self._process_files_sync_fallback(file_paths)
    
    async def _process_files_sync_fallback(self, file_paths: List[Path]) -> List[DocumentInfo]:
        """동기 처리 폴백 (기존 DataCleaner 사용)"""
        start_time = time.time()
        
        try:
            # 기존 DataCleaner 사용
            results = self.fallback_cleaner.process_files(file_paths)
            
            processing_time = time.time() - start_time
            self.performance_metrics['sync_times'].append(processing_time)
            
            # 마이그레이션 통계 업데이트
            if self.enable_migration_stats:
                with self.bridge_lock:
                    self.migration_stats.fallback_files += len(results)
                    self.migration_stats.total_files += len(file_paths)
            
            logger.info(f"동기 처리 폴백 완료: {len(results)}개 파일, {processing_time:.2f}초")
            return results
            
        except Exception as e:
            logger.error(f"동기 처리 폴백 오류: {str(e)}")
            return []
    
    def process_files_parallel(self, file_paths: List[Path]) -> List[DocumentInfo]:
        """병렬 파일 처리 (호환성 메소드)"""
        logger.info(f"병렬 파일 처리 시작: {len(file_paths)}개 파일")
        
        start_time = time.time()
        
        try:
            if self.use_async:
                # 비동기 처리 실행
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    # 새로운 이벤트 루프에서 실행
                    import concurrent.futures
                    with concurrent.futures.ThreadPoolExecutor() as executor:
                        future = executor.submit(
                            asyncio.run, 
                            self.process_files_async(file_paths)
                        )
                        results = future.result()
                else:
                    results = asyncio.run(self.process_files_async(file_paths))
            else:
                # 동기 처리 실행
                results = self.fallback_cleaner.process_files_parallel(file_paths)
            
            processing_time = time.time() - start_time
            
            # 성능 측정
            self._measure_performance(len(file_paths), processing_time)
            
            logger.info(f"병렬 처리 완료: {len(results)}개 파일, {processing_time:.2f}초")
            return results
            
        except Exception as e:
            logger.error(f"병렬 처리 오류: {str(e)}")
            return []
    
    def process_directory_parallel(self, directory: Optional[str] = None) -> List[DocumentInfo]:
        """디렉토리 병렬 처리 (호환성 메소드)"""
        logger.info(f"디렉토리 병렬 처리 시작: {directory}")
        
        start_time = time.time()
        
        try:
            if directory is None:
                from config import WINFORMS_DOCS_DIR
                directory = str(WINFORMS_DOCS_DIR)
            
            # 파일 수집
            markdown_files = self._collect_markdown_files(Path(directory))
            
            if self.use_async:
                # 비동기 처리 실행
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    # 새로운 이벤트 루프에서 실행
                    import concurrent.futures
                    with concurrent.futures.ThreadPoolExecutor() as executor:
                        future = executor.submit(
                            asyncio.run, 
                            self.process_files_async(markdown_files)
                        )
                        results = future.result()
                else:
                    results = asyncio.run(self.process_files_async(markdown_files))
            else:
                # 기존 DataCleaner 사용
                results = self.fallback_cleaner.process_directory_parallel(directory)
            
            processing_time = time.time() - start_time
            
            # 성능 측정
            self._measure_performance(len(markdown_files), processing_time)
            
            logger.info(f"디렉토리 처리 완료: {len(results)}개 파일, {processing_time:.2f}초")
            return results
            
        except Exception as e:
            logger.error(f"디렉토리 처리 오류: {str(e)}")
            return []
    
    def _collect_markdown_files(self, directory: Path) -> List[Path]:
        """마크다운 파일 수집"""
        markdown_files = []
        
        try:
            for file_path in directory.rglob("*.md"):
                if file_path.is_file():
                    markdown_files.append(file_path)
            
            logger.info(f"마크다운 파일 발견: {len(markdown_files)}개")
            return markdown_files
            
        except Exception as e:
            logger.error(f"마크다운 파일 수집 오류: {str(e)}")
            return []
    
    def _measure_performance(self, file_count: int, processing_time: float) -> None:
        """성능 측정"""
        try:
            # 메모리 사용량 측정
            memory_usage = psutil.Process().memory_info().rss / 1024 / 1024  # MB
            
            # 처리량 계산
            throughput = file_count / max(processing_time, 0.001)  # 파일/초
            
            # 성능 메트릭 저장
            self.performance_metrics['memory_usage'].append(memory_usage)
            
            logger.debug(f"성능 측정: 처리량={throughput:.2f} 파일/초, 메모리={memory_usage:.2f}MB")
            
        except Exception as e:
            logger.error(f"성능 측정 오류: {str(e)}")
    
    def get_performance_comparison(self) -> Dict[str, Any]:
        """성능 비교 정보 반환"""
        try:
            async_avg = sum(self.performance_metrics['async_times']) / max(len(self.performance_metrics['async_times']), 1)
            sync_avg = sum(self.performance_metrics['sync_times']) / max(len(self.performance_metrics['sync_times']), 1)
            
            memory_avg = sum(self.performance_metrics['memory_usage']) / max(len(self.performance_metrics['memory_usage']), 1)
            
            improvement = 0.0
            if sync_avg > 0 and async_avg > 0:
                improvement = ((sync_avg - async_avg) / sync_avg) * 100
            
            return {
                'async_average_time': async_avg,
                'sync_average_time': sync_avg,
                'performance_improvement': improvement,
                'average_memory_usage': memory_avg,
                'total_async_operations': len(self.performance_metrics['async_times']),
                'total_sync_operations': len(self.performance_metrics['sync_times'])
            }
            
        except Exception as e:
            logger.error(f"성능 비교 계산 오류: {str(e)}")
            return {}
    
    def get_migration_stats(self) -> MigrationStats:
        """마이그레이션 통계 반환"""
        with self.bridge_lock:
            # 성능 개선 계산
            if self.migration_stats.total_files > 0:
                async_count = self.migration_stats.migrated_files
                sync_count = self.migration_stats.fallback_files
                
                if sync_count > 0:
                    async_avg = sum(self.performance_metrics['async_times']) / max(async_count, 1)
                    sync_avg = sum(self.performance_metrics['sync_times']) / max(sync_count, 1)
                    
                    if sync_avg > 0 and async_avg > 0:
                        self.migration_stats.performance_improvement = ((sync_avg - async_avg) / sync_avg) * 100
            
            return self.migration_stats
    
    def get_async_manager_stats(self) -> Optional[Dict[str, Any]]:
        """AsyncFileManager 통계 반환"""
        if not self.async_manager:
            return None
        
        try:
            processing_stats = self.async_manager.get_processing_stats()
            queue_stats = self.async_manager.get_queue_stats()
            
            return {
                'processing_stats': asdict(processing_stats),
                'queue_stats': asdict(queue_stats)
            }
            
        except Exception as e:
            logger.error(f"AsyncFileManager 통계 조회 오류: {str(e)}")
            return None
    
    def switch_mode(self, use_async: bool) -> None:
        """처리 모드 전환"""
        with self.bridge_lock:
            old_mode = self.use_async
            self.use_async = use_async
            
            if use_async and not self.async_manager:
                self.async_manager = AsyncFileManager(self.max_concurrent, self.io_workers)
            elif not use_async:
                self.async_manager = None
            
            logger.info(f"처리 모드 전환: {old_mode} -> {use_async}")
    
    def cleanup(self) -> None:
        """자원 정리"""
        try:
            if self.async_manager:
                asyncio.run(self.async_manager.stop_processing())
            
            # 메모리 정리
            gc.collect()
            
            logger.info("AsyncFileBridge 자원 정리 완료")
            
        except Exception as e:
            logger.error(f"자원 정리 오류: {str(e)}")

# 유틸리티 함수
def create_async_file_bridge(use_async: bool = True, 
                           max_concurrent: int = 10, 
                           io_workers: int = 4) -> AsyncFileBridge:
    """AsyncFileBridge 인스턴스 생성"""
    return AsyncFileBridge(
        use_async=use_async,
        max_concurrent=max_concurrent,
        io_workers=io_workers
    )

# 테스트 함수
async def test_async_file_bridge():
    """AsyncFileBridge 테스트"""
    import tempfile
    import os
    
    # 테스트 파일 생성
    test_dir = Path(tempfile.mkdtemp())
    test_files = []
    
    for i in range(5):
        test_file = test_dir / f"test_{i}.md"
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(f"# 테스트 문서 {i+1}\n\n")
            f.write(f"이것은 테스트 문서 {i+1}의 내용입니다.\n" * 10)
        test_files.append(test_file)
    
    try:
        # AsyncFileBridge 생성
        bridge = create_async_file_bridge(use_async=True)
        
        # 비동기 처리 테스트
        print("비동기 처리 테스트 시작...")
        results = await bridge.process_files_async(test_files)
        print(f"비동기 처리 결과: {len(results)}개 파일")
        
        # 성능 비조 정보
        perf_comparison = bridge.get_performance_comparison()
        print(f"성능 비교: {perf_comparison}")
        
        # 마이그레이션 통계
        migration_stats = bridge.get_migration_stats()
        print(f"마이그레이션 통계: {asdict(migration_stats)}")
        
        # 모드 전환 테스트
        print("모드 전환 테스트...")
        bridge.switch_mode(False)
        sync_results = bridge.process_files_parallel(test_files)
        print(f"동기 처리 결과: {len(sync_results)}개 파일")
        
        # 다시 비동기 모드로 전환
        bridge.switch_mode(True)
        
    finally:
        # 테스트 정리
        bridge.cleanup()
        for test_file in test_files:
            try:
                test_file.unlink()
            except:
                pass
        try:
            test_dir.rmdir()
        except:
            pass

if __name__ == "__main__":
    # 테스트 실행
    asyncio.run(test_async_file_bridge())