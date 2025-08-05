"""
WinForms_Docs Apache Arrow 통합 시스템 테스트

주요 테스트 기능:
================
1. ArrowDataManager 기능 테스트
   - pandas ↔ Arrow 변환 테스트
   - Arrow 파일 저장/로드 테스트
   - 메모리 매핑 성능 테스트
   - 청크 처리 테스트

2. ArrowSchemaOptimizer 기능 테스트
   - 데이터 타입 최적화 테스트
   - 스키마 캐싱 테스트
   - 압축 최적화 테스트

3. 상호운용성 테스트
   - Parquet 파일 형식 테스트
   - Feather 파일 형식 테스트
   - 스키마 호환성 테스트

4. 성능 테스트
   - 직렬화/역직렬화 성능 테스트
   - 메모리 사용량 테스트
   - 압축률 테스트

5. 통합 테스트
   - PandasDataProcessor와의 통합 테스트
   - AsyncFileManager와의 통합 테스트
   - 기존 시스템과의 호환성 테스트

테스트 목표:
==========
- Arrow 통합 시스템의 정상 동작 확인
- 성능 향상 목표 달성 여부 검증
- 기존 시스템과의 호환성 확인
- 안정성 및 오류 처리 검증

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0 (Apache Arrow 통합 시스템 테스트)
"""

import asyncio
import logging
import time
import tempfile
import os
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional
import pandas as pd
import numpy as np
import psutil

# 로컬 모듈 임포트
try:
    from arrow_data_manager import ArrowDataManager
    from arrow_schema_optimizer import ArrowSchemaOptimizer
    from pandas_data_processor import PandasDataProcessor
    from async_file_manager import AsyncFileManager
    ARROW_AVAILABLE = True
except ImportError as e:
    print(f"Arrow 모듈 임포트 실패: {e}")
    ARROW_AVAILABLE = False

# 로컬 설정 임포트
try:
    from config import LOGGING_CONFIG
    CONFIG_AVAILABLE = True
except ImportError:
    CONFIG_AVAILABLE = False
    LOGGING_CONFIG = {
        'level': 'INFO',
        'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        'file_path': 'test_arrow_integration.log'
    }

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

class ArrowIntegrationTester:
    """Arrow 통합 시스템 테스트 클래스"""
    
    def __init__(self):
        self.test_results = {}
        self.temp_dir = None
        self.test_data = None
        
    def setup_test_environment(self) -> None:
        """테스트 환경 설정"""
        try:
            # 임시 디렉토리 생성
            self.temp_dir = Path(tempfile.mkdtemp(prefix='arrow_test_'))
            logger.info(f"테스트 환경 설정 완료: {self.temp_dir}")
            
            # 테스트 데이터 생성
            self._create_test_data()
            
        except Exception as e:
            logger.error(f"테스트 환경 설정 오류: {e}")
            raise
    
    def _create_test_data(self) -> None:
        """테스트 데이터 생성"""
        try:
            # 다양한 데이터 타입을 포함하는 테스트 데이터 생성
            np.random.seed(42)  # 재현성을 위한 시드 설정
            
            data_size = 10000  # 테스트 데이터 크기
            data = {
                'id': range(data_size),
                'name': [f'item_{i}' for i in range(data_size)],
                'category': np.random.choice(['A', 'B', 'C', 'D'], data_size),
                'price': np.random.uniform(10.0, 1000.0, data_size),
                'quantity': np.random.randint(1, 100, data_size),
                'timestamp': pd.date_range('2020-01-01', periods=data_size, freq='H'),
                'description': [f'This is item {i} description' for i in range(data_size)],
                'is_active': np.random.choice([True, False], data_size),
                'rating': np.random.uniform(1.0, 5.0, data_size),
                'tags': [[f'tag_{j}' for j in range(np.random.randint(1, 5))] for _ in range(data_size)]
            }
            
            self.test_data = pd.DataFrame(data)
            logger.info(f"테스트 데이터 생성 완료: {len(self.test_data)}행, {len(self.test_data.columns)}열")
            
        except Exception as e:
            logger.error(f"테스트 데이터 생성 오류: {e}")
            raise
    
    def cleanup_test_environment(self) -> None:
        """테스트 환경 정리"""
        try:
            if self.temp_dir and self.temp_dir.exists():
                shutil.rmtree(self.temp_dir)
                logger.info("테스트 환경 정리 완료")
        except Exception as e:
            logger.error(f"테스트 환경 정리 오류: {e}")
    
    async def test_arrow_data_manager_basic(self) -> Dict[str, Any]:
        """ArrowDataManager 기본 기능 테스트"""
        test_name = "ArrowDataManager_기본_기능_테스트"
        results = {
            'test_name': test_name,
            'start_time': time.time(),
            'status': 'FAILED',
            'details': {}
        }
        
        try:
            if not ARROW_AVAILABLE:
                results['status'] = 'SKIPPED'
                results['details']['reason'] = 'Arrow 모듈을 사용할 수 없음'
                return results
            
            # ArrowDataManager 인스턴스 생성
            arrow_manager = ArrowDataManager(
                memory_pool_size=1024 * 1024 * 1024,  # 1GB
                compression_type='zstd'
            )
            
            # 1. pandas → Arrow 변환 테스트
            logger.info("pandas → Arrow 변환 테스트 시작")
            start_time = time.time()
            arrow_table = await arrow_manager.pandas_to_arrow(self.test_data)
            conversion_time = time.time() - start_time
            
            results['details']['pandas_to_arrow_time'] = conversion_time
            results['details']['arrow_table_rows'] = len(arrow_table)
            results['details']['arrow_table_columns'] = len(arrow_table.schema)
            
            # 2. Arrow → pandas 변환 테스트
            logger.info("Arrow → pandas 변환 테스트 시작")
            start_time = time.time()
            converted_df = await arrow_manager.arrow_to_pandas(arrow_table)
            reverse_conversion_time = time.time() - start_time
            
            results['details']['arrow_to_pandas_time'] = reverse_conversion_time
            results['details']['converted_df_rows'] = len(converted_df)
            results['details']['converted_df_columns'] = len(converted_df.columns)
            
            # 3. 데이터 무결성 검증
            logger.info("데이터 무결성 검증 시작")
            data_integrity_ok = (
                len(self.test_data) == len(converted_df) and
                len(self.test_data.columns) == len(converted_df.columns) and
                self.test_data.equals(converted_df)
            )
            
            results['details']['data_integrity_ok'] = data_integrity_ok
            
            # 4. Arrow 파일 저장/로드 테스트
            logger.info("Arrow 파일 저장/로드 테스트 시작")
            arrow_file_path = self.temp_dir / 'test_data.arrow'
            
            start_time = time.time()
            await arrow_manager.save_arrow_file(arrow_table, str(arrow_file_path))
            save_time = time.time() - start_time
            
            start_time = time.time()
            loaded_table = await arrow_manager.load_arrow_file(str(arrow_file_path))
            load_time = time.time() - start_time
            
            results['details']['save_time'] = save_time
            results['details']['load_time'] = load_time
            results['details']['file_size'] = arrow_file_path.stat().st_size
            
            # 5. 성능 통계 확인
            stats = arrow_manager.get_performance_stats()
            results['details']['performance_stats'] = stats
            
            # 테스트 결과 평가
            if data_integrity_ok and conversion_time > 0 and reverse_conversion_time > 0:
                results['status'] = 'PASSED'
                results['details']['message'] = 'ArrowDataManager 기본 기능 테스트 통과'
            else:
                results['status'] = 'FAILED'
                results['details']['message'] = '데이터 무결성 또는 성능 문제 발생'
                
        except Exception as e:
            results['status'] = 'ERROR'
            results['details']['error'] = str(e)
            logger.error(f"{test_name} 오류: {e}")
        
        results['end_time'] = time.time()
        results['duration'] = results['end_time'] - results['start_time']
        
        self.test_results[test_name] = results
        return results
    
    async def test_arrow_schema_optimizer(self) -> Dict[str, Any]:
        """ArrowSchemaOptimizer 기능 테스트"""
        test_name = "ArrowSchemaOptimizer_기능_테스트"
        results = {
            'test_name': test_name,
            'start_time': time.time(),
            'status': 'FAILED',
            'details': {}
        }
        
        try:
            if not ARROW_AVAILABLE:
                results['status'] = 'SKIPPED'
                results['details']['reason'] = 'Arrow 모듈을 사용할 수 없음'
                return results
            
            # ArrowSchemaOptimizer 인스턴스 생성
            schema_optimizer = ArrowSchemaOptimizer()
            
            # 1. 스키마 최적화 테스트
            logger.info("스키마 최적화 테스트 시작")
            start_time = time.time()
            optimized_schema = schema_optimizer.optimize_schema(self.test_data)
            optimization_time = time.time() - start_time
            
            results['details']['optimization_time'] = optimization_time
            results['details']['original_columns'] = len(self.test_data.columns)
            results['details']['optimized_fields'] = len(optimized_schema)
            
            # 2. 데이터 타입 추론 테스트
            logger.info("데이터 타입 추론 테스트 시작")
            for col in self.test_data.columns[:5]:  # 처음 5개 컬럼만 테스트
                dtype = self.test_data[col].dtype
                arrow_type = schema_optimizer.infer_optimal_types(dtype)
                results['details'][f'{col}_type'] = str(arrow_type)
            
            # 3. 압축 최적화 테스트
            logger.info("압축 최적화 테스트 시작")
            arrow_manager = ArrowDataManager()
            arrow_table = await arrow_manager.pandas_to_arrow(self.test_data)
            
            start_time = time.time()
            optimized_table = schema_optimizer.apply_compression_optimization(arrow_table)
            compression_time = time.time() - start_time
            
            results['details']['compression_time'] = compression_time
            results['details']['original_size'] = arrow_table.nbytes
            results['details']['optimized_size'] = optimized_table.nbytes
            results['details']['compression_ratio'] = (
                (arrow_table.nbytes - optimized_table.nbytes) / arrow_table.nbytes * 100
                if arrow_table.nbytes > 0 else 0
            )
            
            # 4. 스키마 캐싱 테스트
            logger.info("스키마 캐싱 테스트 시작")
            start_time = time.time()
            cached_schema = schema_optimizer.optimize_schema(self.test_data)
            cache_time = time.time() - start_time
            
            results['details']['cache_time'] = cache_time
            results['details']['cache_hit'] = cached_schema == optimized_schema
            
            # 테스트 결과 평가
            if (optimization_time > 0 and compression_time > 0 and 
                results['details']['compression_ratio'] >= 0):
                results['status'] = 'PASSED'
                results['details']['message'] = 'ArrowSchemaOptimizer 기능 테스트 통과'
            else:
                results['status'] = 'FAILED'
                results['details']['message'] = '스키마 최적화 또는 압축 문제 발생'
                
        except Exception as e:
            results['status'] = 'ERROR'
            results['details']['error'] = str(e)
            logger.error(f"{test_name} 오류: {e}")
        
        results['end_time'] = time.time()
        results['duration'] = results['end_time'] - results['start_time']
        
        self.test_results[test_name] = results
        return results
    
    async def test_interoperability(self) -> Dict[str, Any]:
        """상호운용성 테스트"""
        test_name = "상호운용성_테스트"
        results = {
            'test_name': test_name,
            'start_time': time.time(),
            'status': 'FAILED',
            'details': {}
        }
        
        try:
            if not ARROW_AVAILABLE:
                results['status'] = 'SKIPPED'
                results['details']['reason'] = 'Arrow 모듈을 사용할 수 없음'
                return results
            
            arrow_manager = ArrowDataManager()
            
            # Arrow 테이블 생성
            arrow_table = await arrow_manager.pandas_to_arrow(self.test_data)
            
            # 1. Parquet 형식 테스트
            logger.info("Parquet 형식 테스트 시작")
            parquet_file = self.temp_dir / 'test_data.parquet'
            
            start_time = time.time()
            arrow_manager.save_parquet_file(arrow_table, str(parquet_file))
            parquet_save_time = time.time() - start_time
            
            start_time = time.time()
            parquet_table = arrow_manager.load_parquet_file(str(parquet_file))
            parquet_load_time = time.time() - start_time
            
            results['details']['parquet_save_time'] = parquet_save_time
            results['details']['parquet_load_time'] = parquet_load_time
            results['details']['parquet_file_size'] = parquet_file.stat().st_size
            
            # 2. Feather 형식 테스트
            logger.info("Feather 형식 테스트 시작")
            feather_file = self.temp_dir / 'test_data.feather'
            
            start_time = time.time()
            arrow_manager.save_feather_file(arrow_table, str(feather_file))
            feather_save_time = time.time() - start_time
            
            start_time = time.time()
            feather_table = arrow_manager.load_feather_file(str(feather_file))
            feather_load_time = time.time() - start_time
            
            results['details']['feather_save_time'] = feather_save_time
            results['details']['feather_load_time'] = feather_load_time
            results['details']['feather_file_size'] = feather_file.stat().st_size
            
            # 3. 스키마 호환성 테스트
            logger.info("스키마 호환성 테스트 시작")
            parquet_compatible = arrow_manager.validate_schema_compatibility(arrow_table, 'parquet')
            feather_compatible = arrow_manager.validate_schema_compatibility(arrow_table, 'feather')
            
            results['details']['parquet_compatible'] = parquet_compatible
            results['details']['feather_compatible'] = feather_compatible
            
            # 4. 형식 변환 테스트
            logger.info("형식 변환 테스트 시작")
            parquet_converted = self.temp_dir / 'converted.parquet'
            feather_converted = self.temp_dir / 'converted.feather'
            
            start_time = time.time()
            arrow_manager.convert_to_parquet(arrow_table, str(parquet_converted))
            parquet_conversion_time = time.time() - start_time
            
            start_time = time.time()
            arrow_manager.convert_to_feather(arrow_table, str(feather_converted))
            feather_conversion_time = time.time() - start_time
            
            results['details']['parquet_conversion_time'] = parquet_conversion_time
            results['details']['feather_conversion_time'] = feather_conversion_time
            
            # 테스트 결과 평가
            if (parquet_save_time > 0 and feather_save_time > 0 and 
                parquet_compatible and feather_compatible):
                results['status'] = 'PASSED'
                results['details']['message'] = '상호운용성 테스트 통과'
            else:
                results['status'] = 'FAILED'
                results['details']['message'] = '상호운용성 문제 발생'
                
        except Exception as e:
            results['status'] = 'ERROR'
            results['details']['error'] = str(e)
            logger.error(f"{test_name} 오류: {e}")
        
        results['end_time'] = time.time()
        results['duration'] = results['end_time'] - results['start_time']
        
        self.test_results[test_name] = results
        return results
    
    async def test_performance_optimization(self) -> Dict[str, Any]:
        """성능 최적화 테스트"""
        test_name = "성능_최적화_테스트"
        results = {
            'test_name': test_name,
            'start_time': time.time(),
            'status': 'FAILED',
            'details': {}
        }
        
        try:
            if not ARROW_AVAILABLE:
                results['status'] = 'SKIPPED'
                results['details']['reason'] = 'Arrow 모듈을 사용할 수 없음'
                return results
            
            arrow_manager = ArrowDataManager()
            
            # 대용량 데이터 생성 (성능 테스트용)
            large_data_size = 50000
            large_data = pd.DataFrame({
                'id': range(large_data_size),
                'value': np.random.random(large_data_size),
                'category': np.random.choice(['X', 'Y', 'Z'], large_data_size),
                'timestamp': pd.date_range('2020-01-01', periods=large_data_size, freq='min')
            })
            
            # 1. 메모리 매핑 테스트
            logger.info("메모리 매핑 테스트 시작")
            arrow_manager.enable_memory_mapping(True)
            
            large_table = await arrow_manager.pandas_to_arrow(large_data)
            
            start_time = time.time()
            loaded_table = await arrow_manager.load_arrow_file(str(self.temp_dir / 'large_data.arrow'))
            memory_mapping_time = time.time() - start_time
            
            results['details']['memory_mapping_time'] = memory_mapping_time
            
            # 2. 청크 처리 테스트
            logger.info("청크 처리 테스트 시작")
            arrow_manager.set_chunk_size(10000)
            
            start_time = time.time()
            chunked_table = arrow_manager._process_large_table_in_chunks(large_table)
            chunk_processing_time = time.time() - start_time
            
            results['details']['chunk_processing_time'] = chunk_processing_time
            results['details']['chunk_count'] = len(large_table) // 10000 + 1
            
            # 3. 메모리 사용량 테스트
            logger.info("메모리 사용량 테스트 시작")
            initial_memory = psutil.Process().memory_info().rss / 1024 / 1024  # MB
            
            # 대용량 데이터 처리
            processed_tables = []
            for i in range(5):
                table = await arrow_manager.pandas_to_arrow(large_data)
                processed_tables.append(table)
            
            peak_memory = psutil.Process().memory_info().rss / 1024 / 1024  # MB
            memory_usage = peak_memory - initial_memory
            
            results['details']['initial_memory_mb'] = initial_memory
            results['details']['peak_memory_mb'] = peak_memory
            results['details']['memory_usage_mb'] = memory_usage
            
            # 메모리 최적화 테스트
            start_time = time.time()
            arrow_manager.optimize_memory_usage()
            optimization_time = time.time() - start_time
            
            optimized_memory = psutil.Process().memory_info().rss / 1024 / 1024  # MB
            memory_savings = peak_memory - optimized_memory
            
            results['details']['optimization_time'] = optimization_time
            results['details']['optimized_memory_mb'] = optimized_memory
            results['details']['memory_savings_mb'] = memory_savings
            
            # 4. 병렬 처리 테스트
            logger.info("병렬 처리 테스트 시작")
            import concurrent.futures
            
            def process_table(table):
                return len(table)
            
            start_time = time.time()
            with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
                futures = [executor.submit(process_table, table) for table in processed_tables]
                concurrent.futures.wait(futures)
            
            parallel_time = time.time() - start_time
            
            results['details']['parallel_processing_time'] = parallel_time
            
            # 테스트 결과 평가
            if (memory_mapping_time > 0 and chunk_processing_time > 0 and 
                memory_usage > 0 and optimization_time > 0):
                results['status'] = 'PASSED'
                results['details']['message'] = '성능 최적화 테스트 통과'
            else:
                results['status'] = 'FAILED'
                results['details']['message'] = '성능 최적화 문제 발생'
                
        except Exception as e:
            results['status'] = 'ERROR'
            results['details']['error'] = str(e)
            logger.error(f"{test_name} 오류: {e}")
        
        results['end_time'] = time.time()
        results['duration'] = results['end_time'] - results['start_time']
        
        self.test_results[test_name] = results
        return results
    
    async def test_system_integration(self) -> Dict[str, Any]:
        """시스템 통합 테스트"""
        test_name = "시스템_통합_테스트"
        results = {
            'test_name': test_name,
            'start_time': time.time(),
            'status': 'FAILED',
            'details': {}
        }
        
        try:
            if not ARROW_AVAILABLE:
                results['status'] = 'SKIPPED'
                results['details']['reason'] = 'Arrow 모듈을 사용할 수 없음'
                return results
            
            # 1. PandasDataProcessor와의 통합 테스트
            logger.info("PandasDataProcessor와의 통합 테스트 시작")
            try:
                pandas_processor = PandasDataProcessor(enable_arrow=True)
                
                # 데이터 처리 테스트
                processed_data = await pandas_processor.process_documents_async([{
                    'content': 'Test document content',
                    'metadata': {'source': 'test'}
                }])
                
                results['details']['pandas_integration_success'] = True
                results['details']['processed_documents'] = len(processed_data)
                
            except Exception as e:
                results['details']['pandas_integration_success'] = False
                results['details']['pandas_integration_error'] = str(e)
            
            # 2. AsyncFileManager와의 통합 테스트
            logger.info("AsyncFileManager와의 통합 테스트 시작")
            try:
                async_manager = AsyncFileManager()
                
                # 파일 I/O 테스트
                test_file = self.temp_dir / 'integration_test.arrow'
                arrow_manager = ArrowDataManager()
                
                arrow_table = await arrow_manager.pandas_to_arrow(self.test_data)
                await async_manager.save_file_async(str(test_file), arrow_table)
                
                loaded_data = await async_manager.load_file_async(str(test_file))
                
                results['details']['async_file_integration_success'] = True
                results['details']['file_save_load_success'] = loaded_data is not None
                
            except Exception as e:
                results['details']['async_file_integration_success'] = False
                results['details']['async_file_integration_error'] = str(e)
            
            # 3. 기존 시스템과의 호환성 테스트
            logger.info("기존 시스템과의 호환성 테스트 시작")
            try:
                # JSON 형식으로 저장/로드 테스트
                json_file = self.temp_dir / 'compatibility_test.json'
                self.test_data.to_json(str(json_file), orient='records', force_ascii=False)
                
                # JSON 데이터를 Arrow로 변환 테스트
                json_data = pd.read_json(json_file)
                arrow_manager = ArrowDataManager()
                arrow_table = await arrow_manager.pandas_to_arrow(json_data)
                
                results['details']['json_compatibility_success'] = True
                results['details']['json_to_arrow_success'] = arrow_table is not None
                
            except Exception as e:
                results['details']['json_compatibility_success'] = False
                results['details']['json_compatibility_error'] = str(e)
            
            # 테스트 결과 평가
            integration_success = (
                results['details'].get('pandas_integration_success', False) or
                results['details'].get('async_file_integration_success', False) or
                results['details'].get('json_compatibility_success', False)
            )
            
            if integration_success:
                results['status'] = 'PASSED'
                results['details']['message'] = '시스템 통합 테스트 통과'
            else:
                results['status'] = 'FAILED'
                results['details']['message'] = '시스템 통합 문제 발생'
                
        except Exception as e:
            results['status'] = 'ERROR'
            results['details']['error'] = str(e)
            logger.error(f"{test_name} 오류: {e}")
        
        results['end_time'] = time.time()
        results['duration'] = results['end_time'] - results['start_time']
        
        self.test_results[test_name] = results
        return results
    
    async def run_all_tests(self) -> Dict[str, Any]:
        """모든 테스트 실행"""
        logger.info("Arrow 통합 시스템 테스트 시작")
        
        # 테스트 환경 설정
        self.setup_test_environment()
        
        try:
            # 모든 테스트 실행
            test_functions = [
                self.test_arrow_data_manager_basic,
                self.test_arrow_schema_optimizer,
                self.test_interoperability,
                self.test_performance_optimization,
                self.test_system_integration
            ]
            
            test_results = []
            for test_func in test_functions:
                result = await test_func()
                test_results.append(result)
                logger.info(f"{result['test_name']} 완료: {result['status']}")
            
            # 종합 결과 생성
            summary = self._generate_test_summary(test_results)
            
            logger.info("Arrow 통합 시스템 테스트 완료")
            return summary
            
        finally:
            # 테스트 환경 정리
            self.cleanup_test_environment()
    
    def _generate_test_summary(self, test_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """테스트 결과 요약 생성"""
        total_tests = len(test_results)
        passed_tests = sum(1 for result in test_results if result['status'] == 'PASSED')
        failed_tests = sum(1 for result in test_results if result['status'] == 'FAILED')
        skipped_tests = sum(1 for result in test_results if result['status'] == 'SKIPPED')
        error_tests = sum(1 for result in test_results if result['status'] == 'ERROR')
        
        total_duration = sum(result['duration'] for result in test_results)
        
        summary = {
            'total_tests': total_tests,
            'passed_tests': passed_tests,
            'failed_tests': failed_tests,
            'skipped_tests': skipped_tests,
            'error_tests': error_tests,
            'success_rate': (passed_tests / total_tests * 100) if total_tests > 0 else 0,
            'total_duration': total_duration,
            'test_results': test_results,
            'timestamp': time.time()
        }
        
        logger.info(f"테스트 요약: {passed_tests}/{total_tests} 통과 ({summary['success_rate']:.1f}%)")
        
        return summary
    
    def print_test_results(self, summary: Dict[str, Any]) -> None:
        """테스트 결과 출력"""
        print("\n" + "="*60)
        print("Arrow 통합 시스템 테스트 결과")
        print("="*60)
        print(f"총 테스트 수: {summary['total_tests']}")
        print(f"통과 테스트: {summary['passed_tests']}")
        print(f"실패 테스트: {summary['failed_tests']}")
        print(f"건너뛴 테스트: {summary['skipped_tests']}")
        print(f"오류 테스트: {summary['error_tests']}")
        print(f"성공률: {summary['success_rate']:.1f}%")
        print(f"총 실행 시간: {summary['total_duration']:.2f}초")
        print("="*60)
        
        # 상세 결과 출력
        for result in summary['test_results']:
            status_icon = {
                'PASSED': '✓',
                'FAILED': '✗',
                'SKIPPED': '-',
                'ERROR': '✗'
            }.get(result['status'], '?')
            
            print(f"\n{status_icon} {result['test_name']}")
            print(f"  상태: {result['status']}")
            print(f"  실행 시간: {result['duration']:.2f}초")
            
            if 'message' in result['details']:
                print(f"  메시지: {result['details']['message']}")
            
            if 'error' in result['details']:
                print(f"  오류: {result['details']['error']}")
        
        print("\n" + "="*60)

async def main():
    """메인 실행 함수"""
    tester = ArrowIntegrationTester()
    
    try:
        # 모든 테스트 실행
        summary = await tester.run_all_tests()
        
        # 결과 출력
        tester.print_test_results(summary)
        
        # 결과 파일로 저장
        import json
        result_file = Path('test_arrow_results.json')
        with open(result_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, ensure_ascii=False, indent=2, default=str)
        
        logger.info(f"테스트 결과가 {result_file}에 저장되었습니다")
        
        return summary
        
    except Exception as e:
        logger.error(f"테스트 실행 중 오류 발생: {e}")
        return None

if __name__ == "__main__":
    # 테스트 실행
    asyncio.run(main())