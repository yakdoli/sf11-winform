"""
WinForms_Docs 병렬 처리 설정 및 관리 모듈

CPU 코어 수에 따른 동적 작업 분할, 파일 배치 처리, 병렬 정규식 처리,
해시 기반 중복 검사, 작업 큐 관리, 성능 모니터링을 통합 관리합니다.
"""

import os
import json
import logging
import time
import multiprocessing as mp
from pathlib import Path
from typing import Dict, List, Set, Optional, Any, Tuple, Union
from dataclasses import dataclass, asdict
from datetime import datetime
import psutil
import gc
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import traceback

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class ParallelConfig:
    """병렬 처리 설정 데이터 클래스"""
    # 기본 설정
    max_workers: int = 0
    chunk_size: int = 100
    memory_limit_mb: int = 2048
    cpu_threshold: float = 0.8
    
    # 작업 분할 설정
    min_chunk_size: int = 10
    max_chunk_size: int = 1000
    dynamic_chunk_adjustment: bool = True
    
    # 메모리 관리 설정
    memory_cleanup_interval: int = 100
    memory_cleanup_threshold: float = 0.8
    
    # 성능 모니터링 설정
    monitoring_interval: int = 10
    log_performance_metrics: bool = True
    
    # 병렬 처리 전략
    processing_strategy: str = "adaptive"  # "adaptive", "conservative", "aggressive"
    
    # 해시 기반 최적화 설정
    hash_cache_size: int = 10000
    hash_cleanup_interval: int = 1000
    
    def __post_init__(self):
        """초기화 후 설정 값 보정"""
        if self.max_workers <= 0:
            self.max_workers = min(mp.cpu_count(), 8)
        
        if self.memory_limit_mb <= 0:
            self.memory_limit_mb = psutil.virtual_memory().total // (1024 * 1024) // 2

class ParallelProcessor:
    """병렬 처리 관리 클래스"""
    
    def __init__(self, config: Optional[ParallelConfig] = None):
        self.config = config or ParallelConfig()
        self.process = psutil.Process()
        
        # 성능 모니터링
        self.start_time = time.time()
        self.start_memory = self.process.memory_info().rss / 1024 / 1024  # MB
        self.peak_memory = self.start_memory
        self.total_processed = 0
        self.total_errors = 0
        
        # 작업 큐 관리
        self.task_queue = []
        self.completed_tasks = set()
        self.active_tasks = set()
        
        # 해시 캐시
        self.content_hash_cache = {}
        self.code_hash_cache = {}
        self.filename_hash_cache = {}
        
        # 메모리 관리
        self.last_cleanup_time = time.time()
        self.processed_since_cleanup = 0
        
        # 로깅
        self.logger = logging.getLogger(__name__)
        
    def get_optimal_workers(self) -> int:
        """최적 워커 수 계산"""
        cpu_count = mp.cpu_count()
        available_memory = psutil.virtual_memory().available / (1024 * 1024)  # MB
        cpu_usage = self.process.cpu_percent() / 100
        
        # CPU 사용량 기반 조정
        if cpu_usage > self.config.cpu_threshold:
            return max(1, cpu_count // 2)
        
        # 메모리 사용량 기반 조정
        if available_memory < self.config.memory_limit_mb:
            return max(1, cpu_count // 2)
        
        # 기본값 반환
        return self.config.max_workers
    
    def calculate_optimal_chunk_size(self, total_items: int) -> int:
        """최적 청크 크기 계산"""
        if total_items <= 0:
            return self.config.min_chunk_size
        
        # 기본 청크 크기 계산
        base_chunk = max(self.config.min_chunk_size, 
                        min(total_items // self.get_optimal_workers(), 
                            self.config.max_chunk_size))
        
        # 동적 조정
        if self.config.dynamic_chunk_adjustment:
            memory_factor = min(1.0, psutil.virtual_memory().available / (1024 * 1024 * 1024))
            cpu_factor = max(0.1, 1.0 - self.process.cpu_percent() / 100)
            
            adjusted_chunk = int(base_chunk * memory_factor * cpu_factor)
            return max(self.config.min_chunk_size, 
                      min(adjusted_chunk, self.config.max_chunk_size))
        
        return base_chunk
    
    def create_work_chunks(self, items: List[Any], chunk_size: int) -> List[List[Any]]:
        """작업 청크 생성"""
        chunks = []
        
        # 크기 기반 청크 생성
        for i in range(0, len(items), chunk_size):
            chunk = items[i:i + chunk_size]
            if chunk:
                chunks.append(chunk)
        
        return chunks
    
    def execute_parallel_tasks(self, task_func, items: List[Any], 
                             task_type: str = "general") -> List[Any]:
        """병렬 작업 실행"""
        start_time = time.time()
        
        # 최적 워커 수 계산
        optimal_workers = self.get_optimal_workers()
        
        # 최적 청크 크기 계산
        chunk_size = self.calculate_optimal_chunk_size(len(items))
        
        # 작업 청크 생성
        work_chunks = self.create_work_chunks(items, chunk_size)
        
        self.logger.info(f"병렬 작업 시작: {len(items)}개 항목, "
                        f"워커 수: {optimal_workers}, 청크 크기: {chunk_size}")
        
        results = []
        
        try:
            # 프로세스 풀을 이용한 병렬 처리
            with ProcessPoolExecutor(max_workers=optimal_workers) as executor:
                # 청크별로 작업 제출
                future_to_chunk = {
                    executor.submit(task_func, chunk): chunk 
                    for chunk in work_chunks
                }
                
                # 결과 수집
                for future in as_completed(future_to_chunk):
                    try:
                        chunk_result = future.result()
                        results.extend(chunk_result)
                        
                        # 통계 업데이트
                        self.total_processed += len(chunk_result)
                        self.processed_since_cleanup += len(chunk_result)
                        
                        # 메모리 정리 주기 확인
                        if self.processed_since_cleanup >= self.config.memory_cleanup_interval:
                            self._cleanup_memory()
                            self.processed_since_cleanup = 0
                        
                    except Exception as e:
                        self.logger.error(f"작업 처리 오류: {str(e)}")
                        self.logger.error(traceback.format_exc())
                        self.total_errors += 1
        
        except Exception as e:
            self.logger.error(f"병렬 처리 오류: {str(e)}")
            self.logger.error(traceback.format_exc())
            self.total_errors += 1
        
        # 성능 모니터링
        processing_time = time.time() - start_time
        self._update_performance_metrics(processing_time, len(items))
        
        self.logger.info(f"병렬 작업 완료: {len(results)}개 결과, "
                        f"처리 시간: {processing_time:.2f}초, "
                        f"평균 속도: {len(items)/processing_time:.2f} 항목/초")
        
        return results
    
    def _cleanup_memory(self):
        """메모리 정리"""
        try:
            gc.collect()
            
            # 해시 캐시 정리
            if len(self.content_hash_cache) > self.config.hash_cache_size:
                # 가장 오래된 항목 제거 (간소화된 버전)
                keys_to_remove = list(self.content_hash_cache.keys())[:1000]
                for key in keys_to_remove:
                    del self.content_hash_cache[key]
            
            if len(self.code_hash_cache) > self.config.hash_cache_size:
                keys_to_remove = list(self.code_hash_cache.keys())[:1000]
                for key in keys_to_remove:
                    del self.code_hash_cache[key]
            
            if len(self.filename_hash_cache) > self.config.hash_cache_size:
                keys_to_remove = list(self.filename_hash_cache.keys())[:1000]
                for key in keys_to_remove:
                    del self.filename_hash_cache[key]
            
            # 메모리 사용량 업데이트
            current_memory = self.process.memory_info().rss / 1024 / 1024
            self.peak_memory = max(self.peak_memory, current_memory)
            
            self.logger.debug(f"메모리 정리 완료: {current_memory:.2f}MB")
            
        except Exception as e:
            self.logger.error(f"메모리 정리 오류: {str(e)}")
    
    def _update_performance_metrics(self, processing_time: float, items_processed: int):
        """성능 지표 업데이트"""
        current_memory = self.process.memory_info().rss / 1024 / 1024
        cpu_usage = self.process.cpu_percent()
        
        if self.config.log_performance_metrics:
            self.logger.info(f"성능 지표: "
                           f"메모리: {current_memory:.2f}MB, "
                           f"CPU: {cpu_usage:.1f}%, "
                           f"처리 속도: {items_processed/processing_time:.2f} 항목/초")
    
    def get_performance_stats(self) -> Dict[str, Any]:
        """성능 통계 반환"""
        current_memory = self.process.memory_info().rss / 1024 / 1024
        cpu_usage = self.process.cpu_percent()
        elapsed_time = time.time() - self.start_time
        
        return {
            'elapsed_time': elapsed_time,
            'peak_memory_mb': self.peak_memory,
            'current_memory_mb': current_memory,
            'cpu_usage': cpu_usage,
            'total_processed': self.total_processed,
            'total_errors': self.total_errors,
            'processing_rate': self.total_processed / elapsed_time if elapsed_time > 0 else 0,
            'error_rate': self.total_errors / (self.total_processed + self.total_errors) * 100 if (self.total_processed + self.total_errors) > 0 else 0
        }
    
    def save_config(self, config_path: Path):
        """설정 저장"""
        try:
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(asdict(self.config), f, indent=2, ensure_ascii=False)
            self.logger.info(f"설정 저장 완료: {config_path}")
        except Exception as e:
            self.logger.error(f"설정 저장 오류: {str(e)}")
    
    @classmethod
    def load_config(cls, config_path: Path) -> 'ParallelProcessor':
        """설정 로드"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config_data = json.load(f)
            
            config = ParallelConfig(**config_data)
            return cls(config)
        except Exception as e:
            logger.error(f"설정 로드 오류: {str(e)}, 기본 설정 사용")
            return cls()

class TaskQueueManager:
    """작업 큐 관리 클래스"""
    
    def __init__(self, max_queue_size: int = 1000):
        self.max_queue_size = max_queue_size
        self.task_queue = []
        self.completed_tasks = set()
        self.active_tasks = set()
        self.task_priorities = {}
        
    def add_task(self, task_id: str, task_func, priority: int = 0, **kwargs):
        """작업 추가"""
        if len(self.task_queue) >= self.max_queue_size:
            raise ValueError("작업 큐가 가득 찼습니다.")
        
        task = {
            'id': task_id,
            'func': task_func,
            'priority': priority,
            'kwargs': kwargs,
            'created_at': datetime.now(),
            'status': 'pending'
        }
        
        self.task_queue.append(task)
        self.task_priorities[task_id] = priority
        
        # 우선순위 기반 정렬
        self.task_queue.sort(key=lambda x: x['priority'], reverse=True)
    
    def get_next_task(self) -> Optional[Dict[str, Any]]:
        """다음 작업 가져오기"""
        for task in self.task_queue:
            if task['id'] not in self.completed_tasks and task['id'] not in self.active_tasks:
                task['status'] = 'active'
                self.active_tasks.add(task['id'])
                return task
        
        return None
    
    def complete_task(self, task_id: str):
        """작업 완료"""
        self.completed_tasks.add(task_id)
        self.active_tasks.discard(task_id)
        
        # 큐에서 제거
        self.task_queue = [t for t in self.task_queue if t['id'] != task_id]
    
    def get_queue_status(self) -> Dict[str, Any]:
        """큐 상태 반환"""
        return {
            'total_tasks': len(self.task_queue),
            'pending_tasks': len([t for t in self.task_queue if t['id'] not in self.completed_tasks and t['id'] not in self.active_tasks]),
            'active_tasks': len(self.active_tasks),
            'completed_tasks': len(self.completed_tasks),
            'queue_utilization': len(self.task_queue) / self.max_queue_size * 100
        }

# 전역 인스턴스
_default_processor = None

def get_default_processor() -> ParallelProcessor:
    """기본 병렬 처리기 인스턴스 반환"""
    global _default_processor
    if _default_processor is None:
        _default_processor = ParallelProcessor()
    return _default_processor

def configure_parallel_processing(config: Optional[ParallelConfig] = None) -> ParallelProcessor:
    """병렬 처리 설정"""
    global _default_processor
    _default_processor = ParallelProcessor(config)
    return _default_processor