"""
WinForms_Docs 메모리 관리 시스템 - 통합 모듈

주요 기능:
==========
1. 메모리 관리 시스템 통합
   - MemoryManager 통합
   - AdaptiveMemoryPool 통합
   - GC 최적화 통합
   - Windows 메모리 최적화 통합

2. 통합 모니터링
   - 실시간 메모리 사용량 모니터링
   - 성능 지표 수집 및 분석
   - 시스템 리소스 상태 추적
   - 자동 최적화 트리거

3. 다중 풀 관리
   - Arrow 데이터용 메모리 풀
   - pandas 데이터용 메모리 풀
   - 일반 데이터용 메모리 풀
   - 적응적 풀 크기 조정

4. 성능 보고
   - 통합 성능 보고서 생성
   - 메모리 사용량 추적
   - GC 성능 분석
   - 시스템 안정성 평가

성능 목표:
- 메모리 사용량: 추가 15-25% 감소
- GC 오버헤드: 50-70% 감소
- 대용량 파일 처리 안정성: 95% 이상
- 메모리 단편화: 80% 이상 감소
- 시스템 응답성: 메모리 압박 상황에서도 안정적 동작

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0 (메모리 관리 시스템 통합)
"""

import asyncio
import time
import logging
import threading
import json
import psutil
import platform
import statistics
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

# 로컬 모듈 임포트
try:
    from memory_manager import (
        MemoryManager, MemoryPoolType, MemoryStats, 
        create_memory_manager, get_system_memory_info
    )
    MEMORY_MANAGER_AVAILABLE = True
except ImportError:
    MEMORY_MANAGER_AVAILABLE = False
    MemoryManager = None
    MemoryPoolType = None
    MemoryStats = None
    create_memory_manager = None
    get_system_memory_info = None

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
    from gc_optimizer import (
        GCOptimizer, GCConfig, GCOptimizationMode, GCTarget,
        create_gc_optimizer, create_default_gc_config
    )
    GC_OPTIMIZER_AVAILABLE = True
except ImportError:
    GC_OPTIMIZER_AVAILABLE = False
    GCOptimizer = None
    GCConfig = None
    GCOptimizationMode = None
    GCTarget = None
    create_gc_optimizer = None
    create_default_gc_config = None

try:
    from windows_memory_optimizer import (
        WindowsMemoryOptimizer, WindowsMemoryConfig, WindowsMemoryOptimizationMode,
        create_windows_memory_optimizer, create_default_windows_config
    )
    WINDOWS_OPTIMIZER_AVAILABLE = True
except ImportError:
    WINDOWS_OPTIMIZER_AVAILABLE = False
    WindowsMemoryOptimizer = None
    WindowsMemoryConfig = None
    WindowsMemoryOptimizationMode = None
    create_windows_memory_optimizer = None
    create_default_windows_config = None

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

class MemorySystemStatus(Enum):
    """메모리 시스템 상태"""
    INITIALIZING = "initializing"
    RUNNING = "running"
    OPTIMIZING = "optimizing"
    ERROR = "error"
    STOPPED = "stopped"

@dataclass
class MemorySystemConfig:
    """메모리 시스템 설정"""
    enable_memory_manager: bool = True
    enable_memory_integration: bool = True
    enable_gc_optimizer: bool = True
    enable_windows_optimizer: bool = True
    enable_monitoring: bool = True
    enable_auto_optimization: bool = True
    
    # 메모리 관리자 설정
    memory_manager_config: Optional[Dict[str, Any]] = None
    
    # 통합 관리자 설정
    integration_config: Optional[Dict[str, Any]] = None
    
    # GC 최적화 설정
    gc_config: Optional[Dict[str, Any]] = None
    
    # Windows 최적화 설정
    windows_config: Optional[Dict[str, Any]] = None
    
    # 모니터링 설정
    monitoring_interval: float = 5.0
    optimization_interval: float = 60.0
    performance_history_size: int = 1000

@dataclass
class MemorySystemStats:
    """메모리 시스템 통계"""
    system_status: MemorySystemStatus = MemorySystemStatus.STOPPED
    start_time: float = 0.0
    uptime_seconds: float = 0.0
    total_memory_allocated_mb: float = 0.0
    peak_memory_usage_mb: float = 0.0
    current_memory_usage_mb: float = 0.0
    gc_collections: int = 0
    gc_time_seconds: float = 0.0
    optimization_events: int = 0
    last_optimization_time: float = 0.0
    memory_pressure_events: int = 0
    error_count: int = 0
    
    # 성능 지표
    average_processing_time: float = 0.0
    throughput: float = 0.0
    success_rate: float = 0.0
    
    # 시스템 정보
    system_info: Dict[str, Any] = field(default_factory=dict)
    component_status: Dict[str, Any] = field(default_factory=dict)

class MemoryManagementSystem:
    """메모리 관리 시스템"""
    
    def __init__(self, config: MemorySystemConfig):
        self.config = config
        self.stats = MemorySystemStats()
        self.performance_history = []
        
        # 컴포넌트
        self.memory_manager = None
        self.memory_integration = None
        self.gc_optimizer = None
        self.windows_optimizer = None
        self.async_file_manager = None
        self.pandas_processor = None
        self.arrow_manager = None
        
        # 모니터링
        self.monitoring_active = False
        self.monitoring_thread = None
        self.optimization_thread = None
        
        # 상태 관리
        self.is_running = False
        self.last_error = None
        
        logger.info("MemoryManagementSystem 초기화 시작")
        
        # 시스템 초기화
        self._initialize_system()
        
        logger.info("MemoryManagementSystem 초기화 완료")
    
    def _initialize_system(self) -> bool:
        """시스템 초기화"""
        try:
            self.stats.system_status = MemorySystemStatus.INITIALIZING
            self.stats.start_time = time.time()
            
            # 시스템 정보 수집
            self.stats.system_info = self._collect_system_info()
            
            # 메모리 관리자 초기화
            if self.config.enable_memory_manager and MEMORY_MANAGER_AVAILABLE:
                self.memory_manager = create_memory_manager()
                self.stats.component_status['memory_manager'] = 'initialized'
                logger.info("메모리 관리자 초기화 완료")
            else:
                self.stats.component_status['memory_manager'] = 'disabled'
            
            # 메모리 통합 관리자 초기화
            if self.config.enable_memory_integration and MEMORY_INTEGRATION_AVAILABLE:
                integration_config = create_default_config()
                if self.config.integration_config:
                    integration_config.update(self.config.integration_config)
                
                self.memory_integration = create_memory_integration_manager(integration_config)
                self.stats.component_status['memory_integration'] = 'initialized'
                logger.info("메모리 통합 관리자 초기화 완료")
            else:
                self.stats.component_status['memory_integration'] = 'disabled'
            
            # GC 최적화기 초기화
            if self.config.enable_gc_optimizer and GC_OPTIMIZER_AVAILABLE:
                gc_config = create_default_gc_config()
                if self.config.gc_config:
                    # 설정 업데이트 로직 추가 필요
                    pass
                
                self.gc_optimizer = create_gc_optimizer(gc_config)
                self.stats.component_status['gc_optimizer'] = 'initialized'
                logger.info("GC 최적화기 초기화 완료")
            else:
                self.stats.component_status['gc_optimizer'] = 'disabled'
            
            # Windows 메모리 최적화기 초기화
            if self.config.enable_windows_optimizer and WINDOWS_OPTIMIZER_AVAILABLE:
                windows_config = create_default_windows_config()
                if self.config.windows_config:
                    # 설정 업데이트 로직 추가 필요
                    pass
                
                self.windows_optimizer = create_windows_memory_optimizer(windows_config)
                self.stats.component_status['windows_optimizer'] = 'initialized'
                logger.info("Windows 메모리 최적화기 초기화 완료")
            else:
                self.stats.component_status['windows_optimizer'] = 'disabled'
            
            # 데이터 처리 컴포넌트 초기화
            if ASYNC_FILE_MANAGER_AVAILABLE:
                self.async_file_manager = AsyncFileManager()
                self.stats.component_status['async_file_manager'] = 'initialized'
            
            if PANDAS_AVAILABLE:
                self.pandas_processor = PandasDataProcessor()
                self.stats.component_status['pandas_processor'] = 'initialized'
            
            if ARROW_AVAILABLE:
                self.arrow_manager = ArrowDataManager()
                self.stats.component_status['arrow_manager'] = 'initialized'
            
            # 통합 설정
            self._setup_integrations()
            
            self.stats.system_status = MemorySystemStatus.STOPPED
            return True
            
        except Exception as e:
            self.stats.system_status = MemorySystemStatus.ERROR
            self.stats.error_count += 1
            self.last_error = str(e)
            logger.error(f"시스템 초기화 오류: {str(e)}")
            return False
    
    def _collect_system_info(self) -> Dict[str, Any]:
        """시스템 정보 수집"""
        try:
            return {
                'platform': platform.system(),
                'platform_version': platform.version(),
                'architecture': platform.architecture()[0],
                'processor': platform.processor(),
                'python_version': platform.python_version(),
                'cpu_count': psutil.cpu_count(),
                'total_memory_mb': psutil.virtual_memory().total / 1024 / 1024,
                'available_memory_mb': psutil.virtual_memory().available / 1024 / 1024,
                'memory_usage_percent': psutil.virtual_memory().percent,
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"시스템 정보 수집 오류: {str(e)}")
            return {}
    
    def _setup_integrations(self) -> bool:
        """통합 설정"""
        try:
            # 메모리 통합 관리자 설정
            if self.memory_integration and self.async_file_manager:
                if not self.memory_integration.integrate_file_manager(self.async_file_manager):
                    logger.warning("파일 관리자 통합 실패")
            
            if self.memory_integration and self.pandas_processor:
                if not self.memory_integration.integrate_pandas_processor(self.pandas_processor):
                    logger.warning("pandas 프로세서 통합 실패")
            
            if self.memory_integration and self.arrow_manager:
                if not self.memory_integration.integrate_arrow_manager(self.arrow_manager):
                    logger.warning("Arrow 관리자 통합 실패")
            
            return True
            
        except Exception as e:
            logger.error(f"통합 설정 오류: {str(e)}")
            return False
    
    def start_system(self) -> bool:
        """시스템 시작"""
        try:
            if self.is_running:
                logger.warning("시스템이 이미 실행 중입니다")
                return False
            
            logger.info("메모리 관리 시스템 시작")
            
            # GC 최적화기 시작
            if self.gc_optimizer:
                self.gc_optimizer.start_monitoring()
                logger.info("GC 최적화기 모니터링 시작")
            
            # Windows 메모리 최적화기 시작
            if self.windows_optimizer:
                self.windows_optimizer.start_monitoring()
                logger.info("Windows 메모리 최적화기 모니터링 시작")
            
            # 메모리 통합 관리자 시작
            if self.memory_integration:
                self.memory_integration.start_auto_optimization()
                logger.info("메모리 통합 관리자 자동 최적화 시작")
            
            # 모니터링 시작
            if self.config.enable_monitoring:
                self.start_monitoring()
                logger.info("시스템 모니터링 시작")
            
            self.is_running = True
            self.stats.system_status = MemorySystemStatus.RUNNING
            
            logger.info("메모리 관리 시스템 시작 완료")
            return True
            
        except Exception as e:
            self.stats.system_status = MemorySystemStatus.ERROR
            self.stats.error_count += 1
            self.last_error = str(e)
            logger.error(f"시스템 시작 오류: {str(e)}")
            return False
    
    def stop_system(self) -> bool:
        """시스템 중지"""
        try:
            if not self.is_running:
                logger.warning("시스템이 실행 중이 아닙니다")
                return False
            
            logger.info("메모리 관리 시스템 중지")
            
            # 모니터링 중지
            self.stop_monitoring()
            
            # GC 최적화기 중지
            if self.gc_optimizer:
                self.gc_optimizer.stop_monitoring()
            
            # Windows 메모리 최적화기 중지
            if self.windows_optimizer:
                self.windows_optimizer.stop_monitoring()
            
            # 메모리 통합 관리자 중지
            if self.memory_integration:
                self.memory_integration.stop_auto_optimization()
            
            # 메모리 관리자 정리
            if self.memory_manager:
                self.memory_manager.cleanup_memory()
            
            self.is_running = False
            self.stats.system_status = MemorySystemStatus.STOPPED
            self.stats.uptime_seconds = time.time() - self.stats.start_time
            
            logger.info("메모리 관리 시스템 중지 완료")
            return True
            
        except Exception as e:
            self.stats.system_status = MemorySystemStatus.ERROR
            self.stats.error_count += 1
            self.last_error = str(e)
            logger.error(f"시스템 중지 오류: {str(e)}")
            return False
    
    def start_monitoring(self) -> bool:
        """모니터링 시작"""
        try:
            if self.monitoring_active:
                logger.warning("모니터링이 이미 활성화되어 있습니다")
                return False
            
            self.monitoring_active = True
            
            # 모니터링 스레드 시작
            self.monitoring_thread = threading.Thread(target=self._monitoring_loop)
            self.monitoring_thread.daemon = True
            self.monitoring_thread.start()
            
            logger.info(f"시스템 모니터링 시작 (간격: {self.config.monitoring_interval}초)")
            return True
            
        except Exception as e:
            logger.error(f"모니터링 시작 오류: {str(e)}")
            return False
    
    def _monitoring_loop(self) -> None:
        """모니터링 루프"""
        while self.monitoring_active:
            try:
                # 시스템 상태 모니터링
                self._monitor_system_status()
                
                # 성능 지표 수집
                self._collect_performance_metrics()
                
                # 자동 최적화
                if self.config.enable_auto_optimization:
                    self._perform_auto_optimization()
                
                # 대기
                time.sleep(self.config.monitoring_interval)
                
            except Exception as e:
                logger.error(f"모니터링 루프 오류: {str(e)}")
                time.sleep(self.config.monitoring_interval)
    
    def _monitor_system_status(self) -> None:
        """시스템 상태 모니터링"""
        try:
            # 현재 메모리 사용량
            memory_info = get_system_memory_info()
            if memory_info:
                self.stats.current_memory_usage_mb = memory_info.get('used_memory_mb', 0)
                self.stats.peak_memory_usage_mb = max(self.stats.peak_memory_usage_mb, self.stats.current_memory_usage_mb)
            
            # GC 통계
            if self.gc_optimizer:
                gc_stats = self.gc_optimizer.get_gc_stats()
                self.stats.gc_collections = gc_stats.total_collections
                self.stats.gc_time_seconds = gc_stats.total_collection_time
            
            # 메모리 압박 이벤트
            if self.windows_optimizer:
                pressure_info = self.windows_optimizer.get_windows_memory_stats()
                if pressure_info and pressure_info.memory_usage_percent > 80:
                    self.stats.memory_pressure_events += 1
            
            # 업타임 업데이트
            if self.is_running:
                self.stats.uptime_seconds = time.time() - self.stats.start_time
            
        except Exception as e:
            logger.error(f"시스템 상태 모니터링 오류: {str(e)}")
    
    def _collect_performance_metrics(self) -> None:
        """성능 지표 수집"""
        try:
            timestamp = time.time()
            
            # 성능 지표 생성
            metrics = {
                'timestamp': timestamp,
                'memory_usage_mb': self.stats.current_memory_usage_mb,
                'gc_collections': self.stats.gc_collections,
                'gc_time_seconds': self.stats.gc_time_seconds,
                'memory_pressure_events': self.stats.memory_pressure_events,
                'optimization_events': self.stats.optimization_events,
                'system_status': self.stats.system_status.value
            }
            
            # 성능 기록 추가
            self.performance_history.append(metrics)
            
            # 최근 기록만 유지
            if len(self.performance_history) > self.config.performance_history_size:
                self.performance_history = self.performance_history[-self.config.performance_history_size:]
                
        except Exception as e:
            logger.error(f"성능 지표 수집 오류: {str(e)}")
    
    def _perform_auto_optimization(self) -> None:
        """자동 최적화 수행"""
        try:
            # 최적화 간격 확인
            current_time = time.time()
            if current_time - self.stats.last_optimization_time < self.config.optimization_interval:
                return
            
            # 메모리 압박 확인
            if self.stats.current_memory_usage_mb > self.stats.system_info.get('total_memory_mb', 0) * 0.8:
                logger.info("메모리 압박 감지, 자동 최적화 수행")
                
                # GC 최적화
                if self.gc_optimizer:
                    self.gc_optimizer.optimize_gc_settings()
                
                # Windows 메모리 최적화
                if self.windows_optimizer:
                    self.windows_optimizer.optimize_memory_usage()
                
                # 메모리 관리자 최적화
                if self.memory_manager:
                    self.memory_manager.optimize_memory_pools()
                
                self.stats.optimization_events += 1
                self.stats.last_optimization_time = current_time
                
        except Exception as e:
            logger.error(f"자동 최적화 오류: {str(e)}")
    
    def stop_monitoring(self) -> bool:
        """모니터링 중지"""
        try:
            self.monitoring_active = False
            
            if self.monitoring_thread:
                self.monitoring_thread.join(timeout=5)
                self.monitoring_thread = None
            
            logger.info("시스템 모니터링 중지")
            return True
            
        except Exception as e:
            logger.error(f"모니터링 중지 오류: {str(e)}")
            return False
    
    def get_system_stats(self) -> MemorySystemStats:
        """시스템 통계 반환"""
        return self.stats
    
    def get_performance_summary(self, hours: int = 24) -> Dict[str, Any]:
        """성능 요약 정보 반환"""
        try:
            end_time = time.time()
            start_time = end_time - (hours * 3600)
            
            # 관련 성능 기록 필터링
            relevant_history = []
            for record in self.performance_history:
                if record['timestamp'] >= start_time:
                    relevant_history.append(record)
            
            if not relevant_history:
                return {}
            
            # 기본 통계
            memory_usage_values = [r['memory_usage_mb'] for r in relevant_history]
            gc_collections_values = [r['gc_collections'] for r in relevant_history]
            
            summary = {
                'period_hours': hours,
                'average_memory_usage_mb': statistics.mean(memory_usage_values),
                'max_memory_usage_mb': max(memory_usage_values),
                'min_memory_usage_mb': min(memory_usage_values),
                'total_gc_collections': self.stats.gc_collections,
                'total_gc_time_seconds': self.stats.gc_time_seconds,
                'optimization_events': self.stats.optimization_events,
                'memory_pressure_events': self.stats.memory_pressure_events,
                'error_count': self.stats.error_count,
                'system_uptime_seconds': self.stats.uptime_seconds,
                'start_time': start_time,
                'end_time': end_time,
                'component_status': self.stats.component_status
            }
            
            return summary
            
        except Exception as e:
            logger.error(f"성능 요약 조회 오류: {str(e)}")
            return {}
    
    def export_system_report(self, output_path: str) -> bool:
        """시스템 보고서 내보내기"""
        try:
            # 보고서 데이터 구조화
            report = {
                'export_timestamp': datetime.now().isoformat(),
                'system_config': self.config.__dict__,
                'system_stats': self.stats.__dict__,
                'system_info': self.stats.system_info,
                'performance_summary': self.get_performance_summary(hours=24),
                'performance_history_count': len(self.performance_history),
                'last_error': self.last_error,
                'component_status': self.stats.component_status
            }
            
            # 파일 저장
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            
            logger.info(f"시스템 보고서 내보내기 완료: {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"시스템 보고서 내보내기 오류: {str(e)}")
            return False
    
    def cleanup(self) -> None:
        """정리"""
        try:
            # 시스템 중지
            self.stop_system()
            
            # 모니터링 중지
            self.stop_monitoring()
            
            # 컴포넌트 정리
            if self.memory_manager:
                self.memory_manager.cleanup_memory()
            
            if self.gc_optimizer:
                self.gc_optimizer.cleanup()
            
            if self.windows_optimizer:
                self.windows_optimizer.cleanup()
            
            if self.memory_integration:
                self.memory_integration.cleanup()
            
            logger.info("MemoryManagementSystem 정리 완료")
            
        except Exception as e:
            logger.error(f"정리 중 오류: {str(e)}")

# 유틸리티 함수
def create_memory_management_system(config: MemorySystemConfig) -> MemoryManagementSystem:
    """MemoryManagementSystem 인스턴스 생성"""
    return MemoryManagementSystem(config)

def create_default_memory_system_config() -> MemorySystemConfig:
    """기본 메모리 시스템 설정 생성"""
    return MemorySystemConfig(
        enable_memory_manager=True,
        enable_memory_integration=True,
        enable_gc_optimizer=True,
        enable_windows_optimizer=True,
        enable_monitoring=True,
        enable_auto_optimization=True,
        monitoring_interval=5.0,
        optimization_interval=60.0,
        performance_history_size=1000
    )

# 테스트 함수
def test_memory_management_system():
    """메모리 관리 시스템 테스트"""
    try:
        print("메모리 관리 시스템 테스트 시작")
        
        # 설정 생성
        config = create_default_memory_system_config()
        
        # 시스템 생성
        system = create_memory_management_system(config)
        
        # 시스템 시작
        success = system.start_system()
        print(f"시스템 시작: {'성공' if success else '실패'}")
        
        if success:
            # 잠시 대기
            time.sleep(10)
            
            # 시스템 통계 확인
            stats = system.get_system_stats()
            print(f"\n시스템 통계:")
            print(f"  상태: {stats.system_status.value}")
            print(f"  업타임: {stats.uptime_seconds:.1f}초")
            print(f"  현재 메모리 사용: {stats.current_memory_usage_mb:.2f}MB")
            print(f"  최대 메모리 사용: {stats.peak_memory_usage_mb:.2f}MB")
            print(f"  GC 수집 횟수: {stats.gc_collections}")
            print(f"  GC 시간: {stats.gc_time_seconds:.3f}초")
            print(f"  최적화 이벤트: {stats.optimization_events}")
            print(f"  메모리 압박 이벤트: {stats.memory_pressure_events}")
            print(f"  오류 수: {stats.error_count}")
            
            # 성능 요약 확인
            summary = system.get_performance_summary(hours=1)
            if summary:
                print(f"\n성능 요약:")
                print(f"  평균 메모리 사용: {summary.get('average_memory_usage_mb', 0):.2f}MB")
                print(f"  최대 메모리 사용: {summary.get('max_memory_usage_mb', 0):.2f}MB")
                print(f"  총 GC 수집: {summary.get('total_gc_collections', 0)}")
                print(f"  최적화 이벤트: {summary.get('optimization_events', 0)}")
            
            # 시스템 중지
            system.stop_system()
            print(f"\n시스템 중지 완료")
            
            # 최종 통계 확인
            final_stats = system.get_system_stats()
            print(f"  총 업타임: {final_stats.uptime_seconds:.1f}초")
            
            # 보고서 내보내기
            system.export_system_report("memory_management_system_report.json")
            print(f"보고서 내보내기 완료: memory_management_system_report.json")
        
        # 정리
        system.cleanup()
        
    except Exception as e:
        print(f"메모리 관리 시스템 테스트 오류: {str(e)}")

if __name__ == "__main__":
    # 테스트 실행
    test_memory_management_system()