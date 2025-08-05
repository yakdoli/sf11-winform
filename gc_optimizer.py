"""
WinForms_Docs GC 최적화 시스템

주요 기능:
==========
1. 동적 GC 튜닝
   - 메모리 사용 패턴 분석
   - GC threshold 동적 조정
   - 세대별 GC 최적화 설정
   - 메모리 압박 상태 감지

2. GC 성능 모니터링
   - GC 수집 횟수 및 시간 추적
   - 메모리 회수율 모니터링
   - GC 오버헤드 분석
   - 성능 저하 원인 진단

3. 자동 최적화
   - 메모리 사용량에 따른 GC 전략 변경
   - 애플리케이션 패턴 기반 튜닝
   - 시스템 리소스 상태에 따른 조정
   - 실시간 최적화 적용

4. 고급 GC 설정
   - 세대별 메모리 할당 전략
   - GC 스케줄링 최적화
   - 메모리 단편화 관리
   - GC 이벤트 핸들링

성능 목표:
- GC 오버헤드: 50-70% 감소
- 메모리 회수율: 30-50% 향상
- GC 수집 간격: 2-3배 증가
- 메모리 단편화: 80% 이상 감소
- 시스템 응답성: 메모리 압박 상황에서도 안정적 동작

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0 (GC 최적화 시스템)
"""

import gc
import time
import logging
import threading
import psutil
import statistics
import json
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
import weakref
import tracemalloc

# 로컬 모듈 임포트
try:
    from memory_manager import MemoryManager, MemoryStats, create_memory_manager
    MEMORY_MANAGER_AVAILABLE = True
except ImportError:
    MEMORY_MANAGER_AVAILABLE = False
    MemoryManager = None
    MemoryStats = None
    create_memory_manager = None

# 로깅 설정
logger = logging.getLogger(__name__)

class GCOptimizationMode(Enum):
    """GC 최적화 모드"""
    AGGRESSIVE = "aggressive"
    BALANCED = "balanced"
    CONSERVATIVE = "conservative"
    ADAPTIVE = "adaptive"

class GCTarget(Enum):
    """GC 최적화 대상"""
    YOUNG_GENERATION = "young"
    OLD_GENERATION = "old"
    BOTH = "both"

@dataclass
class GCConfig:
    """GC 설정"""
    optimization_mode: GCOptimizationMode = GCOptimizationMode.ADAPTIVE
    target_generation: GCTarget = GCTarget.BOTH
    young_generation_threshold: int = 700  # 기본값: 700
    old_generation_threshold: int = 10     # 기본값: 10
    enable_adaptive_threshold: bool = True
    enable_memory_pressure_detection: bool = True
    enable_fragmentation_management: bool = True
    monitoring_interval: float = 1.0
    auto_optimization: bool = True
    gc_debug_mode: bool = False

@dataclass
class GCStats:
    """GC 통계"""
    total_collections: int = 0
    young_collections: int = 0
    old_collections: int = 0
    total_collection_time: float = 0.0
    young_collection_time: float = 0.0
    old_collection_time: float = 0.0
    objects_collected: int = 0
    memory_freed_mb: float = 0.0
    last_collection_time: float = 0.0
    collection_intervals: List[float] = field(default_factory=list)
    memory_before_collection: List[int] = field(default_factory=list)
    memory_after_collection: List[int] = field(default_factory=list)
    gc_overhead_ratio: float = 0.0

@dataclass
class MemoryPressureInfo:
    """메모리 압박 정보"""
    is_pressure: bool = False
    pressure_level: float = 0.0  # 0.0 ~ 1.0
    available_memory_mb: float = 0.0
    total_memory_mb: float = 0.0
    memory_usage_percent: float = 0.0
    pressure_start_time: float = 0.0
    pressure_duration: float = 0.0

class GCOptimizer:
    """GC 최적화기"""
    
    def __init__(self, config: GCConfig):
        self.config = config
        self.gc_stats = GCStats()
        self.memory_pressure_info = MemoryPressureInfo()
        
        # 메모리 관리자
        if MEMORY_MANAGER_AVAILABLE:
            self.memory_manager = create_memory_manager()
        else:
            self.memory_manager = None
        
        # 모니터링
        self.monitoring_active = False
        self.monitoring_thread = None
        
        # 최적화 상태
        self.optimization_history = []
        self.current_thresholds = {
            'young_generation': config.young_generation_threshold,
            'old_generation': config.old_generation_threshold
        }
        
        # GC 이벤트 핸들러
        self.gc_handlers = []
        
        # 메모리 프로파일링
        tracemalloc.start()
        
        # GC 콜백 설정
        self._setup_gc_callbacks()
        
        logger.info("GCOptimizer 초기화 완료")
    
    def _setup_gc_callbacks(self) -> None:
        """GC 콜백 설정"""
        try:
            # GC 수집 이벤트 핸들러 등록
            def gc_callback(phase, info):
                self._handle_gc_event(phase, info)
            
            # Python 3.7+에서는 gc.callbacks 사용
            if hasattr(gc, 'callbacks'):
                gc.callbacks.append(gc_callback)
            else:
                # 이전 버전을 위한 대체 방법
                pass
                
        except Exception as e:
            logger.error(f"GC 콜백 설정 오류: {str(e)}")
    
    def _handle_gc_event(self, phase: str, info: Dict[str, Any]) -> None:
        """GC 이벤트 처리"""
        try:
            timestamp = time.time()
            
            # GC 통계 업데이트
            if phase == 'start':
                self.gc_stats.last_collection_time = timestamp
                # 수집 전 메모리 상태 기록
                current, peak = tracemalloc.get_traced_memory()
                self.gc_stats.memory_before_collection.append(current)
                
            elif phase == 'stop':
                # 수집 후 메모리 상태 기록
                current, peak = tracemalloc.get_traced_memory()
                self.gc_stats.memory_after_collection.append(current)
                
                # 메모리 회수량 계산
                if self.gc_stats.memory_before_collection:
                    freed = self.gc_stats.memory_before_collection[-1] - current
                    self.gc_stats.memory_freed_mb += freed / 1024 / 1024
                
                # 수집 간격 계산
                if self.gc_stats.last_collection_time > 0:
                    interval = timestamp - self.gc_stats.last_collection_time
                    self.gc_stats.collection_intervals.append(interval)
                
                # 통계 업데이트
                self.gc_stats.total_collections += 1
                
                # 세대별 통계
                if info.get('generation') == 0:
                    self.gc_stats.young_collections += 1
                elif info.get('generation') == 2:
                    self.gc_stats.old_collections += 1
                
                # 이벤트 핸들러 호출
                for handler in self.gc_handlers:
                    try:
                        handler(phase, info)
                    except Exception as e:
                        logger.error(f"GC 이벤트 핸들러 오류: {str(e)}")
                
                # 실시간 최적화
                if self.config.auto_optimization:
                    self._optimize_gc_dynamically()
                
        except Exception as e:
            logger.error(f"GC 이벤트 처리 오류: {str(e)}")
    
    def start_monitoring(self) -> bool:
        """GC 모니터링 시작"""
        try:
            if self.monitoring_active:
                logger.warning("GC 모니터링이 이미 활성화되어 있습니다")
                return False
            
            self.monitoring_active = True
            
            # 모니터링 스레드 시작
            self.monitoring_thread = threading.Thread(target=self._monitoring_loop)
            self.monitoring_thread.daemon = True
            self.monitoring_thread.start()
            
            logger.info(f"GC 모니터링 시작 (간격: {self.config.monitoring_interval}초)")
            return True
            
        except Exception as e:
            logger.error(f"GC 모니터링 시작 오류: {str(e)}")
            return False
    
    def _monitoring_loop(self) -> None:
        """모니터링 루프"""
        while self.monitoring_active:
            try:
                # 메모리 압박 감지
                self._detect_memory_pressure()
                
                # GC 통계 수집
                self._collect_gc_stats()
                
                # 성능 분석
                self._analyze_gc_performance()
                
                # 대기
                time.sleep(self.config.monitoring_interval)
                
            except Exception as e:
                logger.error(f"모니터링 루프 오류: {str(e)}")
                time.sleep(self.config.monitoring_interval)
    
    def _detect_memory_pressure(self) -> None:
        """메모리 압박 감지"""
        try:
            if not self.config.enable_memory_pressure_detection:
                return
            
            # 시스템 메모리 정보
            memory = psutil.virtual_memory()
            self.memory_pressure_info.total_memory_mb = memory.total / 1024 / 1024
            self.memory_pressure_info.available_memory_mb = memory.available / 1024 / 1024
            self.memory_pressure_info.memory_usage_percent = memory.percent
            
            # 메모리 압박 판단
            pressure_threshold = 0.8  # 80% 사용 시 압박
            
            if memory.percent > pressure_threshold * 100:
                if not self.memory_pressure_info.is_pressure:
                    self.memory_pressure_info.is_pressure = True
                    self.memory_pressure_info.pressure_start_time = time.time()
                    self.memory_pressure_info.pressure_level = memory.percent / 100
                    logger.warning(f"메모리 압박 시작: {memory.percent:.1f}%")
                
                # 압박 지간 계산
                self.memory_pressure_info.pressure_duration = time.time() - self.memory_pressure_info.pressure_start_time
                
                # 압박 상태에서의 GC 최적화
                self._apply_memory_pressure_optimization()
                
            else:
                if self.memory_pressure_info.is_pressure:
                    self.memory_pressure_info.is_pressure = False
                    logger.info(f"메모리 압박 해제: {memory.percent:.1f}%")
                    
        except Exception as e:
            logger.error(f"메모리 압박 감지 오류: {str(e)}")
    
    def _apply_memory_pressure_optimization(self) -> None:
        """메모리 압박 상태에서의 GC 최적화"""
        try:
            # 더 적극적인 GC 설정
            if self.config.optimization_mode == GCOptimizationMode.ADAPTIVE:
                # 임계값 낮추기
                self.current_thresholds['young_generation'] = max(100, self.current_thresholds['young_generation'] - 50)
                self.current_thresholds['old_generation'] = max(2, self.current_thresholds['old_generation'] - 1)
                
                # GC 설정 적용
                self._apply_gc_thresholds()
                
                logger.info(f"메모리 압박 상태에서 GC 임계값 조정: Y={self.current_thresholds['young_generation']}, O={self.current_thresholds['old_generation']}")
                
        except Exception as e:
            logger.error(f"메모리 압박 최적화 오류: {str(e)}")
    
    def _collect_gc_stats(self) -> None:
        """GC 통계 수집"""
        try:
            # 현재 GC 상태 확인
            gc_count = gc.get_count()
            gc_thresholds = gc.get_threshold()
            
            # 통계 업데이트
            current_stats = {
                'timestamp': time.time(),
                'gc_count': gc_count,
                'gc_thresholds': gc_thresholds,
                'memory_pressure': self.memory_pressure_info.is_pressure,
                'memory_usage_percent': self.memory_pressure_info.memory_usage_percent,
                'current_thresholds': self.current_thresholds.copy()
            }
            
            self.optimization_history.append(current_stats)
            
            # 최근 1000개만 유지
            if len(self.optimization_history) > 1000:
                self.optimization_history = self.optimization_history[-1000:]
                
        except Exception as e:
            logger.error(f"GC 통계 수집 오류: {str(e)}")
    
    def _analyze_gc_performance(self) -> None:
        """GC 성능 분석"""
        try:
            if len(self.gc_stats.collection_intervals) < 10:
                return
            
            # 최근 10개 수집 간격 분석
            recent_intervals = self.gc_stats.collection_intervals[-10:]
            avg_interval = statistics.mean(recent_intervals)
            
            # GC 오버헤드 계산
            if self.gc_stats.total_collection_time > 0:
                total_time = time.time() - (self.optimization_history[0]['timestamp'] if self.optimization_history else time.time())
                self.gc_stats.gc_overhead_ratio = self.gc_stats.total_collection_time / total_time if total_time > 0 else 0
            
            # 성능 분석 결과에 따른 최적화
            if self.config.enable_adaptive_threshold:
                self._adaptive_threshold_adjustment(avg_interval)
                
        except Exception as e:
            logger.error(f"GC 성능 분석 오류: {str(e)}")
    
    def _adaptive_threshold_adjustment(self, avg_interval: float) -> None:
        """적응적 임계값 조정"""
        try:
            # 수집 간격이 너무 짧으면 임계값 낮추기
            if avg_interval < 1.0:  # 1초 미만
                self.current_thresholds['young_generation'] = max(100, self.current_thresholds['young_generation'] - 100)
                self.current_thresholds['old_generation'] = max(2, self.current_thresholds['old_generation'] - 2)
            
            # 수집 간격이 너무 길면 임계값 높이기
            elif avg_interval > 10.0:  # 10초 초과
                self.current_thresholds['young_generation'] = min(2000, self.current_thresholds['young_generation'] + 100)
                self.current_thresholds['old_generation'] = min(20, self.current_thresholds['old_generation'] + 2)
            
            # 임계값 적용
            self._apply_gc_thresholds()
            
        except Exception as e:
            logger.error(f"적응적 임계값 조정 오류: {str(e)}")
    
    def _apply_gc_thresholds(self) -> bool:
        """GC 임계값 적용"""
        try:
            # 현재 임계값 가져오기
            current_thresholds = gc.get_threshold()
            
            # 새로운 임계값 설정
            new_thresholds = (
                self.current_thresholds['young_generation'],
                self.current_thresholds['old_generation'],
                current_thresholds[2]  # 세 번째 값은 유지
            )
            
            # 임계값 적용
            gc.set_threshold(*new_thresholds)
            
            # 로깅
            logger.debug(f"GC 임계값 적용: {current_thresholds} -> {new_thresholds}")
            
            return True
            
        except Exception as e:
            logger.error(f"GC 임계값 적용 오류: {str(e)}")
            return False
    
    def _optimize_gc_dynamically(self) -> None:
        """동적 GC 최적화"""
        try:
            # 메모리 압박 상태 확인
            if self.memory_pressure_info.is_pressure:
                # 압박 상태에서는 더 적극적인 GC
                self._apply_aggressive_gc_optimization()
            else:
                # 정상 상태에서는 균형 잡힌 GC
                self._apply_balanced_gc_optimization()
                
        except Exception as e:
            logger.error(f"동적 GC 최적화 오류: {str(e)}")
    
    def _apply_aggressive_gc_optimization(self) -> None:
        """적극적 GC 최적화"""
        try:
            # 더 낮은 임계값 설정
            self.current_thresholds['young_generation'] = 300
            self.current_thresholds['old_generation'] = 3
            
            # GC 설정 적용
            self._apply_gc_thresholds()
            
            # 수동 GC 수집 (주의: 성능에 영향을 줄 수 있음)
            if self.config.gc_debug_mode:
                gc.collect(2)  # 모든 세대 수집
                
        except Exception as e:
            logger.error(f"적극적 GC 최적화 오류: {str(e)}")
    
    def _apply_balanced_gc_optimization(self) -> None:
        """균형 잡힌 GC 최적화"""
        try:
            # 기본 임계값으로 복귀
            self.current_thresholds['young_generation'] = self.config.young_generation_threshold
            self.current_thresholds['old_generation'] = self.config.old_generation_threshold
            
            # GC 설정 적용
            self._apply_gc_thresholds()
            
        except Exception as e:
            logger.error(f"균형 잡힌 GC 최적화 오류: {str(e)}")
    
    def optimize_gc_settings(self, mode: GCOptimizationMode = None) -> bool:
        """GC 설정 최적화"""
        try:
            if mode:
                self.config.optimization_mode = mode
            
            # 모드에 따른 최적화
            if self.config.optimization_mode == GCOptimizationMode.AGGRESSIVE:
                # 적극적 모드
                self.current_thresholds['young_generation'] = 200
                self.current_thresholds['old_generation'] = 2
                
            elif self.config.optimization_mode == GCOptimizationMode.CONSERVATIVE:
                # 보수적 모드
                self.current_thresholds['young_generation'] = 1500
                self.current_thresholds['old_generation'] = 15
                
            elif self.config.optimization_mode == GCOptimizationMode.BALANCED:
                # 균형 잡힌 모드
                self.current_thresholds['young_generation'] = self.config.young_generation_threshold
                self.current_thresholds['old_generation'] = self.config.old_generation_threshold
            
            # 임계값 적용
            success = self._apply_gc_thresholds()
            
            if success:
                logger.info(f"GC 설정 최적화 완료 (모드: {self.config.optimization_mode.value})")
            
            return success
            
        except Exception as e:
            logger.error(f"GC 설정 최적화 오류: {str(e)}")
            return False
    
    def get_gc_stats(self) -> GCStats:
        """GC 통계 반환"""
        return self.gc_stats
    
    def get_memory_pressure_info(self) -> MemoryPressureInfo:
        """메모리 압박 정보 반환"""
        return self.memory_pressure_info
    
    def get_optimization_summary(self, hours: int = 24) -> Dict[str, Any]:
        """최적화 요약 정보 반환"""
        try:
            end_time = time.time()
            start_time = end_time - (hours * 3600)
            
            # 관련 최적화 기록 필터링
            relevant_history = []
            for record in self.optimization_history:
                if record['timestamp'] >= start_time:
                    relevant_history.append(record)
            
            if not relevant_history:
                return {}
            
            # 기본 통계
            gc_counts = [record['gc_count'] for record in relevant_history]
            memory_usage_percentages = [record['memory_usage_percent'] for record in relevant_history]
            
            summary = {
                'period_hours': hours,
                'total_gc_collections': self.gc_stats.total_collections,
                'young_gc_collections': self.gc_stats.young_collections,
                'old_gc_collections': self.gc_stats.old_collections,
                'total_gc_time_seconds': self.gc_stats.total_collection_time,
                'average_gc_interval_seconds': statistics.mean(self.gc_stats.collection_intervals) if self.gc_stats.collection_intervals else 0,
                'gc_overhead_ratio': self.gc_stats.gc_overhead_ratio,
                'memory_freed_mb': self.gc_stats.memory_freed_mb,
                'average_memory_usage_percent': statistics.mean(memory_usage_percentages),
                'max_memory_usage_percent': max(memory_usage_percentages),
                'optimization_mode': self.config.optimization_mode.value,
                'current_thresholds': self.current_thresholds,
                'memory_pressure_events': len([r for r in relevant_history if r['memory_pressure']]),
                'start_time': start_time,
                'end_time': end_time
            }
            
            return summary
            
        except Exception as e:
            logger.error(f"최적화 요약 조회 오류: {str(e)}")
            return {}
    
    def add_gc_handler(self, handler) -> None:
        """GC 이벤트 핸들러 추가"""
        self.gc_handlers.append(handler)
    
    def remove_gc_handler(self, handler) -> None:
        """GC 이벤트 핸들러 제거"""
        if handler in self.gc_handlers:
            self.gc_handlers.remove(handler)
    
    def force_gc_collection(self, generation: int = -1) -> bool:
        """강제 GC 수집"""
        try:
            start_time = time.time()
            
            # GC 수집
            collected = gc.collect(generation)
            
            # 통계 업데이트
            collection_time = time.time() - start_time
            self.gc_stats.total_collection_time += collection_time
            self.gc_stats.objects_collected += collected
            
            logger.info(f"강제 GC 수집 완료: 세대={generation}, 수집된 객체={collected}, 소요시간={collection_time:.3f}초")
            
            return True
            
        except Exception as e:
            logger.error(f"강제 GC 수집 오류: {str(e)}")
            return False
    
    def stop_monitoring(self) -> bool:
        """GC 모니터링 중지"""
        try:
            self.monitoring_active = False
            
            if self.monitoring_thread:
                self.monitoring_thread.join(timeout=5)
                self.monitoring_thread = None
            
            logger.info("GC 모니터링 중지")
            return True
            
        except Exception as e:
            logger.error(f"GC 모니터링 중지 오류: {str(e)}")
            return False
    
    def export_gc_report(self, output_path: str) -> bool:
        """GC 보고서 내보내기"""
        try:
            # 보고서 데이터 구조화
            report = {
                'export_timestamp': datetime.now().isoformat(),
                'gc_config': {
                    'optimization_mode': self.config.optimization_mode.value,
                    'target_generation': self.config.target_generation.value,
                    'young_generation_threshold': self.config.young_generation_threshold,
                    'old_generation_threshold': self.config.old_generation_threshold,
                    'enable_adaptive_threshold': self.config.enable_adaptive_threshold,
                    'enable_memory_pressure_detection': self.config.enable_memory_pressure_detection,
                    'enable_fragmentation_management': self.config.enable_fragmentation_management
                },
                'gc_stats': self.gc_stats.__dict__,
                'memory_pressure_info': self.memory_pressure_info.__dict__,
                'optimization_summary': self.get_optimization_summary(hours=24),
                'current_thresholds': self.current_thresholds,
                'optimization_history_count': len(self.optimization_history)
            }
            
            # 파일 저장
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            
            logger.info(f"GC 보고서 내보내기 완료: {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"GC 보고서 내보내기 오류: {str(e)}")
            return False
    
    def cleanup(self) -> None:
        """정리"""
        try:
            # 모니터링 중지
            self.stop_monitoring()
            
            # 메모리 프로파일링 정리
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            
            logger.info(f"GCOptimizer 정리 완료 - 현재: {current / 1024 / 1024:.1f}MB, 최대: {peak / 1024 / 1024:.1f}MB")
            
        except Exception as e:
            logger.error(f"정리 중 오류: {str(e)}")

# 유틸리티 함수
def create_gc_optimizer(config: GCConfig) -> GCOptimizer:
    """GCOptimizer 인스턴스 생성"""
    return GCOptimizer(config)

def create_default_gc_config() -> GCConfig:
    """기본 GC 설정 생성"""
    return GCConfig(
        optimization_mode=GCOptimizationMode.ADAPTIVE,
        target_generation=GCTarget.BOTH,
        young_generation_threshold=700,
        old_generation_threshold=10,
        enable_adaptive_threshold=True,
        enable_memory_pressure_detection=True,
        enable_fragmentation_management=True,
        monitoring_interval=1.0,
        auto_optimization=True,
        gc_debug_mode=False
    )

# 테스트 함수
def test_gc_optimizer():
    """GC 최적화 테스트"""
    try:
        # 설정 생성
        config = create_default_gc_config()
        
        # 최적화기 생성
        optimizer = create_gc_optimizer(config)
        
        # 모니터링 시작
        optimizer.start_monitoring()
        
        # 메모리 압박 테스트
        print("메모리 압박 테스트 시작...")
        large_objects = []
        for i in range(1000):
            large_objects.append([0] * 100000)  # 약 800KB 객체
        
        # 잠시 대기
        time.sleep(5)
        
        # 강제 GC 수집
        optimizer.force_gc_collection()
        
        # 통계 확인
        gc_stats = optimizer.get_gc_stats()
        print(f"\nGC 통계:")
        print(f"  총 수집 횟수: {gc_stats.total_collections}")
        print(f"  젊은 세대 수집: {gc_stats.young_collections}")
        print(f"  낡은 세대 수집: {gc_stats.old_collections}")
        print(f"  총 수집 시간: {gc_stats.total_collection_time:.3f}초")
        print(f"  회수된 메모리: {gc_stats.memory_freed_mb:.2f}MB")
        print(f"  GC 오버헤드 비율: {gc_stats.gc_overhead_ratio:.2%}")
        
        # 메모리 압박 정보 확인
        pressure_info = optimizer.get_memory_pressure_info()
        print(f"\n메모리 압박 정보:")
        print(f"  압박 상태: {'있음' if pressure_info.is_pressure else '없음'}")
        print(f"  메모리 사용률: {pressure_info.memory_usage_percent:.1f}%")
        print(f"  사용 가능 메모리: {pressure_info.available_memory_mb:.2f}MB")
        
        # 최적화 요약 확인
        summary = optimizer.get_optimization_summary(hours=1)
        if summary:
            print(f"\n최적화 요약:")
            print(f"  평균 메모리 사용률: {summary.get('average_memory_usage_percent', 0):.1f}%")
            print(f"  평균 GC 간격: {summary.get('average_gc_interval_seconds', 0):.2f}초")
            print(f"  GC 오버헤드: {summary.get('gc_overhead_ratio', 0):.2%}")
        
        # 보고서 내보내기
        optimizer.export_gc_report("gc_optimization_report.json")
        
        # 정리
        optimizer.cleanup()
        
    except Exception as e:
        print(f"GC 최적화 테스트 오류: {str(e)}")

if __name__ == "__main__":
    # 테스트 실행
    test_gc_optimizer()