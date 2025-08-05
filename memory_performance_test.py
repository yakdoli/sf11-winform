"""
WinForms_Docs 메모리 관리 시스템 성능 테스트

주요 기능:
==========
1. 메모리 관리 성능 테스트
   - 메모리 할당/해제 성능 측정
   - 메모리 풀 관리 효율성 검증
   - GC 오버헤드 측정
   - 단편화 관리 성능 평가

2. 통합 시스템 성능 테스트
   - AsyncFileManager와의 통합 성능
   - pandas 데이터 처리 메모리 효율성
   - Arrow 데이터 관리 성능
   - 종합 시스템 안정성 검증

3. 부하 테스트
   - 대용량 데이터 처리 메모리 사용량
   - 장시간 실행 시 메모리 누수 검증
   - 메모리 압박 상황에서의 성능
   - 동시성 처리 메모리 관리

4. 성능 모니터링
   - 실시간 메모리 사용량 추적
   - 성능 지표 수집 및 분석
   - 자동화된 보고서 생성
   - 최적화 효과 검증

성능 목표:
- 메모리 사용량: 추가 15-25% 감소
- GC 오버헤드: 50-70% 감소
- 대용량 파일 처리 안정성: 95% 이상
- 메모리 단편화: 80% 이상 감소
- 시스템 응답성: 메모리 압박 상황에서도 안정적 동작

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0 (메모리 관리 성능 테스트)
"""

import asyncio
import time
import logging
import psutil
import gc
import threading
import os
import json
import random
import string
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
import statistics
import tracemalloc

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
    from memory_integration import (
        MemoryIntegrationManager, MemoryIntegratedFileManager,
        MemoryIntegratedPandasProcessor, MemoryIntegratedArrowManager,
        create_memory_integration_manager, create_default_config
    )
    MEMORY_INTEGRATION_AVAILABLE = True
except ImportError:
    MEMORY_INTEGRATION_AVAILABLE = False
    MemoryIntegrationManager = None
    MemoryIntegratedFileManager = None
    MemoryIntegratedPandasProcessor = None
    MemoryIntegratedArrowManager = None
    create_memory_integration_manager = None
    create_default_config = None

try:
    from async_file_manager import AsyncFileManager
    ASYNC_FILE_MANAGER_AVAILABLE = True
except ImportError:
    ASYNC_FILE_MANAGER_AVAILABLE = False
    AsyncFileManager = None

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
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class PerformanceMetrics:
    """성능 메트릭"""
    test_name: str
    start_time: float
    end_time: float
    duration: float
    memory_usage_mb: float
    peak_memory_mb: float
    gc_collections: int
    gc_time_seconds: float
    throughput: float
    success_rate: float
    error_count: int = 0
    additional_metrics: Dict[str, Any] = field(default_factory=dict)

@dataclass
class TestResult:
    """테스트 결과"""
    test_name: str
    metrics: PerformanceMetrics
    system_info: Dict[str, Any]
    memory_stats: MemoryStats
    recommendations: List[str] = field(default_factory=list)

class MemoryPerformanceTester:
    """메모리 성능 테스터"""
    
    def __init__(self):
        self.test_results: List[TestResult] = []
        self.test_configs = self._load_test_configs()
        self.system_baseline = self._get_system_baseline()
        
        # 메모리 프로파일링 시작
        tracemalloc.start()
        
        logger.info("MemoryPerformanceTester 초기화 완료")
    
    def _load_test_configs(self) -> Dict[str, Any]:
        """테스트 설정 로드"""
        return {
            'memory_allocation': {
                'iterations': 1000,
                'min_size': 1024,  # 1KB
                'max_size': 10 * 1024 * 1024,  # 10MB
                'pool_types': [MemoryPoolType.GENERAL, MemoryPoolType.ARROW, MemoryPoolType.PANDAS]
            },
            'file_io': {
                'file_sizes': [1024, 1024*1024, 10*1024*1024],  # 1KB, 1MB, 10MB
                'file_count': 100,
                'concurrent_operations': 10
            },
            'data_processing': {
                'data_sizes': [1000, 10000, 100000],  # row count
                'iterations': 100,
                'concurrent_operations': 5
            },
            'stress_test': {
                'duration_minutes': 30,
                'memory_pressure_threshold': 0.8,
                'concurrent_users': 50
            }
        }
    
    def _get_system_baseline(self) -> Dict[str, Any]:
        """시스템 베이스라인 정보"""
        try:
            memory = psutil.virtual_memory()
            cpu_count = psutil.cpu_count()
            
            return {
                'total_memory_mb': memory.total / 1024 / 1024,
                'available_memory_mb': memory.available / 1024 / 1024,
                'cpu_count': cpu_count,
                'platform': platform.system(),
                'python_version': platform.python_version()
            }
        except Exception as e:
            logger.error(f"시스템 베이스라인 조회 오류: {str(e)}")
            return {}
    
    def run_memory_allocation_test(self) -> TestResult:
        """메모리 할당 테스트 실행"""
        test_name = "Memory Allocation Test"
        logger.info(f"메모리 할당 테스트 시작: {test_name}")
        
        start_time = time.time()
        error_count = 0
        successful_allocations = 0
        total_allocated_memory = 0
        allocation_times = []
        gc_collections_start = len(gc.get_objects())
        
        try:
            if not MEMORY_MANAGER_AVAILABLE:
                raise Exception("MemoryManager를 사용할 수 없습니다")
            
            memory_manager = create_memory_manager()
            memory_manager.start_monitoring(interval=1.0)
            
            config = self.test_configs['memory_allocation']
            
            for i in range(config['iterations']):
                try:
                    # 랜덤 크기와 풀 타입 선택
                    size = random.randint(config['min_size'], config['max_size'])
                    pool_type = random.choice(config['pool_types'])
                    
                    # 메모리 할당
                    alloc_start = time.time()
                    block_id = memory_manager.allocate_memory_sync(size, pool_type)
                    alloc_time = time.time() - alloc_start
                    
                    if block_id:
                        successful_allocations += 1
                        total_allocated_memory += size
                        allocation_times.append(alloc_time)
                        
                        # 잠시 대기 후 해제
                        time.sleep(0.001)
                        memory_manager.deallocate_memory_sync(block_id)
                    else:
                        error_count += 1
                    
                    # 진행률 로깅
                    if (i + 1) % 100 == 0:
                        logger.info(f"메모리 할당 테스트 진행: {i + 1}/{config['iterations']}")
                        
                except Exception as e:
                    error_count += 1
                    logger.warning(f"메모리 할당 오류: {str(e)}")
            
            # 메모리 통계 수집
            memory_stats = memory_manager.get_memory_stats()
            end_time = time.time()
            duration = end_time - start_time
            
            # GC 통계
            gc_collections_end = len(gc.get_objects())
            gc_collections = gc_collections_end - gc_collections_start
            
            # 성능 메트릭 계산
            throughput = successful_allocations / duration if duration > 0 else 0
            success_rate = successful_allocations / config['iterations'] if config['iterations'] > 0 else 0
            avg_allocation_time = statistics.mean(allocation_times) if allocation_times else 0
            peak_memory = memory_stats.peak_usage / 1024 / 1024 if memory_stats.peak_usage else 0
            
            # 추가 메트릭
            additional_metrics = {
                'average_allocation_time_ms': avg_allocation_time * 1000,
                'total_allocated_memory_mb': total_allocated_memory / 1024 / 1024,
                'allocation_size_distribution': {
                    'min_size': config['min_size'],
                    'max_size': config['max_size'],
                    'avg_size': total_allocated_memory / successful_allocations if successful_allocations > 0 else 0
                }
            }
            
            # 성능 메트릭 생성
            metrics = PerformanceMetrics(
                test_name=test_name,
                start_time=start_time,
                end_time=end_time,
                duration=duration,
                memory_usage_mb=memory_stats.used_memory / 1024 / 1024,
                peak_memory_mb=peak_memory,
                gc_collections=gc_collections,
                gc_time_seconds=memory_stats.gc_times.get('total_time', 0),
                throughput=throughput,
                success_rate=success_rate,
                error_count=error_count,
                additional_metrics=additional_metrics
            )
            
            # 테스트 결과 생성
            result = TestResult(
                test_name=test_name,
                metrics=metrics,
                system_info=self.system_baseline,
                memory_stats=memory_stats,
                recommendations=self._generate_recommendations(metrics)
            )
            
            self.test_results.append(result)
            logger.info(f"메모리 할당 테스트 완료: {test_name}")
            
            return result
            
        except Exception as e:
            logger.error(f"메모리 할당 테스트 오류: {str(e)}")
            end_time = time.time()
            duration = end_time - start_time
            
            # 오류 상태의 메트릭 생성
            metrics = PerformanceMetrics(
                test_name=test_name,
                start_time=start_time,
                end_time=end_time,
                duration=duration,
                memory_usage_mb=0,
                peak_memory_mb=0,
                gc_collections=0,
                gc_time_seconds=0,
                throughput=0,
                success_rate=0,
                error_count=error_count
            )
            
            result = TestResult(
                test_name=test_name,
                metrics=metrics,
                system_info=self.system_baseline,
                memory_stats=MemoryStats(),
                recommendations=["테스트 실행 중 오류 발생"]
            )
            
            self.test_results.append(result)
            return result
    
    def run_file_io_test(self) -> TestResult:
        """파일 I/O 메모리 테스트 실행"""
        test_name = "File I/O Memory Test"
        logger.info(f"파일 I/O 메모리 테스트 시작: {test_name}")
        
        start_time = time.time()
        error_count = 0
        successful_operations = 0
        total_processed_size = 0
        
        try:
            if not MEMORY_MANAGER_AVAILABLE or not ASYNC_FILE_MANAGER_AVAILABLE:
                raise Exception("필수 모듈을 사용할 수 없습니다")
            
            # 통합 관리자 생성
            integration_manager = create_memory_integration_manager(create_default_config())
            file_manager = AsyncFileManager()
            
            # 통합
            if not integration_manager.integrate_file_manager(file_manager):
                raise Exception("파일 관리자 통합 실패")
            
            integration_manager.start_auto_optimization()
            
            config = self.test_configs['file_io']
            
            for file_size in config['file_sizes']:
                for i in range(config['file_count'] // len(config['file_sizes'])):
                    try:
                        # 테스트 파일 생성
                        test_file = f"test_file_{i}_{file_size}.bin"
                        
                        # 테스트 데이터 생성
                        test_data = os.urandom(file_size)
                        
                        # 파일 쓰기 테스트
                        write_start = time.time()
                        success = asyncio.run(integration_manager.file_manager.write_file_with_memory_management(test_file, test_data))
                        write_time = time.time() - write_start
                        
                        if success:
                            successful_operations += 1
                            total_processed_size += file_size
                            
                            # 파일 읽기 테스트
                            read_start = time.time()
                            read_data = asyncio.run(integration_manager.file_manager.read_file_with_memory_management(test_file))
                            read_time = time.time() - read_start
                            
                            if read_data:
                                successful_operations += 1
                                total_processed_size += file_size
                            
                            # 파일 삭제
                            try:
                                os.remove(test_file)
                            except:
                                pass
                        else:
                            error_count += 1
                        
                        # 진행률 로깅
                        if (i + 1) % 10 == 0:
                            logger.info(f"파일 I/O 테스트 진행: {i + 1}/{config['file_count'] // len(config['file_sizes'])}")
                            
                    except Exception as e:
                        error_count += 1
                        logger.warning(f"파일 I/O 테스트 오류: {str(e)}")
            
            # 통계 수집
            end_time = time.time()
            duration = end_time - start_time
            
            # 성능 메트릭 계산
            throughput = successful_operations / duration if duration > 0 else 0
            success_rate = successful_operations / (config['file_count'] * 2) if config['file_count'] > 0 else 0
            
            # 시스템 메모리 정보
            memory_info = get_system_memory_info()
            peak_memory = memory_info.get('used_memory_mb', 0)
            
            # 추가 메트릭
            additional_metrics = {
                'total_processed_size_mb': total_processed_size / 1024 / 1024,
                'average_write_time_ms': 0,  # 측정 로직 추가 필요
                'average_read_time_ms': 0,   # 측정 로직 추가 필요
                'file_size_distribution': {
                    'sizes': config['file_sizes'],
                    'count_per_size': config['file_count'] // len(config['file_sizes'])
                }
            }
            
            # 성능 메트릭 생성
            metrics = PerformanceMetrics(
                test_name=test_name,
                start_time=start_time,
                end_time=end_time,
                duration=duration,
                memory_usage_mb=memory_info.get('used_memory_mb', 0),
                peak_memory_mb=peak_memory,
                gc_collections=0,
                gc_time_seconds=0,
                throughput=throughput,
                success_rate=success_rate,
                error_count=error_count,
                additional_metrics=additional_metrics
            )
            
            # 테스트 결과 생성
            result = TestResult(
                test_name=test_name,
                metrics=metrics,
                system_info=self.system_baseline,
                memory_stats=MemoryStats(),
                recommendations=self._generate_recommendations(metrics)
            )
            
            self.test_results.append(result)
            logger.info(f"파일 I/O 메모리 테스트 완료: {test_name}")
            
            return result
            
        except Exception as e:
            logger.error(f"파일 I/O 메모리 테스트 오류: {str(e)}")
            end_time = time.time()
            duration = end_time - start_time
            
            # 오류 상태의 메트릭 생성
            metrics = PerformanceMetrics(
                test_name=test_name,
                start_time=start_time,
                end_time=end_time,
                duration=duration,
                memory_usage_mb=0,
                peak_memory_mb=0,
                gc_collections=0,
                gc_time_seconds=0,
                throughput=0,
                success_rate=0,
                error_count=error_count
            )
            
            result = TestResult(
                test_name=test_name,
                metrics=metrics,
                system_info=self.system_baseline,
                memory_stats=MemoryStats(),
                recommendations=["테스트 실행 중 오류 발생"]
            )
            
            self.test_results.append(result)
            return result
    
    def run_data_processing_test(self) -> TestResult:
        """데이터 처리 메모리 테스트 실행"""
        test_name = "Data Processing Memory Test"
        logger.info(f"데이터 처리 메모리 테스트 시작: {test_name}")
        
        start_time = time.time()
        error_count = 0
        successful_operations = 0
        total_processed_rows = 0
        
        try:
            if not MEMORY_MANAGER_AVAILABLE or not PANDAS_AVAILABLE:
                raise Exception("필수 모듈을 사용할 수 없습니다")
            
            # 통합 관리자 생성
            integration_manager = create_memory_integration_manager(create_default_config())
            pandas_processor = PandasDataProcessor()
            
            # 통합
            if not integration_manager.integrate_pandas_processor(pandas_processor):
                raise Exception("pandas 프로세서 통합 실패")
            
            integration_manager.start_auto_optimization()
            
            config = self.test_configs['data_processing']
            
            for data_size in config['data_sizes']:
                for i in range(config['iterations'] // len(config['data_sizes'])):
                    try:
                        # 테스트 데이터 생성
                        test_data = {
                            'id': list(range(data_size)),
                            'value': [random.random() for _ in range(data_size)],
                            'category': [random.choice(['A', 'B', 'C']) for _ in range(data_size)]
                        }
                        
                        data_id = f"test_data_{i}_{data_size}"
                        
                        # 데이터 처리 테스트
                        process_start = time.time()
                        result = asyncio.run(integration_manager.pandas_processor.process_data_with_memory_management(test_data, data_id))
                        process_time = time.time() - process_start
                        
                        if result is not None:
                            successful_operations += 1
                            total_processed_rows += data_size
                        else:
                            error_count += 1
                        
                        # 진행률 로깅
                        if (i + 1) % 10 == 0:
                            logger.info(f"데이터 처리 테스트 진행: {i + 1}/{config['iterations'] // len(config['data_sizes'])}")
                            
                    except Exception as e:
                        error_count += 1
                        logger.warning(f"데이터 처리 테스트 오류: {str(e)}")
            
            # 통계 수집
            end_time = time.time()
            duration = end_time - start_time
            
            # 성능 메트릭 계산
            throughput = successful_operations / duration if duration > 0 else 0
            success_rate = successful_operations / config['iterations'] if config['iterations'] > 0 else 0
            
            # 시스템 메모리 정보
            memory_info = get_system_memory_info()
            peak_memory = memory_info.get('used_memory_mb', 0)
            
            # 추가 메트릭
            additional_metrics = {
                'total_processed_rows': total_processed_rows,
                'average_processing_time_ms': 0,  # 측정 로직 추가 필요
                'rows_per_second': total_processed_rows / duration if duration > 0 else 0,
                'data_size_distribution': {
                    'sizes': config['data_sizes'],
                    'count_per_size': config['iterations'] // len(config['data_sizes'])
                }
            }
            
            # 성능 메트릭 생성
            metrics = PerformanceMetrics(
                test_name=test_name,
                start_time=start_time,
                end_time=end_time,
                duration=duration,
                memory_usage_mb=memory_info.get('used_memory_mb', 0),
                peak_memory_mb=peak_memory,
                gc_collections=0,
                gc_time_seconds=0,
                throughput=throughput,
                success_rate=success_rate,
                error_count=error_count,
                additional_metrics=additional_metrics
            )
            
            # 테스트 결과 생성
            result = TestResult(
                test_name=test_name,
                metrics=metrics,
                system_info=self.system_baseline,
                memory_stats=MemoryStats(),
                recommendations=self._generate_recommendations(metrics)
            )
            
            self.test_results.append(result)
            logger.info(f"데이터 처리 메모리 테스트 완료: {test_name}")
            
            return result
            
        except Exception as e:
            logger.error(f"데이터 처리 메모리 테스트 오류: {str(e)}")
            end_time = time.time()
            duration = end_time - start_time
            
            # 오류 상태의 메트릭 생성
            metrics = PerformanceMetrics(
                test_name=test_name,
                start_time=start_time,
                end_time=end_time,
                duration=duration,
                memory_usage_mb=0,
                peak_memory_mb=0,
                gc_collections=0,
                gc_time_seconds=0,
                throughput=0,
                success_rate=0,
                error_count=error_count
            )
            
            result = TestResult(
                test_name=test_name,
                metrics=metrics,
                system_info=self.system_baseline,
                memory_stats=MemoryStats(),
                recommendations=["테스트 실행 중 오류 발생"]
            )
            
            self.test_results.append(result)
            return result
    
    def run_stress_test(self) -> TestResult:
        """스트레스 테스트 실행"""
        test_name = "Memory Stress Test"
        logger.info(f"메모리 스트레스 테스트 시작: {test_name}")
        
        start_time = time.time()
        error_count = 0
        successful_operations = 0
        
        try:
            if not MEMORY_MANAGER_AVAILABLE:
                raise Exception("MemoryManager를 사용할 수 없습니다")
            
            memory_manager = create_memory_manager()
            memory_manager.start_monitoring(interval=1.0)
            
            config = self.test_configs['stress_test']
            
            # 스트레스 테스트 스레드 생성
            stress_threads = []
            
            def stress_worker(thread_id: int):
                nonlocal error_count, successful_operations
                
                try:
                    for i in range(1000):  # 각 스레드당 1000번 반복
                        # 랜덤 메모리 할당
                        size = random.randint(1024, 1024 * 1024)  # 1KB ~ 1MB
                        pool_type = random.choice(list(MemoryPoolType))
                        
                        block_id = memory_manager.allocate_memory_sync(size, pool_type)
                        if block_id:
                            successful_operations += 1
                            
                            # 잠시 대기
                            time.sleep(random.uniform(0.001, 0.01))
                            
                            # 메모리 해제
                            if memory_manager.deallocate_memory_sync(block_id):
                                successful_operations += 1
                            else:
                                error_count += 1
                        else:
                            error_count += 1
                        
                        # 메모리 압박 확인
                        stats = memory_manager.get_memory_stats()
                        if stats.memory_percent > config['memory_pressure_threshold'] * 100:
                            logger.warning(f"메모리 압박 감지: {stats.memory_percent:.1f}%")
                        
                        # 스레드 간격
                        time.sleep(0.001)
                        
                except Exception as e:
                    error_count += 1
                    logger.warning(f"스트레스 워커 오류: {str(e)}")
            
            # 스트레스 스레드 시작
            for i in range(config['concurrent_users']):
                thread = threading.Thread(target=stress_worker, args=(i,))
                thread.daemon = True
                thread.start()
                stress_threads.append(thread)
            
            # 테스트 지간 동안 실행
            test_duration = config['duration_minutes'] * 60
            time.sleep(test_duration)
            
            # 스레드 종료 대기
            for thread in stress_threads:
                thread.join(timeout=5)
            
            # 통계 수집
            end_time = time.time()
            duration = end_time - start_time
            
            # 성능 메트릭 계산
            throughput = successful_operations / duration if duration > 0 else 0
            
            # 시스템 메모리 정보
            memory_stats = memory_manager.get_memory_stats()
            peak_memory = memory_stats.peak_usage / 1024 / 1024
            
            # 추가 메트릭
            additional_metrics = {
                'concurrent_users': config['concurrent_users'],
                'test_duration_minutes': config['duration_minutes'],
                'total_operations': successful_operations,
                'error_rate': error_count / (successful_operations + error_count) if (successful_operations + error_count) > 0 else 0
            }
            
            # 성능 메트릭 생성
            metrics = PerformanceMetrics(
                test_name=test_name,
                start_time=start_time,
                end_time=end_time,
                duration=duration,
                memory_usage_mb=memory_stats.used_memory / 1024 / 1024,
                peak_memory_mb=peak_memory,
                gc_collections=memory_stats.gc_collections.get('generation_0', 0) + 
                              memory_stats.gc_collections.get('generation_1', 0) + 
                              memory_stats.gc_collections.get('generation_2', 0),
                gc_time_seconds=memory_stats.gc_times.get('total_time', 0),
                throughput=throughput,
                success_rate=successful_operations / (successful_operations + error_count) if (successful_operations + error_count) > 0 else 0,
                error_count=error_count,
                additional_metrics=additional_metrics
            )
            
            # 테스트 결과 생성
            result = TestResult(
                test_name=test_name,
                metrics=metrics,
                system_info=self.system_baseline,
                memory_stats=memory_stats,
                recommendations=self._generate_recommendations(metrics)
            )
            
            self.test_results.append(result)
            logger.info(f"메모리 스트레스 테스트 완료: {test_name}")
            
            return result
            
        except Exception as e:
            logger.error(f"메모리 스트레스 테스트 오류: {str(e)}")
            end_time = time.time()
            duration = end_time - start_time
            
            # 오류 상태의 메트릭 생성
            metrics = PerformanceMetrics(
                test_name=test_name,
                start_time=start_time,
                end_time=end_time,
                duration=duration,
                memory_usage_mb=0,
                peak_memory_mb=0,
                gc_collections=0,
                gc_time_seconds=0,
                throughput=0,
                success_rate=0,
                error_count=error_count
            )
            
            result = TestResult(
                test_name=test_name,
                metrics=metrics,
                system_info=self.system_baseline,
                memory_stats=MemoryStats(),
                recommendations=["테스트 실행 중 오류 발생"]
            )
            
            self.test_results.append(result)
            return result
    
    def _generate_recommendations(self, metrics: PerformanceMetrics) -> List[str]:
        """성능 개선 권장사항 생성"""
        recommendations = []
        
        # 메모리 사용량 기반 권장사항
        if metrics.peak_memory_mb > 1000:  # 1GB 이상
            recommendations.append("메모리 사용량이 높습니다. 메모리 풀 크기를 조정하거나 메모리 누수를 확인하세요.")
        
        # 성공률 기반 권장사항
        if metrics.success_rate < 0.95:  # 95% 미만
            recommendations.append("성공률이 낮습니다. 메모리 할당 전략을 최적화하거나 시스템 리소스를 확인하세요.")
        
        # 처리량 기반 권장사항
        if metrics.throughput < 100:  # 100회/초 미만
            recommendations.append("처리량이 낮습니다. 동시성을 증가시키거나 처리 로직을 최적화하세요.")
        
        # GC 오버헤드 기반 권장사항
        if metrics.gc_time_seconds > metrics.duration * 0.1:  # 전체 시간의 10% 이상
            recommendations.append("GC 오버헤드가 높습니다. GC 설정을 최적화하거나 객체 생성 패턴을 개선하세요.")
        
        # 에러율 기반 권장사항
        error_rate = metrics.error_count / (metrics.throughput * metrics.duration) if metrics.throughput > 0 else 0
        if error_rate > 0.05:  # 5% 이상
            recommendations.append("에러율이 높습니다. 오류 처리 로직을 강화하고 리소스 제한을 확인하세요.")
        
        return recommendations
    
    def run_all_tests(self) -> List[TestResult]:
        """모든 테스트 실행"""
        logger.info("모든 메모리 성능 테스트 시작")
        
        # 개별 테스트 실행
        self.run_memory_allocation_test()
        self.run_file_io_test()
        self.run_data_processing_test()
        self.run_stress_test()
        
        # 종합 결과 생성
        summary = self.generate_test_summary()
        
        logger.info("모든 메모리 성능 테스트 완료")
        logger.info(f"테스트 요약: {summary}")
        
        return self.test_results
    
    def generate_test_summary(self) -> Dict[str, Any]:
        """테스트 요약 생성"""
        if not self.test_results:
            return {"message": "실행된 테스트가 없습니다"}
        
        summary = {
            "total_tests": len(self.test_results),
            "test_names": [result.test_name for result in self.test_results],
            "average_success_rate": 0,
            "average_throughput": 0,
            "total_errors": 0,
            "peak_memory_usage_mb": 0,
            "recommendations": []
        }
        
        # 통계 계산
        success_rates = []
        throughputs = []
        peak_memories = []
        
        for result in self.test_results:
            success_rates.append(result.metrics.success_rate)
            throughputs.append(result.metrics.throughput)
            peak_memories.append(result.metrics.peak_memory_mb)
            summary["total_errors"] += result.metrics.error_count
            summary["recommendations"].extend(result.recommendations)
        
        # 평균 계산
        summary["average_success_rate"] = statistics.mean(success_rates) if success_rates else 0
        summary["average_throughput"] = statistics.mean(throughputs) if throughputs else 0
        summary["peak_memory_usage_mb"] = max(peak_memories) if peak_memories else 0
        
        # 중복 권장사항 제거
        summary["recommendations"] = list(set(summary["recommendations"]))
        
        return summary
    
    def export_test_results(self, output_path: str) -> bool:
        """테스트 결과 내보내기"""
        try:
            # 결과 데이터 구조화
            export_data = {
                "test_summary": self.generate_test_summary(),
                "test_results": [],
                "system_info": self.system_baseline,
                "export_timestamp": datetime.now().isoformat()
            }
            
            # 각 테스트 결과 변환
            for result in self.test_results:
                result_data = {
                    "test_name": result.test_name,
                    "metrics": {
                        "duration": result.metrics.duration,
                        "memory_usage_mb": result.metrics.memory_usage_mb,
                        "peak_memory_mb": result.metrics.peak_memory_mb,
                        "gc_collections": result.metrics.gc_collections,
                        "gc_time_seconds": result.metrics.gc_time_seconds,
                        "throughput": result.metrics.throughput,
                        "success_rate": result.metrics.success_rate,
                        "error_count": result.metrics.error_count
                    },
                    "system_info": result.system_info,
                    "memory_stats": {
                        "total_memory_mb": result.memory_stats.total_memory / 1024 / 1024,
                        "used_memory_mb": result.memory_stats.used_memory / 1024 / 1024,
                        "memory_percent": result.memory_stats.memory_percent,
                        "fragmentation_ratio": result.memory_stats.fragmentation_ratio
                    },
                    "recommendations": result.recommendations
                }
                
                export_data["test_results"].append(result_data)
            
            # 파일 저장
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)
            
            logger.info(f"테스트 결과 내보내기 완료: {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"테스트 결과 내보내기 오류: {str(e)}")
            return False
    
    def cleanup(self) -> None:
        """정리"""
        try:
            # 메모리 프로파일링 정리
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            
            logger.info(f"메모리 프로파일링 정리 - 현재: {current / 1024 / 1024:.1f}MB, 최대: {peak / 1024 / 1024:.1f}MB")
            
        except Exception as e:
            logger.error(f"정리 중 오류: {str(e)}")

# 유틸리티 함수
def run_memory_performance_tests() -> List[TestResult]:
    """메모리 성능 테스트 실행"""
    tester = MemoryPerformanceTester()
    
    try:
        # 모든 테스트 실행
        results = tester.run_all_tests()
        
        # 결과 내보내기
        tester.export_test_results("memory_performance_test_results.json")
        
        return results
        
    finally:
        # 정리
        tester.cleanup()

def print_test_results(results: List[TestResult]) -> None:
    """테스트 결과 출력"""
    print("\n" + "="*60)
    print("메모리 성능 테스트 결과")
    print("="*60)
    
    for result in results:
        print(f"\n테스트 이름: {result.test_name}")
        print(f"실행 시간: {result.metrics.duration:.2f}초")
        print(f"메모리 사용량: {result.metrics.memory_usage_mb:.2f}MB")
        print(f"최대 메모리: {result.metrics.peak_memory_mb:.2f}MB")
        print(f"처리량: {result.metrics.throughput:.2f}회/초")
        print(f"성공률: {result.metrics.success_rate:.1%}")
        print(f"GC 수집 횟수: {result.metrics.gc_collections}")
        print(f"GC 시간: {result.metrics.gc_time_seconds:.3f}초")
        print(f"오류 수: {result.metrics.error_count}")
        
        if result.recommendations:
            print("\n권장사항:")
            for rec in result.recommendations:
                print(f"  - {rec}")
    
    # 요약
    summary = results[0].test_results[0].generate_test_summary() if results else {}
    print(f"\n테스트 요약:")
    print(f"  총 테스트 수: {summary.get('total_tests', 0)}")
    print(f"  평균 성공률: {summary.get('average_success_rate', 0):.1%}")
    print(f"  평균 처리량: {summary.get('average_throughput', 0):.2f}회/초")
    print(f"  최대 메모리 사용: {summary.get('peak_memory_usage_mb', 0):.2f}MB")
    print(f"  총 오류 수: {summary.get('total_errors', 0)}")

# 테스트 함수
def test_memory_performance():
    """메모리 성능 테스트 실행"""
    try:
        print("메모리 성능 테스트를 시작합니다...")
        
        # 테스트 실행
        results = run_memory_performance_tests()
        
        # 결과 출력
        print_test_results(results)
        
        print("\n테스트가 완료되었습니다. 결과 파일: memory_performance_test_results.json")
        
    except Exception as e:
        print(f"테스트 실행 중 오류 발생: {str(e)}")

if __name__ == "__main__":
    # 테스트 실행
    test_memory_performance()