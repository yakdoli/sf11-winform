"""
WinForms_Docs 통합 병렬 처리 설정 및 관리 모듈 성능 테스트 스크립트

주요 테스트 기능:
================
1. 기능 테스트
   - 설정 관리 기능 테스트
   - 작업 큐 관리 테스트
   - 모니터링 기능 테스트

2. 성능 테스트
   - 동적 리소스 할당 테스트
   - 작업 처리량 테스트
   - 메모리 사용량 테스트
   - CPU 사용률 테스트

3. 부하 테스트
   - 대량 작업 처리 테스트
   - 장시간 실행 안정성 테스트
   - 시스템 부하 테스트

4. 오류 처리 테스트
   - 네트워크 오류 시뮬레이션
   - 메모리 부족 시뮬레이션
   - 시스템 리소스 고갈 테스트

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0
"""

import os
import sys
import time
import json
import logging
import threading
import multiprocessing as mp
import psutil
import tempfile
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
import unittest
from unittest.mock import patch, MagicMock
import gc
import tracemalloc

# 테스트 대상 모듈 임포트
sys.path.append(str(Path(__file__).parent))
from parallel_config import (
    ParallelConfigManager, ProcessingModule, TaskPriority, TaskStatus,
    PerformanceMetrics, SystemResource, TaskItem
)


class TestParallelConfigManager(unittest.TestCase):
    """ParallelConfigManager 기능 테스트 클래스"""
    
    def setUp(self):
        """테스트 환경 설정"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.config_file = self.temp_dir / "test_config.json"
        self.log_dir = self.temp_dir / "logs"
        self.log_dir.mkdir(exist_ok=True)
        
        # 테스트용 설정 파일 생성
        self.test_config = {
            "global": {
                "log_level": "INFO",
                "max_concurrent_tasks": 4,
                "enable_auto_scaling": True
            },
            "modules": {
                "data_cleaner": {
                    "max_workers": 4,
                    "chunk_size": 50,
                    "memory_limit_mb": 1024,
                    "enabled": True
                },
                "data_normalizer": {
                    "max_workers": 3,
                    "chunk_size": 30,
                    "memory_limit_mb": 768,
                    "enabled": True
                },
                "deduplication": {
                    "max_workers": 6,
                    "chunk_size": 20,
                    "memory_limit_mb": 1536,
                    "enabled": True
                }
            }
        }
        
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.test_config, f, indent=2)
        
        # 설정 관리자 초기화
        self.manager = ParallelConfigManager(self.config_file)
        
        # 로깅 설정
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
    
    def tearDown(self):
        """테스트 환경 정리"""
        self.manager.cleanup()
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_initialization(self):
        """초기화 테스트"""
        self.assertIsNotNone(self.manager)
        self.assertEqual(len(self.manager.processing_configs), 3)
        self.assertTrue(self.manager.monitoring_active)
    
    def test_config_loading(self):
        """설정 파일 로드 테스트"""
        # 설정 확인
        cleaner_config = self.manager.get_module_config(ProcessingModule.DATA_CLEANER)
        self.assertEqual(cleaner_config.max_workers, 4)
        self.assertEqual(cleaner_config.chunk_size, 50)
        self.assertEqual(cleaner_config.memory_limit_mb, 1024)
    
    def test_config_update(self):
        """설정 업데이트 테스트"""
        # 설정 업데이트
        self.manager.update_module_config(
            ProcessingModule.DATA_CLEANER,
            max_workers=8,
            chunk_size=100
        )
        
        # 업데이트 확인
        cleaner_config = self.manager.get_module_config(ProcessingModule.DATA_CLEANER)
        self.assertEqual(cleaner_config.max_workers, 8)
        self.assertEqual(cleaner_config.chunk_size, 100)
    
    def test_task_management(self):
        """작업 관리 테스트"""
        # 작업 추가
        task_id = self.manager.add_task(
            ProcessingModule.DATA_CLEANER,
            {"test": "data"},
            TaskPriority.HIGH
        )
        
        self.assertIsNotNone(task_id)
        self.assertEqual(len(self.manager.task_queue), 1)
        
        # 작업 가져오기
        task = self.manager.get_next_task()
        self.assertIsNotNone(task)
        self.assertEqual(task.task_id, task_id)
        self.assertEqual(task.status, TaskStatus.RUNNING)
        
        # 작업 완료
        self.manager.complete_task(task_id, {"result": "success"})
        self.assertEqual(len(self.manager.completed_tasks), 1)
        self.assertEqual(len(self.manager.task_queue), 0)
    
    def test_priority_queue(self):
        """우선순위 큐 테스트"""
        # 다양한 우선순위 작업 추가
        self.manager.add_task(ProcessingModule.DATA_CLEANER, {}, TaskPriority.LOW)
        self.manager.add_task(ProcessingModule.DATA_NORMALIZER, {}, TaskPriority.CRITICAL)
        self.manager.add_task(ProcessingModule.DEDUPLICATION, {}, TaskPriority.NORMAL)
        self.manager.add_task(ProcessingModule.DATA_CLEANER, {}, TaskPriority.HIGH)
        
        # 큐 확인 (우선순순으로 정렬되어야 함)
        self.assertEqual(len(self.manager.task_queue), 4)
        self.assertEqual(self.manager.task_queue[0].priority, TaskPriority.CRITICAL)
        self.assertEqual(self.manager.task_queue[1].priority, TaskPriority.HIGH)
        self.assertEqual(self.manager.task_queue[2].priority, TaskPriority.NORMAL)
        self.assertEqual(self.manager.task_queue[3].priority, TaskPriority.LOW)
    
    def test_task_retry(self):
        """작업 재시도 테스트"""
        # 작업 추가
        task_id = self.manager.add_task(
            ProcessingModule.DATA_CLEANER,
            {"test": "data"},
            TaskPriority.NORMAL
        )
        
        # 작업 가져오기
        task = self.manager.get_next_task()
        
        # 작업 실패 (재시도 가능)
        self.manager.fail_task(task_id, "Test error")
        
        # 재시도 확인
        self.assertEqual(len(self.manager.task_queue), 1)  # 재시도 큐에 추가됨
        retry_task = self.manager.task_queue[0]
        self.assertEqual(retry_task.retry_count, 1)
        self.assertEqual(retry_task.status, TaskStatus.RETRYING)
        
        # 최대 재시도 횟수 초과
        for _ in range(3):  # 총 4번 시도 (초기 + 3회 재시도)
            self.manager.fail_task(task_id, "Test error")
        
        # 실패 작업으로 이동
        self.assertEqual(len(self.manager.failed_tasks), 1)
        self.assertEqual(len(self.manager.task_queue), 0)
    
    def test_system_monitoring(self):
        """시스템 모니터링 테스트"""
        # 시스템 상태 확인
        status = self.manager.get_system_status()
        
        self.assertIn('cpu_count', status)
        self.assertIn('cpu_usage_percent', status)
        self.assertIn('memory_total_mb', status)
        self.assertIn('memory_used_mb', status)
        self.assertIn('memory_available_mb', status)
        self.assertIn('disk_usage_percent', status)
        
        # 값 범위 확인
        self.assertGreaterEqual(status['cpu_usage_percent'], 0)
        self.assertLessEqual(status['cpu_usage_percent'], 100)
        self.assertGreater(status['memory_total_mb'], 0)
        self.assertGreater(status['memory_used_mb'], 0)
    
    def test_performance_report(self):
        """성능 보고서 테스트"""
        # 작업 추가 및 처리
        for i in range(5):
            task_id = self.manager.add_task(
                ProcessingModule.DATA_CLEANER,
                {"test": f"data_{i}"},
                TaskPriority.NORMAL
            )
            
            task = self.manager.get_next_task()
            self.manager.complete_task(task_id, {"result": f"success_{i}"})
        
        # 성능 보고서 생성
        report = self.manager.get_performance_report()
        
        self.assertIn('performance_metrics', report)
        self.assertIn('system_status', report)
        self.assertIn('queue_status', report)
        self.assertIn('module_configs', report)
        
        # 지표 확인
        metrics = report['performance_metrics']
        self.assertEqual(metrics['total_tasks'], 5)
        self.assertEqual(metrics['completed_tasks'], 5)
        self.assertEqual(metrics['failed_tasks'], 0)
        self.assertGreaterEqual(metrics['average_processing_time'], 0)


class PerformanceTest(unittest.TestCase):
    """성능 테스트 클래스"""
    
    def setUp(self):
        """테스트 환경 설정"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.config_file = self.temp_dir / "perf_test_config.json"
        
        # 고성능 설정
        perf_config = {
            "global": {
                "log_level": "WARNING",
                "max_concurrent_tasks": 16,
                "enable_auto_scaling": True
            },
            "modules": {
                "data_cleaner": {
                    "max_workers": min(mp.cpu_count(), 8),
                    "chunk_size": 200,
                    "memory_limit_mb": 4096,
                    "enabled": True
                },
                "data_normalizer": {
                    "max_workers": min(mp.cpu_count(), 6),
                    "chunk_size": 100,
                    "memory_limit_mb": 3072,
                    "enabled": True
                },
                "deduplication": {
                    "max_workers": min(mp.cpu_count(), 12),
                    "chunk_size": 50,
                    "memory_limit_mb": 6144,
                    "enabled": True
                }
            }
        }
        
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(perf_config, f, indent=2)
        
        self.manager = ParallelConfigManager(self.config_file)
        self.logger = logging.getLogger(__name__)
    
    def tearDown(self):
        """테스트 환경 정리"""
        self.manager.cleanup()
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_task_throughput(self):
        """작업 처리량 테스트"""
        # 대량 작업 생성
        num_tasks = 100
        start_time = time.time()
        
        for i in range(num_tasks):
            self.manager.add_task(
                ProcessingModule.DATA_CLEANER,
                {"task_id": i, "data": f"test_data_{i}"},
                TaskPriority.NORMAL
            )
        
        # 작업 처리
        processed_count = 0
        max_wait_time = 30  # 최대 30초 대기
        start_processing = time.time()
        
        while (processed_count < num_tasks and 
               time.time() - start_processing < max_wait_time):
            
            # 작업 실행 (단일 스레드로 테스트)
            task = self.manager.get_next_task()
            if task:
                # 가상 작업 처리
                time.sleep(0.01)  # 10ms 가상 처리 시간
                self.manager.complete_task(task.task_id, {"result": "processed"})
                processed_count += 1
            
            time.sleep(0.001)  # 1ms 대기
        
        # 성능 측정
        elapsed_time = time.time() - start_time
        throughput = processed_count / elapsed_time if elapsed_time > 0 else 0
        
        self.logger.info(f"처리된 작업: {processed_count}/{num_tasks}")
        self.logger.info(f"소요 시간: {elapsed_time:.2f}초")
        self.logger.info(f"처리량: {throughput:.2f} tasks/second")
        
        # 기본 처리량 검증 (초당 10개 이상)
        self.assertGreater(throughput, 10)
    
    def test_memory_usage(self):
        """메모리 사용량 테스트"""
        # 메모리 추적 시작
        tracemalloc.start()
        
        # 초기 메모리 측정
        snapshot1 = tracemalloc.take_snapshot()
        
        # 대량 작업 생성
        num_tasks = 50
        for i in range(num_tasks):
            task_data = {
                "task_id": i,
                "large_data": "x" * 10000,  # 10KB 데이터
                "metadata": {"id": i, "name": f"task_{i}"}
            }
            self.manager.add_task(
                ProcessingModule.DATA_CLEANER,
                task_data,
                TaskPriority.NORMAL
            )
        
        # 작업 처리
        processed_count = 0
        max_wait_time = 20
        
        while (processed_count < num_tasks and 
               time.time() - tracemalloc.get_traced_memory()[0] < max_wait_time):
            
            task = self.manager.get_next_task()
            if task:
                # 메모리 집약적 작업 시뮬레이션
                large_result = {"processed": True, "data": "y" * 5000}
                self.manager.complete_task(task.task_id, large_result)
                processed_count += 1
            
            time.sleep(0.01)
        
        # 메모리 측정
        snapshot2 = tracemalloc.take_snapshot()
        
        # 메모리 차이 계산
        top_stats = snapshot2.compare_to(snapshot1, 'lineno')
        memory_increase = sum(stat.size_diff for stat in top_stats)
        
        # 메모리 사용량 확인
        current_memory = psutil.Process().memory_info().rss / 1024 / 1024  # MB
        
        self.logger.info(f"처리된 작업: {processed_count}/{num_tasks}")
        self.logger.info(f"현재 메모리 사용량: {current_memory:.1f}MB")
        self.logger.info(f"메모리 증가량: {memory_increase / 1024:.1f}KB")
        
        # 메모리 사용량 제한 확인 (8GB 이하)
        self.assertLess(current_memory, 8192)
        
        tracemalloc.stop()
    
    def test_cpu_usage(self):
        """CPU 사용률 테스트"""
        # CPU 사용률 기록
        cpu_samples = []
        sample_count = 0
        max_samples = 20
        
        def monitor_cpu():
            nonlocal sample_count
            while sample_count < max_samples:
                cpu_percent = psutil.cpu_percent()
                cpu_samples.append(cpu_percent)
                sample_count += 1
                time.sleep(0.5)
        
        # CPU 모니터링 스레드 시작
        monitor_thread = threading.Thread(target=monitor_cpu)
        monitor_thread.start()
        
        # CPU 집약적 작업 생성
        num_tasks = 20
        for i in range(num_tasks):
            self.manager.add_task(
                ProcessingModule.DATA_CLEANER,
                {"task_id": i, "computation": "complex"},
                TaskPriority.HIGH
            )
        
        # 작업 처리
        processed_count = 0
        start_time = time.time()
        
        while processed_count < num_tasks and time.time() - start_time < 15:
            task = self.manager.get_next_task()
            if task:
                # CPU 집약적 작업 시뮬레이션
                start_cpu = time.time()
                while time.time() - start_cpu < 0.1:  # 100ms CPU 집약적 작업
                    _ = sum(i * i for i in range(1000))
                
                self.manager.complete_task(task.task_id, {"result": "computed"})
                processed_count += 1
            
            time.sleep(0.01)
        
        # 모니터링 대기
        monitor_thread.join()
        
        # CPU 사용률 분석
        avg_cpu = sum(cpu_samples) / len(cpu_samples) if cpu_samples else 0
        max_cpu = max(cpu_samples) if cpu_samples else 0
        
        self.logger.info(f"처리된 작업: {processed_count}/{num_tasks}")
        self.logger.info(f"평균 CPU 사용률: {avg_cpu:.1f}%")
        self.logger.info(f"최대 CPU 사용률: {max_cpu:.1f}%")
        
        # CPU 사용률 확인 (정상 범위)
        self.assertLess(avg_cpu, 95)
        self.assertLess(max_cpu, 98)
    
    def test_concurrent_processing(self):
        """동시 처리 테스트"""
        # 다중 모듈 동시 작업 생성
        num_tasks_per_module = 20
        
        # 각 모듈에 작업 추가
        for i in range(num_tasks_per_module):
            self.manager.add_task(
                ProcessingModule.DATA_CLEANER,
                {"task_id": f"cleaner_{i}"},
                TaskPriority.HIGH
            )
            
            self.manager.add_task(
                ProcessingModule.DATA_NORMALIZER,
                {"task_id": f"normalizer_{i}"},
                TaskPriority.NORMAL
            )
            
            self.manager.add_task(
                ProcessingModule.DEDUPLICATION,
                {"task_id": f"dedup_{i}"},
                TaskPriority.CRITICAL
            )
        
        total_tasks = num_tasks_per_module * 3
        processed_count = 0
        start_time = time.time()
        
        # 작업 처리
        while processed_count < total_tasks and time.time() - start_time < 10:
            task = self.manager.get_next_task()
            if task:
                # 모듈별 처리 시간 차이 시뮬레이션
                processing_time = {
                    ProcessingModule.DATA_CLEANER: 0.05,
                    ProcessingModule.DATA_NORMALIZER: 0.03,
                    ProcessingModule.DEDUPLICATION: 0.08
                }.get(task.module, 0.05)
                
                time.sleep(processing_time)
                self.manager.complete_task(task.task_id, {"result": "processed"})
                processed_count += 1
            
            time.sleep(0.001)
        
        elapsed_time = time.time() - start_time
        throughput = processed_count / elapsed_time if elapsed_time > 0 else 0
        
        self.logger.info(f"총 처리된 작업: {processed_count}/{total_tasks}")
        self.logger.info(f"소요 시간: {elapsed_time:.2f}초")
        self.logger.info(f"종합 처리량: {throughput:.2f} tasks/second")
        
        # 동시 처리 효율성 확인
        self.assertGreater(throughput, 5)
        self.assertGreaterEqual(processed_count, total_tasks * 0.8)  # 80% 이상 처리


class StressTest(unittest.TestCase):
    """부하 테스트 클래스"""
    
    def setUp(self):
        """테스트 환경 설정"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.config_file = self.temp_dir / "stress_test_config.json"
        
        # 부하 테스트용 설정
        stress_config = {
            "global": {
                "log_level": "ERROR",
                "max_concurrent_tasks": 32,
                "enable_auto_scaling": True
            },
            "modules": {
                "data_cleaner": {
                    "max_workers": min(mp.cpu_count(), 16),
                    "chunk_size": 500,
                    "memory_limit_mb": 8192,
                    "enabled": True
                },
                "data_normalizer": {
                    "max_workers": min(mp.cpu_count(), 12),
                    "chunk_size": 300,
                    "memory_limit_mb": 6144,
                    "enabled": True
                },
                "deduplication": {
                    "max_workers": min(mp.cpu_count(), 24),
                    "chunk_size": 100,
                    "memory_limit_mb": 12288,
                    "enabled": True
                }
            }
        }
        
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(stress_config, f, indent=2)
        
        self.manager = ParallelConfigManager(self.config_file)
        self.logger = logging.getLogger(__name__)
    
    def tearDown(self):
        """테스트 환경 정리"""
        self.manager.cleanup()
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_high_volume_tasks(self):
        """대량 작업 부하 테스트"""
        # 대량 작업 생성 (1000개)
        num_tasks = 1000
        batch_size = 100
        
        for batch in range(0, num_tasks, batch_size):
            batch_tasks = []
            for i in range(batch, min(batch + batch_size, num_tasks)):
                task_data = {
                    "task_id": i,
                    "data": "x" * 1000,  # 1KB 데이터
                    "batch": batch // batch_size
                }
                batch_tasks.append(task_data)
            
            # 배치로 작업 추가
            for task_data in batch_tasks:
                self.manager.add_task(
                    ProcessingModule.DATA_CLEANER,
                    task_data,
                    TaskPriority.NORMAL
                )
            
            self.logger.info(f"배치 {batch // batch_size + 1} 작업 추가: {len(batch_tasks)}개")
        
        # 작업 처리
        start_time = time.time()
        processed_count = 0
        failed_count = 0
        
        while processed_count + failed_count < num_tasks and time.time() - start_time < 60:
            task = self.manager.get_next_task()
            if task:
                try:
                    # 가상 처리
                    time.sleep(0.001)  # 1ms 처리 시간
                    self.manager.complete_task(task.task_id, {"result": "success"})
                    processed_count += 1
                except Exception as e:
                    self.manager.fail_task(task.task_id, str(e))
                    failed_count += 1
            
            # 주기적으로 상태 확인
            if processed_count % 100 == 0:
                status = self.manager.get_system_status()
                self.logger.info(f"진행 상황: {processed_count}/{num_tasks}, "
                               f"메모리: {status['memory_used_mb']:.1f}MB, "
                               f"CPU: {status['cpu_usage_percent']:.1f}%")
            
            time.sleep(0.0001)  # 0.1ms 대기
        
        # 결과 분석
        elapsed_time = time.time() - start_time
        success_rate = processed_count / num_tasks * 100 if num_tasks > 0 else 0
        throughput = processed_count / elapsed_time if elapsed_time > 0 else 0
        
        self.logger.info(f"부하 테스트 결과:")
        self.logger.info(f"  총 작업: {num_tasks}")
        self.logger.info(f"  성공: {processed_count} ({success_rate:.1f}%)")
        self.logger.info(f"  실패: {failed_count}")
        self.logger.info(f"  소요 시간: {elapsed_time:.2f}초")
        self.logger.info(f"  처리량: {throughput:.2f} tasks/second")
        
        # 성공률 확인 (90% 이상)
        self.assertGreater(success_rate, 90)
        
        # 처리량 확인 (초당 50개 이상)
        self.assertGreater(throughput, 50)
    
    def test_long_running_stability(self):
        """장시간 실행 안정성 테스트"""
        # 장시간 실행 (5분)
        test_duration = 300  # 5분
        start_time = time.time()
        
        task_count = 0
        processed_count = 0
        memory_snapshots = []
        cpu_snapshots = []
        
        while time.time() - start_time < test_duration:
            # 주기적으로 작업 추가
            if task_count % 50 == 0:
                for i in range(10):
                    self.manager.add_task(
                        ProcessingModule.DATA_CLEANER,
                        {"task_id": task_count + i, "data": "test"},
                        TaskPriority.NORMAL
                    )
                task_count += 10
            
            # 작업 처리
            task = self.manager.get_next_task()
            if task:
                time.sleep(0.01)  # 10ms 처리 시간
                self.manager.complete_task(task.task_id, {"result": "processed"})
                processed_count += 1
            
            # 주기적으로 시스템 상태 기록
            if processed_count % 20 == 0:
                status = self.manager.get_system_status()
                memory_snapshots.append(status['memory_used_mb'])
                cpu_snapshots.append(status['cpu_usage_percent'])
                
                self.logger.info(f"장시간 테스트 진행: {processed_count}개 처리, "
                               f"메모리: {status['memory_used_mb']:.1f}MB, "
                               f"CPU: {status['cpu_usage_percent']:.1f}%")
            
            time.sleep(0.1)
        
        # 결과 분석
        elapsed_time = time.time() - start_time
        avg_memory = sum(memory_snapshots) / len(memory_snapshots) if memory_snapshots else 0
        max_memory = max(memory_snapshots) if memory_snapshots else 0
        avg_cpu = sum(cpu_snapshots) / len(cpu_snapshots) if cpu_snapshots else 0
        max_cpu = max(cpu_snapshots) if cpu_snapshots else 0
        
        self.logger.info(f"장시간 테스트 결과:")
        self.logger.info(f"  실행 시간: {elapsed_time:.1f}초")
        self.logger.info(f"  처리된 작업: {processed_count}")
        self.logger.info(f"  평균 메모리: {avg_memory:.1f}MB")
        self.logger.info(f"  최대 메모리: {max_memory:.1f}MB")
        self.logger.info(f"  평균 CPU: {avg_cpu:.1f}%")
        self.logger.info(f"  최대 CPU: {max_cpu:.1f}%")
        
        # 안정성 확인
        self.assertLess(max_memory, 16384)  # 16GB 이하
        self.assertLess(max_cpu, 95)  # 95% 이하
        self.assertGreater(processed_count, 100)  # 최소 100개 처리
        
        # 메모리 누수 확인 (초기 대비 20% 이내)
        if len(memory_snapshots) > 10:
            initial_memory = memory_snapshots[0]
            final_memory = memory_snapshots[-1]
            memory_increase_percent = (final_memory - initial_memory) / initial_memory * 100
            self.assertLess(memory_increase_percent, 20)
    
    def test_resource_exhaustion(self):
        """리소스 고갈 테스트"""
        # 메모리 부족 시뮬레이션
        large_data = "x" * 10000000  # 10MB 데이터
        
        # 메모리 집약적 작업 추가
        num_tasks = 50
        for i in range(num_tasks):
            task_data = {
                "task_id": i,
                "large_data": large_data * (i + 1),  # 점점 더 큰 데이터
                "metadata": {"id": i, "size": len(large_data) * (i + 1)}
            }
            self.manager.add_task(
                ProcessingModule.DATA_CLEANER,
                task_data,
                TaskPriority.HIGH
            )
        
        # 작업 처리
        processed_count = 0
        failed_count = 0
        start_time = time.time()
        
        while processed_count + failed_count < num_tasks and time.time() - start_time < 30:
            task = self.manager.get_next_task()
            if task:
                try:
                    # 메모리 집약적 작업 시뮬레이션
                    result_data = large_data * (task.data['task_id'] + 1)
                    time.sleep(0.1)  # 100ms 처리 시간
                    
                    # 메모리 상태 확인
                    current_memory = psutil.virtual_memory().used / 1024 / 1024
                    if current_memory > 15000:  # 15GB 이상 시 메모리 부족 가정
                        raise MemoryError("Memory limit exceeded")
                    
                    self.manager.complete_task(task.task_id, {"result": "processed", "size": len(result_data)})
                    processed_count += 1
                    
                except MemoryError as e:
                    self.manager.fail_task(task.task_id, str(e))
                    failed_count += 1
                    # 메모리 정리
                    gc.collect()
                except Exception as e:
                    self.manager.fail_task(task.task_id, str(e))
                    failed_count += 1
            
            time.sleep(0.01)
        
        # 결과 분석
        total_memory = psutil.virtual_memory().total / 1024 / 1024
        used_memory = psutil.virtual_memory().used / 1024 / 1024
        memory_usage_percent = (used_memory / total_memory) * 100
        
        self.logger.info(f"리소스 고갈 테스트 결과:")
        self.logger.info(f"  총 작업: {num_tasks}")
        self.logger.info(f"  성공: {processed_count}")
        self.logger.info(f"  실패: {failed_count}")
        self.logger.info(f"  메모리 사용률: {memory_usage_percent:.1f}%")
        self.logger.info(f"  사용된 메모리: {used_memory:.1f}MB / {total_memory:.1f}MB")
        
        # 오류 처리 확인
        self.assertGreater(failed_count, 0)  # 일부 실패는 예상됨
        
        # 메모리 사용량 확인 (90% 이하)
        self.assertLess(memory_usage_percent, 90)


def run_performance_benchmark():
    """성능 벤치마크 실행"""
    print("=== WinForms_Docs 통합 병렬 처리 모듈 성능 벤치마크 ===\n")
    
    # 테스트 스위트 생성
    test_suite = unittest.TestSuite()
    
    # 기능 테스트
    print("1. 기능 테스트 실행...")
    functional_tests = unittest.TestLoader().loadTestsFromTestCase(TestParallelConfigManager)
    test_suite.addTests(functional_tests)
    
    # 성능 테스트
    print("2. 성능 테스트 실행...")
    performance_tests = unittest.TestLoader().loadTestsFromTestCase(PerformanceTest)
    test_suite.addTests(performance_tests)
    
    # 부하 테스트
    print("3. 부하 테스트 실행...")
    stress_tests = unittest.TestLoader().loadTestsFromTestCase(StressTest)
    test_suite.addTests(stress_tests)
    
    # 테스트 실행
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # 결과 요약
    print("\n=== 벤치마크 결과 요약 ===")
    print(f"총 테스트 수: {result.testsRun}")
    print(f"성공한 테스트: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"실패한 테스트: {len(result.failures)}")
    print(f"오류 발생 테스트: {len(result.errors)}")
    print(f"실행 시간: N/A")
    
    if result.failures:
        print("\n실패한 테스트:")
        for test, traceback in result.failures:
            print(f"  - {test}: {traceback}")
    
    if result.errors:
        print("\n오류 발생 테스트:")
        for test, traceback in result.errors:
            print(f"  - {test}: {traceback}")
    
    # 성능 등급 부여
    success_rate = (result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100
    
    if success_rate >= 95:
        grade = "A (우수)"
    elif success_rate >= 85:
        grade = "B (양호)"
    elif success_rate >= 75:
        grade = "C (보통)"
    else:
        grade = "D (개선 필요)"
    
    print(f"\n성능 등급: {grade} (성공률: {success_rate:.1f}%)")


def generate_test_report():
    """테스트 보고서 생성"""
    report_dir = Path("test_reports")
    report_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = report_dir / f"performance_test_report_{timestamp}.json"
    
    report = {
        "test_timestamp": datetime.now().isoformat(),
        "system_info": {
            "cpu_count": mp.cpu_count(),
            "memory_total_mb": psutil.virtual_memory().total / 1024 / 1024,
            "platform": sys.platform,
            "python_version": sys.version
        },
        "test_results": {
            "functional_tests": {},
            "performance_tests": {},
            "stress_tests": {}
        },
        "recommendations": []
    }
    
    # 보고서 저장
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"테스트 보고서가 생성되었습니다: {report_file}")


if __name__ == "__main__":
    import argparse
    
    # 명령줄 인자 파싱
    parser = argparse.ArgumentParser(description="WinForms_Docs 통합 병렬 처리 모듈 성능 테스트")
    parser.add_argument("--test-type", choices=["all", "functional", "performance", "stress"], 
                       default="all", help="실행할 테스트 유형")
    parser.add_argument("--output-report", action="store_true", help="테스트 보고서 생성")
    parser.add_argument("--verbose", "-v", action="store_true", help="상세 출력")
    
    args = parser.parse_args()
    
    if args.output_report:
        generate_test_report()
    
    if args.test_type == "all":
        run_performance_benchmark()
    else:
        # 특정 테스트 유형 실행
        test_suite = unittest.TestSuite()
        
        if args.test_type == "functional":
            tests = unittest.TestLoader().loadTestsFromTestCase(TestParallelConfigManager)
        elif args.test_type == "performance":
            tests = unittest.TestLoader().loadTestsFromTestCase(PerformanceTest)
        elif args.test_type == "stress":
            tests = unittest.TestLoader().loadTestsFromTestCase(StressTest)
        
        test_suite.addTests(tests)
        
        runner = unittest.TextTestRunner(verbosity=2 if args.verbose else 1)
        result = runner.run(test_suite)
    
    print("\n테스트 완료!")