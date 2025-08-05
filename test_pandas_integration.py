"""
WinForms_Docs pandas 통합 시스템 통합 테스트

테스트 목적:
- PandasDataProcessor, VectorizedOperations 클래스의 기능 검증
- 기존 시스템(data_cleaner.py, data_normalizer.py, deduplication.py)과의 통합 검증
- AsyncFileManager와의 데이터 파이프라인 연동 검증
- 메모리 관리 최적화 성능 검증
- 성능 모니터링 기능 검증

성능 목표:
- 텍스트 처리 속도: 기존 대비 200-300% 향상
- 메모리 사용량: 30-50% 감소
- 중복 검출 속도: 기존 대비 400-500% 향상
- 대용량 파일 처리: 기존 대비 150-200% 향상
"""

import asyncio
import time
import logging
import json
import pandas as pd
import numpy as np
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime

# 테스트용 모듈 임포트
from pandas_data_processor import PandasDataProcessor, create_pandas_processor
from vectorized_operations import VectorizedOperations, create_vectorized_operations
from async_file_manager import AsyncFileManager
from data_cleaner import DataCleaner
from data_normalizer import DataNormalizer
from deduplication import Deduplicator

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PandasIntegrationTest:
    """pandas 통합 시스템 통합 테스트 클래스"""
    
    def __init__(self):
        self.test_results = {}
        self.performance_baseline = {}
        self.test_data_dir = Path("test_data")
        self.test_results_dir = Path("test_results")
        
        # 테스트 디렉토리 생성
        self.test_data_dir.mkdir(exist_ok=True)
        self.test_results_dir.mkdir(exist_ok=True)
        
        # 테스트 데이터 생성
        self._create_test_data()
        
    def _create_test_data(self):
        """테스트 데이터 생성"""
        logger.info("테스트 데이터 생성 시작")
        
        # 대용량 텍스트 데이터 생성
        test_documents = []
        for i in range(1000):  # 1000개 문서 생성
            document = {
                'file_path': f'test_document_{i:04d}.md',
                'content': f'''# 테스트 문서 {i+1}

이것은 테스트 문서입니다. {i+1}번째 문서입니다.

## 코드 예시
```python
def test_function_{i}():
    """테스트 함수 {i}"""
    print("Hello, World!")
    return True
```

## 설명
이 문서는 pandas 통합 시스템의 성능을 테스트하기 위한 데이터입니다.
문서 번호: {i+1}
생성 시간: {datetime.now().isoformat()}
''',
                'metadata': {
                    'document_id': i + 1,
                    'category': f'category_{i % 10}',
                    'tags': [f'tag_{j}' for j in range(3)],
                    'created_date': datetime.now().isoformat()
                }
            }
            test_documents.append(document)
        
        # 테스트 데이터 저장
        test_data_file = self.test_data_dir / 'test_documents.json'
        with open(test_data_file, 'w', encoding='utf-8') as f:
            json.dump(test_documents, f, ensure_ascii=False, indent=2)
        
        logger.info(f"테스트 데이터 생성 완료: {len(test_documents)}개 문서")
    
    def test_pandas_data_processor(self):
        """PandasDataProcessor 기능 테스트"""
        logger.info("PandasDataProcessor 기능 테스트 시작")
        
        start_time = time.time()
        
        try:
            # PandasDataProcessor 생성
            processor = create_pandas_processor(max_workers=4, chunk_size=100)
            
            # 테스트 데이터 로드
            test_data_file = self.test_data_dir / 'test_documents.json'
            with open(test_data_file, 'r', encoding='utf-8') as f:
                documents = json.load(f)
            
            # DataFrame으로 변환 테스트
            df = pd.DataFrame(documents)
            logger.info(f"DataFrame 변환 완료: {len(df)}행 {len(df.columns)}열")
            
            # 벡터화된 텍스트 처리 테스트
            vectorized_ops = create_vectorized_operations()
            df_processed = processor.vectorize_text_operations(df)
            logger.info(f"벡터화된 텍스트 처리 완료")
            
            # 메모리 최적화 테스트
            df_optimized = processor.optimize_memory_usage_advanced(df_processed)
            original_memory = df.memory_usage(deep=True).sum()
            optimized_memory = df_optimized.memory_usage(deep=True).sum()
            memory_reduction = (original_memory - optimized_memory) / original_memory * 100
            
            logger.info(f"메모리 최적화 완료: {memory_reduction:.1f}% 감소")
            
            # 성능 측정
            processing_time = time.time() - start_time
            
            self.test_results['pandas_data_processor'] = {
                'status': 'success',
                'processing_time': processing_time,
                'memory_reduction': memory_reduction,
                'rows_processed': len(df),
                'columns_processed': len(df.columns)
            }
            
            logger.info(f"PandasDataProcessor 테스트 완료: {processing_time:.3f}초")
            
        except Exception as e:
            logger.error(f"PandasDataProcessor 테스트 실패: {str(e)}")
            self.test_results['pandas_data_processor'] = {
                'status': 'failed',
                'error': str(e)
            }
    
    def test_vectorized_operations(self):
        """VectorizedOperations 기능 테스트"""
        logger.info("VectorizedOperations 기능 테스트 시작")
        
        start_time = time.time()
        
        try:
            # VectorizedOperations 생성
            vectorized_ops = create_vectorized_operations()
            
            # 테스트 데이터 생성
            test_texts = [
                "Hello, World! This is a test text.",
                "Python programming is awesome!",
                "Data processing with pandas is efficient.",
                "Vectorized operations improve performance significantly.",
                "This is another test text for validation."
            ] * 100  # 500개 텍스트 생성
            
            # 벡터화된 정규식 처리 테스트
            pattern = r'\b\w+\b'  # 단어 추출 패턴
            processed_texts = vectorized_ops.vectorized_regex_replace(
                pd.Series(test_texts), pattern
            )
            
            # 배치 텍스트 정규화 테스트
            normalized_texts = vectorized_ops.batch_text_normalization(
                pd.Series(test_texts)
            )
            
            # 성능 측정
            processing_time = time.time() - start_time
            
            self.test_results['vectorized_operations'] = {
                'status': 'success',
                'processing_time': processing_time,
                'texts_processed': len(test_texts),
                'operations_performed': ['regex_replace', 'text_normalization']
            }
            
            logger.info(f"VectorizedOperations 테스트 완료: {processing_time:.3f}초")
            
        except Exception as e:
            logger.error(f"VectorizedOperations 테스트 실패: {str(e)}")
            self.test_results['vectorized_operations'] = {
                'status': 'failed',
                'error': str(e)
            }
    
    def test_system_integration(self):
        """시스템 통합 테스트"""
        logger.info("시스템 통합 테스트 시작")
        
        start_time = time.time()
        
        try:
            # AsyncFileManager 생성 (pandas 통합 활성화)
            async_manager = AsyncFileManager(max_concurrent=5, io_workers=4, enable_pandas=True)
            
            # 데이터 클리너 생성
            data_cleaner = DataCleaner()
            
            # 데이터 정규화기 생성
            data_normalizer = DataNormalizer()
            
            # 중복 제거기 생성
            deduplicator = Deduplicator()
            
            # 테스트 데이터 로드
            test_data_file = self.test_data_dir / 'test_documents.json'
            with open(test_data_file, 'r', encoding='utf-8') as f:
                documents = json.load(f)
            
            # 데이터 처리 파이프라인 테스트
            processed_documents = []
            
            for doc in documents[:100]:  # 100개 문서만 테스트
                # 1. 데이터 클리닝
                cleaned_doc = data_cleaner.clean_document(doc)
                
                # 2. 데이터 정규화
                normalized_doc = data_normalizer.normalize_document(cleaned_doc)
                
                # 3. 중복 제거
                deduplicated_doc = deduplicator.remove_duplicates([normalized_doc])[0]
                
                processed_documents.append(deduplicated_doc)
            
            # 성능 측정
            processing_time = time.time() - start_time
            
            self.test_results['system_integration'] = {
                'status': 'success',
                'processing_time': processing_time,
                'documents_processed': len(processed_documents),
                'pipeline_steps': ['cleaning', 'normalization', 'deduplication']
            }
            
            logger.info(f"시스템 통합 테스트 완료: {processing_time:.3f}초")
            
        except Exception as e:
            logger.error(f"시스템 통합 테스트 실패: {str(e)}")
            self.test_results['system_integration'] = {
                'status': 'failed',
                'error': str(e)
            }
    
    def test_memory_management(self):
        """메모리 관리 최적화 테스트"""
        logger.info("메모리 관리 최적화 테스트 시작")
        
        start_time = time.time()
        
        try:
            # PandasDataProcessor 생성
            processor = create_pandas_processor(max_workers=4, chunk_size=100)
            
            # 대용량 데이터 생성 (10,000행)
            large_data = pd.DataFrame({
                'id': range(10000),
                'text': [f"Test text {i}" for i in range(10000)],
                'category': [f"category_{i % 100}" for i in range(10000)],
                'value': np.random.rand(10000) * 100
            })
            
            # 메모리 사용량 측정
            initial_memory = processor.get_memory_usage()
            
            # 메모리 최적화 적용
            optimized_data = processor.optimize_memory_usage_advanced(large_data.copy())
            
            # 최적화 후 메모리 사용량 측정
            final_memory = processor.get_memory_usage()
            
            # 청크 처리 테스트
            chunks = processor.manage_memory_chunks(large_data, max_chunk_size=1000)
            
            # 메모리 정리 테스트
            processor.cleanup_memory()
            
            # 성능 측정
            processing_time = time.time() - start_time
            
            self.test_results['memory_management'] = {
                'status': 'success',
                'processing_time': processing_time,
                'initial_memory_mb': initial_memory['rss'],
                'final_memory_mb': final_memory['rss'],
                'memory_reduction_percent': (initial_memory['rss'] - final_memory['rss']) / initial_memory['rss'] * 100,
                'chunks_created': len(chunks),
                'rows_processed': len(large_data)
            }
            
            logger.info(f"메모리 관리 최적화 테스트 완료: {processing_time:.3f}초")
            
        except Exception as e:
            logger.error(f"메모리 관리 최적화 테스트 실패: {str(e)}")
            self.test_results['memory_management'] = {
                'status': 'failed',
                'error': str(e)
            }
    
    def test_performance_monitoring(self):
        """성능 모니터링 테스트"""
        logger.info("성능 모니터링 테스트 시작")
        
        start_time = time.time()
        
        try:
            # PandasDataProcessor 생성
            processor = create_pandas_processor(max_workers=4, chunk_size=100)
            
            # 성능 모니터링 연동
            processor.integrate_performance_monitor(monitor_interval=1.0)
            
            # 가짜 데이터 처리로 성능 모니터링 트리거
            test_data = pd.DataFrame({
                'id': range(1000),
                'text': [f"Test text {i}" for i in range(1000)],
                'value': np.random.rand(1000) * 100
            })
            
            # 데이터 처리
            processed_data = processor.vectorize_text_operations(test_data)
            optimized_data = processor.optimize_memory_usage_advanced(processed_data)
            
            # 성능 지표 수집
            performance_metrics = processor.get_performance_metrics()
            
            # 성능 보고서 생성
            processor.log_performance_report()
            
            # 성능 측정
            processing_time = time.time() - start_time
            
            self.test_results['performance_monitoring'] = {
                'status': 'success',
                'processing_time': processing_time,
                'metrics_collected': len(performance_metrics),
                'memory_info_available': 'memory' in performance_metrics,
                'processing_info_available': 'processing' in performance_metrics,
                'report_generated': True
            }
            
            logger.info(f"성능 모니터링 테스트 완료: {processing_time:.3f}초")
            
        except Exception as e:
            logger.error(f"성능 모니터링 테스트 실패: {str(e)}")
            self.test_results['performance_monitoring'] = {
                'status': 'failed',
                'error': str(e)
            }
    
    def run_all_tests(self):
        """모든 테스트 실행"""
        logger.info("모든 테스트 실행 시작")
        
        test_start_time = time.time()
        
        # 개별 테스트 실행
        self.test_pandas_data_processor()
        self.test_vectorized_operations()
        self.test_system_integration()
        self.test_memory_management()
        self.test_performance_monitoring()
        
        # 전체 테스트 시간 측정
        total_test_time = time.time() - test_start_time
        
        # 테스트 결과 요약
        successful_tests = sum(1 for result in self.test_results.values() if result.get('status') == 'success')
        total_tests = len(self.test_results)
        
        # 테스트 결과 저장
        test_summary = {
            'test_timestamp': datetime.now().isoformat(),
            'total_test_time': total_test_time,
            'successful_tests': successful_tests,
            'total_tests': total_tests,
            'success_rate': successful_tests / total_tests * 100,
            'test_results': self.test_results
        }
        
        # 테스트 결과 파일 저장
        result_file = self.test_results_dir / f'pandas_integration_test_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        with open(result_file, 'w', encoding='utf-8') as f:
            json.dump(test_summary, f, ensure_ascii=False, indent=2)
        
        logger.info(f"모든 테스트 완료: {successful_tests}/{total_tests} 성공 ({successful_tests/total_tests*100:.1f}%)")
        logger.info(f"전체 테스트 시간: {total_test_time:.3f}초")
        logger.info(f"테스트 결과 저장: {result_file}")
        
        return test_summary
    
    def print_test_results(self):
        """테스트 결과 출력"""
        logger.info("=== 테스트 결과 요약 ===")
        
        for test_name, result in self.test_results.items():
            status = result.get('status', 'unknown')
            if status == 'success':
                logger.info(f"✓ {test_name}: 성공 ({result.get('processing_time', 0):.3f}초)")
            else:
                logger.error(f"✗ {test_name}: 실패 - {result.get('error', 'Unknown error')}")
        
        # 성능 개선 효과 요약
        if 'pandas_data_processor' in self.test_results:
            processor_result = self.test_results['pandas_data_processor']
            if processor_result.get('status') == 'success':
                memory_reduction = processor_result.get('memory_reduction', 0)
                logger.info(f"메모리 최적화 효과: {memory_reduction:.1f}% 감소")
        
        if 'memory_management' in self.test_results:
            memory_result = self.test_results['memory_management']
            if memory_result.get('status') == 'success':
                memory_reduction = memory_result.get('memory_reduction_percent', 0)
                logger.info(f"메모리 관리 효과: {memory_reduction:.1f}% 감소")

def main():
    """메인 테스트 실행 함수"""
    logger.info("WinForms_Docs pandas 통합 시스템 통합 테스트 시작")
    
    # 테스트 인스턴스 생성
    test = PandasIntegrationTest()
    
    # 모든 테스트 실행
    test_summary = test.run_all_tests()
    
    # 테스트 결과 출력
    test.print_test_results()
    
    # 테스트 결과 반환
    return test_summary

if __name__ == "__main__":
    # 테스트 실행
    summary = main()
    
    # 테스트 결과 출력
    print("\n" + "="*50)
    print("Pandas 통합 시스템 통합 테스트 완료")
    print("="*50)
    print(f"성공률: {summary['success_rate']:.1f}%")
    print(f"전체 테스트 시간: {summary['total_test_time']:.3f}초")
    print(f"성공한 테스트: {summary['successful_tests']}/{summary['total_tests']}")
    print("="*50)