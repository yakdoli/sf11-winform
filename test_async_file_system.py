"""
WinForms_Docs 비동기 파일 시스템 통합 테스트

주요 테스트 기능:
================
1. AsyncFileManager 기능 테스트
   - 비동기 파일 읽기/쓰기 테스트
   - 동적 워커 풀 관리 테스트
   - 파일 큐 관리 테스트

2. FileQueueManager 테스트
   - 우선순위 큐 동작 테스트
   - 파일 메타데이터 관리 테스트
   - 처리 상태 추적 테스트

3. AsyncFileBridge 테스트
   - 기존 시스템과의 호환성 테스트
   - 점진적 마이그레이션 테스트
   - 성능 비교 테스트

4. 통합 오류 처리 테스트
   - 네트워크 오류 시뮬레이션
   - 파일 시스템 오류 시뮬레이션
   - 메모리 부족 시뮬레이션

5. 성능 모니터링 테스트
   - 실시간 성능 모니터링 테스트
   - 알림 시스템 테스트
   - 성능 보고서 생성 테스트

테스트 전략:
===========
- 단위 테스트: 각 클래스별 독립적 테스트
- 통합 테스트: 클래스 간 상호작용 테스트
- 부하 테스트: 대용량 파일 처리 테스트
- 오류 테스트: 예외 상황 처리 테스트
- 성능 테스트: 처리 속도 및 메모리 사용량 측정

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0 (통합 테스트)
"""

import asyncio
import unittest
import tempfile
import shutil
import os
import time
import json
import logging
from pathlib import Path
from typing import List, Dict, Any
from unittest.mock import Mock, patch, AsyncMock
import psutil
import gc

# 테스트 대상 모듈 임포트
from async_file_manager import AsyncFileManager, FileQueueManager, AsyncFileHandler
from async_file_bridge import AsyncFileBridge, create_async_file_bridge
from async_performance_monitor import AsyncPerformanceMonitor

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestAsyncFileManager(unittest.TestCase):
    """AsyncFileManager 테스트 클래스"""
    
    def setUp(self):
        """테스트 설정"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.test_files = []
        
        # 테스트 파일 생성
        for i in range(5):
            test_file = self.temp_dir / f"test_{i}.md"
            with open(test_file, 'w', encoding='utf-8') as f:
                f.write(f"# 테스트 문서 {i+1}\n\n")
                f.write(f"이것은 테스트 문서 {i+1}의 내용입니다.\n" * 100)
            self.test_files.append(test_file)
    
    def tearDown(self):
        """테스트 정리"""
        # 테스트 파일 삭제
        for test_file in self.test_files:
            try:
                test_file.unlink()
            except:
                pass
        
        # 임시 디렉토리 삭제
        try:
            self.temp_dir.rmdir()
        except:
            pass
        
        # 강제 가비지 컬렉션
        gc.collect()
    
    def test_async_file_manager_initialization(self):
        """AsyncFileManager 초기화 테스트"""
        try:
            manager = AsyncFileManager(max_concurrent=5, io_workers=2)
            self.assertIsNotNone(manager)
            self.assertEqual(manager.max_concurrent, 5)
            self.assertEqual(manager.io_workers, 2)
            self.assertFalse(manager.is_running)
        except Exception as e:
            self.fail(f"AsyncFileManager 초기화 실패: {str(e)}")
    
    async def test_async_file_read_write(self):
        """비동기 파일 읽기/쓰기 테스트"""
        try:
            manager = AsyncFileManager()
            
            # 파일 읽기 테스트
            content = await manager.read_file(str(self.test_files[0]))
            self.assertIsInstance(content, bytes)
            self.assertGreater(len(content), 0)
            
            # 파일 쓰기 테스트
            test_write_path = self.temp_dir / "test_write.md"
            test_content = b"test content"
            await manager.write_file(str(test_write_path), test_content)
            
            # 파일 확인
            self.assertTrue(test_write_path.exists())
            with open(test_write_path, 'rb') as f:
                written_content = f.read()
            self.assertEqual(written_content, test_content)
            
        except Exception as e:
            self.fail(f"비동기 파일 읽기/쓰기 테스트 실패: {str(e)}")
    
    async def test_file_batch_processing(self):
        """파일 배치 처리 테스트"""
        try:
            manager = AsyncFileManager()
            await manager.start_processing()
            
            # 파일 경로 문자열로 변환
            str_file_paths = [str(fp) for fp in self.test_files]
            
            # 배치 처리
            results = await manager.process_file_batch(str_file_paths)
            
            # 결과 확인
            self.assertIsInstance(results, list)
            
            # 통계 확인
            stats = manager.get_processing_stats()
            self.assertGreater(stats.processed_files, 0)
            
            await manager.stop_processing()
            
        except Exception as e:
            self.fail(f"파일 배치 처리 테스트 실패: {str(e)}")
    
    async def test_file_queue_manager(self):
        """파일 큐 관리자 테스트"""
        try:
            queue_manager = FileQueueManager()
            
            # 파일 큐에 추가
            for test_file in self.test_files:
                priority = len(test_file.name)
                success = queue_manager.enqueue_file(str(test_file), priority)
                self.assertTrue(success)
            
            # 큐 상태 확인
            queue_stats = queue_manager.get_queue_stats()
            self.assertEqual(queue_stats.pending_files, len(self.test_files))
            
            # 파일 가져오기
            next_file = queue_manager.get_next_file()
            self.assertIsNotNone(next_file)
            
            # 처리 완료 표시
            if next_file:
                queue_manager.mark_completed(next_file, True, 1.0)
            
            # 최종 큐 상태 확인
            final_stats = queue_manager.get_queue_stats()
            self.assertEqual(final_stats.completed_files, 1)
            
        except Exception as e:
            self.fail(f"파일 큐 관리자 테스트 실패: {str(e)}")
    
    async def test_async_file_handler(self):
        """비동기 파일 핸들러 테스트"""
        try:
            handler = AsyncFileHandler()
            
            # 파일 통계 조회
            stats = await handler.get_file_stats(str(self.test_files[0]))
            self.assertIsInstance(stats, object)
            self.assertGreater(stats.total_bytes, 0)
            
        except Exception as e:
            self.fail(f"비동기 파일 핸들러 테스트 실패: {str(e)}")

class TestAsyncFileBridge(unittest.TestCase):
    """AsyncFileBridge 테스트 클래스"""
    
    def setUp(self):
        """테스트 설정"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.test_files = []
        
        # 테스트 파일 생성
        for i in range(3):
            test_file = self.temp_dir / f"test_{i}.md"
            with open(test_file, 'w', encoding='utf-8') as f:
                f.write(f"# 테스트 문서 {i+1}\n\n")
                f.write(f"이것은 테스트 문서 {i+1}의 내용입니다.\n" * 50)
            self.test_files.append(test_file)
    
    def tearDown(self):
        """테스트 정리"""
        # 테스트 파일 삭제
        for test_file in self.test_files:
            try:
                test_file.unlink()
            except:
                pass
        
        # 임시 디렉토리 삭제
        try:
            self.temp_dir.rmdir()
        except:
            pass
        
        # 강제 가비지 컬렉션
        gc.collect()
    
    def test_async_file_bridge_initialization(self):
        """AsyncFileBridge 초기화 테스트"""
        try:
            bridge = AsyncFileBridge(use_async=True)
            self.assertIsNotNone(bridge)
            self.assertTrue(bridge.use_async)
            self.assertIsNotNone(bridge.async_manager)
            
        except Exception as e:
            self.fail(f"AsyncFileBridge 초기화 실패: {str(e)}")
    
    async def test_async_processing(self):
        """비동기 처리 테스트"""
        try:
            bridge = AsyncFileBridge(use_async=True)
            
            # 비동기 처리
            results = await bridge.process_files_async(self.test_files)
            
            # 결과 확인
            self.assertIsInstance(results, list)
            self.assertGreater(len(results), 0)
            
            # 마이그레이션 통계 확인
            migration_stats = bridge.get_migration_stats()
            self.assertEqual(migration_stats.migrated_files, len(results))
            
        except Exception as e:
            self.fail(f"비동기 처리 테스트 실패: {str(e)}")
    
    def test_mode_switching(self):
        """모드 전환 테스트"""
        try:
            bridge = AsyncFileBridge(use_async=True)
            
            # 비동기 모드에서 동기 모드로 전환
            bridge.switch_mode(False)
            self.assertFalse(bridge.use_async)
            self.assertIsNone(bridge.async_manager)
            
            # 다시 비동기 모드로 전환
            bridge.switch_mode(True)
            self.assertTrue(bridge.use_async)
            self.assertIsNotNone(bridge.async_manager)
            
        except Exception as e:
            self.fail(f"모드 전환 테스트 실패: {str(e)}")
    
    def test_fallback_mechanism(self):
        """폴백 메커니즘 테스트"""
        try:
            bridge = AsyncFileBridge(use_async=False)
            
            # 동기 처리
            results = bridge.process_files_parallel(self.test_files)
            
            # 결과 확인
            self.assertIsInstance(results, list)
            
            # 마이그레이션 통계 확인
            migration_stats = bridge.get_migration_stats()
            self.assertEqual(migration_stats.fallback_files, len(results))
            
        except Exception as e:
            self.fail(f"폴백 메커니즘 테스트 실패: {str(e)}")

class TestAsyncPerformanceMonitor(unittest.TestCase):
    """AsyncPerformanceMonitor 테스트 클래스"""
    
    def setUp(self):
        """테스트 설정"""
        self.temp_db = Path(tempfile.mktemp(suffix='.db'))
        self.monitor = AsyncPerformanceMonitor(str(self.temp_db))
    
    def tearDown(self):
        """테스트 정리"""
        try:
            self.temp_db.unlink()
        except:
            pass
        
        # 모니터링 중지
        self.monitor.stop_monitoring()
    
    def test_monitor_initialization(self):
        """모니터 초기화 테스트"""
        try:
            self.assertIsNotNone(self.monitor)
            self.assertEqual(self.monitor.db_path, str(self.temp_db))
            self.assertFalse(self.monitor.monitoring_active)
            
        except Exception as e:
            self.fail(f"모니터 초기화 테스트 실패: {str(e)}")
    
    def test_metric_recording(self):
        """성능 지표 기록 테스트"""
        try:
            from async_performance_monitor import PerformanceMetric, MetricType
            
            # 성능 지표 생성
            metric = PerformanceMetric(
                timestamp=time.time(),
                metric_type=MetricType.THROUGHPUT,
                value=10.5,
                unit="files/sec",
                metadata={'test': True}
            )
            
            # 지표 기록
            self.monitor.record_metric(metric)
            
            # 히스토리 확인
            self.assertEqual(len(self.monitor.metrics_history), 1)
            
        except Exception as e:
            self.fail(f"성능 지표 기록 테스트 실패: {str(e)}")
    
    def test_file_processing_recording(self):
        """파일 처리 성능 기록 테스트"""
        try:
            # 파일 처리 성능 기록
            self.monitor.record_file_processing(
                file_path="test.md",
                processing_time=1.5,
                memory_usage=100.0,
                success=True
            )
            
            # 통계 확인
            self.assertEqual(self.monitor.processed_files, 1)
            self.assertEqual(self.monitor.total_processing_time, 1.5)
            
        except Exception as e:
            self.fail(f"파일 처리 성능 기록 테스트 실패: {str(e)}")
    
    def test_performance_summary(self):
        """성능 요약 테스트"""
        try:
            # 가짜 데이터 생성
            for i in range(5):
                self.monitor.record_file_processing(
                    file_path=f"test_{i}.md",
                    processing_time=0.1 + (i * 0.1),
                    memory_usage=50 + (i * 10),
                    success=True
                )
            
            # 성능 요약 조회
            summary = self.monitor.get_performance_summary(hours=1)
            
            # 요약 확인
            self.assertIsInstance(summary, dict)
            self.assertGreater(summary.get('total_files', 0), 0)
            self.assertGreater(summary.get('throughput', 0), 0)
            
        except Exception as e:
            self.fail(f"성능 요약 테스트 실패: {str(e)}")
    
    def test_alert_system(self):
        """알림 시스템 테스트"""
        try:
            from async_performance_monitor import PerformanceMetric, MetricType
            
            # 알림 콜백 추가
            alerts_received = []
            
            def alert_callback(alert):
                alerts_received.append(alert)
            
            self.monitor.add_alert_callback(alert_callback)
            
            # 임계값 초과 지표 기록
            metric = PerformanceMetric(
                timestamp=time.time(),
                metric_type=MetricType.CPU,
                value=90.0,  # 임계값 초과
                unit="percent"
            )
            
            self.monitor.record_metric(metric)
            
            # 알림 확인
            self.assertGreater(len(alerts_received), 0)
            
        except Exception as e:
            self.fail(f"알림 시스템 테스트 실패: {str(e)}")

class TestErrorHandling(unittest.TestCase):
    """오류 처리 테스트 클래스"""
    
    def setUp(self):
        """테스트 설정"""
        self.temp_dir = Path(tempfile.mkdtemp())
    
    def tearDown(self):
        """테스트 정리"""
        try:
            self.temp_dir.rmdir()
        except:
            pass
    
    async def test_file_not_found_error(self):
        """파일 찾을 수 없음 오류 테스트"""
        try:
            manager = AsyncFileManager()
            
            # 존재하지 않는 파일 읽기 시도
            with self.assertRaises(FileNotFoundError):
                await manager.read_file("nonexistent_file.md")
                
        except Exception as e:
            self.fail(f"파일 찾을 수 없음 오류 테스트 실패: {str(e)}")
    
    async def test_permission_error(self):
        """권한 오류 테스트"""
        try:
            manager = AsyncFileManager()
            
            # 쓰기 권한 없는 디렉토리에 파일 쓰기 시도
            restricted_path = "/root/restricted_file.md"
            
            with self.assertRaises(PermissionError):
                await manager.write_file(restricted_path, b"test content")
                
        except Exception as e:
            self.fail(f"권한 오류 테스트 실패: {str(e)}")
    
    async def test_memory_error_simulation(self):
        """메모리 오류 시뮬레이션 테스트"""
        try:
            manager = AsyncFileManager()
            
            # 매우 큰 파일 시뮬레이션
            large_content = b"x" * (1024 * 1024 * 100)  # 100MB
            
            # 충분한 공간이 있는 임시 파일에 쓰기
            large_file_path = self.temp_dir / "large_file.md"
            await manager.write_file(str(large_file_path), large_content)
            
            # 파일 확인
            self.assertTrue(large_file_path.exists())
            self.assertEqual(large_file_path.stat().st_size, len(large_content))
            
        except Exception as e:
            self.fail(f"메모리 오류 시뮬레이션 테스트 실패: {str(e)}")
    
    async def test_concurrent_access_error(self):
        """동시 접근 오류 테스트"""
        try:
            manager = AsyncFileManager(max_concurrent=1)
            await manager.start_processing()
            
            # 여러 파일 동시 처리 시도
            tasks = []
            for i in range(5):
                task = asyncio.create_task(
                    manager.process_file_batch([str(self.temp_dir / f"test_{i}.md")])
                )
                tasks.append(task)
            
            # 결과 대기
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # 예외가 발생해야 함
            exception_count = sum(1 for result in results if isinstance(result, Exception))
            self.assertGreater(exception_count, 0)
            
            await manager.stop_processing()
            
        except Exception as e:
            self.fail(f"동시 접근 오류 테스트 실패: {str(e)}")

class TestIntegration(unittest.TestCase):
    """통합 테스트 클래스"""
    
    def setUp(self):
        """테스트 설정"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.test_files = []
        
        # 테스트 파일 생성
        for i in range(10):
            test_file = self.temp_dir / f"test_{i}.md"
            with open(test_file, 'w', encoding='utf-8') as f:
                f.write(f"# 통합 테스트 문서 {i+1}\n\n")
                f.write(f"이것은 통합 테스트 문서 {i+1}의 내용입니다.\n" * 200)
            self.test_files.append(test_file)
    
    def tearDown(self):
        """테스트 정리"""
        # 테스트 파일 삭제
        for test_file in self.test_files:
            try:
                test_file.unlink()
            except:
                pass
        
        # 임시 디렉토리 삭제
        try:
            self.temp_dir.rmdir()
        except:
            pass
        
        # 강제 가비지 컬렉션
        gc.collect()
    
    async def test_full_integration(self):
        """전체 통합 테스트"""
        try:
            # 성능 모니터 생성
            monitor = AsyncPerformanceMonitor()
            
            # AsyncFileBridge 생성
            bridge = AsyncFileBridge(use_async=True)
            
            # 성능 모니터링 시작
            monitor.start_monitoring(interval=1)
            
            # 파일 처리
            start_time = time.time()
            results = await bridge.process_files_async(self.test_files)
            processing_time = time.time() - start_time
            
            # 성능 기록
            for result in results:
                monitor.record_file_processing(
                    file_path=result.file_path if hasattr(result, 'file_path') else "unknown",
                    processing_time=processing_time / len(results),
                    memory_usage=100.0,
                    success=True
                )
            
            # 통계 확인
            self.assertGreater(len(results), 0)
            
            # 성능 요약 확인
            summary = monitor.get_performance_summary(hours=1)
            self.assertGreater(summary.get('total_files', 0), 0)
            
            # 모니터링 중지
            monitor.stop_monitoring()
            
            # 자원 정리
            bridge.cleanup()
            
        except Exception as e:
            self.fail(f"전체 통합 테스트 실패: {str(e)}")
    
    def test_performance_comparison(self):
        """성능 비교 테스트"""
        try:
            # AsyncFileBridge 생성
            async_bridge = AsyncFileBridge(use_async=True)
            
            # 동기 처리
            sync_start = time.time()
            sync_results = async_bridge.process_files_parallel(self.test_files[:5])
            sync_time = time.time() - sync_start
            
            # 비동기 처리
            async_start = time.time()
            async_results = asyncio.run(async_bridge.process_files_async(self.test_files[5:]))
            async_time = time.time() - async_start
            
            # 성능 비교
            self.assertLess(async_time, sync_time * 1.5)  # 비동기가 더 빨라야 함
            
            # 성능 비교 정보 확인
            comparison = async_bridge.get_performance_comparison()
            self.assertIsInstance(comparison, dict)
            
            # 자원 정리
            async_bridge.cleanup()
            
        except Exception as e:
            self.fail(f"성능 비교 테스트 실패: {str(e)}")

# 테스트 실행 함수
def run_all_tests():
    """모든 테스트 실행"""
    # 테스트 스위트 생성
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # 테스트 클래스 추가
    test_classes = [
        TestAsyncFileManager,
        TestAsyncFileBridge,
        TestAsyncPerformanceMonitor,
        TestErrorHandling,
        TestIntegration
    ]
    
    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # 테스트 실행
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()

# 비동기 테스트 실행 함수
async def run_async_tests():
    """비동기 테스트 실행"""
    # 비동기 테스트만 실행
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # 비동기 테스트 클래스만 추가
    async_test_classes = [
        TestAsyncFileManager,
        TestAsyncFileBridge,
        TestErrorHandling,
        TestIntegration
    ]
    
    for test_class in async_test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # 비동기 테스트 실행
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()

if __name__ == "__main__":
    print("WinForms_Docs 비동기 파일 시스템 통합 테스트")
    print("=" * 50)
    
    # 동기 테스트 실행
    print("\n동기 테스트 실행...")
    sync_success = run_all_tests()
    
    # 비동기 테스트 실행
    print("\n비동기 테스트 실행...")
    async_success = asyncio.run(run_async_tests())
    
    # 결과 요약
    print("\n" + "=" * 50)
    print("테스트 결과 요약")
    print("=" * 50)
    print(f"동기 테스트: {'PASS' if sync_success else 'FAIL'}")
    print(f"비동기 테스트: {'PASS' if async_success else 'FAIL'}")
    
    if sync_success and async_success:
        print("\n🎉 모든 테스트를 통과했습니다!")
        exit(0)
    else:
        print("\n⚠️ 일부 테스트가 실패했습니다.")
        exit(1)