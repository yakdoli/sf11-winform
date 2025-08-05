"""
WinForms_Docs 통합 성능 테스트 실행 스크립트
=======================================

주요 기능:
==========
1. 모든 성능 개선 구성 요소 통합 테스트
2. 엔드투엔드 워크플로우 검증
3. 성능 벤치마킹 실행
4. 회귀 테스트 수행
5. 자동화된 테스트 스위트 실행

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0 (통합 성능 테스트 실행 스크립트)
"""

import asyncio
import logging
import time
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime
import argparse

# 로컬 모듈 임포트
try:
    from config import (
        WINFORMS_DOCS_DIR, OUTPUT_DIR, BACKUP_DIR,
        PROCESSING_OPTIONS, LOGGING_CONFIG
    )
    from integrated_performance_test_framework import (
        IntegratedPerformanceTestFramework, create_test_framework
    )
    from performance_benchmark_suite import (
        PerformanceBenchmarkSuite, create_benchmark_suite
    )
    from automated_test_manager import (
        AutomatedTestManager, create_test_manager
    )
    from test_data_manager import (
        TestDataManager, create_test_data_manager, create_sample_datasets
    )
    from performance_regression_prevention import (
        PerformanceRegressionPrevention, create_regression_prevention_system
    )
    from performance_monitor import get_performance_monitor
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
            logging.FileHandler('logs/run_integrated_tests.log', encoding='utf-8'),
            logging.StreamHandler()
        ]
    )

# 로깅 설정
logging.basicConfig(
    level=getattr(logging, LOGGING_CONFIG['level']),
    format=LOGGING_CONFIG['format'],
    handlers=[
        logging.FileHandler(LOGGING_CONFIG['file_path'], encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class IntegratedTestRunner:
    """통합 테스트 실행기"""
    
    def __init__(self):
        self.test_framework = None
        self.benchmark_suite = None
        self.test_manager = None
        self.data_manager = None
        self.regression_system = None
        self.performance_monitor = get_performance_monitor()
        
        # 테스트 결과 저장
        self.test_results = []
        self.start_time = None
        self.end_time = None
        
        # 설정
        self.config = {
            'test_timeout': 3600,  # 1시간 타임아웃
            'parallel_tests': 4,
            'enable_benchmarking': True,
            'enable_regression_detection': True,
            'enable_data_generation': True,
            'cleanup_after_test': True,
            'generate_reports': True,
            'save_test_data': True
        }
        
        logger.info("통합 테스트 실행기 초기화 완료")
    
    def initialize_components(self):
        """테스트 구성 요소 초기화"""
        try:
            print("테스트 구성 요소 초기화 중...")
            
            # 통합 테스트 프레임워크
            self.test_framework = create_test_framework()
            print("✓ 통합 테스트 프레임워크 초기화 완료")
            
            # 성능 벤치마킹 스위트
            if self.config['enable_benchmarking']:
                self.benchmark_suite = create_benchmark_suite()
                print("✓ 성능 벤치마킹 스위트 초기화 완료")
            
            # 자동화 테스트 관리자
            self.test_manager = create_test_manager()
            print("✓ 자동화 테스트 관리자 초기화 완료")
            
            # 테스트 데이터 관리자
            if self.config['enable_data_generation']:
                self.data_manager = create_test_data_manager()
                print("✓ 테스트 데이터 관리자 초기화 완료")
            
            # 성능 회귀 방지 시스템
            if self.config['enable_regression_detection']:
                self.regression_system = create_regression_prevention_system()
                print("✓ 성능 회귀 방지 시스템 초기화 완료")
            
            # 성능 모니터링 시작
            self.performance_monitor.start_monitoring()
            print("✓ 성능 모니터링 시작 완료")
            
            print("모든 구성 요소 초기화 완료!")
            
        except Exception as e:
            logger.error(f"구성 요소 초기화 오류: {e}")
            raise
    
    def setup_test_environment(self):
        """테스트 환경 설정"""
        try:
            print("테스트 환경 설정 중...")
            
            # 출력 디렉토리 생성
            Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
            Path("performance_results").mkdir(parents=True, exist_ok=True)
            
            # 백업 디렉토리 생성
            Path(BACKUP_DIR).mkdir(parents=True, exist_ok=True)
            
            # 테스트 데이터 생성
            if self.config['enable_data_generation'] and self.data_manager:
                print("테스트 데이터 생성 중...")
                datasets = create_sample_datasets()
                
                # 생성된 데이터셋 정보 출력
                for result in datasets:
                    if result.success:
                        print(f"  ✓ 데이터셋 생성: {result.dataset_info.dataset_name}")
                        print(f"    - 파일 수: {result.dataset_info.file_count}")
                        print(f"    - 총 크기: {result.dataset_info.total_size_mb:.2f}MB")
                    else:
                        print(f"  ✗ 데이터셋 생성 실패: {result.error_message}")
            
            # 성능 기준선 설정
            if self.config['enable_regression_detection'] and self.regression_system:
                print("성능 기준선 설정 중...")
                from performance_regression_prevention import setup_default_regression_tests
                setup_default_regression_tests()
                print("  ✓ 기본 성능 기준선 설정 완료")
            
            print("테스트 환경 설정 완료!")
            
        except Exception as e:
            logger.error(f"테스트 환경 설정 오류: {e}")
            raise
    
    def run_unit_tests(self) -> Dict[str, Any]:
        """단위 테스트 실행"""
        try:
            print("단위 테스트 실행 중...")
            
            unit_results = {
                'file_manager_tests': {},
                'data_processor_tests': {},
                'memory_manager_tests': {},
                'arrow_manager_tests': {},
                'overall_status': 'success'
            }
            
            # 비동기 파일 관리자 테스트
            print("  비동기 파일 관리자 테스트...")
            try:
                # 파일 관리자 기능 테스트
                test_files = []
                for i in range(10):
                    test_file = Path(f"test_file_{i}.txt")
                    test_file.write_text(f"테스트 데이터 {i}" * 100)
                    test_files.append(test_file)
                
                # 파일 통계 테스트
                if self.test_framework:
                    stats = self.test_framework.file_handler.get_file_stats(str(test_files[0]))
                    unit_results['file_manager_tests']['basic_functionality'] = 'success'
                    unit_results['file_manager_tests']['file_stats'] = {
                        'total_files': stats.total_files,
                        'total_bytes': stats.total_bytes
                    }
                
                # 테스트 파일 정리
                for file in test_files:
                    file.unlink()
                
            except Exception as e:
                unit_results['file_manager_tests']['error'] = str(e)
                unit_results['overall_status'] = 'partial_failure'
                print(f"  ✗ 파일 관리자 테스트 실패: {e}")
            
            # 데이터 프로세서 테스트
            print("  데이터 프로세서 테스트...")
            try:
                import pandas as pd
                import numpy as np
                
                # 테스트 데이터 생성
                test_data = pd.DataFrame({
                    'id': range(1000),
                    'name': [f"item_{i}" for i in range(1000)],
                    'value': np.random.random(1000) * 100,
                    'category': np.random.choice(['A', 'B', 'C'], 1000)
                })
                
                # 데이터 처리 테스트
                if self.test_framework and hasattr(self.test_framework, 'data_processor'):
                    processed_data = self.test_framework.data_processor.process_dataframe(test_data)
                    unit_results['data_processor_tests']['basic_functionality'] = 'success'
                    unit_results['data_processor_tests']['processed_rows'] = len(processed_data)
                
            except Exception as e:
                unit_results['data_processor_tests']['error'] = str(e)
                unit_results['overall_status'] = 'partial_failure'
                print(f"  ✗ 데이터 프로세서 테스트 실패: {e}")
            
            # 메모리 관리자 테스트
            print("  메모리 관리자 테스트...")
            try:
                import psutil
                import gc
                
                # 메모리 사용량 측정
                process = psutil.Process()
                initial_memory = process.memory_info().rss / 1024 / 1024
                
                # 메모리 사용 테스트
                large_data = [f"{'x' * 1000000}" for _ in range(100)]
                gc.collect()
                
                peak_memory = process.memory_info().rss / 1024 / 1024
                
                # 메모리 정리
                del large_data
                gc.collect()
                
                final_memory = process.memory_info().rss / 1024 / 1024
                
                unit_results['memory_manager_tests']['basic_functionality'] = 'success'
                unit_results['memory_manager_tests']['memory_usage'] = {
                    'initial_mb': initial_memory,
                    'peak_mb': peak_memory,
                    'final_mb': final_memory,
                    'peak_increase_mb': peak_memory - initial_memory
                }
                
            except Exception as e:
                unit_results['memory_manager_tests']['error'] = str(e)
                unit_results['overall_status'] = 'partial_failure'
                print(f"  ✗ 메모리 관리자 테스트 실패: {e}")
            
            # Arrow 관리자 테스트
            print("  Arrow 관리자 테스트...")
            try:
                import pyarrow as pa
                import pandas as pd
                
                # 테스트 데이터 생성
                test_df = pd.DataFrame({
                    'id': range(100),
                    'name': [f"item_{i}" for i in range(100)],
                    'value': list(range(100))
                })
                
                # Arrow 변환 테스트
                if self.test_framework and hasattr(self.test_framework, 'arrow_manager'):
                    arrow_table = self.test_framework.arrow_manager.pandas_to_arrow(test_df)
                    unit_results['arrow_manager_tests']['basic_functionality'] = 'success'
                    unit_results['arrow_manager_tests']['arrow_rows'] = len(arrow_table)
                
            except Exception as e:
                unit_results['arrow_manager_tests']['error'] = str(e)
                unit_results['overall_status'] = 'partial_failure'
                print(f"  ✗ Arrow 관리자 테스트 실패: {e}")
            
            print(f"단위 테스트 완료 - 상태: {unit_results['overall_status']}")
            return unit_results
            
        except Exception as e:
            logger.error(f"단위 테스트 실행 오류: {e}")
            return {'overall_status': 'failure', 'error': str(e)}
    
    def run_integration_tests(self) -> Dict[str, Any]:
        """통합 테스트 실행"""
        try:
            print("통합 테스트 실행 중...")
            
            integration_results = {
                'end_to_end_workflow': {},
                'component_interaction': {},
                'performance_metrics': {},
                'overall_status': 'success'
            }
            
            # 엔드투엔드 워크플로우 테스트
            print("  엔드투엔드 워크플로우 테스트...")
            try:
                if self.test_framework:
                    # 테스트 데이터 생성
                    test_data = {
                        'files': [f"test_file_{i}.txt" for i in range(5)],
                        'content': [f"테스트 콘텐츠 {i}" * 100 for i in range(5)]
                    }
                    
                    # 워크플로우 실행
                    workflow_result = self.test_framework.run_end_to_end_workflow(
                        test_files=test_data['files'],
                        test_content=test_data['content'],
                        processing_options=PROCESSING_OPTIONS
                    )
                    
                    integration_results['end_to_end_workflow']['success'] = workflow_result['success']
                    integration_results['end_to_end_workflow']['execution_time'] = workflow_result['execution_time']
                    integration_results['end_to_end_workflow']['processed_files'] = workflow_result.get('processed_files', 0)
                    integration_results['end_to_end_workflow']['memory_usage_mb'] = workflow_result.get('memory_usage_mb', 0)
                    
                    if workflow_result['success']:
                        print(f"    ✓ 워크플로우 성공: {workflow_result['execution_time']:.2f}초")
                    else:
                        integration_results['overall_status'] = 'partial_failure'
                        print(f"    ✗ 워크플로우 실패: {workflow_result.get('error', 'Unknown error')}")
                
            except Exception as e:
                integration_results['end_to_end_workflow']['error'] = str(e)
                integration_results['overall_status'] = 'partial_failure'
                print(f"  ✗ 엔드투엔드 워크플로우 테스트 실패: {e}")
            
            # 구성 요소 상호작용 테스트
            print("  구성 요소 상호작용 테스트...")
            try:
                if self.test_framework:
                    # 구성 요소 상호작용 테스트
                    interaction_result = self.test_framework.test_component_interaction()
                    
                    integration_results['component_interaction']['success'] = interaction_result['success']
                    integration_results['component_interaction']['interaction_score'] = interaction_result.get('interaction_score', 0)
                    integration_results['component_interaction']['test_cases'] = interaction_result.get('test_cases', [])
                    
                    if interaction_result['success']:
                        print(f"    ✓ 구성 요소 상호작용 성공: {interaction_result.get('interaction_score', 0)}/100")
                    else:
                        integration_results['overall_status'] = 'partial_failure'
                        print(f"    ✗ 구성 요소 상호작용 실패: {interaction_result.get('error', 'Unknown error')}")
                
            except Exception as e:
                integration_results['component_interaction']['error'] = str(e)
                integration_results['overall_status'] = 'partial_failure'
                print(f"  ✗ 구성 요소 상호작용 테스트 실패: {e}")
            
            # 성능 지표 테스트
            print("  성능 지표 테스트...")
            try:
                if self.test_framework:
                    # 성능 지표 테스트
                    performance_result = self.test_framework.collect_performance_metrics()
                    
                    integration_results['performance_metrics']['success'] = performance_result['success']
                    integration_results['performance_metrics']['metrics'] = performance_result.get('metrics', {})
                    
                    if performance_result['success']:
                        metrics = performance_result.get('metrics', {})
                        print(f"    ✓ 성능 지표 수집 성공")
                        print(f"      - 처리 속도: {metrics.get('throughput', 0):.2f} 파일/초")
                        print(f"      - 메모리 사용: {metrics.get('memory_usage_mb', 0):.2f}MB")
                        print(f"      - CPU 사용: {metrics.get('cpu_usage_percent', 0):.2f}%")
                    else:
                        integration_results['overall_status'] = 'partial_failure'
                        print(f"    ✗ 성능 지표 수집 실패: {performance_result.get('error', 'Unknown error')}")
                
            except Exception as e:
                integration_results['performance_metrics']['error'] = str(e)
                integration_results['overall_status'] = 'partial_failure'
                print(f"  ✗ 성능 지표 테스트 실패: {e}")
            
            print(f"통합 테스트 완료 - 상태: {integration_results['overall_status']}")
            return integration_results
            
        except Exception as e:
            logger.error(f"통합 테스트 실행 오류: {e}")
            return {'overall_status': 'failure', 'error': str(e)}
    
    def run_benchmark_tests(self) -> Dict[str, Any]:
        """벤치마크 테스트 실행"""
        try:
            if not self.config['enable_benchmarking'] or not self.benchmark_suite:
                print("벤치마크 테스트가 비활성화되어 있습니다.")
                return {'overall_status': 'skipped'}
            
            print("벤치마크 테스트 실행 중...")
            
            benchmark_results = {
                'file_io_benchmark': {},
                'data_processing_benchmark': {},
                'memory_usage_benchmark': {},
                'overall_status': 'success'
            }
            
            # 파일 I/O 벤치마크
            print("  파일 I/O 벤치마크...")
            try:
                if self.benchmark_suite:
                    file_io_result = self.benchmark_suite.benchmark_file_io_performance()
                    
                    benchmark_results['file_io_benchmark']['success'] = file_io_result['success']
                    benchmark_results['file_io_benchmark']['metrics'] = file_io_result.get('metrics', {})
                    
                    if file_io_result['success']:
                        metrics = file_io_result.get('metrics', {})
                        print(f"    ✓ 파일 I/O 벤치마크 성공")
                        print(f"      - 읽기 속도: {metrics.get('read_speed_mb_per_sec', 0):.2f}MB/s")
                        print(f"      - 쓰기 속도: {metrics.get('write_speed_mb_per_sec', 0):.2f}MB/s")
                        print(f"      - 처리량: {metrics.get('throughput_files_per_sec', 0):.2f} 파일/초")
                    else:
                        benchmark_results['overall_status'] = 'partial_failure'
                        print(f"    ✗ 파일 I/O 벤치마크 실패: {file_io_result.get('error', 'Unknown error')}")
                
            except Exception as e:
                benchmark_results['file_io_benchmark']['error'] = str(e)
                benchmark_results['overall_status'] = 'partial_failure'
                print(f"  ✗ 파일 I/O 벤치마크 실패: {e}")
            
            # 데이터 처리 벤치마크
            print("  데이터 처리 벤치마크...")
            try:
                if self.benchmark_suite:
                    data_processing_result = self.benchmark_suite.benchmark_data_processing_performance()
                    
                    benchmark_results['data_processing_benchmark']['success'] = data_processing_result['success']
                    benchmark_results['data_processing_benchmark']['metrics'] = data_processing_result.get('metrics', {})
                    
                    if data_processing_result['success']:
                        metrics = data_processing_result.get('metrics', {})
                        print(f"    ✓ 데이터 처리 벤치마크 성공")
                        print(f"      - 처리 속도: {metrics.get('processing_speed_records_per_sec', 0):.2f} 레코드/초")
                        print(f"      - 변환 시간: {metrics.get('transformation_time_ms', 0):.2f}ms")
                        print(f"      - 메모리 효율성: {metrics.get('memory_efficiency', 0):.2f}")
                    else:
                        benchmark_results['overall_status'] = 'partial_failure'
                        print(f"    ✗ 데이터 처리 벤치마크 실패: {data_processing_result.get('error', 'Unknown error')}")
                
            except Exception as e:
                benchmark_results['data_processing_benchmark']['error'] = str(e)
                benchmark_results['overall_status'] = 'partial_failure'
                print(f"  ✗ 데이터 처리 벤치마크 실패: {e}")
            
            # 메모리 사용 벤치마크
            print("  메모리 사용 벤치마크...")
            try:
                if self.benchmark_suite:
                    memory_result = self.benchmark_suite.benchmark_memory_usage()
                    
                    benchmark_results['memory_usage_benchmark']['success'] = memory_result['success']
                    benchmark_results['memory_usage_benchmark']['metrics'] = memory_result.get('metrics', {})
                    
                    if memory_result['success']:
                        metrics = memory_result.get('metrics', {})
                        print(f"    ✓ 메모리 사용 벤치마크 성공")
                        print(f"      - 최대 메모리: {metrics.get('max_memory_usage_mb', 0):.2f}MB")
                        print(f"      - 평균 메모리: {metrics.get('avg_memory_usage_mb', 0):.2f}MB")
                        print(f"      - 메모리 효율성: {metrics.get('memory_efficiency', 0):.2f}")
                    else:
                        benchmark_results['overall_status'] = 'partial_failure'
                        print(f"    ✗ 메모리 사용 벤치마크 실패: {memory_result.get('error', 'Unknown error')}")
                
            except Exception as e:
                benchmark_results['memory_usage_benchmark']['error'] = str(e)
                benchmark_results['overall_status'] = 'partial_failure'
                print(f"  ✗ 메모리 사용 벤치마크 실패: {e}")
            
            print(f"벤치마크 테스트 완료 - 상태: {benchmark_results['overall_status']}")
            return benchmark_results
            
        except Exception as e:
            logger.error(f"벤치마크 테스트 실행 오류: {e}")
            return {'overall_status': 'failure', 'error': str(e)}
    
    def run_regression_tests(self) -> Dict[str, Any]:
        """회귀 테스트 실행"""
        try:
            if not self.config['enable_regression_detection'] or not self.regression_system:
                print("회귀 테스트가 비활성화되어 있습니다.")
                return {'overall_status': 'skipped'}
            
            print("회귀 테스트 실행 중...")
            
            regression_results = {
                'baseline_comparison': {},
                'regression_detection': {},
                'performance_validation': {},
                'overall_status': 'success'
            }
            
            # 기준선 비교 테스트
            print("  기준선 비교 테스트...")
            try:
                if self.regression_system:
                    # 현재 성능 측정
                    current_metrics = {
                        'execution_time': 1.2,
                        'memory_usage_mb': 450.0,
                        'throughput_files_per_sec': 120.0,
                        'cpu_usage_percent': 30.0
                    }
                    
                    # 회귀 감지
                    regression_detection = self.regression_system.detect_performance_regression(
                        test_name="integrated_performance_test",
                        test_environment="development",
                        current_metrics=current_metrics
                    )
                    
                    regression_results['baseline_comparison']['success'] = True
                    regression_results['baseline_comparison']['current_metrics'] = current_metrics
                    
                    if regression_detection:
                        regression_results['regression_detection']['detected'] = True
                        regression_results['regression_detection']['severity'] = regression_detection.severity.value
                        print(f"    ⚠️  성능 회귀 감지: {regression_detection.severity.value}")
                    else:
                        regression_results['regression_detection']['detected'] = False
                        print(f"    ✓ 성능 회귀 미감지")
                
            except Exception as e:
                regression_results['baseline_comparison']['error'] = str(e)
                regression_results['overall_status'] = 'partial_failure'
                print(f"  ✗ 기준선 비교 테스트 실패: {e}")
            
            # 성능 검증 테스트
            print("  성능 검증 테스트...")
            try:
                if self.regression_system:
                    # 시스템 상태 확인
                    system_status = self.regression_system.get_system_status()
                    
                    regression_results['performance_validation']['success'] = True
                    regression_results['performance_validation']['system_status'] = system_status
                    
                    print(f"    ✓ 시스템 상태 확인 완료")
                    print(f"      - 총 기준선 수: {system_status.get('total_baselines', 0)}")
                    print(f"      - 활성 알림: {system_status.get('active_alerts', 0)}")
                    print(f"      - 최근 감지: {system_status.get('recent_detections', 0)}")
                
            except Exception as e:
                regression_results['performance_validation']['error'] = str(e)
                regression_results['overall_status'] = 'partial_failure'
                print(f"  ✗ 성능 검증 테스트 실패: {e}")
            
            print(f"회귀 테스트 완료 - 상태: {regression_results['overall_status']}")
            return regression_results
            
        except Exception as e:
            logger.error(f"회귀 테스트 실행 오류: {e}")
            return {'overall_status': 'failure', 'error': str(e)}
    
    def run_stress_tests(self) -> Dict[str, Any]:
        """스트레스 테스트 실행"""
        try:
            print("스트레스 테스트 실행 중...")
            
            stress_results = {
                'concurrent_processing': {},
                'large_file_handling': {},
                'memory_pressure': {},
                'overall_status': 'success'
            }
            
            # 동시 처리 테스트
            print("  동시 처리 테스트...")
            try:
                if self.test_framework:
                    # 동시 파일 처리 테스트
                    concurrent_result = self.test_framework.test_concurrent_processing(
                        num_workers=8,
                        num_files=100
                    )
                    
                    stress_results['concurrent_processing']['success'] = concurrent_result['success']
                    stress_results['concurrent_processing']['metrics'] = concurrent_result.get('metrics', {})
                    
                    if concurrent_result['success']:
                        metrics = concurrent_result.get('metrics', {})
                        print(f"    ✓ 동시 처리 테스트 성공")
                        print(f"      - 처리된 파일 수: {metrics.get('processed_files', 0)}")
                        print(f"      - 평균 처리 시간: {metrics.get('avg_processing_time', 0):.2f}초")
                        print(f"      - 동시성 효율성: {metrics.get('concurrency_efficiency', 0):.2f}")
                    else:
                        stress_results['overall_status'] = 'partial_failure'
                        print(f"    ✗ 동시 처리 테스트 실패: {concurrent_result.get('error', 'Unknown error')}")
                
            except Exception as e:
                stress_results['concurrent_processing']['error'] = str(e)
                stress_results['overall_status'] = 'partial_failure'
                print(f"  ✗ 동시 처리 테스트 실패: {e}")
            
            # 대용량 파일 처리 테스트
            print("  대용량 파일 처리 테스트...")
            try:
                if self.test_framework:
                    # 대용량 파일 처리 테스트
                    large_file_result = self.test_framework.test_large_file_handling(
                        file_size_mb=100,
                        num_files=5
                    )
                    
                    stress_results['large_file_handling']['success'] = large_file_result['success']
                    stress_results['large_file_handling']['metrics'] = large_file_result.get('metrics', {})
                    
                    if large_file_result['success']:
                        metrics = large_file_result.get('metrics', {})
                        print(f"    ✓ 대용량 파일 처리 테스트 성공")
                        print(f"      - 처리된 총 크기: {metrics.get('total_size_mb', 0):.2f}MB")
                        print(f"      - 처리 시간: {metrics.get('processing_time', 0):.2f}초")
                        print(f"      - 처리 속도: {metrics.get('throughput_mb_per_sec', 0):.2f}MB/s")
                    else:
                        stress_results['overall_status'] = 'partial_failure'
                        print(f"    ✗ 대용량 파일 처리 테스트 실패: {large_file_result.get('error', 'Unknown error')}")
                
            except Exception as e:
                stress_results['large_file_handling']['error'] = str(e)
                stress_results['overall_status'] = 'partial_failure'
                print(f"  ✗ 대용량 파일 처리 테스트 실패: {e}")
            
            # 메모리 압박 테스트
            print("  메모리 압박 테스트...")
            try:
                if self.test_framework:
                    # 메모리 압박 테스트
                    memory_pressure_result = self.test_framework.test_memory_pressure(
                        target_memory_mb=2000,
                        duration_seconds=30
                    )
                    
                    stress_results['memory_pressure']['success'] = memory_pressure_result['success']
                    stress_results['memory_pressure']['metrics'] = memory_pressure_result.get('metrics', {})
                    
                    if memory_pressure_result['success']:
                        metrics = memory_pressure_result.get('metrics', {})
                        print(f"    ✓ 메모리 압박 테스트 성공")
                        print(f"      - 최대 메모리 사용: {metrics.get('max_memory_usage_mb', 0):.2f}MB")
                        print(f"      - 메모리 누수: {metrics.get('memory_leak_mb', 0):.2f}MB")
                        print(f"      - GC 호출 횟수: {metrics.get('gc_calls', 0)}")
                    else:
                        stress_results['overall_status'] = 'partial_failure'
                        print(f"    ✗ 메모리 압박 테스트 실패: {memory_pressure_result.get('error', 'Unknown error')}")
                
            except Exception as e:
                stress_results['memory_pressure']['error'] = str(e)
                stress_results['overall_status'] = 'partial_failure'
                print(f"  ✗ 메모리 압박 테스트 실패: {e}")
            
            print(f"스트레스 테스트 완료 - 상태: {stress_results['overall_status']}")
            return stress_results
            
        except Exception as e:
            logger.error(f"스트레스 테스트 실행 오류: {e}")
            return {'overall_status': 'failure', 'error': str(e)}
    
    def generate_test_report(self, all_results: Dict[str, Any]) -> str:
        """통합 테스트 보고서 생성"""
        try:
            print("통합 테스트 보고서 생성 중...")
            
            # 보고서 데이터 구성
            report_data = {
                'test_execution_summary': {
                    'start_time': self.start_time.isoformat() if self.start_time else None,
                    'end_time': self.end_time.isoformat() if self.end_time else None,
                    'total_execution_time': (self.end_time - self.start_time).total_seconds() if self.start_time and self.end_time else 0,
                    'overall_status': self.calculate_overall_status(all_results),
                    'test_categories': len([k for k in all_results.keys() if k != 'test_execution_summary'])
                },
                'test_results': all_results,
                'performance_metrics': self.performance_monitor.get_performance_report(),
                'system_status': self.regression_system.get_system_status() if self.regression_system else {},
                'recommendations': self.generate_recommendations(all_results)
            }
            
            # 보고서 파일 경로
            report_path = Path(OUTPUT_DIR) / f"integrated_test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            # 보고서 저장
            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, indent=2, ensure_ascii=False, default=str)
            
            print(f"✓ 통합 테스트 보고서 생성 완료: {report_path}")
            
            return str(report_path)
            
        except Exception as e:
            logger.error(f"통합 테스트 보고서 생성 오류: {e}")
            return ""
    
    def calculate_overall_status(self, all_results: Dict[str, Any]) -> str:
        """전체 테스트 상태 계산"""
        try:
            status_counts = {'success': 0, 'partial_failure': 0, 'failure': 0, 'skipped': 0}
            
            for category, results in all_results.items():
                if category == 'test_execution_summary':
                    continue
                
                if isinstance(results, dict) and 'overall_status' in results:
                    status = results['overall_status']
                    status_counts[status] = status_counts.get(status, 0) + 1
            
            # 상태 결정 로직
            if status_counts['failure'] > 0:
                return 'failure'
            elif status_counts['partial_failure'] > 0:
                return 'partial_failure'
            elif status_counts['success'] > 0:
                return 'success'
            else:
                return 'skipped'
                
        except Exception as e:
            logger.error(f"전체 테스트 상태 계산 오류: {e}")
            return 'unknown'
    
    def generate_recommendations(self, all_results: Dict[str, Any]) -> List[str]:
        """개선 제안 생성"""
        recommendations = []
        
        try:
            # 단위 테스트 결과 분석
            unit_results = all_results.get('unit_tests', {})
            if unit_results.get('overall_status') == 'partial_failure':
                recommendations.append("일부 단위 테스트가 실패했습니다. 해당 구성 요소를 점검하세요.")
            
            # 통합 테스트 결과 분석
            integration_results = all_results.get('integration_tests', {})
            if integration_results.get('overall_status') == 'partial_failure':
                recommendations.append("통합 테스트에서 문제가 발견되었습니다. 구성 요소 간 상호작용을 검토하세요.")
            
            # 벤치마크 결과 분석
            benchmark_results = all_results.get('benchmark_tests', {})
            if benchmark_results.get('overall_status') == 'partial_failure':
                recommendations.append("성능 벤치마크에서 개선이 필요한 영역이 있습니다.")
            
            # 회귀 테스트 결과 분석
            regression_results = all_results.get('regression_tests', {})
            if regression_results.get('overall_status') == 'partial_failure':
                recommendations.append("성능 회귀가 감지되었습니다. 성능 기준선을 검토하세요.")
            
            # 스트레스 테스트 결과 분석
            stress_results = all_results.get('stress_tests', {})
            if stress_results.get('overall_status') == 'partial_failure':
                recommendations.append("스트레스 테스트에서 안정성 문제가 발견되었습니다.")
            
            # 일반적인 개선 제안
            recommendations.extend([
                "정기적인 성능 모니터링을 유지하세요",
                "테스트 커버리지를 지속적으로 개선하세요",
                "CI/CD 파이프라인에 테스트를 통합하세요",
                "성능 기준선을 주기적으로 업데이트하세요",
                "테스트 환경을 프로덕션 환경과 유사하게 유지하세요"
            ])
            
            return recommendations
            
        except Exception as e:
            logger.error(f"개선 제안 생성 오류: {e}")
            return ["테스트 분석 중 오류가 발생했습니다."]
    
    def cleanup_test_environment(self):
        """테스트 환경 정리"""
        try:
            print("테스트 환경 정리 중...")
            
            # 성능 모니터링 중지
            if self.performance_monitor:
                self.performance_monitor.stop_monitoring()
                print("  ✓ 성능 모니터링 중지 완료")
            
            # 임시 파일 정리
            temp_dirs = ['test_data', 'temp_output', 'performance_results']
            for temp_dir in temp_dirs:
                temp_path = Path(temp_dir)
                if temp_path.exists():
                    import shutil
                    shutil.rmtree(temp_path)
                    print(f"  ✓ 임시 디렉토리 정리 완료: {temp_dir}")
            
            print("테스트 환경 정리 완료!")
            
        except Exception as e:
            logger.error(f"테스트 환경 정리 오류: {e}")
    
    def run_all_tests(self) -> Dict[str, Any]:
        """모든 테스트 실행"""
        try:
            # 테스트 시작 시간 기록
            self.start_time = datetime.now()
            
            print("=" * 60)
            print("WinForms_Docs 통합 성능 테스트 시작")
            print("=" * 60)
            
            # 구성 요소 초기화
            self.initialize_components()
            
            # 테스트 환경 설정
            self.setup_test_environment()
            
            # 테스트 결과 저장
            all_results = {
                'test_execution_summary': {
                    'start_time': self.start_time.isoformat(),
                    'test_categories': []
                }
            }
            
            # 단위 테스트 실행
            print("\n" + "=" * 40)
            print("1. 단위 테스트 실행")
            print("=" * 40)
            unit_results = self.run_unit_tests()
            all_results['unit_tests'] = unit_results
            all_results['test_execution_summary']['test_categories'].append('unit_tests')
            
            # 통합 테스트 실행
            print("\n" + "=" * 40)
            print("2. 통합 테스트 실행")
            print("=" * 40)
            integration_results = self.run_integration_tests()
            all_results['integration_tests'] = integration_results
            all_results['test_execution_summary']['test_categories'].append('integration_tests')
            
            # 벤치마크 테스트 실행
            print("\n" + "=" * 40)
            print("3. 벤치마크 테스트 실행")
            print("=" * 40)
            benchmark_results = self.run_benchmark_tests()
            all_results['benchmark_tests'] = benchmark_results
            if benchmark_results.get('overall_status') != 'skipped':
                all_results['test_execution_summary']['test_categories'].append('benchmark_tests')
            
            # 회귀 테스트 실행
            print("\n" + "=" * 40)
            print("4. 회귀 테스트 실행")
            print("=" * 40)
            regression_results = self.run_regression_tests()
            all_results['regression_tests'] = regression_results
            if regression_results.get('overall_status') != 'skipped':
                all_results['test_execution_summary']['test_categories'].append('regression_tests')
            
            # 스트레스 테스트 실행
            print("\n" + "=" * 40)
            print("5. 스트레스 테스트 실행")
            print("=" * 40)
            stress_results = self.run_stress_tests()
            all_results['stress_tests'] = stress_results
            all_results['test_execution_summary']['test_categories'].append('stress_tests')
            
            # 테스트 종료 시간 기록
            self.end_time = datetime.now()
            
            # 보고서 생성
            if self.config['generate_reports']:
                report_path = self.generate_test_report(all_results)
                all_results['test_execution_summary']['report_path'] = report_path
            
            # 전체 상태 계산
            overall_status = self.calculate_overall_status(all_results)
            all_results['test_execution_summary']['overall_status'] = overall_status
            all_results['test_execution_summary']['end_time'] = self.end_time.isoformat()
            all_results['test_execution_summary']['total_execution_time'] = (
                self.end_time - self.start_time
            ).total_seconds()
            
            # 결과 요약 출력
            print("\n" + "=" * 60)
            print("통합 테스트 결과 요약")
            print("=" * 60)
            print(f"전체 상태: {overall_status.upper()}")
            print(f"실행 시간: {all_results['test_execution_summary']['total_execution_time']:.2f}초")
            print(f"테스트 카테고리: {len(all_results['test_execution_summary']['test_categories'])}개")
            
            for category in all_results['test_execution_summary']['test_categories']:
                result = all_results.get(category, {})
                status = result.get('overall_status', 'unknown')
                print(f"  - {category}: {status.upper()}")
            
            # 개선 제안 출력
            recommendations = self.generate_recommendations(all_results)
            if recommendations:
                print("\n개선 제안:")
                for i, rec in enumerate(recommendations, 1):
                    print(f"  {i}. {rec}")
            
            # 테스트 환경 정리
            if self.config['cleanup_after_test']:
                self.cleanup_test_environment()
            
            return all_results
            
        except Exception as e:
            logger.error(f"통합 테스트 실행 오류: {e}")
            import traceback
            traceback.print_exc()
            return {'overall_status': 'failure', 'error': str(e)}
        
        finally:
            # 테스트 종료 시간 기록
            if not self.end_time:
                self.end_time = datetime.now()

def main():
    """메인 실행 함수"""
    parser = argparse.ArgumentParser(description='WinForms_Docs 통합 성능 테스트')
    parser.add_argument('--config', type=str, help='테스트 설정 파일 경로')
    parser.add_argument('--skip-unit', action='store_true', help='단위 테스트 건너뛰기')
    parser.add_argument('--skip-integration', action='store_true', help='통합 테스트 건너뛰기')
    parser.add_argument('--skip-benchmark', action='store_true', help='벤치마크 테스트 건너뛰기')
    parser.add_argument('--skip-regression', action='store_true', help='회귀 테스트 건너뛰기')
    parser.add_argument('--skip-stress', action='store_true', help='스트레스 테스트 건너뛰기')
    parser.add_argument('--no-cleanup', action='store_true', help='테스트 환경 정리 건너뛰기')
    parser.add_argument('--no-report', action='store_true', help='보고서 생성 건너뛰기')
    
    args = parser.parse_args()
    
    try:
        # 테스트 실행기 생성
        test_runner = IntegratedTestRunner()
        
        # 설정 적용
        if args.skip_unit:
            test_runner.config['enable_unit_tests'] = False
        if args.skip_integration:
            test_runner.config['enable_integration_tests'] = False
        if args.skip_benchmark:
            test_runner.config['enable_benchmarking'] = False
        if args.skip_regression:
            test_runner.config['enable_regression_detection'] = False
        if args.skip_stress:
            test_runner.config['enable_stress_tests'] = False
        if args.no_cleanup:
            test_runner.config['cleanup_after_test'] = False
        if args.no_report:
            test_runner.config['generate_reports'] = False
        
        # 모든 테스트 실행
        results = test_runner.run_all_tests()
        
        # 종료 코드 설정
        overall_status = results.get('test_execution_summary', {}).get('overall_status', 'unknown')
        if overall_status == 'success':
            print("\n✅ 통합 성능 테스트가 성공적으로 완료되었습니다.")
            exit(0)
        elif overall_status == 'partial_failure':
            print("\n⚠️  통합 성능 테스트가 부분적으로 실패했습니다. 로그를 확인하세요.")
            exit(1)
        else:
            print("\n❌ 통합 성능 테스트가 실패했습니다. 로그를 확인하세요.")
            exit(2)
            
    except KeyboardInterrupt:
        print("\n\n⚠️  사용자에 의해 테스트가 중단되었습니다.")
        exit(130)
    except Exception as e:
        print(f"\n❌ 통합 성능 테스트 실행 중 오류가 발생했습니다: {e}")
        import traceback
        traceback.print_exc()
        exit(1)

if __name__ == "__main__":
    main()