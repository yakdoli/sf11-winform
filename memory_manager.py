import psutil
import gc
import time
import threading
import logging
import numpy as np
import pandas as pd
from typing import Dict, List, Optional, Union, Callable, Any
from dataclasses import dataclass, asdict
from datetime import datetime
import json
import os
import sys
import tracemalloc
from functools import lru_cache
import weakref
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor, as_completed

@dataclass
class MemoryStats:
    """메모리 통계 정보"""
    total_memory_mb: float = 0.0
    available_memory_mb: float = 0.0
    used_memory_mb: float = 0.0
    memory_usage_percent: float = 0.0
    peak_memory_mb: float = 0.0
    objects_count: int = 0
    gc_collections: Dict[str, int] = None
    
    def __post_init__(self):
        if self.gc_collections is None:
            self.gc_collections = {'0': 0, '1': 0, '2': 0}

class MemoryManager:
    """
    고급 메모리 관리 시스템
    - 실시간 메모리 모니터링
    - 자동 메모리 최적화
    - 메모리 누수 감지
    - 성능 분석
    """
    
    def __init__(self, config: Optional[Dict] = None):
        """
        MemoryManager 초기화
        
        Args:
            config: 설정 딕셔너리
        """
        self.config = config or {}
        self.logger = self._setup_logger()
        
        # 설정 값
        self.memory_threshold = self.config.get('memory_threshold', 80)
        self.gc_threshold = self.config.get('gc_threshold', 85)
        self.monitoring_interval = self.config.get('monitoring_interval', 1)
        self.enable_tracing = self.config.get('enable_tracing', False)
        self.max_workers = self.config.get('max_workers', psutil.cpu_count())
        
        # 메모리 통계
        self.stats = MemoryStats()
        self.peak_memory = 0
        self.monitoring_active = False
        self.monitoring_thread = None
        
        # 메모리 트레이싱
        if self.enable_tracing:
            tracemalloc.start()
        
        # 객체 추적
        self.tracked_objects = weakref.WeakSet()
        self.object_allocations = {}
        
        # 가비지 컬렉션 통계
        self.gc_stats = {'0': 0, '1': 0, '2': 0}
        
        # 알림 콜백
        self.notification_callbacks = []
        
        self.logger.info("MemoryManager 초기화 완료")
    
    def _setup_logger(self) -> logging.Logger:
        """로거 설정"""
        logger = logging.getLogger('MemoryManager')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def start_monitoring(self):
        """메모리 모니터링 시작"""
        if self.monitoring_active:
            self.logger.warning("메모리 모니터링이 이미 활성화되어 있습니다")
            return
        
        self.monitoring_active = True
        self.monitoring_thread = threading.Thread(target=self._monitor_memory, daemon=True)
        self.monitoring_thread.start()
        self.logger.info("메모리 모니터링 시작")
    
    def stop_monitoring(self):
        """메모리 모니터링 중지"""
        if not self.monitoring_active:
            return
        
        self.monitoring_active = False
        if self.monitoring_thread:
            self.monitoring_thread.join(timeout=5)
        
        if self.enable_tracing:
            tracemalloc.stop()
        
        self.logger.info("메모리 모니터링 중지")
    
    def _monitor_memory(self):
        """메모리 모니터링 루프"""
        while self.monitoring_active:
            try:
                # 메모리 정보 업데이트
                self._update_memory_stats()
                
                # 메모리 임계값 확인
                if self.stats.memory_usage_percent > self.memory_threshold:
                    self.logger.warning(f"메모리 사용량 임계값 초과: {self.stats.memory_usage_percent:.1f}%")
                    self._trigger_memory_optimization()
                
                # 가비지 컬렉션 임계값 확인
                if self.stats.memory_usage_percent > self.gc_threshold:
                    self.logger.warning(f"가비지 컬렉션 임계값 도달: {self.stats.memory_usage_percent:.1f}%")
                    self.force_gc()
                
                # 알림 콜백 실행
                self._execute_notifications()
                
                time.sleep(self.monitoring_interval)
                
            except Exception as e:
                self.logger.error(f"메모리 모니터링 오류: {e}")
                time.sleep(self.monitoring_interval)
    
    def _update_memory_stats(self):
        """메모리 통계 업데이트"""
        memory = psutil.virtual_memory()
        
        self.stats.total_memory_mb = memory.total / (1024 * 1024)
        self.stats.available_memory_mb = memory.available / (1024 * 1024)
        self.stats.used_memory_mb = memory.used / (1024 * 1024)
        self.stats.memory_usage_percent = memory.percent
        
        # 피크 메모리 업데이트
        if self.enable_tracing:
            current, peak = tracemalloc.get_traced_memory()
            self.stats.peak_memory_mb = peak / (1024 * 1024)
        
        # 객체 수 카운트
        self.stats.objects_count = len(gc.get_objects())
        
        # 가비지 컬렉션 통계
        self.gc_stats = {
            '0': gc.collect(0),
            '1': gc.collect(1),
            '2': gc.collect(2)
        }
        self.stats.gc_collections = self.gc_stats.copy()
    
    def _trigger_memory_optimization(self):
        """메모리 최적화 트리거"""
        self.optimize_memory()
    
    def _execute_notifications(self):
        """알림 콜백 실행"""
        for callback in self.notification_callbacks:
            try:
                callback(self.stats)
            except Exception as e:
                self.logger.error(f"알림 콜백 실행 오류: {e}")
    
    def add_notification_callback(self, callback: Callable[[MemoryStats], None]):
        """알림 콜백 추가"""
        self.notification_callbacks.append(callback)
    
    def remove_notification_callback(self, callback: Callable[[MemoryStats], None]):
        """알림 콜백 제거"""
        if callback in self.notification_callbacks:
            self.notification_callbacks.remove(callback)
    
    def optimize_memory(self):
        """메모리 최적화"""
        start_time = time.time()
        
        try:
            # 1. 약한 참조 객체 정리
            self._cleanup_weak_references()
            
            # 2. 캐시 정리
            self._clear_caches()
            
            # 3. 데이터프레임 메모리 최적화
            self._optimize_dataframes()
            
            # 4. 가비지 컬렉션 실행
            self.force_gc()
            
            # 5. 메모리 조각화 방지
            self._defragment_memory()
            
            optimization_time = time.time() - start_time
            self.logger.info(f"메모리 최적화 완료: {optimization_time:.2f}초")
            
        except Exception as e:
            self.logger.error(f"메모리 최적화 오류: {e}")
    
    def _cleanup_weak_references(self):
        """약한 참조 객체 정리"""
        # 약한 참조 객체 정리
        gc.collect()
        
        # 추적된 객체 정리
        self.tracked_objects.clear()
        self.object_allocations.clear()
    
    def _clear_caches(self):
        """캐시 정리"""
        # lru_cache 정리
        for func in gc.get_objects():
            if hasattr(func, 'cache_clear'):
                try:
                    func.cache_clear()
                except:
                    pass
    
    def _optimize_dataframes(self):
        """데이터프레임 메모리 최적화"""
        for obj in gc.get_objects():
            if isinstance(obj, pd.DataFrame):
                try:
                    # 데이터 타입 최적화
                    for col in obj.select_dtypes(include=['int64']).columns:
                        obj[col] = pd.to_numeric(obj[col], downcast='integer')
                    
                    for col in obj.select_dtypes(include=['float64']).columns:
                        obj[col] = pd.to_numeric(obj[col], downcast='float')
                    
                    # 카테고리형 변환
                    for col in obj.select_dtypes(include=['object']).columns:
                        if obj[col].nunique() / len(obj[col]) < 0.5:
                            obj[col] = obj[col].astype('category')
                
                except Exception as e:
                    self.logger.debug(f"데이터프레임 최적화 오류: {e}")
    
    def _defragment_memory(self):
        """메모리 조각화 방지"""
        # 메모리 조각화 방지를 위한 추가 작업
        gc.collect()
    
    def force_gc(self):
        """강제 가비지 컬렉션"""
        start_time = time.time()
        
        # 세대별 가비지 컬렉션
        gc.collect(0)
        gc.collect(1)
        gc.collect(2)
        
        gc_time = time.time() - start_time
        self.logger.debug(f"가비지 컬렉션 완료: {gc_time:.2f}초")
    
    def track_object(self, obj: Any, name: Optional[str] = None):
        """객체 추적"""
        self.tracked_objects.add(obj)
        if name:
            self.object_allocations[name] = obj
    
    def untrack_object(self, obj: Any):
        """객체 추적 해제"""
        self.tracked_objects.discard(obj)
    
    def get_memory_snapshot(self) -> Dict:
        """메모리 스냅샷 생성"""
        if self.enable_tracing:
            current, peak = tracemalloc.get_traced_memory()
            return {
                'current_memory_mb': current / (1024 * 1024),
                'peak_memory_mb': peak / (1024 * 1024),
                'traceback': tracemalloc.take_snapshot().format_stats()
            }
        return {}
    
    def analyze_memory_usage(self) -> Dict:
        """메모리 사용량 분석"""
        analysis = {
            'current_stats': asdict(self.stats),
            'memory_snapshot': self.get_memory_snapshot(),
            'tracked_objects': len(self.tracked_objects),
            'gc_stats': self.gc_stats,
            'system_info': self._get_system_info()
        }
        
        return analysis
    
    def _get_system_info(self) -> Dict:
        """시스템 정보 가져오기"""
        return {
            'cpu_count': psutil.cpu_count(),
            'cpu_percent': psutil.cpu_percent(),
            'memory_total': psutil.virtual_memory().total,
            'memory_available': psutil.virtual_memory().available,
            'swap_total': psutil.swap_memory().total,
            'swap_used': psutil.swap_memory().used
        }
    
    def get_stats(self) -> Dict:
        """메모리 통계 정보 반환"""
        return asdict(self.stats)
    
    def reset_stats(self):
        """통계 정보 초기화"""
        self.stats = MemoryStats()
        self.peak_memory = 0
        self.gc_stats = {'0': 0, '1': 0, '2': 0}
        self.logger.info("메모리 통계 초기화 완료")
    
    def save_memory_report(self, filename: str):
        """메모리 리포트 저장"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'stats': asdict(self.stats),
            'analysis': self.analyze_memory_usage(),
            'config': self.config
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        self.logger.info(f"메모리 리포트 저장 완료: {filename}")
    
    def __enter__(self):
        """컨텍스트 관리자 진입"""
        self.start_monitoring()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """컨텍스트 관리자 종료"""
        self.stop_monitoring()


class MemoryOptimizer:
    """
    메모리 최적화 유틸리티 클래스
    """
    
    @staticmethod
    def optimize_pandas(df: pd.DataFrame) -> pd.DataFrame:
        """판다스 데이터프레임 메모리 최적화"""
        # 수치형 데이터 타입 최적화
        for col in df.select_dtypes(include=['int64']).columns:
            df[col] = pd.to_numeric(df[col], downcast='integer')
        
        for col in df.select_dtypes(include=['float64']).columns:
            df[col] = pd.to_numeric(df[col], downcast='float')
        
        # 카테고리형 변환
        for col in df.select_dtypes(include=['object']).columns:
            if df[col].nunique() / len(df[col]) < 0.5:
                df[col] = df[col].astype('category')
        
        return df
    
    @staticmethod
    def optimize_numpy(arr: np.ndarray) -> np.ndarray:
        """넘파이 배열 메모리 최적화"""
        if arr.dtype == np.float64:
            return arr.astype(np.float32)
        elif arr.dtype == np.int64:
            return arr.astype(np.int32)
        return arr
    
    @staticmethod
    def clear_memory():
        """메모리 정리"""
        gc.collect()
        # 캐시 정리
        for func in gc.get_objects():
            if hasattr(func, 'cache_clear'):
                try:
                    func.cache_clear()
                except:
                    pass


def main():
    """메인 실행 함수"""
    import argparse
    
    parser = argparse.ArgumentParser(description='메모리 관리 도구')
    parser.add_argument('--monitor', action='store_true', help='메모리 모니터링 시작')
    parser.add_argument('--threshold', type=int, default=80, help='메모리 임계값 (%)')
    parser.add_argument('--gc-threshold', type=int, default=85, help='가비지 컬렉션 임계값 (%)')
    parser.add_argument('--report', help='메모리 리포트 파일 경로')
    
    args = parser.parse_args()
    
    config = {
        'memory_threshold': args.threshold,
        'gc_threshold': args.gc_threshold,
        'enable_tracing': True
    }
    
    manager = MemoryManager(config)
    
    if args.monitor:
        manager.start_monitoring()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            manager.stop_monitoring()
    
    if args.report:
        manager.save_memory_report(args.report)


if __name__ == '__main__':
    main()