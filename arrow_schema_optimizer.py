"""
WinForms_Docs Apache Arrow 스키마 최적화기 - 데이터 타입 및 스키마 자동 최적화

주요 기능:
==========
1. 데이터 타입 자동 최적화
   - int64 → int32, int16, int8로의 자동 다운캐스팅
   - string → category 타입 변환
   - float64 → float32로의 메모리 절약 변환
   - datetime 타입 최적화

2. 스키마 캠싱 및 재사용
   - 데이터 패턴 기반 스키마 캐싱
   - 유사 데이터 구조의 스키마 재사용
   - 스키마 버전 관리
   - 스키마 검증 및 호환성 확인

3. 압축 프로파일 최적화
   - 데이터 특성에 따른 최적 압축 알고리즘 선택
   - 압축 레벨 자동 조정
   - 압축 성능 벤치마킹
   - 저장 공간과 속도의 균형 최적화

4. 메모리 사용량 예측 및 조정
   - 데이터 크기 예측
   - 메모리 사용량 모니터링
   - 동적 메모리 할당
   - 메모리 누수 방지

성능 향상 목표:
=============
- 메모리 사용량: 추가 20-30% 감소
- 데이터 타입 최적화: 40-60% 메모리 절약
- 스키마 재사용: 50-70% 처리 시간 감소
- 압축 효율: 50-70% 파일 크기 감소

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0 (Apache Arrow 스키마 최적화 시스템)
"""

import asyncio
import logging
import time
import json
import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any, Union, Callable
from dataclasses import dataclass, asdict
from datetime import datetime
import pickle
import psutil
import gc

import pandas as pd
import numpy as np

# Apache Arrow 임포트
try:
    import pyarrow as pa
    import pyarrow.parquet as pq
    import pyarrow.feather as feather
    from pyarrow import compute as pc
    ARROW_AVAILABLE = True
except ImportError:
    ARROW_AVAILABLE = False
    pa = None
    pq = None
    feather = None
    pc = None

# 로컬 모듈 임포트
try:
    from arrow_data_manager import ArrowDataManager, CompressionProfile
    ARROW_MANAGER_AVAILABLE = True
except ImportError:
    ARROW_MANAGER_AVAILABLE = False
    ArrowDataManager = None
    CompressionProfile = None

# 로컬 설정 임포트
try:
    from config import (
        WINFORMS_DOCS_DIR, OUTPUT_DIR, BACKUP_DIR,
        PROCESSING_OPTIONS, LOGGING_CONFIG
    )
    CONFIG_AVAILABLE = True
except ImportError:
    CONFIG_AVAILABLE = False

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

@dataclass
class SchemaOptimizationResult:
    """스키마 최적화 결과 데이터 클래스"""
    original_schema: pa.Schema
    optimized_schema: pa.Schema
    memory_reduction: float
    type_optimizations: Dict[str, str]
    compression_savings: float
    processing_time: float
    schema_hash: str
    validation_passed: bool

@dataclass
class TypeOptimizationRule:
    """데이터 타입 최적화 규칙"""
    source_type: str
    target_type: str
    condition: Callable
    priority: int
    memory_savings: float
    description: str

@dataclass
class CompressionBenchmark:
    """압축 벤치마크 결과"""
    algorithm: str
    compression_level: int
    original_size: int
    compressed_size: int
    compression_ratio: float
    compression_time: float
    decompression_time: float
    memory_usage: float
    score: float

class ArrowSchemaOptimizer:
    """Apache Arrow 스키마 최적화기 - 핵심 스키마 최적화 시스템"""
    
    def __init__(self, cache_dir: str = None, enable_compression_benchmark: bool = True):
        if not ARROW_AVAILABLE:
            raise ImportError("Apache Arrow(pyarrow)가 설치되지 않았습니다. pip install pyarrow로 설치하세요.")
        
        self.cache_dir = Path(cache_dir) if cache_dir else Path.cwd() / '.arrow_cache'
        self.cache_dir.mkdir(exist_ok=True)
        
        # 타입 최적화 규칙
        self.type_optimization_rules = self._setup_type_optimization_rules()
        
        # 스키마 캐시
        self.schema_cache: Dict[str, pa.Schema] = {}
        self.type_inference_cache: Dict[str, pa.DataType] = {}
        
        # 압축 프로파일
        self.compression_profiles: Dict[str, CompressionProfile] = {}
        self.compression_benchmarks: List[CompressionBenchmark] = []
        
        # 최적화 결과 캐시
        self.optimization_results: Dict[str, SchemaOptimizationResult] = {}
        
        # 성능 모니터링
        self.process = psutil.Process()
        self.start_memory = self.process.memory_info().rss / 1024 / 1024  # MB
        self.peak_memory = self.start_memory
        
        # 압축 벤치마킹 활성화
        self.enable_compression_benchmark = enable_compression_benchmark
        
        # Windows 11 최적화
        self._windows_optimization()
        
        logger.info("ArrowSchemaOptimizer 초기화 완료")
    
    def _windows_optimization(self) -> None:
        """Windows 11 환경 최적화"""
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            
            # Windows 환경에서 스키마 최적화 설정
            if hasattr(kernel32, 'SetProcessWorkingSetSize'):
                kernel32.SetProcessWorkingSetSize(
                    kernel32.GetCurrentProcess(),
                    -1,  # 최소 작업 집합 크기
                    -1   # 최대 작업 집합 크기
                )
                logger.info("Windows 11 스키마 최적화 적용")
            
        except Exception as e:
            logger.warning(f"Windows 스키마 최적화 적용 실패: {str(e)}")
    
    def _setup_type_optimization_rules(self) -> List[TypeOptimizationRule]:
        """데이터 타입 최적화 규칙 설정"""
        rules = [
            # 정수형 최적화 규칙
            TypeOptimizationRule(
                source_type='int64',
                target_type='int32',
                condition=lambda series: series.min() >= -2147483648 and series.max() <= 2147483647,
                priority=1,
                memory_savings=0.5,
                description='int64 → int32 (32비트 범위 내)'
            ),
            TypeOptimizationRule(
                source_type='int64',
                target_type='int16',
                condition=lambda series: series.min() >= -32768 and series.max() <= 32767,
                priority=2,
                memory_savings=0.75,
                description='int64 → int16 (16비트 범위 내)'
            ),
            TypeOptimizationRule(
                source_type='int64',
                target_type='int8',
                condition=lambda series: series.min() >= -128 and series.max() <= 127,
                priority=3,
                memory_savings=0.875,
                description='int64 → int8 (8비트 범위 내)'
            ),
            TypeOptimizationRule(
                source_type='int64',
                target_type='uint32',
                condition=lambda series: series.min() >= 0 and series.max() <= 4294967295,
                priority=4,
                memory_savings=0.5,
                description='int64 → uint32 (양수 32비트 범위 내)'
            ),
            TypeOptimizationRule(
                source_type='int64',
                target_type='uint16',
                condition=lambda series: series.min() >= 0 and series.max() <= 65535,
                priority=5,
                memory_savings=0.75,
                description='int64 → uint16 (양수 16비트 범위 내)'
            ),
            TypeOptimizationRule(
                source_type='int64',
                target_type='uint8',
                condition=lambda series: series.min() >= 0 and series.max() <= 255,
                priority=6,
                memory_savings=0.875,
                description='int64 → uint8 (양수 8비트 범위 내)'
            ),
            
            # 실수형 최적화 규칙
            TypeOptimizationRule(
                source_type='float64',
                target_type='float32',
                condition=lambda series: True,  # 항상 적용 가능
                priority=7,
                memory_savings=0.5,
                description='float64 → float32 (메모리 절약)'
            ),
            
            # 문자열 최적화 규칙
            TypeOptimizationRule(
                source_type='string',
                target_type='dictionary',
                condition=lambda series: series.nunique() / len(series) < 0.5,
                priority=8,
                memory_savings=0.3,
                description='string → dictionary (고유값 비율 < 50%)'
            ),
            TypeOptimizationRule(
                source_type='string',
                target_type='category',
                condition=lambda series: series.nunique() / len(series) < 0.3,
                priority=9,
                memory_savings=0.5,
                description='string → category (고유값 비율 < 30%)'
            ),
            
            # 불리언 최적화 규칙
            TypeOptimizationRule(
                source_type='bool',
                target_type='int8',
                condition=lambda series: True,  # 항상 적용 가능
                priority=10,
                memory_savings=0.875,
                description='bool → int8 (메모리 절약)'
            ),
            
            # 날짜/시간 최적화 규칙
            TypeOptimizationRule(
                source_type='timestamp[ns]',
                target_type='timestamp[ms]',
                condition=lambda series: True,  # 항상 적용 가능
                priority=11,
                memory_savings=0.75,
                description='timestamp[ns] → timestamp[ms] (밀리초 단위)'
            ),
        ]
        
        return sorted(rules, key=lambda x: x.priority)
    
    def optimize_schema(self, df: pd.DataFrame, schema_name: str = None) -> SchemaOptimizationResult:
        """DataFrame에 대한 최적화된 스키마 생성"""
        start_time = time.time()
        
        try:
            # 원본 스키마 생성
            original_schema = self._create_schema_from_dataframe(df)
            
            # 스키마 캐시 확인
            schema_hash = self._generate_schema_hash(df)
            cached_result = self.optimization_results.get(schema_hash)
            
            if cached_result and cached_result.validation_passed:
                logger.debug(f"캐시된 스키마 최적화 결과 사용: {schema_name or 'unnamed'}")
                return cached_result
            
            # 스키마 최적화 수행
            optimized_schema = self._apply_optimization_rules(df, original_schema)
            
            # 메모리 사용량 계산
            original_memory = self._estimate_schema_memory_usage(original_schema, len(df))
            optimized_memory = self._estimate_schema_memory_usage(optimized_schema, len(df))
            memory_reduction = (original_memory - optimized_memory) / original_memory * 100 if original_memory > 0 else 0
            
            # 타입 최적화 기록
            type_optimizations = self._get_type_optimizations(original_schema, optimized_schema)
            
            # 압축 절감량 예측
            compression_savings = self._estimate_compression_savings(optimized_schema)
            
            # 스키마 검증
            validation_passed = self._validate_schema(optimized_schema, df)
            
            # 결과 생성
            result = SchemaOptimizationResult(
                original_schema=original_schema,
                optimized_schema=optimized_schema,
                memory_reduction=memory_reduction,
                type_optimizations=type_optimizations,
                compression_savings=compression_savings,
                processing_time=time.time() - start_time,
                schema_hash=schema_hash,
                validation_passed=validation_passed
            )
            
            # 캐시 저장
            if schema_name:
                self.schema_cache[schema_name] = optimized_schema
            self.optimization_results[schema_hash] = result
            
            # 결과 로깅
            logger.info(f"스키마 최적화 완료: {schema_name or 'unnamed'}")
            logger.info(f"메모리 감소: {memory_reduction:.1f}%")
            logger.info(f"타입 최적화: {len(type_optimizations)}개")
            logger.info(f"압축 절감 예상: {compression_savings:.1f}%")
            logger.info(f"처리 시간: {result.processing_time:.3f}s")
            
            return result
            
        except Exception as e:
            logger.error(f"스키마 최적화 오류: {str(e)}")
            raise
    
    def _create_schema_from_dataframe(self, df: pd.DataFrame) -> pa.Schema:
        """DataFrame에서 Arrow 스키마 생성"""
        fields = []
        
        for column_name, dtype in df.dtypes.items():
            arrow_type = self._infer_arrow_type(dtype, df[column_name])
            fields.append(pa.field(column_name, arrow_type))
        
        return pa.schema(fields)
    
    def _infer_arrow_type(self, dtype, series) -> pa.DataType:
        """Arrow 데이터 타입 추론"""
        # 캐시 확인
        cache_key = f"{dtype}_{series.nunique()}_{len(series)}"
        if cache_key in self.type_inference_cache:
            return self.type_inference_cache[cache_key]
        
        # 타입 추론
        if pd.api.types.is_integer_dtype(dtype):
            arrow_type = self._optimize_integer_type(series)
        elif pd.api.types.is_float_dtype(dtype):
            arrow_type = self._optimize_float_type(series)
        elif pd.api.types.is_bool_dtype(dtype):
            arrow_type = pa.bool_()
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            arrow_type = pa.timestamp('ms')  # 밀리초 단위로 최적화
        elif pd.api.types.is_string_dtype(dtype):
            arrow_type = self._optimize_string_type(series)
        elif pd.api.types.is_object_dtype(dtype):
            arrow_type = self._optimize_object_type(series)
        else:
            arrow_type = pa.string()
        
        # 캐시 저장
        self.type_inference_cache[cache_key] = arrow_type
        
        return arrow_type
    
    def _optimize_integer_type(self, series: pd.Series) -> pa.DataType:
        """정수형 최적화"""
        min_val = series.min()
        max_val = series.max()
        
        if min_val >= 0:
            if max_val <= 255:
                return pa.uint8()
            elif max_val <= 65535:
                return pa.uint16()
            elif max_val <= 4294967295:
                return pa.uint32()
            else:
                return pa.uint64()
        else:
            if min_val >= -128 and max_val <= 127:
                return pa.int8()
            elif min_val >= -32768 and max_val <= 32767:
                return pa.int16()
            elif min_val >= -2147483648 and max_val <= 2147483647:
                return pa.int32()
            else:
                return pa.int64()
    
    def _optimize_float_type(self, series: pd.Series) -> pa.DataType:
        """실수형 최적화"""
        return pa.float32()  # float32로 최적화
    
    def _optimize_string_type(self, series: pd.Series) -> pa.DataType:
        """문자열 최적화"""
        unique_ratio = series.nunique() / len(series)
        
        if unique_ratio < 0.3:  # 고유값 비율이 30% 미만이면 category
            return pa.dictionary(pa.int32(), pa.string())
        elif unique_ratio < 0.5:  # 고유값 비율이 50% 미만이면 dictionary
            return pa.dictionary(pa.int32(), pa.string())
        else:
            return pa.string()
    
    def _optimize_object_type(self, series: pd.Series) -> pa.DataType:
        """객체 타입 최적화"""
        # 문자열인지 확인
        if series.apply(lambda x: isinstance(x, str)).all():
            return self._optimize_string_type(series)
        else:
            return pa.string()
    
    def _apply_optimization_rules(self, df: pd.DataFrame, schema: pa.Schema) -> pa.Schema:
        """최적화 규칙 적용"""
        optimized_fields = []
        
        for field in schema:
            column_name = field.name
            if column_name in df.columns:
                series = df[column_name]
                optimized_type = self._apply_type_optimization_rules(series, field.type)
                optimized_fields.append(pa.field(column_name, optimized_type))
            else:
                optimized_fields.append(field)
        
        return pa.schema(optimized_fields)
    
    def _apply_type_optimization_rules(self, series: pd.Series, current_type: pa.DataType) -> pa.DataType:
        """타입 최적화 규칙 적용"""
        for rule in self.type_optimization_rules:
            if self._matches_type(current_type, rule.source_type):
                if rule.condition(series):
                    logger.debug(f"타입 최적화 적용: {rule.description}")
                    return self._get_target_type(rule.target_type)
        
        return current_type
    
    def _matches_type(self, arrow_type: pa.DataType, source_type: str) -> bool:
        """타입 매칭 확인"""
        type_str = str(arrow_type)
        
        if source_type == 'int64' and 'int64' in type_str:
            return True
        elif source_type == 'int32' and 'int32' in type_str:
            return True
        elif source_type == 'int16' and 'int16' in type_str:
            return True
        elif source_type == 'int8' and 'int8' in type_str:
            return True
        elif source_type == 'uint64' and 'uint64' in type_str:
            return True
        elif source_type == 'uint32' and 'uint32' in type_str:
            return True
        elif source_type == 'uint16' and 'uint16' in type_str:
            return True
        elif source_type == 'uint8' and 'uint8' in type_str:
            return True
        elif source_type == 'float64' and 'float64' in type_str:
            return True
        elif source_type == 'float32' and 'float32' in type_str:
            return True
        elif source_type == 'bool' and 'bool' in type_str:
            return True
        elif source_type == 'string' and 'string' in type_str:
            return True
        elif source_type == 'timestamp' and 'timestamp' in type_str:
            return True
        elif source_type == 'dictionary' and 'dictionary' in type_str:
            return True
        elif source_type == 'category' and 'dictionary' in type_str:
            return True
        
        return False
    
    def _get_target_type(self, target_type: str) -> pa.DataType:
        """타겟 타입 가져오기"""
        type_map = {
            'int8': pa.int8(),
            'int16': pa.int16(),
            'int32': pa.int32(),
            'int64': pa.int64(),
            'uint8': pa.uint8(),
            'uint16': pa.uint16(),
            'uint32': pa.uint32(),
            'uint64': pa.uint64(),
            'float32': pa.float32(),
            'float64': pa.float64(),
            'bool': pa.bool_(),
            'string': pa.string(),
            'timestamp': pa.timestamp('ms'),
            'dictionary': pa.dictionary(pa.int32(), pa.string()),
            'category': pa.dictionary(pa.int32(), pa.string())
        }
        
        return type_map.get(target_type, pa.string())
    
    def _generate_schema_hash(self, df: pd.DataFrame) -> str:
        """스키마 해시 생성"""
        schema_data = {
            'columns': list(df.columns),
            'dtypes': {col: str(dtype) for col, dtype in df.dtypes.items()},
            'shape': df.shape,
            'memory_usage': df.memory_usage(deep=True).sum()
        }
        
        schema_str = json.dumps(schema_data, sort_keys=True)
        return hashlib.md5(schema_str.encode()).hexdigest()
    
    def _estimate_schema_memory_usage(self, schema: pa.Schema, row_count: int) -> int:
        """스키마 메모리 사용량 추정"""
        total_memory = 0
        
        for field in schema:
            type_name = field.type.name
            
            if type_name == 'int8':
                total_memory += row_count * 1
            elif type_name == 'int16':
                total_memory += row_count * 2
            elif type_name == 'int32':
                total_memory += row_count * 4
            elif type_name == 'int64':
                total_memory += row_count * 8
            elif type_name == 'uint8':
                total_memory += row_count * 1
            elif type_name == 'uint16':
                total_memory += row_count * 2
            elif type_name == 'uint32':
                total_memory += row_count * 4
            elif type_name == 'uint64':
                total_memory += row_count * 8
            elif type_name == 'float32':
                total_memory += row_count * 4
            elif type_name == 'float64':
                total_memory += row_count * 8
            elif type_name == 'bool':
                total_memory += row_count * 1
            elif type_name == 'string':
                total_memory += row_count * 32  # 평균 문자열 길이 가정
            elif type_name == 'timestamp':
                total_memory += row_count * 8
            elif type_name == 'dictionary':
                total_memory += row_count * 4 + row_count * 16  # 인덱스 + 값
            else:
                total_memory += row_count * 32  # 기본값
        
        return total_memory
    
    def _get_type_optimizations(self, original_schema: pa.Schema, optimized_schema: pa.Schema) -> Dict[str, str]:
        """타입 최적화 기록"""
        optimizations = {}
        
        for orig_field, opt_field in zip(original_schema, optimized_schema):
            if orig_field.type != opt_field.type:
                optimizations[orig_field.name] = f"{orig_field.type} → {opt_field.type}"
        
        return optimizations
    
    def _estimate_compression_savings(self, schema: pa.Schema) -> float:
        """압축 절감량 추정"""
        # 데이터 타입에 따른 압축 효율 추정
        compression_factors = {
            'int8': 0.7,
            'int16': 0.6,
            'int32': 0.5,
            'int64': 0.4,
            'uint8': 0.7,
            'uint16': 0.6,
            'uint32': 0.5,
            'uint64': 0.4,
            'float32': 0.5,
            'float64': 0.4,
            'bool': 0.8,
            'string': 0.3,
            'timestamp': 0.4,
            'dictionary': 0.2
        }
        
        total_compression = 0
        field_count = 0
        
        for field in schema:
            type_name = field.type.name
            if type_name in compression_factors:
                total_compression += compression_factors[type_name]
                field_count += 1
        
        return (total_compression / field_count * 100) if field_count > 0 else 0
    
    def _validate_schema(self, schema: pa.Schema, df: pd.DataFrame) -> bool:
        """스키마 검증"""
        try:
            # 스키마와 DataFrame의 열 수 확인
            if len(schema) != len(df.columns):
                return False
            
            # 각 필드 타입 검증
            for field, column_name in zip(schema, df.columns):
                if field.name != column_name:
                    return False
            
            # 스키마 직렬화/역직렬화 테스트
            serialized = schema.serialize()
            deserialized = pa.schema.deserialize(serialized)
            
            return schema.equals(deserialized)
            
        except Exception as e:
            logger.warning(f"스키마 검증 실패: {str(e)}")
            return False
    
    def benchmark_compression_algorithms(self, data: Union[pd.DataFrame, pa.Table], 
                                       algorithms: List[str] = None) -> List[CompressionBenchmark]:
        """압축 알고리즘 벤치마킹"""
        if not self.enable_compression_benchmark:
            logger.info("압축 벤치마킹이 비활성화되어 있습니다.")
            return []
        
        if algorithms is None:
            algorithms = ['zstd', 'lz4', 'snappy', 'gzip']
        
        if isinstance(data, pd.DataFrame):
            table = pa.Table.from_pandas(data)
        else:
            table = data
        
        benchmarks = []
        original_size = table.nbytes
        
        for algorithm in algorithms:
            try:
                start_time = time.time()
                
                # 압축 테스트
                compressed_data = table.to_string(compression=algorithm.upper())
                compressed_size = len(compressed_data.encode('utf-8'))
                
                compression_time = time.time() - start_time
                
                # 압축 해제 테스트
                decompression_start = time.time()
                decompressed_data = pa.Table.from_string(compressed_data)
                decompression_time = time.time() - decompression_start
                
                # 메모리 사용량 측정
                memory_usage = self.process.memory_info().rss / 1024 / 1024
                
                # 점수 계산 (압축률, 속도, 메모리 사용량 종합)
                compression_ratio = (original_size - compressed_size) / original_size * 100
                score = (compression_ratio * 0.4 + 
                        (1 / compression_time) * 0.3 + 
                        (1 / memory_usage) * 0.3)
                
                benchmark = CompressionBenchmark(
                    algorithm=algorithm,
                    compression_level=6,
                    original_size=original_size,
                    compressed_size=compressed_size,
                    compression_ratio=compression_ratio,
                    compression_time=compression_time,
                    decompression_time=decompression_time,
                    memory_usage=memory_usage,
                    score=score
                )
                
                benchmarks.append(benchmark)
                
                logger.info(f"압축 벤치마킹 완료: {algorithm} - "
                           f"압축률: {compression_ratio:.1f}%, "
                           f"압축 시간: {compression_time:.3f}s, "
                           f"해제 시간: {decompression_time:.3f}s")
                
            except Exception as e:
                logger.warning(f"압축 벤치마킹 실패: {algorithm} - {str(e)}")
                continue
        
        # 벤치마크 결과 정렬
        benchmarks.sort(key=lambda x: x.score, reverse=True)
        
        # 최고 성능 알고리즘 저장
        if benchmarks:
            best_algorithm = benchmarks[0].algorithm
            if best_algorithm not in self.compression_profiles:
                self.compression_profiles[best_algorithm] = CompressionProfile(
                    name=best_algorithm,
                    algorithm=best_algorithm,
                    compression_level=6,
                    enabled=True
                )
        
        self.compression_benchmarks = benchmarks
        return benchmarks
    
    def get_optimal_compression_algorithm(self) -> str:
        """최적의 압축 알고리즘 반환"""
        if not self.compression_benchmarks:
            return 'zstd'  # 기본값
        
        return self.compression_benchmarks[0].algorithm
    
    def save_schema_cache(self, cache_file: str = None) -> None:
        """스키마 캐시 저장"""
        cache_file = cache_file or self.cache_dir / 'schema_cache.pkl'
        
        try:
            cache_data = {
                'schema_cache': self.schema_cache,
                'type_inference_cache': self.type_inference_cache,
                'optimization_results': {
                    k: asdict(v) for k, v in self.optimization_results.items()
                },
                'compression_profiles': {
                    k: asdict(v) for k, v in self.compression_profiles.items()
                }
            }
            
            with open(cache_file, 'wb') as f:
                pickle.dump(cache_data, f)
            
            logger.info(f"스키마 캐시 저장 완료: {cache_file}")
            
        except Exception as e:
            logger.error(f"스키마 캐시 저장 오류: {str(e)}")
    
    def load_schema_cache(self, cache_file: str = None) -> None:
        """스키마 캐시 로드"""
        cache_file = cache_file or self.cache_dir / 'schema_cache.pkl'
        
        try:
            if not cache_file.exists():
                logger.info("스키마 캐시 파일이 없습니다.")
                return
            
            with open(cache_file, 'rb') as f:
                cache_data = pickle.load(f)
            
            self.schema_cache = cache_data.get('schema_cache', {})
            self.type_inference_cache = cache_data.get('type_inference_cache', {})
            
            # 최적화 결과 복원
            self.optimization_results = {}
            for k, v in cache_data.get('optimization_results', {}).items():
                self.optimization_results[k] = SchemaOptimizationResult(**v)
            
            # 압축 프로파일 복원
            self.compression_profiles = {}
            for k, v in cache_data.get('compression_profiles', {}).items():
                self.compression_profiles[k] = CompressionProfile(**v)
            
            logger.info(f"스키마 캐시 로드 완료: {cache_file}")
            
        except Exception as e:
            logger.error(f"스키마 캐시 로드 오류: {str(e)}")
    
    def get_memory_stats(self) -> Dict[str, float]:
        """메모리 통계 반환"""
        current_memory = self.process.memory_info().rss / 1024 / 1024  # MB
        self.peak_memory = max(self.peak_memory, current_memory)
        
        return {
            'current_memory_mb': current_memory,
            'peak_memory_mb': self.peak_memory,
            'start_memory_mb': self.start_memory,
            'memory_increase_mb': current_memory - self.start_memory,
            'available_memory_mb': psutil.virtual_memory().available / 1024 / 1024,
            'cache_size_mb': len(self.schema_cache) * 0.1  # 추정치
        }
    
    def clear_cache(self) -> None:
        """캐시 정리"""
        self.schema_cache.clear()
        self.type_inference_cache.clear()
        self.optimization_results.clear()
        self.compression_benchmarks.clear()
        
        # 가비지 컬렉션
        gc.collect()
        
        logger.info("스키마 최적화 캐시 정리 완료")
    
    def optimize_memory_usage(self) -> None:
        """메모리 사용량 최적화"""
        try:
            # 캐시 크기 제한
            max_cache_size = 1000  # 최대 1000개 스키마 캐시
            
            if len(self.schema_cache) > max_cache_size:
                # 가장 오래된 캐시 제거
                oldest_keys = list(self.schema_cache.keys())[:len(self.schema_cache) - max_cache_size]
                for key in oldest_keys:
                    del self.schema_cache[key]
            
            # 타입 추론 캐시 정리
            if len(self.type_inference_cache) > 5000:
                oldest_keys = list(self.type_inference_cache.keys())[:len(self.type_inference_cache) - 5000]
                for key in oldest_keys:
                    del self.type_inference_cache[key]
            
            # 가비지 컬렉션
            gc.collect()
            
            logger.info("스키마 최적화 메모리 사용량 최적화 완료")
            
        except Exception as e:
            logger.error(f"메모리 최적화 오류: {str(e)}")
    
    def __del__(self):
        """소멸자"""
        try:
            self.clear_cache()
        except:
            pass

# 유틸리티 함수
def create_schema_optimizer(cache_dir: str = None, enable_compression_benchmark: bool = True) -> ArrowSchemaOptimizer:
    """ArrowSchemaOptimizer 인스턴스 생성"""
    return ArrowSchemaOptimizer(cache_dir=cache_dir, enable_compression_benchmark=enable_compression_benchmark)

def optimize_dataframe_schema(df: pd.DataFrame, cache_dir: str = None) -> SchemaOptimizationResult:
    """DataFrame 스키마 최적화"""
    optimizer = create_schema_optimizer(cache_dir)
    
    try:
        result = optimizer.optimize_schema(df)
        return result
    finally:
        optimizer.clear_cache()

if __name__ == "__main__":
    # 테스트 코드
    def test_schema_optimizer():
        """ArrowSchemaOptimizer 테스트"""
        try:
            # 테스트 데이터 생성
            test_data = {
                'id': range(10000),
                'small_int': np.random.randint(0, 100, 10000),
                'medium_int': np.random.randint(-1000, 1000, 10000),
                'large_int': np.random.randint(-1000000, 1000000, 10000),
                'float_values': np.random.rand(10000) * 1000,
                'string_values': [f'Category_{i % 10}' for i in range(10000)],
                'text_values': [f'Text content {i} ' * 5 for i in range(10000)],
                'boolean_values': np.random.choice([True, False], 10000),
                'timestamp_values': pd.date_range('2025-01-01', periods=10000, freq='h')
            }
            
            df = pd.DataFrame(test_data)
            
            # 스키마 최적화기 생성
            optimizer = create_schema_optimizer(cache_dir='./test_cache')
            
            # 스키마 최적화 테스트
            print("스키마 최적화 테스트...")
            result = optimizer.optimize_schema(df, 'test_schema')
            
            print(f"원본 스키마: {result.original_schema}")
            print(f"최적화된 스키마: {result.optimized_schema}")
            print(f"메모리 감소: {result.memory_reduction:.1f}%")
            print(f"타입 최적화: {result.type_optimizations}")
            print(f"압축 절감 예상: {result.compression_savings:.1f}%")
            print(f"처리 시간: {result.processing_time:.3f}s")
            
            # 압축 벤치마킹 테스트
            print("\n압축 벤치마킹 테스트...")
            benchmarks = optimizer.benchmark_compression_algorithms(df)
            
            for benchmark in benchmarks:
                print(f"알고리즘: {benchmark.algorithm}")
                print(f"  압축률: {benchmark.compression_ratio:.1f}%")
                print(f"  압축 시간: {benchmark.compression_time:.3f}s")
                print(f"  해제 시간: {benchmark.decompression_time:.3f}s")
                print(f"  점수: {benchmark.score:.2f}")
            
            # 최적 압축 알고리즘 확인
            best_algorithm = optimizer.get_optimal_compression_algorithm()
            print(f"\n최적 압축 알고리즘: {best_algorithm}")
            
            # 캐시 저장 및 로드 테스트
            print("\n캐시 저장 테스트...")
            optimizer.save_schema_cache()
            
            print("캐시 로드 테스트...")
            new_optimizer = create_schema_optimizer(cache_dir='./test_cache')
            new_optimizer.load_schema_cache()
            
            # 메모리 통계 출력
            memory_stats = optimizer.get_memory_stats()
            print("\n메모리 통계:")
            print(f"현재 메모리: {memory_stats['current_memory_mb']:.2f}MB")
            print(f"최대 메모리: {memory_stats['peak_memory_mb']:.2f}MB")
            print(f"메모리 증가: {memory_stats['memory_increase_mb']:.2f}MB")
            print(f"캐시 크기: {memory_stats['cache_size_mb']:.2f}MB")
            
            # 정리
            optimizer.clear_cache()
            new_optimizer.clear_cache()
            
        except Exception as e:
            print(f"테스트 오류: {str(e)}")
            import traceback
            traceback.print_exc()
    
    # 테스트 실행
    test_schema_optimizer()