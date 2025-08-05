"""
WinForms_Docs 자동화된 테스트 관리 시스템
=====================================

주요 기능:
==========
1. 테스트 스케줄링 및 실행
   - 주기적인 테스트 실행
   - 이벤트 기반 테스트 트리거
   - 크론 잡 스타일 스케줄링
   - 조건부 테스트 실행

2. 테스트 결과 수집 및 분석
   - 실시간 테스트 모니터링
   - 테스트 결과 집계
   - 성능 지표 추적
   - 이상 탐지 및 알림

3. 성능 회귀 감지
   - 기준선 성능과의 비교
   - 성능 저하 감지
   - 통계적 분석을 통한 회귀 판단
   - 자동 알림 시스템

4. 보고서 자동 생성
   - 테스트 요약 보고서
   - 성능 추이 분석
   - 이상 현상 상세 보고
   - 관리자 알림

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0 (자동화된 테스트 관리 시스템)
"""

import asyncio
import logging
import time
import json
import psutil
import gc
import os
import schedule
import threading
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any, Union, Callable
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed
import sqlite3
import pandas as pd
import numpy as np
from enum import Enum
import smtplib
from email.mime.text import MimeText
from email.mime.multipart import MimeMultipart
import pickle
import hashlib

# 로컬 모듈 임포트
try:
    from integrated_performance_test_framework import IntegratedPerformanceTestFramework, create_test_framework
    from performance_benchmark_suite import PerformanceBenchmarkSuite, create_benchmark_suite
    from performance_monitor import PerformanceMonitor, get_performance_monitor
    from config import (
        WINFORMS_DOCS_DIR, OUTPUT_DIR, BACKUP_DIR,
        PROCESSING_OPTIONS, LOGGING_CONFIG
    )
    MODULES_AVAILABLE = True
except ImportError as e:
    print(f"일부 모듈 임포트 실패: {e}")
    MODULES_AVAILABLE = False

# 로컬 로깅 설정 (config 모듈이 없을 경우 대비)
try:
    from config import LOGGING_CONFIG
    logging.basicConfig(
        level=getattr(logging, LOGGING_CONFIG['level']),
        format=LOGGING_CONFIG['format'],
        handlers=[
            logging.FileHandler(LOGGING_CONFIG['file_path'], encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
except ImportError:
    # 기본 로깅 설정
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/automated_test_manager.log', encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
logger = logging.getLogger(__name__)

class TestStatus(Enum):
    """테스트 상태"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class TestPriority(Enum):
    """테스트 우선순위"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class TestType(Enum):
    """테스트 타입"""
    UNIT_TEST = "unit_test"
    INTEGRATION_TEST = "integration_test"
    LOAD_TEST = "load_test"
    STRESS_TEST = "stress_test"
    REGRESSION_TEST = "regression_test"
    BENCHMARK_TEST = "benchmark_test"

@dataclass
class TestSchedule:
    """테스트 스케줄 데이터 클래스"""
    test_id: str
    test_name: str
    test_type: TestType
    priority: TestPriority
    schedule_time: datetime
    repeat_interval: Optional[timedelta] = None
    enabled: bool = True
    max_retries: int = 3
    timeout_seconds: int = 300
    config: Optional[Dict[str, Any]] = None
    
@dataclass
class TestExecution:
    """테스트 실행 데이터 클래스"""
    execution_id: str
    test_id: str
    test_name: str
    test_type: str
    status: TestStatus
    start_time: datetime
    end_time: Optional[datetime] = None
    duration: Optional[float] = None
    result: Optional[Dict[str, Any]] = None
    error_message: Optional[str] = None
    retry_count: int = 0
    execution_metrics: Optional[Dict[str, Any]] = None
    
@dataclass
class TestAlert:
    """테스트 알림 데이터 클래스"""
    alert_id: str
    test_id: str
    test_name: str
    alert_type: str
    severity: str
    message: str
    timestamp: datetime
    resolved: bool = False
    resolved_at: Optional[datetime] = None
    metadata: Optional[Dict[str, Any]] = None

class AutomatedTestManager:
    """자동화된 테스트 관리 시스템 - 핵심 클래스"""
    
    def __init__(self, db_path: str = "performance_results/test_manager.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 성능 모니터 초기화
        self.performance_monitor = get_performance_monitor()
        
        # 테스트 스케줄러
        self.scheduler = schedule.Scheduler()
        
        # 실행 중인 테스트 추적
        self.running_tests: Dict[str, TestExecution] = {}
        
        # 알림 시스템
        self.alerts: List[TestAlert] = []
        
        # 설정
        self.config = {
            'enable_email_notifications': True,
            'email_smtp_server': 'smtp.gmail.com',
            'email_smtp_port': 587,
            'email_username': '',
            'email_password': '',
            'email_recipients': [],
            'enable_slack_notifications': False,
            'slack_webhook_url': '',
            'test_timeout_seconds': 300,
            'max_concurrent_tests': 5,
            'performance_regression_threshold': 0.1,  # 10% 성능 저하 감지 임계값
            'memory_threshold_mb': 1024,  # 메모리 임계값 (MB)
            'cpu_threshold_percent': 80,  # CPU 임계값 (%)
            'disk_space_threshold_percent': 90,  # 디스크 공간 임계값 (%)
            'auto_cleanup_days': 30  # 자동 정리 기간 (일)
        }
        
        # 스케줄러 스레드
        self.scheduler_thread = None
        self.scheduler_running = False
        
        # 데이터베이스 초기화
        self._init_database()
        
        logger.info("자동화된 테스트 관리 시스템 초기화 완료")
    
    def _init_database(self):
        """데이터베이스 초기화"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 테스트 스케줄 테이블
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS test_schedules (
                        test_id TEXT PRIMARY KEY,
                        test_name TEXT NOT NULL,
                        test_type TEXT NOT NULL,
                        priority INTEGER NOT NULL,
                        schedule_time TEXT NOT NULL,
                        repeat_interval TEXT,
                        enabled BOOLEAN DEFAULT 1,
                        max_retries INTEGER DEFAULT 3,
                        timeout_seconds INTEGER DEFAULT 300,
                        config TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # 테스트 실행 테이블
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS test_executions (
                        execution_id TEXT PRIMARY KEY,
                        test_id TEXT NOT NULL,
                        test_name TEXT NOT NULL,
                        test_type TEXT NOT NULL,
                        status TEXT NOT NULL,
                        start_time TEXT NOT NULL,
                        end_time TEXT,
                        duration REAL,
                        result TEXT,
                        error_message TEXT,
                        retry_count INTEGER DEFAULT 0,
                        execution_metrics TEXT,
                        FOREIGN KEY (test_id) REFERENCES test_schedules (test_id)
                    )
                ''')
                
                # 테스트 알림 테이블
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS test_alerts (
                        alert_id TEXT PRIMARY KEY,
                        test_id TEXT NOT NULL,
                        test_name TEXT NOT NULL,
                        alert_type TEXT NOT NULL,
                        severity TEXT NOT NULL,
                        message TEXT NOT NULL,
                        timestamp TEXT NOT NULL,
                        resolved BOOLEAN DEFAULT 0,
                        resolved_at TEXT,
                        metadata TEXT,
                        FOREIGN KEY (test_id) REFERENCES test_schedules (test_id)
                    )
                ''')
                
                # 성능 기준선 테이블
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS performance_baselines (
                        baseline_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        test_id TEXT NOT NULL,
                        test_name TEXT NOT NULL,
                        metric_name TEXT NOT NULL,
                        metric_value REAL NOT NULL,
                        confidence_interval_lower REAL,
                        confidence_interval_upper REAL,
                        created_at TEXT NOT NULL,
                        FOREIGN KEY (test_id) REFERENCES test_schedules (test_id)
                    )
                ''')
                
                # 인덱스 생성
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_schedules_enabled ON test_schedules(enabled)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_schedules_priority ON test_schedules(priority)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_executions_status ON test_executions(status)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_executions_start_time ON test_executions(start_time)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_alerts_resolved ON test_alerts(resolved)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_alerts_timestamp ON test_alerts(timestamp)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_baselines_test_id ON performance_baselines(test_id)')
                
                conn.commit()
                logger.info("테스트 관리 데이터베이스 초기화 완료")
                
        except Exception as e:
            logger.error(f"데이터베이스 초기화 오류: {e}")
            raise
    
    def start_scheduler(self):
        """스케줄러 시작"""
        if self.scheduler_running:
            logger.warning("스케줄러가 이미 실행 중입니다")
            return
        
        self.scheduler_running = True
        self.scheduler_thread = threading.Thread(target=self._scheduler_loop, daemon=True)
        self.scheduler_thread.start()
        
        logger.info("테스트 스케줄러 시작")
    
    def stop_scheduler(self):
        """스케줄러 중지"""
        if not self.scheduler_running:
            logger.warning("스케줄러가 실행 중이지 않습니다")
            return
        
        self.scheduler_running = False
        if self.scheduler_thread:
            self.scheduler_thread.join(timeout=5)
        
        logger.info("테스트 스케줄러 중지")
    
    def _scheduler_loop(self):
        """스케줄러 루프"""
        while self.scheduler_running:
            try:
                # 스케줄된 작업 실행
                schedule.run_pending()
                
                # 대기 시간
                time.sleep(1)
                
            except Exception as e:
                logger.error(f"스케줄러 루프 오류: {e}")
                time.sleep(5)
    
    def schedule_test(self, test_schedule: TestSchedule) -> bool:
        """테스트 스케줄링"""
        try:
            # 데이터베이스에 저장
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    INSERT OR REPLACE INTO test_schedules 
                    (test_id, test_name, test_type, priority, schedule_time, 
                     repeat_interval, enabled, max_retries, timeout_seconds, config)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    test_schedule.test_id,
                    test_schedule.test_name,
                    test_schedule.test_type.value,
                    test_schedule.priority.value,
                    test_schedule.schedule_time.isoformat(),
                    test_schedule.repeat_interval.total_seconds() if test_schedule.repeat_interval else None,
                    test_schedule.enabled,
                    test_schedule.max_retries,
                    test_schedule.timeout_seconds,
                    json.dumps(test_schedule.config, ensure_ascii=False) if test_schedule.config else None
                ))
                
                conn.commit()
            
            # 스케줄러에 작업 추가
            if test_schedule.repeat_interval:
                # 반복 스케줄
                self.scheduler.every(test_schedule.repeat_interval.total_seconds()).seconds.do(
                    self._execute_scheduled_test, test_schedule.test_id
                )
            else:
                # 단일 실행 스케줄
                scheduled_time = test_schedule.schedule_time
                now = datetime.now()
                
                if scheduled_time > now:
                    delay = (scheduled_time - now).total_seconds()
                    self.scheduler.every(delay).seconds.do(
                        self._execute_scheduled_test, test_schedule.test_id
                    )
            
            logger.info(f"테스트 스케줄링 완료: {test_schedule.test_name}")
            return True
            
        except Exception as e:
            logger.error(f"테스트 스케줄링 오류: {e}")
            return False
    
    def _execute_scheduled_test(self, test_id: str):
        """스케줄된 테스트 실행"""
        try:
            # 테스트 정보 조회
            test_schedule = self.get_test_schedule(test_id)
            if not test_schedule or not test_schedule.enabled:
                return
            
            # 테스트 실행
            self.execute_test(test_schedule)
            
        except Exception as e:
            logger.error(f"스케줄된 테스트 실행 오류: {e}")
    
    def execute_test(self, test_schedule: TestSchedule) -> TestExecution:
        """테스트 실행"""
        execution_id = f"{test_schedule.test_id}_{int(time.time())}"
        
        # 실행 기록 생성
        execution = TestExecution(
            execution_id=execution_id,
            test_id=test_schedule.test_id,
            test_name=test_schedule.test_name,
            test_type=test_schedule.test_type.value,
            status=TestStatus.RUNNING,
            start_time=datetime.now()
        )
        
        # 실행 중인 테스트로 등록
        self.running_tests[execution_id] = execution
        
        try:
            # 테스트 실행
            result = self._run_test_with_timeout(test_schedule, execution)
            
            # 실행 결과 업데이트
            execution.status = TestStatus.COMPLETED if result.get('success', False) else TestStatus.FAILED
            execution.result = result
            execution.end_time = datetime.now()
            execution.duration = (execution.end_time - execution.start_time).total_seconds()
            
            # 성능 회귀 감지
            self._detect_performance_regression(test_schedule, execution)
            
            # 알림 생성
            if not result.get('success', False):
                self._create_test_alert(
                    test_schedule.test_id,
                    test_schedule.test_name,
                    'test_failure',
                    'high',
                    f"테스트 실패: {test_schedule.test_name}",
                    {'execution_id': execution_id, 'error': result.get('error', 'Unknown error')}
                )
            
        except Exception as e:
            execution.status = TestStatus.FAILED
            execution.error_message = str(e)
            execution.end_time = datetime.now()
            execution.duration = (execution.end_time - execution.start_time).total_seconds()
            
            # 알림 생성
            self._create_test_alert(
                test_schedule.test_id,
                test_schedule.test_name,
                'test_error',
                'critical',
                f"테스트 실행 오류: {test_schedule.test_name} - {str(e)}",
                {'execution_id': execution_id}
            )
        
        finally:
            # 실행 중인 테스트에서 제거
            if execution_id in self.running_tests:
                del self.running_tests[execution_id]
            
            # 실행 결과 저장
            self._save_test_execution(execution)
        
        return execution
    
    def _run_test_with_timeout(self, test_schedule: TestSchedule, execution: TestExecution) -> Dict[str, Any]:
        """타임아웃을 적용한 테스트 실행"""
        def run_test():
            try:
                # 테스트 타입에 따라 실행
                if test_schedule.test_type == TestType.UNIT_TEST:
                    return self._run_unit_test(test_schedule)
                elif test_schedule.test_type == TestType.INTEGRATION_TEST:
                    return self._run_integration_test(test_schedule)
                elif test_schedule.test_type == TestType.LOAD_TEST:
                    return self._run_load_test(test_schedule)
                elif test_schedule.test_type == TestType.STRESS_TEST:
                    return self._run_stress_test(test_schedule)
                elif test_schedule.test_type == TestType.REGRESSION_TEST:
                    return self._run_regression_test(test_schedule)
                elif test_schedule.test_type == TestType.BENCHMARK_TEST:
                    return self._run_benchmark_test(test_schedule)
                else:
                    return {'success': False, 'error': f'Unknown test type: {test_schedule.test_type}'}
            
            except Exception as e:
                return {'success': False, 'error': str(e)}
        
        # 타임아웃 적용
        import concurrent.futures
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(run_test)
            try:
                return future.result(timeout=test_schedule.timeout_seconds)
            except concurrent.futures.TimeoutError:
                return {'success': False, 'error': f'Test timeout after {test_schedule.timeout_seconds} seconds'}
    
    def _run_unit_test(self, test_schedule: TestSchedule) -> Dict[str, Any]:
        """단위 테스트 실행"""
        try:
            if MODULES_AVAILABLE:
                test_framework = create_test_framework()
                
                # 단위 테스트 설정
                from integrated_performance_test_framework import TestConfig, TestScenario, TestType as IntegratedTestType
                
                config = TestConfig(
                    scenario=TestScenario.SMALL_DATA,
                    test_type=IntegratedTestType.UNIT_TEST,
                    data_size_mb=0.5,
                    concurrent_files=5,
                    iterations=3
                )
                
                # 테스트 실행
                results = test_framework.run_single_test(config)
                
                return {
                    'success': results.success,
                    'metrics': [asdict(m) for m in results.metrics],
                    'test_count': len(results.metrics),
                    'error': results.error_message if not results.success else None
                }
            else:
                return {'success': False, 'error': 'Test framework not available'}
                
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _run_integration_test(self, test_schedule: TestSchedule) -> Dict[str, Any]:
        """통합 테스트 실행"""
        try:
            if MODULES_AVAILABLE:
                test_framework = create_test_framework()
                
                # 통합 테스트 설정
                from integrated_performance_test_framework import TestConfig, TestScenario, TestType as IntegratedTestType
                
                config = TestConfig(
                    scenario=TestScenario.MEDIUM_DATA,
                    test_type=IntegratedTestType.INTEGRATION_TEST,
                    data_size_mb=50,
                    concurrent_files=3,
                    iterations=2
                )
                
                # 테스트 실행
                results = test_framework.run_single_test(config)
                
                return {
                    'success': results.success,
                    'metrics': [asdict(m) for m in results.metrics],
                    'test_count': len(results.metrics),
                    'error': results.error_message if not results.success else None
                }
            else:
                return {'success': False, 'error': 'Test framework not available'}
                
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _run_load_test(self, test_schedule: TestSchedule) -> Dict[str, Any]:
        """부하 테스트 실행"""
        try:
            if MODULES_AVAILABLE:
                test_framework = create_test_framework()
                
                # 부하 테스트 설정
                from integrated_performance_test_framework import TestConfig, TestScenario, TestType as IntegratedTestType
                
                config = TestConfig(
                    scenario=TestScenario.LARGE_DATA,
                    test_type=IntegratedTestType.LOAD_TEST,
                    data_size_mb=500,
                    concurrent_files=10,
                    iterations=2
                )
                
                # 테스트 실행
                results = test_framework.run_single_test(config)
                
                return {
                    'success': results.success,
                    'metrics': [asdict(m) for m in results.metrics],
                    'test_count': len(results.metrics),
                    'error': results.error_message if not results.success else None
                }
            else:
                return {'success': False, 'error': 'Test framework not available'}
                
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _run_stress_test(self, test_schedule: TestSchedule) -> Dict[str, Any]:
        """스트레스 테스트 실행"""
        try:
            if MODULES_AVAILABLE:
                test_framework = create_test_framework()
                
                # 스트레스 테스트 설정
                from integrated_performance_test_framework import TestConfig, TestScenario, TestType as IntegratedTestType
                
                config = TestConfig(
                    scenario=TestScenario.CONCURRENT_PROCESSING,
                    test_type=IntegratedTestType.STRESS_TEST,
                    data_size_mb=100,
                    concurrent_files=20,
                    iterations=1
                )
                
                # 테스트 실행
                results = test_framework.run_single_test(config)
                
                return {
                    'success': results.success,
                    'metrics': [asdict(m) for m in results.metrics],
                    'test_count': len(results.metrics),
                    'error': results.error_message if not results.success else None
                }
            else:
                return {'success': False, 'error': 'Test framework not available'}
                
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _run_regression_test(self, test_schedule: TestSchedule) -> Dict[str, Any]:
        """회귀 테스트 실행"""
        try:
            # 기존 성능과 비교
            baseline_metrics = self._get_performance_baseline(test_schedule.test_id)
            current_metrics = self._run_current_performance_test(test_schedule)
            
            # 성능 비교
            regression_detected = self._compare_performance(baseline_metrics, current_metrics)
            
            return {
                'success': not regression_detected,
                'baseline_metrics': baseline_metrics,
                'current_metrics': current_metrics,
                'regression_detected': regression_detected,
                'regression_details': self._calculate_regression_details(baseline_metrics, current_metrics)
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _run_benchmark_test(self, test_schedule: TestSchedule) -> Dict[str, Any]:
        """벤치마크 테스트 실행"""
        try:
            if MODULES_AVAILABLE:
                benchmark_suite = create_benchmark_suite()
                
                # 벤치마크 설정
                from performance_benchmark_suite import BenchmarkConfig, BenchmarkType
                
                config = BenchmarkConfig(
                    benchmark_type=BenchmarkType.BATCH_FILES,
                    data_size_mb=50,
                    file_count=20,
                    concurrent_files=5,
                    iterations=3
                )
                
                # 벤치마크 실행
                results = benchmark_suite.run_single_benchmark(config)
                
                return {
                    'success': True,
                    'baseline_metrics': asdict(results.baseline_metrics) if results.baseline_metrics else None,
                    'optimized_metrics': asdict(results.optimized_metrics) if results.optimized_metrics else None,
                    'improvement_percentage': results.improvement_percentage,
                    'confidence_interval': results.confidence_interval,
                    'statistical_significance': results.statistical_significance
                }
            else:
                return {'success': False, 'error': 'Benchmark suite not available'}
                
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _run_current_performance_test(self, test_schedule: TestSchedule) -> Dict[str, Any]:
        """현재 성능 테스트 실행"""
        try:
            if MODULES_AVAILABLE:
                test_framework = create_test_framework()
                
                # 현재 성능 테스트 설정
                from integrated_performance_test_framework import TestConfig, TestScenario, TestType as IntegratedTestType
                
                config = TestConfig(
                    scenario=TestScenario.MEDIUM_DATA,
                    test_type=IntegratedTestType.INTEGRATION_TEST,
                    data_size_mb=50,
                    concurrent_files=3,
                    iterations=3
                )
                
                # 테스트 실행
                results = test_framework.run_single_test(config)
                
                # 평균 메트릭 계산
                if results.metrics:
                    avg_metrics = {
                        'execution_time': sum(m.execution_time for m in results.metrics) / len(results.metrics),
                        'memory_usage_mb': sum(m.memory_usage_mb for m in results.metrics) / len(results.metrics),
                        'throughput_files_per_sec': sum(m.throughput_files_per_sec for m in results.metrics) / len(results.metrics)
                    }
                    return avg_metrics
                
                return {}
            else:
                return {}
                
        except Exception as e:
            logger.error(f"현재 성능 테스트 오류: {e}")
            return {}
    
    def _get_performance_baseline(self, test_id: str) -> Dict[str, Any]:
        """성능 기준선 조회"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    SELECT metric_name, metric_value, confidence_interval_lower, confidence_interval_upper
                    FROM performance_baselines
                    WHERE test_id = ?
                    ORDER BY created_at DESC
                    LIMIT 3
                ''', (test_id,))
                
                baselines = {}
                for row in cursor.fetchall():
                    metric_name = row[0]
                    metric_value = row[1]
                    confidence_interval_lower = row[2]
                    confidence_interval_upper = row[3]
                    
                    baselines[metric_name] = {
                        'value': metric_value,
                        'confidence_interval': (confidence_interval_lower, confidence_interval_upper)
                    }
                
                return baselines
                
        except Exception as e:
            logger.error(f"성능 기준선 조회 오류: {e}")
            return {}
    
    def _compare_performance(self, baseline: Dict[str, Any], current: Dict[str, Any]) -> bool:
        """성능 비교 및 회귀 감지"""
        try:
            for metric_name, baseline_data in baseline.items():
                if metric_name in current:
                    baseline_value = baseline_data['value']
                    current_value = current[metric_name]
                    
                    # 신뢰 구간 확인
                    confidence_interval = baseline_data['confidence_interval']
                    if confidence_interval[0] is not None and confidence_interval[1] is not None:
                        # 현재 값이 신뢰 구간을 벗어나면 회귀로 판단
                        if current_value < confidence_interval[0] or current_value > confidence_interval[1]:
                            logger.warning(f"성능 회귀 감지: {metric_name} - 기준: {baseline_value:.2f}, 현재: {current_value:.2f}")
                            return True
                    
                    # 간단한 비율 기반 회귀 감지
                    if baseline_value > 0:
                        change_ratio = abs(current_value - baseline_value) / baseline_value
                        if change_ratio > self.config['performance_regression_threshold']:
                            logger.warning(f"성능 회귀 감지: {metric_name} - 변화율: {change_ratio:.2%}")
                            return True
            
            return False
            
        except Exception as e:
            logger.error(f"성능 비교 오류: {e}")
            return False
    
    def _calculate_regression_details(self, baseline: Dict[str, Any], current: Dict[str, Any]) -> Dict[str, Any]:
        """회귀 상세 정보 계산"""
        details = {}
        
        try:
            for metric_name, baseline_data in baseline.items():
                if metric_name in current:
                    baseline_value = baseline_data['value']
                    current_value = current[metric_name]
                    
                    if baseline_value > 0:
                        change_ratio = (current_value - baseline_value) / baseline_value
                        change_percent = change_ratio * 100
                        
                        details[metric_name] = {
                            'baseline_value': baseline_value,
                            'current_value': current_value,
                            'change_ratio': change_ratio,
                            'change_percent': change_percent,
                            'regression_detected': change_ratio < -self.config['performance_regression_threshold']
                        }
            
            return details
            
        except Exception as e:
            logger.error(f"회귀 상세 정보 계산 오류: {e}")
            return {}
    
    def _detect_performance_regression(self, test_schedule: TestSchedule, execution: TestExecution):
        """성능 회귀 감지"""
        try:
            if execution.result and 'regression_detected' in execution.result:
                if execution.result['regression_detected']:
                    self._create_test_alert(
                        test_schedule.test_id,
                        test_schedule.test_name,
                        'performance_regression',
                        'high',
                        f"성능 회귀 감지: {test_schedule.test_name}",
                        {
                            'execution_id': execution.execution_id,
                            'regression_details': execution.result.get('regression_details', {})
                        }
                    )
            
        except Exception as e:
            logger.error(f"성능 회귀 감지 오류: {e}")
    
    def _create_test_alert(self, test_id: str, test_name: str, alert_type: str, severity: str, message: str, metadata: Optional[Dict[str, Any]] = None):
        """테스트 알림 생성"""
        try:
            alert_id = f"alert_{int(time.time())}_{hashlib.md5(f'{test_id}_{alert_type}'.encode()).hexdigest()[:8]}"
            
            alert = TestAlert(
                alert_id=alert_id,
                test_id=test_id,
                test_name=test_name,
                alert_type=alert_type,
                severity=severity,
                message=message,
                timestamp=datetime.now(),
                metadata=metadata
            )
            
            # 메모리에 저장
            self.alerts.append(alert)
            
            # 데이터베이스에 저장
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    INSERT INTO test_alerts 
                    (alert_id, test_id, test_name, alert_type, severity, message, timestamp, metadata)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    alert_id,
                    test_id,
                    test_name,
                    alert_type,
                    severity,
                    message,
                    alert.timestamp.isoformat(),
                    json.dumps(metadata, ensure_ascii=False) if metadata else None
                ))
                
                conn.commit()
            
            # 알림 발송
            self._send_alert_notification(alert)
            
            logger.info(f"알림 생성: {alert_type} - {message}")
            
        except Exception as e:
            logger.error(f"알림 생성 오류: {e}")
    
    def _send_alert_notification(self, alert: TestAlert):
        """알림 발송"""
        try:
            # 이메일 알림
            if self.config['enable_email_notifications'] and self.config['email_recipients']:
                self._send_email_alert(alert)
            
            # Slack 알림
            if self.config['enable_slack_notifications'] and self.config['slack_webhook_url']:
                self._send_slack_alert(alert)
            
        except Exception as e:
            logger.error(f"알림 발송 오류: {e}")
    
    def _send_email_alert(self, alert: TestAlert):
        """이메일 알림 발송"""
        try:
            if not self.config['email_username'] or not self.config['email_password']:
                logger.warning("이메일 설정이 되지 않았습니다")
                return
            
            # 이메일 생성
            msg = MimeMultipart()
            msg['From'] = self.config['email_username']
            msg['To'] = ', '.join(self.config['email_recipients'])
            msg['Subject'] = f"[테스트 알림] {alert.severity.upper()}: {alert.test_name}"
            
            # 이메일 내용
            body = f"""
            테스트 알림이 생성되었습니다.
            
            알림 정보:
            - 테스트 이름: {alert.test_name}
            - 알림 타입: {alert.alert_type}
            - 심각도: {alert.severity}
            - 메시지: {alert.message}
            - 시간: {alert.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
            
            상세 정보:
            {json.dumps(alert.metadata, indent=2, ensure_ascii=False) if alert.metadata else '없음'}
            """
            
            msg.attach(MimeText(body, 'plain', 'utf-8'))
            
            # 이메일 발송
            with smtplib.SMTP(self.config['email_smtp_server'], self.config['email_smtp_port']) as server:
                server.starttls()
                server.login(self.config['email_username'], self.config['email_password'])
                server.send_message(msg)
            
            logger.info(f"이메일 알림 발송 완료: {alert.test_name}")
            
        except Exception as e:
            logger.error(f"이메일 알림 발송 오류: {e}")
    
    def _send_slack_alert(self, alert: TestAlert):
        """Slack 알림 발송"""
        try:
            import requests
            
            # Slack 메시지 생성
            slack_message = {
                'text': f"🚨 테스트 알림: {alert.test_name}",
                'attachments': [
                    {
                        'color': 'danger' if alert.severity == 'critical' else 'warning',
                        'fields': [
                            {'title': '알림 타입', 'value': alert.alert_type, 'short': True},
                            {'title': '심각도', 'value': alert.severity, 'short': True},
                            {'title': '메시지', 'value': alert.message, 'short': False},
                            {'title': '시간', 'value': alert.timestamp.strftime('%Y-%m-%d %H:%M:%S'), 'short': True}
                        ]
                    }
                ]
            }
            
            # Slack Webhook 호출
            response = requests.post(
                self.config['slack_webhook_url'],
                json=slack_message,
                timeout=10
            )
            
            if response.status_code == 200:
                logger.info(f"Slack 알림 발송 완료: {alert.test_name}")
            else:
                logger.error(f"Slack 알림 발송 실패: {response.status_code}")
            
        except Exception as e:
            logger.error(f"Slack 알림 발송 오류: {e}")
    
    def _save_test_execution(self, execution: TestExecution):
        """테스트 실행 결과 저장"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    INSERT INTO test_executions 
                    (execution_id, test_id, test_name, test_type, status, 
                     start_time, end_time, duration, result, error_message, 
                     retry_count, execution_metrics)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    execution.execution_id,
                    execution.test_id,
                    execution.test_name,
                    execution.test_type,
                    execution.status.value,
                    execution.start_time.isoformat(),
                    execution.end_time.isoformat() if execution.end_time else None,
                    execution.duration,
                    json.dumps(execution.result, ensure_ascii=False) if execution.result else None,
                    execution.error_message,
                    execution.retry_count,
                    json.dumps(execution.execution_metrics, ensure_ascii=False) if execution.execution_metrics else None
                ))
                
                conn.commit()
                
        except Exception as e:
            logger.error(f"테스트 실행 결과 저장 오류: {e}")
    
    def get_test_schedule(self, test_id: str) -> Optional[TestSchedule]:
        """테스트 스케줄 조회"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    SELECT test_id, test_name, test_type, priority, schedule_time, 
                           repeat_interval, enabled, max_retries, timeout_seconds, config
                    FROM test_schedules
                    WHERE test_id = ?
                ''', (test_id,))
                
                row = cursor.fetchone()
                if row:
                    return TestSchedule(
                        test_id=row[0],
                        test_name=row[1],
                        test_type=TestType(row[2]),
                        priority=TestPriority(row[3]),
                        schedule_time=datetime.fromisoformat(row[4]),
                        repeat_interval=timedelta(seconds=row[5]) if row[5] else None,
                        enabled=bool(row[6]),
                        max_retries=row[7],
                        timeout_seconds=row[8],
                        config=json.loads(row[9]) if row[9] else None
                    )
                
                return None
                
        except Exception as e:
            logger.error(f"테스트 스케줄 조회 오류: {e}")
            return None
    
    def get_test_executions(self, test_id: Optional[str] = None, limit: int = 100) -> List[TestExecution]:
        """테스트 실행 이력 조회"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                if test_id:
                    cursor.execute('''
                        SELECT execution_id, test_id, test_name, test_type, status, 
                               start_time, end_time, duration, result, error_message, 
                               retry_count, execution_metrics
                        FROM test_executions
                        WHERE test_id = ?
                        ORDER BY start_time DESC
                        LIMIT ?
                    ''', (test_id, limit))
                else:
                    cursor.execute('''
                        SELECT execution_id, test_id, test_name, test_type, status, 
                               start_time, end_time, duration, result, error_message, 
                               retry_count, execution_metrics
                        FROM test_executions
                        ORDER BY start_time DESC
                        LIMIT ?
                    ''', (limit,))
                
                executions = []
                for row in cursor.fetchall():
                    execution = TestExecution(
                        execution_id=row[0],
                        test_id=row[1],
                        test_name=row[2],
                        test_type=row[3],
                        status=TestStatus(row[4]),
                        start_time=datetime.fromisoformat(row[5]),
                        end_time=datetime.fromisoformat(row[6]) if row[6] else None,
                        duration=row[7],
                        result=json.loads(row[8]) if row[8] else None,
                        error_message=row[9],
                        retry_count=row[10],
                        execution_metrics=json.loads(row[11]) if row[11] else None
                    )
                    executions.append(execution)
                
                return executions
                
        except Exception as e:
            logger.error(f"테스트 실행 이력 조회 오류: {e}")
            return []
    
    def get_alerts(self, resolved: Optional[bool] = None, limit: int = 100) -> List[TestAlert]:
        """알림 목록 조회"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                query = '''
                    SELECT alert_id, test_id, test_name, alert_type, severity, 
                           message, timestamp, resolved, resolved_at, metadata
                    FROM test_alerts
                '''
                params = []
                
                if resolved is not None:
                    query += ' WHERE resolved = ?'
                    params.append(resolved)
                
                query += ' ORDER BY timestamp DESC LIMIT ?'
                params.append(limit)
                
                cursor.execute(query, params)
                
                alerts = []
                for row in cursor.fetchall():
                    alert = TestAlert(
                        alert_id=row[0],
                        test_id=row[1],
                        test_name=row[2],
                        alert_type=row[3],
                        severity=row[4],
                        message=row[5],
                        timestamp=datetime.fromisoformat(row[6]),
                        resolved=bool(row[7]),
                        resolved_at=datetime.fromisoformat(row[8]) if row[8] else None,
                        metadata=json.loads(row[9]) if row[9] else None
                    )
                    alerts.append(alert)
                
                return alerts
                
        except Exception as e:
            logger.error(f"알림 목록 조회 오류: {e}")
            return []
    
    def resolve_alert(self, alert_id: str) -> bool:
        """알림 해결"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    UPDATE test_alerts 
                    SET resolved = 1, resolved_at = ?
                    WHERE alert_id = ?
                ''', (datetime.now().isoformat(), alert_id))
                
                conn.commit()
                
                # 메모리 내 알림 업데이트
                for alert in self.alerts:
                    if alert.alert_id == alert_id:
                        alert.resolved = True
                        alert.resolved_at = datetime.now()
                        break
                
                return cursor.rowcount > 0
                
        except Exception as e:
            logger.error(f"알림 해결 오류: {e}")
            return False
    
    def update_performance_baseline(self, test_id: str, metrics: Dict[str, Any]):
        """성능 기준선 업데이트"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 기존 기준선 삭제
                cursor.execute('DELETE FROM performance_baselines WHERE test_id = ?', (test_id,))
                
                # 새로운 기준선 추가
                for metric_name, metric_value in metrics.items():
                    if isinstance(metric_value, dict):
                        value = metric_value['value']
                        confidence_interval_lower = metric_value.get('confidence_interval', [None, None])[0]
                        confidence_interval_upper = metric_value.get('confidence_interval', [None, None])[1]
                    else:
                        value = metric_value
                        confidence_interval_lower = None
                        confidence_interval_upper = None
                    
                    cursor.execute('''
                        INSERT INTO performance_baselines 
                        (test_id, test_name, metric_name, metric_value, 
                         confidence_interval_lower, confidence_interval_upper, created_at)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        test_id,
                        self.get_test_schedule(test_id).test_name if self.get_test_schedule(test_id) else 'Unknown',
                        metric_name,
                        value,
                        confidence_interval_lower,
                        confidence_interval_upper,
                        datetime.now().isoformat()
                    ))
                
                conn.commit()
                logger.info(f"성능 기준선 업데이트 완료: {test_id}")
                
        except Exception as e:
            logger.error(f"성능 기준선 업데이트 오류: {e}")
    
    def generate_test_report(self, output_path: str = "performance_results/test_manager_report.html"):
        """테스트 관리 보고서 생성"""
        try:
            # 테스트 실행 통계
            executions = self.get_test_executions(limit=1000)
            
            if not executions:
                logger.warning("생성할 테스트 데이터가 없습니다")
                return False
            
            # 성공률 계산
            success_count = sum(1 for e in executions if e.status == TestStatus.COMPLETED)
            success_rate = success_count / len(executions) * 100
            
            # 평균 실행 시간 계산
            avg_duration = sum(e.duration or 0 for e in executions) / len(executions)
            
            # 알림 통계
            alerts = self.get_alerts(limit=1000)
            unresolved_alerts = sum(1 for a in alerts if not a.resolved)
            
            # 테스트 타입별 통계
            type_stats = {}
            for execution in executions:
                test_type = execution.test_type
                if test_type not in type_stats:
                    type_stats[test_type] = {'total': 0, 'success': 0}
                
                type_stats[test_type]['total'] += 1
                if execution.status == TestStatus.COMPLETED:
                    type_stats[test_type]['success'] += 1
            
            # HTML 보고서 생성
            html_content = self._generate_html_report({
                'total_executions': len(executions),
                'success_rate': success_rate,
                'avg_duration': avg_duration,
                'total_alerts': len(alerts),
                'unresolved_alerts': unresolved_alerts,
                'type_breakdown': type_stats,
                'generated_at': datetime.now().isoformat()
            })
            
            # 파일 저장
            output_path_obj = Path(output_path)
            output_path_obj.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            logger.info(f"테스트 관리 보고서 생성 완료: {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"테스트 관리 보고서 생성 오류: {e}")
            return False
    
    def _generate_html_report(self, stats: Dict[str, Any]) -> str:
        """HTML 보고서 생성"""
        html_template = f"""
        <!DOCTYPE html>
        <html lang="ko">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>WinForms_Docs 자동화 테스트 관리 보고서</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }}
                .container {{ max-width: 1200px; margin: 0 auto; background-color: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
                h1 {{ color: #333; text-align: center; }}
                h2 {{ color: #666; border-bottom: 2px solid #eee; padding-bottom: 10px; }}
                .summary {{ display: flex; justify-content: space-around; margin: 20px 0; }}
                .metric {{ text-align: center; padding: 15px; background-color: #f8f9fa; border-radius: 8px; }}
                .metric-value {{ font-size: 24px; font-weight: bold; color: #007bff; }}
                .metric-label {{ font-size: 14px; color: #666; }}
                table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
                th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }}
                th {{ background-color: #f8f9fa; font-weight: bold; }}
                .success {{ color: #28a745; }}
                .failure {{ color: #dc3545; }}
                .warning {{ color: #ffc107; }}
                .chart-container {{ margin: 20px 0; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>WinForms_Docs 자동화 테스트 관리 보고서</h1>
                <p>생성 시간: {stats['generated_at']}</p>
                
                <h2>📊 테스트 실행 요약</h2>
                <div class="summary">
                    <div class="metric">
                        <div class="metric-value">{stats['total_executions']}</div>
                        <div class="metric-label">총 실행 횟수</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value { 'success' if stats['success_rate'] > 90 else 'failure' }">{stats['success_rate']:.1f}%</div>
                        <div class="metric-label">성공률</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value">{stats['avg_duration']:.1f}s</div>
                        <div class="metric-label">평균 실행 시간</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value { 'warning' if stats['unresolved_alerts'] > 0 else 'success' }">{stats['unresolved_alerts']}</div>
                        <div class="metric-label">미해결 알림</div>
                    </div>
                </div>
                
                <h2>📈 테스트 타입별 상세 결과</h2>
                <table>
                    <thead>
                        <tr>
                            <th>테스트 타입</th>
                            <th>실행 횟수</th>
                            <th>성공 횟수</th>
                            <th>성공률</th>
                        </tr>
                    </thead>
                    <tbody>
        """
        
        for test_type, type_stat in stats['type_breakdown'].items():
            success_rate = type_stat['success'] / type_stat['total'] * 100
            html_template += f"""
                        <tr>
                            <td>{test_type}</td>
                            <td>{type_stat['total']}</td>
                            <td>{type_stat['success']}</td>
                            <td class="{ 'success' if success_rate > 90 else 'failure' }">{success_rate:.1f}%</td>
                        </tr>
            """
        
        html_template += """
                    </tbody>
                </table>
                
                <h2>🚨 알림 현황</h2>
                <table>
                    <thead>
                        <tr>
                            <th>총 알림 수</th>
                            <th>미해결 알림</th>
                            <th>해결된 알림</th>
                            <th>알림 처리율</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>{stats['total_alerts']}</td>
                            <td class="warning">{stats['unresolved_alerts']}</td>
                            <td class="success">{stats['total_alerts'] - stats['unresolved_alerts']}</td>
                            <td class="success">{((stats['total_alerts'] - stats['unresolved_alerts']) / max(stats['total_alerts'], 1) * 100):.1f}%</td>
                        </tr>
                    </tbody>
                </table>
                
                <h2>🔧 시스템 상태</h2>
                <ul>
                    <li>스케줄러 상태: {'실행 중' if self.scheduler_running else '중지됨'}</li>
                    <li>실행 중인 테스트: {len(self.running_tests)}개</li>
                    <li>활성 알림: {len([a for a in self.alerts if not a.resolved])}개</li>
                    <li>메모리 사용량: {psutil.virtual_memory().percent:.1f}%</li>
                    <li>CPU 사용량: {psutil.cpu_percent():.1f}%</li>
                </ul>
                
                <h2>📋 테스트 관리 기능</h2>
                <ul>
                    <li>주기적인 테스트 실행</li>
                    <li>이벤트 기반 테스트 트리거</li>
                    <li>성능 회귀 자동 감지</li>
                    <li>이메일/Slack 알림 시스템</li>
                    <li>자동 보고서 생성</li>
                    <li>성능 기준선 관리</li>
                </ul>
                
                <h2>🎯 향후 계획</h2>
                <ul>
                    <li>CI/CD 파이프라인 통합</li>
                    <li>더 정밀한 성능 모니터링</li>
                    <li>자동 복구 메커니즘</li>
                    <li>분산 테스트 지원</li>
                    <li>머신러닝 기반 이상 탐지</li>
                </ul>
            </div>
        </body>
        </html>
        """
        
        return html_template
    
    def cleanup_old_data(self):
        """오래된 데이터 정리"""
        try:
            cutoff_date = datetime.now() - timedelta(days=self.config['auto_cleanup_days'])
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 오래된 실행 기록 삭제
                cursor.execute('''
                    DELETE FROM test_executions 
                    WHERE start_time < ?
                ''', (cutoff_date.isoformat(),))
                
                # 오래된 알림 삭제 (해결된 알림만)
                cursor.execute('''
                    DELETE FROM test_alerts 
                    WHERE resolved = 1 AND resolved_at < ?
                ''', (cutoff_date.isoformat(),))
                
                conn.commit()
                
                logger.info(f"오래된 데이터 정리 완료: {cutoff_date.strftime('%Y-%m-%d')} 이전 데이터")
                
        except Exception as e:
            logger.error(f"오래된 데이터 정리 오류: {e}")
    
    def cleanup(self):
        """정리 작업"""
        try:
            # 스케줄러 중지
            self.stop_scheduler()
            
            # 성능 모니터링 중지
            if hasattr(self, 'performance_monitor'):
                self.performance_monitor.stop_monitoring()
            
            logger.info("자동화된 테스트 관리 시스템 정리 완료")
            
        except Exception as e:
            logger.error(f"정리 작업 오류: {e}")

# 유틸리티 함수
def create_test_manager(db_path: str = "performance_results/test_manager.db") -> AutomatedTestManager:
    """자동화된 테스트 관리 시스템 인스턴스 생성"""
    return AutomatedTestManager(db_path)

def setup_default_tests(test_manager: AutomatedTestManager):
    """기본 테스트 설정"""
    try:
        # 단위 테스트 스케줄
        unit_test_schedule = TestSchedule(
            test_id="unit_test_daily",
            test_name="일일 단위 테스트",
            test_type=TestType.UNIT_TEST,
            priority=TestPriority.MEDIUM,
            schedule_time=datetime.now().replace(hour=2, minute=0, second=0, microsecond=0),
            repeat_interval=timedelta(days=1),
            enabled=True,
            max_retries=2,
            timeout_seconds=120,
            config={'data_size_mb': 1.0, 'concurrent_files': 5}
        )
        
        # 통합 테스트 스케줄
        integration_test_schedule = TestSchedule(
            test_id="integration_test_weekly",
            test_name="주간 통합 테스트",
            test_type=TestType.INTEGRATION_TEST,
            priority=TestPriority.HIGH,
            schedule_time=datetime.now().replace(hour=3, minute=0, second=0, microsecond=0),
            repeat_interval=timedelta(weeks=1),
            enabled=True,
            max_retries=2,
            timeout_seconds=600,
            config={'data_size_mb': 50.0, 'concurrent_files': 10}
        )
        
        # 성능 회귀 테스트 스케줄
        regression_test_schedule = TestSchedule(
            test_id="regression_test_daily",
            test_name="일일 성능 회귀 테스트",
            test_type=TestType.REGRESSION_TEST,
            priority=TestPriority.HIGH,
            schedule_time=datetime.now().replace(hour=4, minute=0, second=0, microsecond=0),
            repeat_interval=timedelta(days=1),
            enabled=True,
            max_retries=1,
            timeout_seconds=300,
            config={}
        )
        
        # 벤치마크 테스트 스케줄
        benchmark_test_schedule = TestSchedule(
            test_id="benchmark_test_monthly",
            test_name="월간 벤치마크 테스트",
            test_type=TestType.BENCHMARK_TEST,
            priority=TestPriority.LOW,
            schedule_time=datetime.now().replace(day=1, hour=5, minute=0, second=0, microsecond=0),
            repeat_interval=timedelta(weeks=4),
            enabled=True,
            max_retries=1,
            timeout_seconds=1800,
            config={}
        )
        
        # 테스트 스케줄링
        test_manager.schedule_test(unit_test_schedule)
        test_manager.schedule_test(integration_test_schedule)
        test_manager.schedule_test(regression_test_schedule)
        test_manager.schedule_test(benchmark_test_schedule)
        
        logger.info("기본 테스트 설정 완료")
        
    except Exception as e:
        logger.error(f"기본 테스트 설정 오류: {e}")

def run_automated_test_system():
    """자동화 테스트 시스템 실행"""
    test_manager = create_test_manager()
    
    try:
        # 기본 테스트 설정
        setup_default_tests(test_manager)
        
        # 스케줄러 시작
        test_manager.start_scheduler()
        
        print("자동화 테스트 시스템이 시작되었습니다.")
        print("스케줄된 테스트가 자동으로 실행됩니다.")
        print("Ctrl+C를 눌러 시스템을 중지합니다.")
        
        # 시스템 상태 모니터링
        while True:
            try:
                time.sleep(60)  # 1분마다 상태 확인
                
                # 실행 중인 테스트 상태 출력
                if test_manager.running_tests:
                    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 실행 중인 테스트:")
                    for execution_id, execution in test_manager.running_tests.items():
                        duration = (datetime.now() - execution.start_time).total_seconds()
                        print(f"  - {execution.test_name}: {duration:.1f}s 경과")
                
                # 미해결 알림 확인
                unresolved_alerts = test_manager.get_alerts(resolved=False, limit=5)
                if unresolved_alerts:
                    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 미해결 알림:")
                    for alert in unresolved_alerts:
                        print(f"  - {alert.severity}: {alert.message}")
                
            except KeyboardInterrupt:
                print("\n자동화 테스트 시스템을 중지합니다...")
                break
        
    except Exception as e:
        print(f"자동화 테스트 시스템 오류: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # 정리
        test_manager.cleanup()
        print("자동화 테스트 시스템이 정리되었습니다.")

if __name__ == "__main__":
    run_automated_test_system()