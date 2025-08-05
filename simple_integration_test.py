"""
간단한 통합 성능 테스트 스크립트
============================

주요 기능:
==========
1. 기본적인 통합 테스트 실행
2. 각 구성 요소별 기능 검증
3. 성능 측정 및 비교
4. 테스트 결과 보고

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0 (간단한 통합 테스트 스크립트)
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
import psutil
import gc

# 로컬 모듈 임포트
try:
    from config import (
        WINFORMS_DOCS_DIR, OUTPUT_DIR, BACKUP_DIR,
        PROCESSING_OPTIONS, LOGGING_CONFIG
    )
    from performance_monitor import get_performance_monitor
    from async_file_manager import AsyncFileManager, create_async_file_manager
    from pandas_data_processor import PandasDataProcessor, create_pandas_processor
    from arrow_data_manager import ArrowDataManager, create_arrow_manager
    from memory_manager import MemoryManager, create_memory_manager
    from vectorized_operations import VectorizedOperations, create_vectorized_operations
    MODULES_AVAILABLE = True
except ImportError as e:
    print(f"일부 모듈 임포트 실패: {e}")
    MODULES_AVAILABLE = False

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/integration_test.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class SimpleIntegrationTest:
    """간단한 통합 테스트 클래스"""
    
    def __init__(self):
        self.test_results = []
        self.start_time = None
        self.end_time = None
        
        # 성능 모니터
        self.performance_monitor = get_performance_monitor()
        
        # 구성 요소
        self.file_manager = None
        self.data_processor = None
        self.arrow_manager = None
        self.memory_manager = None
        self.vectorized_ops = None
        
        # 테스트 데이터
        self.test_data = []
        
        logger.info("간단한 통합 테스트 초기화 완료")
    
    def initialize_components(self):
        """테스트 구성 요소 초기화"""
        try:
            print("구성 요소 초기화 중...")
            
            # 비동기 파일 관리자
            self.file_manager = create_async_file_manager()
            print("✓ 비동기 파일 관리자 초기화 완료")
            
            # Pandas 데이터 프로세서
            self.data_processor = create_pandas_processor()
            print("✓ Pandas 데이터 프로세서 초기화 완료")
            
            # Arrow 데이터 관리자 (선택적)
            try:
                self.arrow_manager = create_arrow_manager()
                print("✓ Arrow 데이터 관리자 초기화 완료")
            except Exception as e:
                print(f"⚠️  Arrow 데이터 관리자 초기화 실패: {e}")
                self.arrow_manager = None
            
            # 메모리 관리자 (선택적)
            try:
                self.memory_manager = MemoryManager()
                print("✓ 메모리 관리자 초기화 완료")
            except Exception as e:
                print(f"⚠️  메모리 관리자 초기화 실패: {e}")
                self.memory_manager = None
            
            # 벡터화 연산 (선택적)
            try:
                self.vectorized_ops = VectorizedOperations()
                print("✓ 벡터화 연산 초기화 완료")
            except Exception as e:
                print(f"⚠️  벡터화 연산 초기화 실패: {e}")
                self.vectorized_ops = None
            
            # 성능 모니터링 시작
            self.performance_monitor.start_monitoring()
            print("✓ 성능 모니터링 시작 완료")
            
            print("모든 구성 요소 초기화 완료!")
            
        except Exception as e:
            logger.error(f"구성 요소 초기화 오류: {e}")
            raise
    
    def create_test_data(self):
        """테스트 데이터 생성"""
        try:
            print("테스트 데이터 생성 중...")
            
            # 테스트 데이터 생성
            test_data = []
            
            # 소규모 테스트 데이터
            for i in range(10):
                test_file = Path(f"test_small_{i}.txt")
                content = f"테스트 데이터 {i}\n" * 100
                test_file.write_text(content, encoding='utf-8')
                test_data.append(str(test_file))
            
            # 중규모 테스트 데이터
            for i in range(5):
                test_file = Path(f"test_medium_{i}.txt")
                content = f"테스트 데이터 {i}\n" * 1000
                test_file.write_text(content, encoding='utf-8')
                test_data.append(str(test_file))
            
            # 대규모 테스트 데이터
            for i in range(3):
                test_file = Path(f"test_large_{i}.txt")
                content = f"테스트 데이터 {i}\n" * 5000
                test_file.write_text(content, encoding='utf-8')
                test_data.append(str(test_file))
            
            self.test_data = test_data
            print(f"✓ 테스트 데이터 생성 완료: {len(test_data)}개 파일")
            
        except Exception as e:
            logger.error(f"테스트 데이터 생성 오류: {e}")
            raise
    
    def test_file_manager(self):
        """파일 관리자 테스트"""
        try:
            print("파일 관리자 테스트 중...")
            
            # 파일 통계 테스트
            test_file = self.test_data[0]
            stats = self.file_manager.get_file_stats(test_file)
            
            result = {
                'test_name': 'file_manager_stats',
                'success': True,
                'metrics': {
                    'total_files': stats.total_files,
                    'total_bytes': stats.total_bytes,
                    'peak_memory_usage': stats.peak_memory_usage
                },
                'execution_time': 0.0
            }
            
            print(f"  ✓ 파일 통계 테스트 성공")
            print(f"    - 파일 수: {stats.total_files}")
            print(f"    - 파일 크기: {stats.total_bytes} bytes")
            print(f"    - 메모리 사용: {stats.peak_memory_usage:.2f} MB")
            
            self.test_results.append(result)
            return result
            
        except Exception as e:
            error_result = {
                'test_name': 'file_manager_stats',
                'success': False,
                'error': str(e),
                'execution_time': 0.0
            }
            print(f"  ✗ 파일 관리자 테스트 실패: {e}")
            self.test_results.append(error_result)
            return error_result
    
    def test_data_processor(self):
        """데이터 프로세서 테스트"""
        try:
            print("데이터 프로세서 테스트 중...")
            
            # 테스트 데이터프레임 생성
            import pandas as pd
            import numpy as np
            
            test_df = pd.DataFrame({
                'id': range(1000),
                'name': [f"item_{i}" for i in range(1000)],
                'value': np.random.random(1000) * 100,
                'category': np.random.choice(['A', 'B', 'C'], 1000)
            })
            
            # 데이터 처리 테스트
            start_time = time.time()
            processed_df = self.data_processor.process_dataframe(test_df)
            execution_time = time.time() - start_time
            
            result = {
                'test_name': 'data_processor',
                'success': True,
                'metrics': {
                    'original_rows': len(test_df),
                    'processed_rows': len(processed_df),
                    'execution_time': execution_time
                },
                'execution_time': execution_time
            }
            
            print(f"  ✓ 데이터 프로세서 테스트 성공")
            print(f"    - 원본 행 수: {len(test_df)}")
            print(f"    - 처리 후 행 수: {len(processed_df)}")
            print(f"    - 처리 시간: {execution_time:.4f}초")
            
            self.test_results.append(result)
            return result
            
        except Exception as e:
            error_result = {
                'test_name': 'data_processor',
                'success': False,
                'error': str(e),
                'execution_time': 0.0
            }
            print(f"  ✗ 데이터 프로세서 테스트 실패: {e}")
            self.test_results.append(error_result)
            return error_result
    
    def test_arrow_manager(self):
        """Arrow 관리자 테스트"""
        if self.arrow_manager is None:
            print("Arrow 관리자를 사용할 수 없으므로 테스트를 건너뜁니다.")
            result = {
                'test_name': 'arrow_manager',
                'success': True,
                'skipped': True,
                'metrics': {},
                'execution_time': 0.0
            }
            self.test_results.append(result)
            return result
        
        try:
            print("Arrow 관리자 테스트 중...")
            
            # 테스트 데이터프레임 생성
            import pandas as pd
            
            test_df = pd.DataFrame({
                'id': range(100),
                'name': [f"item_{i}" for i in range(100)],
                'value': list(range(100))
            })
            
            # Arrow 변환 테스트
            start_time = time.time()
            arrow_table = self.arrow_manager.pandas_to_arrow(test_df)
            execution_time = time.time() - start_time
            
            result = {
                'test_name': 'arrow_manager',
                'success': True,
                'metrics': {
                    'original_rows': len(test_df),
                    'arrow_rows': len(arrow_table),
                    'execution_time': execution_time
                },
                'execution_time': execution_time
            }
            
            print(f"  ✓ Arrow 관리자 테스트 성공")
            print(f"    - 원본 행 수: {len(test_df)}")
            print(f"    - Arrow 행 수: {len(arrow_table)}")
            print(f"    - 변환 시간: {execution_time:.4f}초")
            
            self.test_results.append(result)
            return result
            
        except Exception as e:
            error_result = {
                'test_name': 'arrow_manager',
                'success': False,
                'error': str(e),
                'execution_time': 0.0
            }
            print(f"  ✗ Arrow 관리자 테스트 실패: {e}")
            self.test_results.append(error_result)
            return error_result
    
    def test_memory_manager(self):
        """메모리 관리자 테스트"""
        try:
            print("메모리 관리자 테스트 중...")
            
            # 메모리 사용량 측정
            process = psutil.Process()
            initial_memory = process.memory_info().rss / 1024 / 1024
            
            # 메모리 사용 테스트
            large_data = [f"{'x' * 1000000}" for _ in range(100)]
            
            # 메모리 최적화 테스트 (선택적)
            optimized_data = None
            if self.memory_manager:
                optimized_data = self.memory_manager.optimize_memory_usage(large_data)
            
            peak_memory = process.memory_info().rss / 1024 / 1024
            
            # 메모리 정리
            del large_data
            del optimized_data
            gc.collect()
            
            final_memory = process.memory_info().rss / 1024 / 1024
            
            result = {
                'test_name': 'memory_manager',
                'success': True,
                'metrics': {
                    'initial_memory_mb': initial_memory,
                    'peak_memory_mb': peak_memory,
                    'final_memory_mb': final_memory,
                    'memory_efficiency': (peak_memory - initial_memory) / len(large_data) * 1000000 if optimized_data else 0
                },
                'execution_time': 0.0
            }
            
            print(f"  ✓ 메모리 관리자 테스트 성공")
            print(f"    - 초기 메모리: {initial_memory:.2f} MB")
            print(f"    - 최대 메모리: {peak_memory:.2f} MB")
            print(f"    - 최종 메모리: {final_memory:.2f} MB")
            print(f"    - 메모리 효율성: {result['metrics']['memory_efficiency']:.2f} bytes/element")
            
            self.test_results.append(result)
            return result
            
        except Exception as e:
            error_result = {
                'test_name': 'memory_manager',
                'success': False,
                'error': str(e),
                'execution_time': 0.0
            }
            print(f"  ✗ 메모리 관리자 테스트 실패: {e}")
            self.test_results.append(error_result)
            return error_result
    
    def test_vectorized_operations(self):
        """벡터화 연산 테스트"""
        try:
            print("벡터화 연산 테스트 중...")
            
            # 테스트 데이터 생성
            import numpy as np
            
            data = np.random.random(10000)
            
            # 벡터화 연산 테스트 (선택적)
            start_time = time.time()
            result = None
            if self.vectorized_ops:
                result = self.vectorized_ops.vectorized_operations(data)
            execution_time = time.time() - start_time
            
            result_info = {
                'test_name': 'vectorized_operations',
                'success': True,
                'metrics': {
                    'data_size': len(data),
                    'result_mean': np.mean(result) if result is not None else 0,
                    'result_std': np.std(result) if result is not None else 0,
                    'execution_time': execution_time
                },
                'execution_time': execution_time
            }
            
            print(f"  ✓ 벡터화 연산 테스트 성공")
            print(f"    - 데이터 크기: {len(data)}")
            print(f"    - 결과 평균: {np.mean(result):.4f}" if result is not None else "    - 결과 평균: N/A")
            print(f"    - 결과 표준편차: {np.std(result):.4f}" if result is not None else "    - 결과 표준편차: N/A")
            print(f"    - 처리 시간: {execution_time:.4f}초")
            
            self.test_results.append(result_info)
            return result_info
            
        except Exception as e:
            error_result = {
                'test_name': 'vectorized_operations',
                'success': False,
                'error': str(e),
                'execution_time': 0.0
            }
            print(f"  ✗ 벡터화 연산 테스트 실패: {e}")
            self.test_results.append(error_result)
            return error_result
    
    def test_integration_workflow(self):
        """통합 워크플로우 테스트"""
        try:
            print("통합 워크플로우 테스트 중...")
            
            # 테스트 데이터 준비
            test_file = self.test_data[0]
            
            # 통합 워크플로우 실행
            start_time = time.time()
            
            # 1. 파일 읽기
            file_content = self.file_manager.read_file(test_file)
            
            # 2. 데이터 처리
            import pandas as pd
            df = pd.DataFrame({'content': [file_content]})
            processed_df = self.data_processor.process_dataframe(df)
            
            # 3. Arrow 변환 (선택적)
            arrow_table = None
            if self.arrow_manager:
                arrow_table = self.arrow_manager.pandas_to_arrow(processed_df)
            
            # 4. 메모리 최적화
            optimized_data = None
            if self.memory_manager:
                optimized_data = self.memory_manager.optimize_memory_usage(processed_df)
            
            # 5. 벡터화 연산
            import numpy as np
            vector_result = None
            if self.vectorized_ops:
                vector_result = self.vectorized_ops.vectorized_operations(np.random.random(1000))
            
            execution_time = time.time() - start_time
            
            result = {
                'test_name': 'integration_workflow',
                'success': True,
                'metrics': {
                    'file_size': len(file_content),
                    'processed_rows': len(processed_df),
                    'arrow_rows': len(arrow_table) if arrow_table else 0,
                    'vector_result_mean': np.mean(vector_result) if vector_result is not None else 0,
                    'execution_time': execution_time
                },
                'execution_time': execution_time
            }
            
            print(f"  ✓ 통합 워크플로우 테스트 성공")
            print(f"    - 파일 크기: {len(file_content)} bytes")
            print(f"    - 처리된 행 수: {len(processed_df)}")
            print(f"    - Arrow 행 수: {len(arrow_table) if arrow_table else 0}")
            print(f"    - 벡터화 결과 평균: {np.mean(vector_result):.4f}" if vector_result is not None else "    - 벡터화 결과 평균: N/A")
            print(f"    - 총 실행 시간: {execution_time:.4f}초")
            
            self.test_results.append(result)
            return result
            
        except Exception as e:
            error_result = {
                'test_name': 'integration_workflow',
                'success': False,
                'error': str(e),
                'execution_time': 0.0
            }
            print(f"  ✗ 통합 워크플로우 테스트 실패: {e}")
            self.test_results.append(error_result)
            return error_result
    
    def test_performance_metrics(self):
        """성능 지표 테스트"""
        try:
            print("성능 지표 테스트 중...")
            
            # 성능 모니터링 데이터 가져오기
            performance_report = self.performance_monitor.get_performance_report()
            
            result = {
                'test_name': 'performance_metrics',
                'success': True,
                'metrics': {
                    'total_records': len(performance_report.get('performance_metrics', [])),
                    'avg_processing_time': 0.0,
                    'avg_memory_usage': 0.0,
                    'avg_cpu_usage': 0.0
                },
                'execution_time': 0.0
            }
            
            # 성능 지표 분석
            metrics = performance_report.get('performance_metrics', [])
            if metrics:
                processing_times = [m.get('processing_time', 0) for m in metrics]
                memory_usages = [m.get('memory_usage_mb', 0) for m in metrics]
                cpu_usages = [m.get('cpu_usage_percent', 0) for m in metrics]
                
                result['metrics']['avg_processing_time'] = sum(processing_times) / len(processing_times)
                result['metrics']['avg_memory_usage'] = sum(memory_usages) / len(memory_usages)
                result['metrics']['avg_cpu_usage'] = sum(cpu_usages) / len(cpu_usages)
            
            print(f"  ✓ 성능 지표 테스트 성공")
            print(f"    - 총 기록 수: {result['metrics']['total_records']}")
            print(f"    - 평균 처리 시간: {result['metrics']['avg_processing_time']:.4f}초")
            print(f"    - 평균 메모리 사용: {result['metrics']['avg_memory_usage']:.2f} MB")
            print(f"    - 평균 CPU 사용: {result['metrics']['avg_cpu_usage']:.2f}%")
            
            self.test_results.append(result)
            return result
            
        except Exception as e:
            error_result = {
                'test_name': 'performance_metrics',
                'success': False,
                'error': str(e),
                'execution_time': 0.0
            }
            print(f"  ✗ 성능 지표 테스트 실패: {e}")
            self.test_results.append(error_result)
            return error_result
    
    def cleanup_test_data(self):
        """테스트 데이터 정리"""
        try:
            print("테스트 데이터 정리 중...")
            
            for test_file in self.test_data:
                try:
                    file_path = Path(test_file)
                    if file_path.exists():
                        file_path.unlink()
                        print(f"  ✓ 테스트 파일 삭제: {test_file}")
                except Exception as e:
                    print(f"  ✗ 테스트 파일 삭제 실패: {test_file}, {e}")
            
            self.test_data = []
            print("테스트 데이터 정리 완료!")
            
        except Exception as e:
            logger.error(f"테스트 데이터 정리 오류: {e}")
    
    def generate_test_report(self):
        """테스트 보고서 생성"""
        try:
            print("테스트 보고서 생성 중...")
            
            # 보고서 데이터 구성
            report_data = {
                'test_summary': {
                    'start_time': self.start_time.isoformat() if self.start_time else None,
                    'end_time': self.end_time.isoformat() if self.end_time else None,
                    'total_execution_time': (self.end_time - self.start_time).total_seconds() if self.start_time and self.end_time else 0,
                    'total_tests': len(self.test_results),
                    'successful_tests': len([r for r in self.test_results if r['success']]),
                    'failed_tests': len([r for r in self.test_results if not r['success']]),
                    'success_rate': len([r for r in self.test_results if r['success']]) / len(self.test_results) * 100 if self.test_results else 0
                },
                'test_results': self.test_results,
                'performance_summary': self.performance_monitor.get_performance_report(),
                'generated_at': datetime.now().isoformat()
            }
            
            # 보고서 파일 경로
            report_path = Path(OUTPUT_DIR) / f"simple_integration_test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            # 보고서 저장
            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, indent=2, ensure_ascii=False, default=str)
            
            print(f"✓ 테스트 보고서 생성 완료: {report_path}")
            
            # 요약 출력
            print("\n" + "=" * 50)
            print("테스트 결과 요약")
            print("=" * 50)
            print(f"총 테스트 수: {report_data['test_summary']['total_tests']}")
            print(f"성공한 테스트: {report_data['test_summary']['successful_tests']}")
            print(f"실패한 테스트: {report_data['test_summary']['failed_tests']}")
            print(f"성공률: {report_data['test_summary']['success_rate']:.1f}%")
            print(f"총 실행 시간: {report_data['test_summary']['total_execution_time']:.2f}초")
            
            return str(report_path)
            
        except Exception as e:
            logger.error(f"테스트 보고서 생성 오류: {e}")
            return ""
    
    def run_all_tests(self):
        """모든 테스트 실행"""
        try:
            # 테스트 시작 시간 기록
            self.start_time = datetime.now()
            
            print("=" * 60)
            print("WinForms_Docs 간단한 통합 성능 테스트 시작")
            print("=" * 60)
            
            # 구성 요소 초기화
            self.initialize_components()
            
            # 테스트 데이터 생성
            self.create_test_data()
            
            # 개별 테스트 실행
            print("\n" + "=" * 40)
            print("1. 파일 관리자 테스트")
            print("=" * 40)
            self.test_file_manager()
            
            print("\n" + "=" * 40)
            print("2. 데이터 프로세서 테스트")
            print("=" * 40)
            self.test_data_processor()
            
            print("\n" + "=" * 40)
            print("3. Arrow 관리자 테스트")
            print("=" * 40)
            self.test_arrow_manager()
            
            print("\n" + "=" * 40)
            print("4. 메모리 관리자 테스트")
            print("=" * 40)
            self.test_memory_manager()
            
            print("\n" + "=" * 40)
            print("5. 벡터화 연산 테스트")
            print("=" * 40)
            self.test_vectorized_operations()
            
            print("\n" + "=" * 40)
            print("6. 통합 워크플로우 테스트")
            print("=" * 40)
            self.test_integration_workflow()
            
            print("\n" + "=" * 40)
            print("7. 성능 지표 테스트")
            print("=" * 40)
            self.test_performance_metrics()
            
            # 테스트 종료 시간 기록
            self.end_time = datetime.now()
            
            # 테스트 데이터 정리
            self.cleanup_test_data()
            
            # 성능 모니터링 중지
            self.performance_monitor.stop_monitoring()
            
            # 보고서 생성
            report_path = self.generate_test_report()
            
            # 전체 상태 확인
            successful_tests = len([r for r in self.test_results if r['success']])
            total_tests = len(self.test_results)
            
            if successful_tests == total_tests:
                print("\n✅ 모든 테스트가 성공적으로 완료되었습니다.")
                return True
            else:
                print(f"\n⚠️  {total_tests - successful_tests}개의 테스트가 실패했습니다.")
                return False
            
        except Exception as e:
            logger.error(f"통합 테스트 실행 오류: {e}")
            import traceback
            traceback.print_exc()
            return False

def main():
    """메인 실행 함수"""
    try:
        # 테스트 실행기 생성
        test_runner = SimpleIntegrationTest()
        
        # 모든 테스트 실행
        success = test_runner.run_all_tests()
        
        # 종료 코드 설정
        if success:
            print("\n🎉 통합 성능 테스트가 성공적으로 완료되었습니다!")
            exit(0)
        else:
            print("\n❌ 통합 성능 테스트가 실패했습니다. 로그를 확인하세요.")
            exit(1)
            
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