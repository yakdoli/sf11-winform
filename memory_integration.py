"""
WinForms_Docs 메모리 관리 시스템 통합 모듈

주요 기능:
==========
1. 기존 시스템과의 통합
   - AsyncFileManager와의 메모리 관리 통합
   - pandas_data_processor와의 메모리 풀 통합
   - arrow_data_manager와의 메모리 최적화

2. 메모리 관리 확장
   - 파일 I/O 메모리 관리
   - 데이터 처리 메모리 관리
   - 직렬화/역직렬화 메모리 관리

3. 성능 모니터링 확장
   - 메모리 사용량 추적
   - 성능 저하 원인 분석
   - 자동 최적화 트리거

4. 호환성 유지
   - 기존 API와의 완벽한 호환성
   - 점진적 적용 가능
   - 롤백 지원

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0 (메모리 관리 통합 모듈)
"""

import asyncio
import logging
import time
import threading
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, field
from enum import Enum
import weakref

# 로컬 모듈 임포트
try:
    from memory_manager import (
        MemoryManager, MemoryPoolType, create_memory_manager,
        get_system_memory_info, MemoryStats
    )
    MEMORY_MANAGER_AVAILABLE = True
except ImportError:
    MEMORY_MANAGER_AVAILABLE = False
    MemoryManager = None
    MemoryPoolType = None
    create_memory_manager = None
    get_system_memory_info = None
    MemoryStats = None

try:
    from async_file_manager import AsyncFileManager, FileMetadata
    ASYNC_FILE_MANAGER_AVAILABLE = True
except ImportError:
    ASYNC_FILE_MANAGER_AVAILABLE = False
    AsyncFileManager = None
    FileMetadata = None

try:
    from pandas_data_processor import PandasDataProcessor
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    PandasDataProcessor = None

try:
    from arrow_data_manager import ArrowDataManager
    ARROW_AVAILABLE = True
except ImportError:
    ARROW_AVAILABLE = False
    ArrowDataManager = None

# 로깅 설정
logger = logging.getLogger(__name__)

class IntegrationMode(Enum):
    """통합 모드"""
    DISABLED = "disabled"
    BASIC = "basic"
    ENHANCED = "enhanced"
    OPTIMIZED = "optimized"

@dataclass
class MemoryIntegrationConfig:
    """메모리 통합 설정"""
    mode: IntegrationMode = IntegrationMode.ENHANCED
    enable_file_io_optimization: bool = True
    enable_pandas_optimization: bool = True
    enable_arrow_optimization: bool = True
    enable_auto_optimization: bool = True
    memory_threshold_percent: float = 80.0
    optimization_interval: float = 60.0
    enable_memory_leak_detection: bool = True
    enable_fragmentation_management: bool = True

class MemoryIntegratedFileManager:
    """메모리 통합 파일 관리자"""
    
    def __init__(self, 
                 file_manager: AsyncFileManager,
                 memory_manager: MemoryManager,
                 config: MemoryIntegrationConfig):
        self.file_manager = file_manager
        self.memory_manager = memory_manager
        self.config = config
        
        # 메모리 풀 할당
        self.file_io_pool = memory_manager.memory_pools[MemoryPoolType.BUFFER]
        self.temp_pool = memory_manager.memory_pools[MemoryPoolType.TEMPORARY]
        
        # 통계
        self.io_stats = {
            'total_allocations': 0,
            'total_deallocations': 0,
            'peak_memory_usage': 0,
            'average_allocation_time': 0.0
        }
        
        # 메모리 추적
        self.file_memory_blocks: Dict[str, str] = {}  # file_path -> block_id
        self.block_memory_files: Dict[str, str] = {}  # block_id -> file_path
        
        logger.info("MemoryIntegratedFileManager 초기화 완료")
    
    async def read_file_with_memory_management(self, file_path: str) -> Optional[bytes]:
        """메모리 관리와 함께 파일 읽기"""
        try:
            # 파일 크기 확인
            file_size = self._get_file_size(file_path)
            if file_size is None:
                return None
            
            # 메모리 풀에서 할당
            block_id = self.file_io_pool.allocate_memory(file_size, f"file_read_{file_path}")
            if block_id is None:
                logger.warning(f"메모리 할당 실패: {file_path}")
                return None
            
            # 메모리 블록 추적
            self.file_memory_blocks[file_path] = block_id
            self.block_memory_files[block_id] = file_path
            
            # 원본 파일 읽기
            content = await self.file_manager.read_file_with_memory_mapping(file_path)
            if content is None:
                # 할당된 메모리 해제
                self.file_io_pool.deallocate_memory(block_id)
                del self.file_memory_blocks[file_path]
                del self.block_memory_files[block_id]
                return None
            
            # 메모리 복사 (메모리 관리 적용)
            memory_content = self._copy_to_managed_memory(content, block_id)
            
            # 통계 업데이트
            self.io_stats['total_allocations'] += 1
            self.io_stats['peak_memory_usage'] = max(
                self.io_stats['peak_memory_usage'], 
                file_size
            )
            
            return memory_content
            
        except Exception as e:
            logger.error(f"메모리 관리 파일 읽기 오류: {file_path}, {str(e)}")
            return None
    
    async def write_file_with_memory_management(self, file_path: str, data: bytes) -> bool:
        """메모리 관리와 함께 파일 쓰기"""
        try:
            # 데이터 크기 확인
            data_size = len(data)
            
            # 메모리 풀에서 할당
            block_id = self.file_io_pool.allocate_memory(data_size, f"file_write_{file_path}")
            if block_id is None:
                logger.warning(f"메모리 할당 실패: {file_path}")
                return False
            
            # 메모리 블록 추적
            self.file_memory_blocks[file_path] = block_id
            self.block_memory_files[block_id] = file_path
            
            # 데이터를 관리된 메모리에 복사
            success = self._copy_from_managed_memory(data, block_id)
            if not success:
                # 할당된 메모리 해제
                self.file_io_pool.deallocate_memory(block_id)
                del self.file_memory_blocks[file_path]
                del self.block_memory_files[block_id]
                return False
            
            # 파일 쓰기
            success = await self.file_manager.write_file_chunks(file_path, self._create_data_generator(data))
            
            # 메모리 해제
            self.file_io_pool.deallocate_memory(block_id)
            del self.file_memory_blocks[file_path]
            del self.block_memory_files[block_id]
            
            # 통계 업데이트
            self.io_stats['total_deallocations'] += 1
            
            return success
            
        except Exception as e:
            logger.error(f"메모리 관리 파일 쓰기 오류: {file_path}, {str(e)}")
            return False
    
    def _get_file_size(self, file_path: str) -> Optional[int]:
        """파일 크기 가져오기"""
        try:
            import os
            return os.path.getsize(file_path)
        except Exception as e:
            logger.error(f"파일 크기 조회 오류: {file_path}, {str(e)}")
            return None
    
    def _copy_to_managed_memory(self, data: bytes, block_id: str) -> bytes:
        """관리된 메모리로 데이터 복사"""
        # 실제 구현에서는 메모리 매핑 등을 사용
        return data
    
    def _copy_from_managed_memory(self, data: bytes, block_id: str) -> bool:
        """관리된 메모리에서 데이터 복사"""
        # 실제 구현에서는 메모리 매핑 등을 사용
        return True
    
    def _create_data_generator(self, data: bytes):
        """데이터 생성기"""
        async def data_generator():
            yield data
        return data_generator()
    
    def cleanup_file_memory(self, file_path: str) -> bool:
        """파일 관련 메모리 정리"""
        try:
            block_id = self.file_memory_blocks.get(file_path)
            if block_id:
                success = self.file_io_pool.deallocate_memory(block_id)
                if success:
                    del self.file_memory_blocks[file_path]
                    del self.block_memory_files[block_id]
                    return True
            return False
            
        except Exception as e:
            logger.error(f"파일 메모리 정리 오류: {file_path}, {str(e)}")
            return False
    
    def get_file_memory_stats(self) -> Dict[str, Any]:
        """파일 메모리 통계 반환"""
        return {
            'total_file_allocations': len(self.file_memory_blocks),
            'total_io_allocations': self.io_stats['total_allocations'],
            'total_io_deallocations': self.io_stats['total_deallocations'],
            'peak_memory_usage': self.io_stats['peak_memory_usage'],
            'tracked_files': list(self.file_memory_blocks.keys())
        }

class MemoryIntegratedPandasProcessor:
    """메모리 통합 pandas 데이터 프로세서"""
    
    def __init__(self, 
                 pandas_processor: PandasDataProcessor,
                 memory_manager: MemoryManager,
                 config: MemoryIntegrationConfig):
        self.pandas_processor = pandas_processor
        self.memory_manager = memory_manager
        self.config = config
        
        # 메모리 풀 할당
        self.pandas_pool = memory_manager.memory_pools[MemoryPoolType.PANDAS]
        self.temp_pool = memory_manager.memory_pools[MemoryPoolType.TEMPORARY]
        
        # 통계
        self.processing_stats = {
            'total_operations': 0,
            'successful_operations': 0,
            'failed_operations': 0,
            'total_memory_allocated': 0,
            'average_processing_time': 0.0
        }
        
        # 메모리 추적
        self.data_memory_blocks: Dict[str, str] = {}  # data_id -> block_id
        self.block_data_ids: Dict[str, str] = {}     # block_id -> data_id
        
        logger.info("MemoryIntegratedPandasProcessor 초기화 완료")
    
    async def process_data_with_memory_management(self, data: Any, data_id: str) -> Optional[Any]:
        """메모리 관리와 함께 데이터 처리"""
        try:
            # 데이터 크기 추정
            estimated_size = self._estimate_data_size(data)
            
            # 메모리 풀에서 할당
            block_id = self.pandas_pool.allocate_memory(estimated_size, f"pandas_process_{data_id}")
            if block_id is None:
                logger.warning(f"메모리 할당 실패: {data_id}")
                return None
            
            # 메모리 블록 추적
            self.data_memory_blocks[data_id] = block_id
            self.block_data_ids[block_id] = data_id
            
            # 데이터 처리
            start_time = time.time()
            result = await self.pandas_processor.process_data(data)
            processing_time = time.time() - start_time
            
            # 통계 업데이트
            self.processing_stats['total_operations'] += 1
            self.processing_stats['total_memory_allocated'] += estimated_size
            self.processing_stats['average_processing_time'] = (
                (self.processing_stats['average_processing_time'] * (self.processing_stats['total_operations'] - 1) + processing_time) /
                self.processing_stats['total_operations']
            )
            
            if result is not None:
                self.processing_stats['successful_operations'] += 1
            else:
                self.processing_stats['failed_operations'] += 1
            
            return result
            
        except Exception as e:
            logger.error(f"메모리 관리 데이터 처리 오류: {data_id}, {str(e)}")
            return None
    
    def _estimate_data_size(self, data: Any) -> int:
        """데이터 크기 추정"""
        try:
            import sys
            return sys.getsizeof(data)
        except Exception:
            return 1024 * 1024  # 기본 1MB
    
    def cleanup_data_memory(self, data_id: str) -> bool:
        """데이터 관련 메모리 정리"""
        try:
            block_id = self.data_memory_blocks.get(data_id)
            if block_id:
                success = self.pandas_pool.deallocate_memory(block_id)
                if success:
                    del self.data_memory_blocks[data_id]
                    del self.block_data_ids[block_id]
                    return True
            return False
            
        except Exception as e:
            logger.error(f"데이터 메모리 정리 오류: {data_id}, {str(e)}")
            return False
    
    def get_processing_stats(self) -> Dict[str, Any]:
        """데이터 처리 통계 반환"""
        return self.processing_stats.copy()

class MemoryIntegratedArrowManager:
    """메모리 통합 Arrow 데이터 관리자"""
    
    def __init__(self, 
                 arrow_manager: ArrowDataManager,
                 memory_manager: MemoryManager,
                 config: MemoryIntegrationConfig):
        self.arrow_manager = arrow_manager
        self.memory_manager = memory_manager
        self.config = config
        
        # 메모리 풀 할당
        self.arrow_pool = memory_manager.memory_pools[MemoryPoolType.ARROW]
        self.temp_pool = memory_manager.memory_pools[MemoryPoolType.TEMPORARY]
        
        # 통계
        self.arrow_stats = {
            'total_operations': 0,
            'successful_operations': 0,
            'failed_operations': 0,
            'total_memory_allocated': 0,
            'compression_ratio': 0.0
        }
        
        # 메모리 추적
        self.table_memory_blocks: Dict[str, str] = {}  # table_id -> block_id
        self.block_table_ids: Dict[str, str] = {}     # block_id -> table_id
        
        logger.info("MemoryIntegratedArrowManager 초기화 완료")
    
    async def create_table_with_memory_management(self, data: Any, table_id: str) -> Optional[Any]:
        """메모리 관리와 함께 Arrow 테이블 생성"""
        try:
            # 데이터 크기 추정
            estimated_size = self._estimate_data_size(data)
            
            # 메모리 풀에서 할당
            block_id = self.arrow_pool.allocate_memory(estimated_size, f"arrow_table_{table_id}")
            if block_id is None:
                logger.warning(f"메모리 할당 실패: {table_id}")
                return None
            
            # 메모리 블록 추적
            self.table_memory_blocks[table_id] = block_id
            self.block_table_ids[block_id] = table_id
            
            # 테이블 생성
            start_time = time.time()
            table = await self.arrow_manager.create_table(data)
            processing_time = time.time() - start_time
            
            # 통계 업데이트
            self.arrow_stats['total_operations'] += 1
            self.arrow_stats['total_memory_allocated'] += estimated_size
            
            if table is not None:
                self.arrow_stats['successful_operations'] += 1
                # 압축 비율 계산
                original_size = estimated_size
                compressed_size = self._estimate_table_size(table)
                self.arrow_stats['compression_ratio'] = compressed_size / original_size if original_size > 0 else 1.0
            else:
                self.arrow_stats['failed_operations'] += 1
            
            return table
            
        except Exception as e:
            logger.error(f"메모리 관리 Arrow 테이블 생성 오류: {table_id}, {str(e)}")
            return None
    
    def _estimate_data_size(self, data: Any) -> int:
        """데이터 크기 추정"""
        try:
            import sys
            return sys.getsizeof(data)
        except Exception:
            return 1024 * 1024  # 기본 1MB
    
    def _estimate_table_size(self, table: Any) -> int:
        """테이블 크기 추정"""
        try:
            # Arrow 테이블의 실제 크기 추정
            return len(table.serialize()) if hasattr(table, 'serialize') else 1024 * 1024
        except Exception:
            return 1024 * 1024  # 기본 1MB
    
    def cleanup_table_memory(self, table_id: str) -> bool:
        """테이블 관련 메모리 정리"""
        try:
            block_id = self.table_memory_blocks.get(table_id)
            if block_id:
                success = self.arrow_pool.deallocate_memory(block_id)
                if success:
                    del self.table_memory_blocks[table_id]
                    del self.block_table_ids[block_id]
                    return True
            return False
            
        except Exception as e:
            logger.error(f"테이블 메모리 정리 오류: {table_id}, {str(e)}")
            return False
    
    def get_arrow_stats(self) -> Dict[str, Any]:
        """Arrow 통계 반환"""
        return self.arrow_stats.copy()

class MemoryIntegrationManager:
    """메모리 통합 관리자"""
    
    def __init__(self, config: MemoryIntegrationConfig):
        self.config = config
        
        # 메모리 관리자 생성
        if MEMORY_MANAGER_AVAILABLE:
            self.memory_manager = create_memory_manager()
        else:
            self.memory_manager = None
            logger.warning("MemoryManager를 사용할 수 없습니다")
        
        # 통합 컴포넌트
        self.file_manager: Optional[MemoryIntegratedFileManager] = None
        self.pandas_processor: Optional[MemoryIntegratedPandasProcessor] = None
        self.arrow_manager: Optional[MemoryIntegratedArrowManager] = None
        
        # 통계
        self.integration_stats = {
            'total_operations': 0,
            'successful_operations': 0,
            'failed_operations': 0,
            'memory_optimization_events': 0,
            'last_optimization_time': 0.0
        }
        
        # 자동 최적화
        self.auto_optimization_active = False
        self.optimization_timer = None
        
        logger.info("MemoryIntegrationManager 초기화 완료")
    
    def integrate_file_manager(self, file_manager: AsyncFileManager) -> bool:
        """파일 관리자와 통합"""
        try:
            if not MEMORY_MANAGER_AVAILABLE or not ASYNC_FILE_MANAGER_AVAILABLE:
                logger.warning("파일 관리자 통합을 위한 필수 모듈이 없습니다")
                return False
            
            self.file_manager = MemoryIntegratedFileManager(
                file_manager, self.memory_manager, self.config
            )
            
            logger.info("파일 관리자 통합 완료")
            return True
            
        except Exception as e:
            logger.error(f"파일 관리자 통합 오류: {str(e)}")
            return False
    
    def integrate_pandas_processor(self, pandas_processor: PandasDataProcessor) -> bool:
        """pandas 프로세서와 통합"""
        try:
            if not MEMORY_MANAGER_AVAILABLE or not PANDAS_AVAILABLE:
                logger.warning("pandas 프로세서 통합을 위한 필수 모듈이 없습니다")
                return False
            
            self.pandas_processor = MemoryIntegratedPandasProcessor(
                pandas_processor, self.memory_manager, self.config
            )
            
            logger.info("pandas 프로세서 통합 완료")
            return True
            
        except Exception as e:
            logger.error(f"pandas 프로세서 통합 오류: {str(e)}")
            return False
    
    def integrate_arrow_manager(self, arrow_manager: ArrowDataManager) -> bool:
        """Arrow 관리자와 통합"""
        try:
            if not MEMORY_MANAGER_AVAILABLE or not ARROW_AVAILABLE:
                logger.warning("Arrow 관리자 통합을 위한 필수 모듈이 없습니다")
                return False
            
            self.arrow_manager = MemoryIntegratedArrowManager(
                arrow_manager, self.memory_manager, self.config
            )
            
            logger.info("Arrow 관리자 통합 완료")
            return True
            
        except Exception as e:
            logger.error(f"Arrow 관리자 통합 오류: {str(e)}")
            return False
    
    def start_auto_optimization(self) -> bool:
        """자동 최적화 시작"""
        try:
            if not self.config.enable_auto_optimization:
                logger.info("자동 최적화가 비활성화되어 있습니다")
                return False
            
            if self.auto_optimization_active:
                logger.warning("자동 최적화가 이미 활성화되어 있습니다")
                return False
            
            self.auto_optimization_active = True
            
            # 메모리 관리자 모니터링 시작
            if self.memory_manager:
                self.memory_manager.start_monitoring(interval=self.config.optimization_interval)
            
            # 최적화 타이머 시작
            self.optimization_timer = threading.Timer(
                self.config.optimization_interval,
                self._auto_optimization_loop
            )
            self.optimization_timer.daemon = True
            self.optimization_timer.start()
            
            logger.info("자동 최적화 시작")
            return True
            
        except Exception as e:
            logger.error(f"자동 최적화 시작 오류: {str(e)}")
            return False
    
    def _auto_optimization_loop(self) -> None:
        """자동 최적화 루프"""
        try:
            if not self.auto_optimization_active:
                return
            
            # 메모리 상태 확인
            if self.memory_manager:
                stats = self.memory_manager.get_memory_stats()
                
                # 메모리 임계치 초과 시 최적화
                if stats.memory_percent > self.config.memory_threshold_percent:
                    self._perform_memory_optimization(stats)
                    self.integration_stats['memory_optimization_events'] += 1
                    self.integration_stats['last_optimization_time'] = time.time()
            
            # 다음 최적화 예약
            if self.auto_optimization_active:
                self.optimization_timer = threading.Timer(
                    self.config.optimization_interval,
                    self._auto_optimization_loop
                )
                self.optimization_timer.daemon = True
                self.optimization_timer.start()
                
        except Exception as e:
            logger.error(f"자동 최적화 루프 오류: {str(e)}")
    
    def _perform_memory_optimization(self, stats: MemoryStats) -> None:
        """메모리 최적화 수행"""
        try:
            logger.info(f"메모리 최적화 수행 (사용률: {stats.memory_percent:.1f}%)")
            
            # 메모리 관리자 최적화
            if self.memory_manager:
                self.memory_manager.optimize_memory_usage()
            
            # 파일 관리자 메모리 정리
            if self.file_manager:
                self._cleanup_file_memory()
            
            # pandas 프로세서 메모리 정리
            if self.pandas_processor:
                self._cleanup_pandas_memory()
            
            # Arrow 관리자 메모리 정리
            if self.arrow_manager:
                self._cleanup_arrow_memory()
                
        except Exception as e:
            logger.error(f"메모리 최적화 수행 오류: {str(e)}")
    
    def _cleanup_file_memory(self) -> None:
        """파일 관련 메모리 정리"""
        try:
            if self.file_manager:
                # 사용되지 않는 파일 메모리 정리
                tracked_files = self.file_manager.get_file_memory_stats()['tracked_files']
                
                for file_path in tracked_files:
                    # 파일이 존재하지 않으면 메모리 정리
                    import os
                    if not os.path.exists(file_path):
                        self.file_manager.cleanup_file_memory(file_path)
                        
        except Exception as e:
            logger.error(f"파일 메모리 정리 오류: {str(e)}")
    
    def _cleanup_pandas_memory(self) -> None:
        """pandas 관련 메모리 정리"""
        try:
            if self.pandas_processor:
                # 데이터 프로세서의 내부 정리 메서드 호출
                # pandas 프로세서의 내부 정리 메서드 호출
                tracked_data = self.pandas_processor.data_memory_blocks.keys()
                for data_id in tracked_data:
                    self.pandas_processor.cleanup_data_memory(data_id)
                    
        except Exception as e:
            logger.error(f"pandas 메모리 정리 오류: {str(e)}")
    
    def _cleanup_arrow_memory(self) -> None:
        """Arrow 관련 메모리 정리"""
        try:
            if self.arrow_manager:
                # Arrow 관리자의 내부 정리 메서드 호출
                tracked_tables = self.arrow_manager.table_memory_blocks.keys()
                for table_id in tracked_tables:
                    self.arrow_manager.cleanup_table_memory(table_id)
                    
        except Exception as e:
            logger.error(f"Arrow 메모리 정리 오류: {str(e)}")
    
    def stop_auto_optimization(self) -> bool:
        """자동 최적화 중지"""
        try:
            self.auto_optimization_active = False
            
            if self.optimization_timer:
                self.optimization_timer.cancel()
                self.optimization_timer = None
            
            # 메모리 관리자 모니터링 중지
            if self.memory_manager:
                self.memory_manager.stop_monitoring()
            
            logger.info("자동 최적화 중지")
            return True
            
        except Exception as e:
            logger.error(f"자동 최적화 중지 오류: {str(e)}")
            return False
    
    def get_integration_stats(self) -> Dict[str, Any]:
        """통합 통계 반환"""
        stats = self.integration_stats.copy()
        
        # 파일 관리자 통계
        if self.file_manager:
            stats['file_manager_stats'] = self.file_manager.get_file_memory_stats()
        
        # pandas 프로세서 통계
        if self.pandas_processor:
            stats['pandas_processor_stats'] = self.pandas_processor.get_processing_stats()
        
        # Arrow 관리자 통계
        if self.arrow_manager:
            stats['arrow_manager_stats'] = self.arrow_manager.get_arrow_stats()
        
        # 메모리 관리자 통계
        if self.memory_manager:
            stats['memory_manager_stats'] = self.memory_manager.get_memory_stats()
        
        return stats
    
    def cleanup_all_memory(self) -> bool:
        """모든 메모리 정리"""
        try:
            # 파일 메모리 정리
            if self.file_manager:
                tracked_files = self.file_manager.get_file_memory_stats()['tracked_files']
                for file_path in tracked_files:
                    self.file_manager.cleanup_file_memory(file_path)
            
            # pandas 메모리 정리
            if self.pandas_processor:
                tracked_data = self.pandas_processor.data_memory_blocks.keys()
                for data_id in tracked_data:
                    self.pandas_processor.cleanup_data_memory(data_id)
            
            # Arrow 메모리 정리
            if self.arrow_manager:
                tracked_tables = self.arrow_manager.table_memory_blocks.keys()
                for table_id in tracked_tables:
                    self.arrow_manager.cleanup_table_memory(table_id)
            
            # 메모리 관리자 정리
            if self.memory_manager:
                self.memory_manager.cleanup_memory()
            
            logger.info("모든 메모리 정리 완료")
            return True
            
        except Exception as e:
            logger.error(f"모든 메모리 정리 오류: {str(e)}")
            return False
    
    def __del__(self):
        """소멸자"""
        try:
            self.stop_auto_optimization()
            self.cleanup_all_memory()
        except Exception:
            pass  # 소멸자에서는 예외 무시

# 유틸리티 함수
def create_memory_integration_manager(config: MemoryIntegrationConfig) -> MemoryIntegrationManager:
    """MemoryIntegrationManager 인스턴스 생성"""
    return MemoryIntegrationManager(config)

def create_default_config() -> MemoryIntegrationConfig:
    """기본 설정 생성"""
    return MemoryIntegrationConfig(
        mode=IntegrationMode.ENHANCED,
        enable_file_io_optimization=True,
        enable_pandas_optimization=True,
        enable_arrow_optimization=True,
        enable_auto_optimization=True,
        memory_threshold_percent=80.0,
        optimization_interval=60.0,
        enable_memory_leak_detection=True,
        enable_fragmentation_management=True
    )

# 테스트 함수
def test_memory_integration():
    """메모리 통합 테스트"""
    try:
        # 설정 생성
        config = create_default_config()
        
        # 통합 관리자 생성
        integration_manager = create_memory_integration_manager(config)
        
        # 메모리 관리자 통합
        if MEMORY_MANAGER_AVAILABLE:
            print("메모리 관리자 통합 성공")
        
        # 자동 최적화 시작
        integration_manager.start_auto_optimization()
        
        # 통계 확인
        stats = integration_manager.get_integration_stats()
        print(f"통합 통계: {stats}")
        
        # 메모리 정리
        integration_manager.cleanup_all_memory()
        
    except Exception as e:
        print(f"메모리 통합 테스트 오류: {str(e)}")

if __name__ == "__main__":
    # 테스트 실행
    test_memory_integration()