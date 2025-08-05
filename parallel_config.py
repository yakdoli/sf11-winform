"""
WinForms_Docs 통합 병렬 처리 설정 및 관리 모듈

주요 기능:
=============
1. 세 개의 모듈(data_cleaner.py, data_normalizer.py, deduplication.py)을 통합 관리
2. 시스템 전체의 병렬 처리 환경 설정 및 관리
3. 동적 리소스 할당 및 모니터링
4. 성능 최적화를 위한 전역 설정 관리

구현된 기능:
=============
- 통합 설정 관리 시스템
- 동적 리소스 관리
- 작업 큐 관리 시스템
- 성능 모니터링 및 로깅
- 오류 처리 및 복구 시스템

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0
"""

import json
import logging
import os
import time
import multiprocessing as mp
import psutil
import threading
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple, Union
from dataclasses import dataclass, asdict, field
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from enum import Enum
import traceback
import gc
import yaml
from functools import lru_cache


class TaskPriority(Enum):
    """작업 우선순위"""
    LOW = 1
    NORMAL = 2
    HIGH = 3
    CRITICAL = 4


class ProcessingModule(Enum):
    """처리 모듈 종류"""
    DATA_CLEANER = "data_cleaner"
    DATA_NORMALIZER = "data_normalizer"
    DEDUPLICATION = "deduplication"


class TaskStatus(Enum):
    """작업 상태"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    RETRYING = "retrying"


@dataclass
class ProcessingConfig:
    """처리 설정 데이터 클래스"""
    module: ProcessingModule
    max_workers: int = 4
    chunk_size: int = 50
    memory_limit_mb: int = 1024
    timeout_seconds: int = 300
    retry_count: int = 3
    priority: TaskPriority = TaskPriority.NORMAL
    enabled: bool = True
    module_specific_config: Dict[str, Any] = field(default_factory=dict)


@dataclass
class SystemResource:
    """시스템 리소스 정보"""
    cpu_count: int
    cpu_usage_percent: float
    memory_total_mb: float
    memory_used_mb: float
    memory_available_mb: float
    disk_usage_percent: float
    timestamp: str


@dataclass
class TaskItem:
    """작업 항목 데이터 클래스"""
    task_id: str
    module: ProcessingModule
    priority: TaskPriority
    data: Any
    status: TaskStatus = TaskStatus.PENDING
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    started_at: Optional[str] = None
    completed_at: Optional[str] = None
    retry_count: int = 0
    error_message: Optional[str] = None
    result: Optional[Any] = None


@dataclass
class PerformanceMetrics:
    """성능 지표 데이터 클래스"""
    total_tasks: int = 0
    completed_tasks: int = 0
    failed_tasks: int = 0
    average_processing_time: float = 0.0
    peak_memory_usage_mb: float = 0.0
    current_memory_usage_mb: float = 0.0
    cpu_usage_percent: float = 0.0
    throughput_tasks_per_second: float = 0.0
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


class ParallelConfigManager:
    """통합 병렬 처리 설정 관리 클래스"""
    
    def __init__(self, config_file: Optional[Path] = None):
        self.config_file = config_file or Path("parallel_config.json")
        self.processing_configs: Dict[ProcessingModule, ProcessingConfig] = {}
        self.task_queue: List[TaskItem] = []
        self.completed_tasks: List[TaskItem] = []
        self.failed_tasks: List[TaskItem] = []
        
        # 시스템 리소스 모니터링
        self.system_resources: List[SystemResource] = []
        self.performance_metrics: PerformanceMetrics = PerformanceMetrics()
        
        # 동기화용 락
        self.task_queue_lock = threading.Lock()
        self.config_lock = threading.Lock()
        self.monitoring_lock = threading.Lock()
        
        # 실행 중인 작업 추적
        self.running_tasks: Dict[str, TaskItem] = {}
        self.task_futures: Dict[str, Any] = {}
        
        # 모니터링 스레드
        self.monitoring_thread = None
        self.monitoring_active = False
        
        # 로깅 설정
        self._setup_logging()
        self.logger = logging.getLogger(__name__)
        
        # 기본 설정 로드
        self._load_default_configs()
        
        # 설정 파일 로드
        self.load_config()
        
        # 시스템 리소스 초기화
        self._update_system_resources()
        
        # 모니터링 시작
        self.start_monitoring()
        
        self.logger.info(f"ParallelConfigManager 초기화 완료 - CPU 코어: {mp.cpu_count()}")
        
        # 설정 파일 로드
        self.load_config()
        
        # 시스템 리소스 초기화
        self._update_system_resources()
        
        # 모니터링 시작
        self.start_monitoring()
        
        self.logger.info(f"ParallelConfigManager 초기화 완료 - CPU 코어: {mp.cpu_count()}")
    
    def _setup_logging(self):
        """로깅 설정"""
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_dir / "parallel_config.log", encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def _load_default_configs(self):
        """기본 설정 로드"""
        default_configs = {
            ProcessingModule.DATA_CLEANER: ProcessingConfig(
                module=ProcessingModule.DATA_CLEANER,
                max_workers=min(mp.cpu_count(), 8),
                chunk_size=100,
                memory_limit_mb=2048,
                timeout_seconds=600,
                retry_count=2,
                priority=TaskPriority.HIGH,
                module_specific_config={
                    "create_backup": True,
                    "html_cleanup": True,
                    "code_extraction": True,
                    "metadata_extraction": True
                }
            ),
            ProcessingModule.DATA_NORMALIZER: ProcessingConfig(
                module=ProcessingModule.DATA_NORMALIZER,
                max_workers=min(mp.cpu_count(), 6),
                chunk_size=50,
                memory_limit_mb=1536,
                timeout_seconds=450,
                retry_count=3,
                priority=TaskPriority.NORMAL,
                module_specific_config={
                    "caching_enabled": True,
                    "object_pooling": True,
                    "batch_processing": True,
                    "compression": False
                }
            ),
            ProcessingModule.DEDUPLICATION: ProcessingConfig(
                module=ProcessingModule.DEDUPLICATION,
                max_workers=min(mp.cpu_count(), 12),
                chunk_size=30,
                memory_limit_mb=3072,
                timeout_seconds=900,
                retry_count=1,
                priority=TaskPriority.CRITICAL,
                module_specific_config={
                    "similarity_threshold": 0.85,
                    "code_similarity_threshold": 0.95,
                    "exact_duplicate_threshold": 0.95,
                    "parallel_code_comparison": True
                }
            )
        }
        
        with self.config_lock:
            self.processing_configs = default_configs
    
    def load_config(self):
        """설정 파일 로드"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    if self.config_file.suffix.lower() == '.json':
                        config_data = json.load(f)
                    elif self.config_file.suffix.lower() in ['.yaml', '.yml']:
                        config_data = yaml.safe_load(f)
                    else:
                        raise ValueError(f"지원되지 않는 설정 파일 형식: {self.config_file.suffix}")
                
                self._parse_config_data(config_data)
                self.logger.info(f"설정 파일 로드 완료: {self.config_file}")
            else:
                self.logger.warning(f"설정 파일이 존재하지 않음: {self.config_file}")
                self.save_config()  # 기본 설정 저장
        except Exception as e:
            self.logger.error(f"설정 파일 로드 오류: {str(e)}")
            self.logger.error(traceback.format_exc())
    
    def _parse_config_data(self, config_data: Dict[str, Any]):
        """설정 데이터 파싱"""
        with self.config_lock:
            # 모듈별 설정 파싱
            for module_name, module_config in config_data.get('modules', {}).items():
                try:
                    module = ProcessingModule(module_name)
                    self.processing_configs[module] = ProcessingConfig(
                        module=module,
                        max_workers=module_config.get('max_workers', 4),
                        chunk_size=module_config.get('chunk_size', 50),
                        memory_limit_mb=module_config.get('memory_limit_mb', 1024),
                        timeout_seconds=module_config.get('timeout_seconds', 300),
                        retry_count=module_config.get('retry_count', 3),
                        priority=TaskPriority(module_config.get('priority', 2)),
                        enabled=module_config.get('enabled', True),
                        module_specific_config=module_config.get('module_specific_config', {})
                    )
                except ValueError as e:
                    self.logger.warning(f"알 수 없는 모듈: {module_name} - {str(e)}")
            
            # 전역 설정 파싱
            global_config = config_data.get('global', {})
            self.global_config = global_config
    
    def save_config(self):
        """설정 파일 저장"""
        try:
            config_data = {
                'global': getattr(self, 'global_config', {}),
                'modules': {}
            }
            
            with self.config_lock:
                for module, config in self.processing_configs.items():
                    config_data['modules'][module.value] = {
                        'max_workers': config.max_workers,
                        'chunk_size': config.chunk_size,
                        'memory_limit_mb': config.memory_limit_mb,
                        'timeout_seconds': config.timeout_seconds,
                        'retry_count': config.retry_count,
                        'priority': config.priority.value,
                        'enabled': config.enabled,
                        'module_specific_config': config.module_specific_config
                    }
            
            with open(self.config_file, 'w', encoding='utf-8') as f:
                if self.config_file.suffix.lower() == '.json':
                    json.dump(config_data, f, indent=2, ensure_ascii=False)
                elif self.config_file.suffix.lower() in ['.yaml', '.yml']:
                    yaml.dump(config_data, f, default_flow_style=False, allow_unicode=True)
            
            self.logger.info(f"설정 파일 저장 완료: {self.config_file}")
        except Exception as e:
            self.logger.error(f"설정 파일 저장 오류: {str(e)}")
            self.logger.error(traceback.format_exc())
    
    def get_module_config(self, module: ProcessingModule) -> ProcessingConfig:
        """모듈 설정 가져오기"""
        with self.config_lock:
            return self.processing_configs.get(module, self.processing_configs[ProcessingModule.DATA_CLEANER])
    
    def update_module_config(self, module: ProcessingModule, **kwargs):
        """모듈 설정 업데이트"""
        with self.config_lock:
            if module in self.processing_configs:
                for key, value in kwargs.items():
                    if hasattr(self.processing_configs[module], key):
                        setattr(self.processing_configs[module], key, value)
                        self.logger.info(f"모듈 설정 업데이트: {module.value} - {key} = {value}")
    
    def add_task(self, module: ProcessingModule, data: Any, priority: Optional[TaskPriority] = None) -> str:
        """작업 추가"""
        task_id = f"{module.value}_{int(time.time())}_{len(self.task_queue)}"
        
        if priority is None:
            priority = self.get_module_config(module).priority
        
        task = TaskItem(
            task_id=task_id,
            module=module,
            priority=priority,
            data=data
        )
        
        with self.task_queue_lock:
            # 우선순위 기반 삽입
            inserted = False
            for i, existing_task in enumerate(self.task_queue):
                if priority.value > existing_task.priority.value:
                    self.task_queue.insert(i, task)
                    inserted = True
                    break
            
            if not inserted:
                self.task_queue.append(task)
            
            self.logger.info(f"작업 추가: {task_id} - 모듈: {module.value}, 우선순위: {priority.name}")
        
        return task_id
    
    def get_next_task(self) -> Optional[TaskItem]:
        """다음 작업 가져오기"""
        with self.task_queue_lock:
            if self.task_queue:
                task = self.task_queue.pop(0)
                task.status = TaskStatus.RUNNING
                task.started_at = datetime.now().isoformat()
                self.running_tasks[task.task_id] = task
                self.performance_metrics.total_tasks += 1
                return task
            return None
    
    def complete_task(self, task_id: str, result: Any = None):
        """작업 완료"""
        with self.task_queue_lock:
            if task_id in self.running_tasks:
                task = self.running_tasks.pop(task_id)
                task.status = TaskStatus.COMPLETED
                task.completed_at = datetime.now().isoformat()
                task.result = result
                
                self.completed_tasks.append(task)
                self.performance_metrics.completed_tasks += 1
                
                # 성능 지표 업데이트
                self._update_performance_metrics(task)
                
                self.logger.info(f"작업 완료: {task_id}")
    
    def fail_task(self, task_id: str, error_message: str):
        """작업 실패"""
        with self.task_queue_lock:
            if task_id in self.running_tasks:
                task = self.running_tasks.pop(task_id)
                task.status = TaskStatus.FAILED
                task.completed_at = datetime.now().isoformat()
                task.error_message = error_message
                
                # 재시도 로직
                if task.retry_count < self.get_module_config(task.module).retry_count:
                    task.retry_count += 1
                    task.status = TaskStatus.RETRYING
                    task.started_at = None
                    task.completed_at = None
                    task.error_message = None
                    
                    # 재시도 큐에 추가
                    with self.task_queue_lock:
                        self.task_queue.append(task)
                    
                    self.logger.warning(f"작업 재시도: {task_id} (시도 {task.retry_count}/{self.get_module_config(task.module).retry_count})")
                else:
                    self.failed_tasks.append(task)
                    self.performance_metrics.failed_tasks += 1
                    self.logger.error(f"작업 실패: {task_id} - {error_message}")
    
    def _update_performance_metrics(self, task: TaskItem):
        """성능 지표 업데이트"""
        if task.started_at and task.completed_at:
            start_time = datetime.fromisoformat(task.started_at)
            end_time = datetime.fromisoformat(task.completed_at)
            processing_time = (end_time - start_time).total_seconds()
            
            # 평균 처리 시간 업데이트
            current_avg = self.performance_metrics.average_processing_time
            total_completed = self.performance_metrics.completed_tasks
            
            if total_completed > 0:
                self.performance_metrics.average_processing_time = (
                    (current_avg * (total_completed - 1) + processing_time) / total_completed
                )
            
            # 처리량 계산
            elapsed_time = (datetime.now() - start_time).total_seconds()
            if elapsed_time > 0:
                self.performance_metrics.throughput_tasks_per_second = (
                    total_completed / elapsed_time
                )
    
    def _update_system_resources(self):
        """시스템 리소스 업데이트"""
        try:
            with self.monitoring_lock:
                process = psutil.Process()
                memory_info = process.memory_info()
                
                system_resource = SystemResource(
                    cpu_count=mp.cpu_count(),
                    cpu_usage_percent=psutil.cpu_percent(),
                    memory_total_mb=psutil.virtual_memory().total / 1024 / 1024,
                    memory_used_mb=memory_info.rss / 1024 / 1024,
                    memory_available_mb=psutil.virtual_memory().available / 1024 / 1024,
                    disk_usage_percent=psutil.disk_usage('/').percent,
                    timestamp=datetime.now().isoformat()
                )
                
                self.system_resources.append(system_resource)
                
                # 최근 100개만 유지
                if len(self.system_resources) > 100:
                    self.system_resources = self.system_resources[-100:]
                
                # 성능 지표 업데이트
                self.performance_metrics.current_memory_usage_mb = system_resource.memory_used_mb
                self.performance_metrics.peak_memory_usage_mb = max(
                    self.performance_metrics.peak_memory_usage_mb,
                    system_resource.memory_used_mb
                )
                self.performance_metrics.cpu_usage_percent = system_resource.cpu_usage_percent
                
        except Exception as e:
            self.logger.error(f"시스템 리소스 업데이트 오류: {str(e)}")
    
    def start_monitoring(self):
        """모니터링 시작"""
        if not self.monitoring_active:
            self.monitoring_active = True
            self.monitoring_thread = threading.Thread(target=self._monitoring_loop, daemon=True)
            self.monitoring_thread.start()
            self.logger.info("시스템 모니터링 시작")
    
    def stop_monitoring(self):
        """모니터링 중지"""
        self.monitoring_active = False
        if self.monitoring_thread:
            self.monitoring_thread.join()
        self.logger.info("시스템 모니터링 중지")
    
    def _monitoring_loop(self):
        """모니터링 루프"""
        while self.monitoring_active:
            try:
                self._update_system_resources()
                
                # 메모리 정리
                if len(self.completed_tasks) % 10 == 0:
                    gc.collect()
                
                time.sleep(5)  # 5초마다 모니터링
            except Exception as e:
                self.logger.error(f"모니터링 루프 오류: {str(e)}")
                time.sleep(10)
    
    def get_system_status(self) -> Dict[str, Any]:
        """시스템 상태 가져오기"""
        with self.monitoring_lock:
            if self.system_resources:
                latest_resource = self.system_resources[-1]
                return {
                    'cpu_count': latest_resource.cpu_count,
                    'cpu_usage_percent': latest_resource.cpu_usage_percent,
                    'memory_total_mb': latest_resource.memory_total_mb,
                    'memory_used_mb': latest_resource.memory_used_mb,
                    'memory_available_mb': latest_resource.memory_available_mb,
                    'memory_usage_percent': (latest_resource.memory_used_mb / latest_resource.memory_total_mb) * 100,
                    'disk_usage_percent': latest_resource.disk_usage_percent,
                    'timestamp': latest_resource.timestamp
                }
            return {}
    
    def get_performance_report(self) -> Dict[str, Any]:
        """성능 보고서 생성"""
        return {
            'performance_metrics': asdict(self.performance_metrics),
            'system_status': self.get_system_status(),
            'queue_status': {
                'pending_tasks': len(self.task_queue),
                'running_tasks': len(self.running_tasks),
                'completed_tasks': len(self.completed_tasks),
                'failed_tasks': len(self.failed_tasks)
            },
            'module_configs': {
                module.value: asdict(config) 
                for module, config in self.processing_configs.items()
            }
        }
    
    def execute_tasks(self, max_concurrent_tasks: Optional[int] = None):
        """작업 실행"""
        if max_concurrent_tasks is None:
            max_concurrent_tasks = min(mp.cpu_count(), 4)
        
        config = self.get_module_config(ProcessingModule.DATA_CLEANER)
        
        with ProcessPoolExecutor(max_workers=max_concurrent_tasks) as executor:
            while self.monitoring_active:
                # 실행 중인 작업 수 확인
                running_count = len(self.running_tasks)
                
                if running_count < max_concurrent_tasks and self.task_queue:
                    # 새 작업 가져오기
                    task = self.get_next_task()
                    if task:
                        # 모듈별 설정에 따라 실행
                        future = executor.submit(self._execute_task, task)
                        self.task_futures[task.task_id] = future
                
                # 완료된 작업 확인
                completed_task_ids = []
                for task_id, future in self.task_futures.items():
                    try:
                        result = future.result(timeout=0.1)  # 비동기 확인
                        if result is not None:
                            self.complete_task(task_id, result)
                            completed_task_ids.append(task_id)
                    except:
                        pass  # 아직 완료되지 않음
                
                # 완료된 작업 정리
                for task_id in completed_task_ids:
                    self.task_futures.pop(task_id, None)
                
                time.sleep(0.1)  # 0.1초 대기
    
    def _execute_task(self, task: TaskItem) -> Any:
        """개별 작업 실행"""
        try:
            module_config = self.get_module_config(task.module)
            
            # 모듈별 실행 로직
            if task.module == ProcessingModule.DATA_CLEANER:
                from data_cleaner import DataCleaner
                cleaner = DataCleaner()
                # 여기에 실제 작업 실행 로직 구현
                return {"status": "success", "task_id": task.task_id}
            
            elif task.module == ProcessingModule.DATA_NORMALIZER:
                from data_normalizer import DataNormalizer
                normalizer = DataNormalizer()
                # 여기에 실제 작업 실행 로직 구현
                return {"status": "success", "task_id": task.task_id}
            
            elif task.module == ProcessingModule.DEDUPLICATION:
                from deduplication import Deduplicator
                deduplicator = Deduplicator()
                # 여기에 실제 작업 실행 로직 구현
                return {"status": "success", "task_id": task.task_id}
            
        except Exception as e:
            error_msg = f"작업 실행 오류: {str(e)}"
            self.logger.error(error_msg)
            self.fail_task(task.task_id, error_msg)
            return None
    
    def cleanup(self):
        """정리"""
        self.stop_monitoring()
        
        # 임시 파일 정리
        temp_files = []
        for task in self.completed_tasks:
            if hasattr(task.result, 'temp_files'):
                if task.result and hasattr(task.result, 'temp_files'):
                    temp_files.extend(task.result.temp_files)
        
        for temp_file in temp_files:
            try:
                if Path(temp_file).exists():
                    Path(temp_file).unlink()
            except Exception as e:
                self.logger.warning(f"임시 파일 정리 오류: {temp_file} - {str(e)}")
        
        self.logger.info("ParallelConfigManager 정리 완료")


# 전역 인스턴스
_config_manager = None


def get_config_manager() -> ParallelConfigManager:
    """전역 설정 관리자 인스턴스 가져오기"""
    global _config_manager
    if _config_manager is None:
        _config_manager = ParallelConfigManager()
    return _config_manager


def initialize_config_manager(config_file: Optional[Path] = None):
    """전역 설정 관리자 초기화"""
    global _config_manager
    _config_manager = ParallelConfigManager(config_file)


# 예제 사용 코드
if __name__ == "__main__":
    # 설정 관리자 초기화
    manager = get_config_manager()
    
    # 작업 추가
    task_id1 = manager.add_task(
        ProcessingModule.DATA_CLEANER,
        {"input_path": "test_data", "output_path": "cleaned_data"},
        TaskPriority.HIGH
    )
    
    task_id2 = manager.add_task(
        ProcessingModule.DATA_NORMALIZER,
        {"input_file": "data.json"},
        TaskPriority.NORMAL
    )
    
    # 시스템 상태 확인
    status = manager.get_system_status()
    print(f"시스템 상태: {status}")
    
    # 성능 보고서 생성
    report = manager.get_performance_report()
    print(f"성능 보고서: {report}")
    
    # 정리
    manager.cleanup()