"""
WinForms_Docs 성능 테스트 스크립트

주요 기능:
============
1. 자동화 성능 테스트 프레임워크
   - 단위 테스트, 통합 테스트, 부하 테스트
   - 다양한 데이터 크기 테스트 (소규모, 중규모, 대규모)
   - 병렬 처리 성능 벤치마킹
   - 메모리 사용량 및 CPU 사용률 모니터링

2. 테스트 실행
   - data_cleaner.py 모듈 테스트
   - data_normalizer.py 모듈 테스트
   - deduplication.py 모듈 테스트
   - parallel_config.py 모듈 테스트

3. 테스트 결과 분석
   - 성능 지표 수집 및 저장
   - 테스트 결과 비교 분석
   - 성능 개선 효과 측정

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0
"""

import os
import sys
import time
import json
import logging
import psutil
import multiprocessing as mp
import tempfile
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple, Callable
from dataclasses import dataclass, asdict
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import traceback
import gc
import statistics

# 로컬 모듈 임포트
sys.path.append('.')
from performance_monitor import PerformanceMonitor, PerformanceMetrics, TestResult, PerformanceDatabase
from data_cleaner import DataCleaner
from data_normalizer import DataNormalizer
from deduplication import Deduplicator
from parallel_config import ParallelConfigManager, ProcessingModule

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class TestConfig:
    """테스트 설정 데이터 클래스"""
    test_name: str
    test_type: str  # 'unit', 'integration', 'load'
    data_size: str  # 'small', 'medium', 'large'
    module_name: str
    iterations: int = 1
    timeout_seconds: int = 300
    expected_success_rate: float = 0.95
    memory_limit_mb: int = 2048
    cpu_limit_percent: int = 80

class PerformanceTestSuite:
    """성능 테스트 스위트 클래스"""
    
    def __init__(self, db_path: str = "performance_test_results.db"):
        self.db = PerformanceDatabase(db_path)
        self.monitor = PerformanceMonitor(db_path)
        self.test_results: List[TestResult] = []
        self.test_configs: List[TestConfig] = []
        
        # 테스트 데이터 생성을 위한 임시 디렉토리
        self.temp_dir = Path(tempfile.mkdtemp(prefix="performance_test_"))
        
        # 테스트 설정 초기화
        self._init_test_configs()
        
    def _init_test_configs(self):
        """테스트 설정 초기화"""
        self.test_configs = [
            # 단위 테스트
            TestConfig("data_cleaner_small", "unit", "small", "data_cleaner", 5, 60, 0.95, 512, 70),
            TestConfig("data_normalizer_small", "unit", "small", "data_normalizer", 5, 60, 0.95, 512, 70),
            TestConfig("deduplication_small", "unit", "small", "deduplication", 5, 60, 0.95, 512, 70),
            
            # 통합 테스트
            TestConfig("data_cleaner_medium", "integration", "medium", "data_cleaner", 3, 180, 0.90, 1024, 80),
            TestConfig("data_normalizer_medium", "integration", "medium", "data_normalizer", 3, 180, 0.90, 1024, 80),
            TestConfig("deduplication_medium", "integration", "medium", "deduplication", 3, 180, 0.90, 1024, 80),
            
            # 부하 테스트
            TestConfig("data_cleaner_large", "load", "large", "data_cleaner", 1, 600, 0.85, 2048, 90),
            TestConfig("data_normalizer_large", "load", "large", "data_normalizer", 1, 600, 0.85, 2048, 90),
            TestConfig("deduplication_large", "load", "large", "deduplication", 1, 600, 0.85, 2048, 90),
            
            # 병렬 처리 테스트
            TestConfig("parallel_processing", "integration", "medium", "parallel_config", 3, 300, 0.90, 1536, 85),
        ]
    
    def create_test_data(self, data_size: str) -> List[Path]:
        """테스트 데이터 생성"""
        test_files = []
        
        if data_size == "small":
            # 소규모 테스트 데이터: 10개 파일, 각 1KB
            num_files = 10
            file_size = 1024
            
        elif data_size == "medium":
            # 중규모 테스트 데이터: 50개 파일, 각 10KB
            num_files = 50
            file_size = 10 * 1024
            
        elif data_size == "large":
            # 대규모 테스트 데이터: 200개 파일, 각 50KB
            num_files = 200
            file_size = 50 * 1024
        
        # 테스트 파일 생성
        for i in range(num_files):
            file_path = self.temp_dir / f"test_file_{i:03d}.md"
            
            # 간단한 마크다운 콘텐츠 생성
            content = f"""# 테스트 문서 {i+1}

## 소개
이것은 성능 테스트를 위한 가짜 문서입니다.

## 코드 예시
```python
def test_function():
    print("Hello, World!")
    return True
```

## 데이터
- 항목 1: 데이터 1
- 항목 2: 데이터 2
- 항목 3: 데이터 3

## 결론
이 문서는 성능 테스트 목적으로 생성되었습니다.
"""
            
            # 파일 크기 조정
            if len(content.encode('utf-8')) < file_size:
                content += "\n" + "추가 내용 " * ((file_size - len(content.encode('utf-8'))) // 10)
            elif len(content.encode('utf-8')) > file_size:
                content = content[:file_size]
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            test_files.append(file_path)
        
        logger.info(f"테스트 데이터 생성 완료: {data_size} - {len(test_files)}개 파일")
        return test_files
    
    def run_test_suite(self) -> Dict[str, Any]:
        """전체 테스트 스위트 실행"""
        logger.info("성능 테스트 스위트 시작")
        
        # 모니터링 시작
        self.monitor.start_monitoring()
        
        try:
            # 각 테스트 설정 실행
            for config in self.test_configs:
                logger.info(f"테스트 실행: {config.test_name}")
                result = self.run_single_test(config)
                self.test_results.append(result)
                self.db.save_test_result(result)
                
                # 테스트 간 정리
                gc.collect()
                time.sleep(2)
            
            # 테스트 결과 요약
            summary = self.generate_test_summary()
            
            logger.info("성능 테스트 스위트 완료")
            return summary
            
        finally:
            # 모니터링 중지
            self.monitor.stop_monitoring()
            # 임시 디렉토리 정리
            shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def run_single_test(self, config: TestConfig) -> TestResult:
        """단일 테스트 실행"""
        start_time = time.time()
        memory_before = psutil.Process().memory_info().rss / 1024 / 1024
        cpu_before = psutil.cpu_percent()
        
        success = False
        error_message = None
        details = {}
        
        try:
            # 테스트 데이터 생성
            test_files = self.create_test_data(config.data_size)
            
            # 모듈별 테스트 실행
            if config.module_name == "data_cleaner":
                result = self.test_data_cleaner(test_files, config)
            elif config.module_name == "data_normalizer":
                result = self.test_data_normalizer(test_files, config)
            elif config.module_name == "deduplication":
                result = self.test_deduplication(test_files, config)
            elif config.module_name == "parallel_config":
                result = self.test_parallel_config(test_files, config)
            else:
                raise ValueError(f"알 수 없는 모듈: {config.module_name}")
            
            success = result.get('success', False)
            error_message = result.get('error_message')
            details = result.get('details', {})
            
        except Exception as e:
            success = False
            error_message = str(e)
            details['error_traceback'] = traceback.format_exc()
        
        finally:
            # 리소스 측정
            memory_after = psutil.Process().memory_info().rss / 1024 / 1024
            cpu_after = psutil.cpu_percent()
            execution_time = time.time() - start_time
            
            # 메모리 정리
            gc.collect()
        
        return TestResult(
            test_name=config.test_name,
            test_type=config.test_type,
            data_size=config.data_size,
            execution_time=execution_time,
            memory_usage_mb=memory_after - memory_before,
            cpu_usage_percent=cpu_after - cpu_before,
            success=success,
            error_message=error_message,
            details=details
        )
    
    def test_data_cleaner(self, test_files: List[Path], config: TestConfig) -> Dict[str, Any]:
        """데이터 정제 모듈 테스트"""
        results = []
        
        for i in range(config.iterations):
            try:
                cleaner = DataCleaner()
                
                start_time = time.time()
                processed_files = cleaner.process_files(test_files)
                processing_time = time.time() - start_time
                
                # 결과 분석
                success_count = len([f for f in processed_files if f is not None])
                total_count = len(test_files)
                success_rate = success_count / total_count if total_count > 0 else 0
                
                results.append({
                    'iteration': i + 1,
                    'processing_time': processing_time,
                    'success_count': success_count,
                    'total_count': total_count,
                    'success_rate': success_rate,
                    'memory_usage_mb': cleaner.stats.peak_memory_usage,
                    'files_processed': cleaner.stats.processed_files
                })
                
                logger.info(f"데이터 정제 테스트 반복 {i+1}: {success_count}/{total_count} 파일 성공")
                
            except Exception as e:
                logger.error(f"데이터 정제 테스트 오류 (반복 {i+1}): {str(e)}")
                results.append({
                    'iteration': i + 1,
                    'error': str(e)
                })
        
        # 전체 결과 요약
        if results:
            successful_results = [r for r in results if 'error' not in r]
            if successful_results:
                avg_processing_time = statistics.mean(r['processing_time'] for r in successful_results)
                avg_success_rate = statistics.mean(r['success_rate'] for r in successful_results)
                avg_memory_usage = statistics.mean(r['memory_usage_mb'] for r in successful_results)
                
                return {
                    'success': avg_success_rate >= config.expected_success_rate,
                    'error_message': None if avg_success_rate >= config.expected_success_rate else f"성공률 낮음: {avg_success_rate:.2%}",
                    'details': {
                        'iterations': results,
                        'avg_processing_time': avg_processing_time,
                        'avg_success_rate': avg_success_rate,
                        'avg_memory_usage_mb': avg_memory_usage,
                        'total_files_processed': sum(r['success_count'] for r in successful_results)
                    }
                }
        
        return {
            'success': False,
            'error_message': '유효한 테스트 결과 없음',
            'details': {'results': results}
        }
    
    def test_data_normalizer(self, test_files: List[Path], config: TestConfig) -> Dict[str, Any]:
        """데이터 정규화 모듈 테스트"""
        results = []
        
        for i in range(config.iterations):
            try:
                normalizer = DataNormalizer()
                
                start_time = time.time()
                normalized_docs = normalizer.process_documents(test_files)
                processing_time = time.time() - start_time
                
                # 결과 분석
                success_count = len([d for d in normalized_docs if d is not None])
                total_count = len(test_files)
                success_rate = success_count / total_count if total_count > 0 else 0
                
                results.append({
                    'iteration': i + 1,
                    'processing_time': processing_time,
                    'success_count': success_count,
                    'total_count': total_count,
                    'success_rate': success_rate,
                    'memory_usage_mb': normalizer.stats.peak_memory_usage,
                    'documents_processed': normalizer.stats.processed_documents
                })
                
                logger.info(f"데이터 정규화 테스트 반복 {i+1}: {success_count}/{total_count} 문서 성공")
                
            except Exception as e:
                logger.error(f"데이터 정규화 테스트 오류 (반복 {i+1}): {str(e)}")
                results.append({
                    'iteration': i + 1,
                    'error': str(e)
                })
        
        # 전체 결과 요약
        if results:
            successful_results = [r for r in results if 'error' not in r]
            if successful_results:
                avg_processing_time = statistics.mean(r['processing_time'] for r in successful_results)
                avg_success_rate = statistics.mean(r['success_rate'] for r in successful_results)
                avg_memory_usage = statistics.mean(r['memory_usage_mb'] for r in successful_results)
                
                return {
                    'success': avg_success_rate >= config.expected_success_rate,
                    'error_message': None if avg_success_rate >= config.expected_success_rate else f"성공률 낮음: {avg_success_rate:.2%}",
                    'details': {
                        'iterations': results,
                        'avg_processing_time': avg_processing_time,
                        'avg_success_rate': avg_success_rate,
                        'avg_memory_usage_mb': avg_memory_usage,
                        'total_documents_processed': sum(r['success_count'] for r in successful_results)
                    }
                }
        
        return {
            'success': False,
            'error_message': '유효한 테스트 결과 없음',
            'details': {'results': results}
        }
    
    def test_deduplication(self, test_files: List[Path], config: TestConfig) -> Dict[str, Any]:
        """중복 제거 모듈 테스트"""
        results = []
        
        for i in range(config.iterations):
            try:
                # 중복 파일 생성을 위한 복사
                duplicate_files = test_files[:len(test_files)//2]  # 절반 복사
                all_files = test_files + duplicate_files
                
                deduplicator = Deduplicator()
                
                start_time = time.time()
                deduplicated_files = deduplicator.remove_duplicates(all_files)
                processing_time = time.time() - start_time
                
                # 결과 분석
                success_count = len([f for f in deduplicated_files if f is not None])
                total_count = len(all_files)
                success_rate = success_count / total_count if total_count > 0 else 0
                
                results.append({
                    'iteration': i + 1,
                    'processing_time': processing_time,
                    'success_count': success_count,
                    'total_count': total_count,
                    'success_rate': success_rate,
                    'memory_usage_mb': getattr(deduplicator, 'peak_memory', 0),
                    'files_processed': success_count
                })
                
                logger.info(f"중복 제거 테스트 반복 {i+1}: {success_count}/{total_count} 파일 성공")
                
            except Exception as e:
                logger.error(f"중복 제거 테스트 오류 (반복 {i+1}): {str(e)}")
                results.append({
                    'iteration': i + 1,
                    'error': str(e)
                })
        
        # 전체 결과 요약
        if results:
            successful_results = [r for r in results if 'error' not in r]
            if successful_results:
                avg_processing_time = statistics.mean(r['processing_time'] for r in successful_results)
                avg_success_rate = statistics.mean(r['success_rate'] for r in successful_results)
                avg_memory_usage = statistics.mean(r['memory_usage_mb'] for r in successful_results)
                
                return {
                    'success': avg_success_rate >= config.expected_success_rate,
                    'error_message': None if avg_success_rate >= config.expected_success_rate else f"성공률 낮음: {avg_success_rate:.2%}",
                    'details': {
                        'iterations': results,
                        'avg_processing_time': avg_processing_time,
                        'avg_success_rate': avg_success_rate,
                        'avg_memory_usage_mb': avg_memory_usage,
                        'total_files_processed': sum(r['success_count'] for r in successful_results)
                    }
                }
        
        return {
            'success': False,
            'error_message': '유효한 테스트 결과 없음',
            'details': {'results': results}
        }
    
    def test_parallel_config(self, test_files: List[Path], config: TestConfig) -> Dict[str, Any]:
        """병렬 설정 모듈 테스트"""
        results = []
        
        for i in range(config.iterations):
            try:
                config_manager = ParallelConfigManager()
                
                start_time = time.time()
                
                # 작업 추가 및 실행
                task_ids = []
                for file_path in test_files[:10]:  # 테스트를 위해 10개 파일만 사용
                    task_id = config_manager.add_task(
                        ProcessingModule.DATA_CLEANER,
                        str(file_path),
                        priority=None
                    )
                    task_ids.append(task_id)
                
                # 작업 실행
                config_manager.execute_tasks(max_concurrent_tasks=4)
                
                processing_time = time.time() - start_time
                
                # 결과 분석
                completed_tasks = len([task_id for task_id in task_ids 
                                     if task_id in [task.task_id for task in config_manager.completed_tasks]])
                total_count = len(task_ids)
                success_rate = completed_tasks / total_count if total_count > 0 else 0
                
                results.append({
                    'iteration': i + 1,
                    'processing_time': processing_time,
                    'success_count': completed_tasks,
                    'total_count': total_count,
                    'success_rate': success_rate,
                    'memory_usage_mb': getattr(config_manager, 'peak_memory_usage_mb', 0),
                    'tasks_completed': completed_tasks
                })
                
                logger.info(f"병렬 설정 테스트 반복 {i+1}: {completed_tasks}/{total_count} 작업 성공")
                
                # 정리
                config_manager.cleanup()
                
            except Exception as e:
                logger.error(f"병렬 설정 테스트 오류 (반복 {i+1}): {str(e)}")
                results.append({
                    'iteration': i + 1,
                    'error': str(e)
                })
        
        # 전체 결과 요약
        if results:
            successful_results = [r for r in results if 'error' not in r]
            if successful_results:
                avg_processing_time = statistics.mean(r['processing_time'] for r in successful_results)
                avg_success_rate = statistics.mean(r['success_rate'] for r in successful_results)
                avg_memory_usage = statistics.mean(r['memory_usage_mb'] for r in successful_results)
                
                return {
                    'success': avg_success_rate >= config.expected_success_rate,
                    'error_message': None if avg_success_rate >= config.expected_success_rate else f"성공률 낮음: {avg_success_rate:.2%}",
                    'details': {
                        'iterations': results,
                        'avg_processing_time': avg_processing_time,
                        'avg_success_rate': avg_success_rate,
                        'avg_memory_usage_mb': avg_memory_usage,
                        'total_tasks_completed': sum(r['success_count'] for r in successful_results)
                    }
                }
        
        return {
            'success': False,
            'error_message': '유효한 테스트 결과 없음',
            'details': {'results': results}
        }
    
    def generate_test_summary(self) -> Dict[str, Any]:
        """테스트 결과 요약 생성"""
        if not self.test_results:
            return {'error': '테스트 결과 없음'}
        
        # 성공률 계산
        successful_tests = [r for r in self.test_results if r.success]
        success_rate = len(successful_tests) / len(self.test_results)
        
        # 평균 실행 시간
        avg_execution_time = statistics.mean(r.execution_time for r in self.test_results)
        
        # 평균 메모리 사용량
        avg_memory_usage = statistics.mean(r.memory_usage_mb for r in self.test_results)
        
        # 평균 CPU 사용량
        avg_cpu_usage = statistics.mean(r.cpu_usage_percent for r in self.test_results)
        
        # 모듈별 성능 분석
        module_performance = {}
        for result in self.test_results:
            module_name = result.test_name.split('_')[0]
            if module_name not in module_performance:
                module_performance[module_name] = []
            module_performance[module_name].append(result)
        
        summary = {
            'total_tests': len(self.test_results),
            'successful_tests': len(successful_tests),
            'success_rate': success_rate,
            'avg_execution_time': avg_execution_time,
            'avg_memory_usage_mb': avg_memory_usage,
            'avg_cpu_usage_percent': avg_cpu_usage,
            'test_results': [r.to_dict() for r in self.test_results],
            'module_performance': {
                module: {
                    'avg_execution_time': statistics.mean(r.execution_time for r in results),
                    'avg_memory_usage_mb': statistics.mean(r.memory_usage_mb for r in results),
                    'avg_cpu_usage_percent': statistics.mean(r.cpu_usage_percent for r in results),
                    'success_rate': len([r for r in results if r.success]) / len(results)
                }
                for module, results in module_performance.items()
            },
            'timestamp': datetime.now().isoformat()
        }
        
        return summary
    
    def save_test_report(self, summary: Dict[str, Any], output_path: str = "performance_test_report.json"):
        """테스트 보고서 저장"""
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2, ensure_ascii=False)
            logger.info(f"테스트 보고서 저장 완료: {output_path}")
        except Exception as e:
            logger.error(f"테스트 보고서 저장 오류: {str(e)}")

def main():
    """메인 실행 함수"""
    logger.info("WinForms_Docs 성능 테스트 시작")
    
    try:
        # 테스트 스위트 생성
        test_suite = PerformanceTestSuite()
        
        # 테스트 실행
        summary = test_suite.run_test_suite()
        
        # 보고서 저장
        test_suite.save_test_report(summary)
        
        # 결과 출력
        print("\n" + "="*50)
        print("성능 테스트 결과 요약")
        print("="*50)
        print(f"총 테스트 수: {summary['total_tests']}")
        print(f"성공한 테스트 수: {summary['successful_tests']}")
        print(f"성공률: {summary['success_rate']:.2%}")
        print(f"평균 실행 시간: {summary['avg_execution_time']:.2f}초")
        print(f"평균 메모리 사용량: {summary['avg_memory_usage_mb']:.2f}MB")
        print(f"평균 CPU 사용량: {summary['avg_cpu_usage_percent']:.2f}%")
        
        print("\n모듈별 성능:")
        for module, perf in summary['module_performance'].items():
            print(f"  {module}:")
            print(f"    평균 실행 시간: {perf['avg_execution_time']:.2f}초")
            print(f"    평균 메모리 사용량: {perf['avg_memory_usage_mb']:.2f}MB")
            print(f"    평균 CPU 사용량: {perf['avg_cpu_usage_percent']:.2f}%")
            print(f"    성공률: {perf['success_rate']:.2%}")
        
        print(f"\n상세 결과: performance_test_report.json")
        
        return summary
        
    except Exception as e:
        logger.error(f"성능 테스트 실행 오류: {str(e)}")
        logger.error(traceback.format_exc())
        return None

if __name__ == "__main__":
    main()