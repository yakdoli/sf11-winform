"""
WinForms_Docs Apache Arrow 데이터 관리자 - 고성능 데이터 직렬화 및 메모리 관리

주요 기능:
==========
1. pandas ↔ Arrow 변환
   - zero-copy 변환을 통한 효율적인 데이터 타입 변환
   - 메모리 매핑을 통한 대용량 데이터 처리
   - 스키마 유지 및 최적화

2. Arrow 파일 관리
   - Arrow 파일 형식으로의 효율적인 저장/로드
   - 압축 옵션 지원 (snappy, lz4, zstd)
   - 메모리 매핑 기반 파일 읽기

3. 메모리 관리
   - Arrow 메모리 을 통한 효율적 메모리 할당
   - 청크 기반 대용량 데이터 처리
   - 가비지 컬렉션 최적화

4. 성능 최적화
   - 병렬 직렬화/역직렬화
   - SIMD 최적화를 통한 벡터화 연산
   - 컬럼형 저장 형식 활용

성능 향상 목표:
=============
- 직렬화/역직렬화 속도: 기존 대비 300-500% 향상
- 메모리 사용량: 추가 20-30% 감소
- 파일 크기: 압축을 통한 50-70% 감소
- 데이터 교환 속도: 시스템 간 전송 속도 200-300% 향상

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0 (Apache Arrow 데이터 관리 시스템)
"""

import asyncio
import logging
import time
import psutil
import gc
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any, Union, AsyncGenerator
from dataclasses import dataclass, asdict
from datetime import datetime
import hashlib
import json
import mmap
from concurrent.futures import ThreadPoolExecutor, as_completed

import pandas as pd
import numpy as np

# Apache Arrow 임포트
try:
    import pyarrow as pa
    import pyarrow.parquet as pq
    import pyarrow.feather as feather
    import pyarrow.csv as csv
    import pyarrow.json as json_arrow
    import pyarrow.compute as pc
    import pyarrow.memory_pool as mp
    ARROW_AVAILABLE = True
except ImportError:
    ARROW_AVAILABLE = False
    pa = None
    pq = None
    feather = None
    csv = None
    json_arrow = None
    pc = None
    mp = None

# 로컬 모듈 임포트
try:
    from pandas_data_processor import PandasDataProcessor
    from async_file_manager import AsyncFileManager
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    PandasDataProcessor = None
    AsyncFileManager = None

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
class ArrowStats:
    """Arrow 처리 통계 데이터 클래스"""
    total_conversions: int = 0
    successful_conversions: int = 0
    failed_conversions: int = 0
    total_processing_time: float = 0.0
    peak_memory_usage: float = 0.0
    average_conversion_time: float = 0.0
    memory_reduction: float = 0.0
    compression_ratio: float = 0.0
    serialization_speed: float = 0.0
    deserialization_speed: float = 0.0

@dataclass
class CompressionProfile:
    """압축 프로파일 데이터 클래스"""
    name: str
    algorithm: str
    compression_level: int
    enabled: bool = True

class ArrowDataManager:
    """Apache Arrow 데이터 관리자 - 핵심 Arrow 데이터 처리 시스템"""
    
    def __init__(self, memory_pool_size: int = 1024 * 1024 * 1024, compression_type: str = 'zstd'):
        if not ARROW_AVAILABLE:
            raise ImportError("Apache Arrow(pyarrow)가 설치되지 않았습니다. pip install pyarrow로 설치하세요.")
        
        self.arrow_tables: Dict[str, Any] = {}
        self.schema_cache: Dict[str, Any] = {}
        self.compression_type = compression_type
        
        # 메모리 풀 설정
        try:
            if ARROW_AVAILABLE and pa:
                self.memory_pool = pa.default_memory_pool()
                # 사용자 정의 메모리 풀 크기 설정 (Windows 11 최적화)
                self._configure_memory_pool(memory_pool_size)
            else:
                self.memory_pool = None
        except Exception as e:
            logger.warning(f"메모리 풀 생성 실패: {str(e)}")
            self.memory_pool = None
        
        # 압축 프로파일 설정
        self.compression_profiles = self._setup_compression_profiles()
        
        # 성능 통계
        self.stats = ArrowStats()
        self.process = psutil.Process()
        self.start_memory = self.process.memory_info().rss / 1024 / 1024  # MB
        self.peak_memory = self.start_memory
        
        # Windows 11 최적화
        self._windows_optimization()
        
        logger.info("ArrowDataManager 초기화 완료")
    
    def _configure_memory_pool(self, pool_size: int) -> None:
        """메모리 풀 크기 설정"""
        try:
            # Windows 11 환경에서 메모리 풀 최적화
            if self.memory_pool and hasattr(self.memory_pool, 'set_limit'):
                self.memory_pool.set_limit(pool_size * 1024 * 1024)  # MB to bytes
                logger.info(f"메모리 풀 크기 설정: {pool_size}MB")
        except Exception as e:
            logger.warning(f"메모리 풀 설정 실패: {str(e)}")
    
    def _windows_optimization(self) -> None:
        """Windows 11 환경 최적화"""
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            
            # Windows 환경에서 Arrow 최적화
            if hasattr(kernel32, 'SetProcessWorkingSetSize'):
                kernel32.SetProcessWorkingSetSize(
                    kernel32.GetCurrentProcess(),
                    -1,  # 최소 작업 집합 크기
                    -1   # 최대 작업 집합 크기
                )
                logger.info("Windows 11 Arrow 메모리 관리 최적화 적용")
            
        except Exception as e:
            logger.warning(f"Windows Arrow 최적화 적용 실패: {str(e)}")
    
    def _setup_compression_profiles(self) -> Dict[str, CompressionProfile]:
        """압축 프로파일 설정"""
        profiles = {
            'snappy': CompressionProfile('snappy', 'snappy', 1),
            'lz4': CompressionProfile('lz4', 'lz4', 4),
            'zstd': CompressionProfile('zstd', 'zstd', 6),
            'gzip': CompressionProfile('gzip', 'gzip', 6),
            'brotli': CompressionProfile('brotli', 'brotli', 4)
        }
        
        # 기본 활성화된 압축 설정
        enabled_profiles = ['zstd', 'lz4', 'snappy']
        for profile_name in enabled_profiles:
            if profile_name in profiles:
                profiles[profile_name].enabled = True
        
        return profiles
    
    async def pandas_to_arrow(self, df: pd.DataFrame, table_name: str = "default") -> Any:
        """pandas DataFrame을 Arrow Table로 비동기 변환"""
        start_time = time.time()
        
        try:
            # Arrow 사용 가능성 확인
            if not ARROW_AVAILABLE:
                logger.warning("Apache Arrow가 설치되지 않았습니다. pandas DataFrame을 그대로 반환합니다.")
                return df
            
            # 메모리 사용량 측정 전
            memory_before = self.process.memory_info().rss / 1024 / 1024  # MB
            
            # zero-copy 변환을 위한 스키마 최적화
            optimized_schema = self._optimize_schema_for_arrow(df)
            
            # DataFrame을 Arrow Table로 변환
            table = pa.Table.from_pandas(
                df,
                schema=optimized_schema,
                preserve_index=False,
                nthreads=min(psutil.cpu_count() or 1, 8)  # 병렬 처리
            )
            
            # 테이블 캐싱
            self.arrow_tables[table_name] = table
            
            # 메모리 사용량 측정 후
            memory_after = self.process.memory_info().rss / 1024 / 1024  # MB
            memory_increase = memory_after - memory_before
            
            # 처리 시간 계산
            processing_time = time.time() - start_time
            
            # 통계 업데이트
            self.stats.total_conversions += 1
            self.stats.successful_conversions += 1
            self.stats.total_processing_time += processing_time
            
            logger.debug(f"pandas → Arrow 변환 완료: {table_name}, "
                        f"행 수: {len(df)}, 처리 시간: {processing_time:.3f}s, "
                        f"메모리 증가: {memory_increase:.2f}MB")
            
            return table
            
        except Exception as e:
            logger.error(f"pandas → Arrow 변환 오류: {str(e)}")
            self.stats.total_conversions += 1
            self.stats.failed_conversions += 1
            # 오류 발생 시 원본 DataFrame 반환
            return df
    
    async def arrow_to_pandas(self, table: Any, table_name: str = "default") -> Any:
        """Arrow Table를 pandas DataFrame으로 비동기 변환"""
        start_time = time.time()
        
        try:
            # 메모리 사용량 측정 전
            memory_before = self.process.memory_info().rss / 1024 / 1024  # MB
            
            # Arrow Table를 DataFrame으로 변환
            if pa:
                df = table.to_pandas(
                    use_threads=True,
                    split_blocks=True,
                    self_destruct=True,
                    types_mapper=self._map_arrow_types_to_pandas
                )
            else:
                raise ImportError("Apache Arrow(pyarrow)가 설치되지 않았습니다.")
            
            # 메모리 사용량 측정 후
            memory_after = self.process.memory_info().rss / 1024 / 1024  # MB
            memory_increase = memory_after - memory_before
            
            # 처리 시간 계산
            processing_time = time.time() - start_time
            
            # 통계 업데이트
            self.stats.total_conversions += 1
            self.stats.successful_conversions += 1
            self.stats.total_processing_time += processing_time
            
            logger.debug(f"Arrow → pandas 변환 완료: {table_name}, "
                        f"행 수: {len(df)}, 처리 시간: {processing_time:.3f}s, "
                        f"메모리 증가: {memory_increase:.2f}MB")
            
            return df
            
        except Exception as e:
            logger.error(f"Arrow → pandas 변환 오류: {str(e)}")
            self.stats.total_conversions += 1
            self.stats.failed_conversions += 1
            raise
    
    def _optimize_schema_for_arrow(self, df: pd.DataFrame) -> Any:
        """Arrow를 위한 스키마 최적화"""
        fields = []
        
        for column_name, dtype in df.dtypes.items():
            # pandas dtype을 Arrow dtype으로 매핑
            arrow_type = self._map_pandas_type_to_arrow(dtype, df[column_name])
            fields.append(pa.field(column_name, arrow_type))
        
        return pa.schema(fields)
    
    def _map_pandas_type_to_arrow(self, dtype, series) -> Any:
        """pandas dtype을 Arrow dtype으로 매핑"""
        if pd.api.types.is_integer_dtype(dtype):
            # 정수형 최적화
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
        
        elif pd.api.types.is_float_dtype(dtype):
            # 실수형 최적화
            return pa.float32() if series.dtype == 'float32' else pa.float64()
        
        elif pd.api.types.is_bool_dtype(dtype):
            return pa.bool_()
        
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            return pa.timestamp('ns')
        
        elif pd.api.types.is_string_dtype(dtype):
            # 문자열 최적화
            unique_ratio = series.nunique() / len(series)
            if unique_ratio < 0.5:  # 고유값 비율이 50% 미만이면
                return pa.dictionary(pa.int32(), pa.string())
            else:
                return pa.string()
        
        elif pd.api.types.is_object_dtype(dtype):
            # 객체 타입 처리
            if series.apply(lambda x: isinstance(x, str)).all():
                unique_ratio = series.nunique() / len(series)
                if unique_ratio < 0.5:
                    return pa.dictionary(pa.int32(), pa.string())
                else:
                    return pa.string()
            else:
                return pa.string()
        
        else:
            # 기본 타입
            return pa.string()
    
    def _map_arrow_types_to_pandas(self, arrow_type: Any) -> Any:
        """Arrow dtype을 pandas dtype으로 매핑"""
        if pa.types.is_integer(arrow_type):
            if arrow_type.bit_width <= 8:
                return 'int8' if arrow_type.signed else 'uint8'
            elif arrow_type.bit_width <= 16:
                return 'int16' if arrow_type.signed else 'uint16'
            elif arrow_type.bit_width <= 32:
                return 'int32' if arrow_type.signed else 'uint32'
            else:
                return 'int64' if arrow_type.signed else 'uint64'
        
        elif pa.types.is_floating(arrow_type):
            return 'float32' if arrow_type.bit_width == 32 else 'float64'
        
        elif pa.types.is_boolean(arrow_type):
            return 'bool'
        
        elif pa.types.is_timestamp(arrow_type):
            return 'datetime64[ns]'
        
        elif pa.types.is_string(arrow_type):
            return 'string'
        
        elif pa.types.is_dictionary(arrow_type):
            return 'category'
        
        else:
            return 'object'
    
    async def save_arrow_file(self, table: Any, file_path: str,
                           compression: str = 'zstd', format: str = 'parquet') -> None:
        """Arrow Table를 파일로 저장"""
        start_time = time.time()
        
        try:
            compression = compression or self.compression_type
            file_path = Path(file_path)
            
            # 파일 확장자에 따른 형식 결정
            if format == 'auto':
                format = file_path.suffix.lower().lstrip('.')
            
            # 디렉토리 생성
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # 압축 옵션 설정
            compression_options = self._get_compression_options(compression)
            
            # 파일 크기 측정 전
            original_size = table.nbytes
            
            # 파일 저장
            if format == 'parquet':
                if pq:
                    pq.write_table(
                        table,
                        file_path,
                        compression=compression_options,
                        memory_map=True,
                        use_dictionary=True,
                        **self._get_parquet_write_options()
                    )
                else:
                    raise ImportError("Apache Arrow(pyarrow)가 설치되지 않았습니다.")
            elif format == 'feather':
                if feather:
                    feather.write_feather(
                        table,
                        file_path,
                        compression=compression_options,
                        **self._get_feather_write_options()
                    )
                else:
                    raise ImportError("Apache Arrow(pyarrow)가 설치되지 않았습니다.")
            elif format == 'arrow':
                if pa:
                    with pa.OSFile(str(file_path), 'wb') as f:
                        with pa.RecordBatchFileWriter(f, table.schema) as writer:
                            writer.write_table(table)
                else:
                    raise ImportError("Apache Arrow(pyarrow)가 설치되지 않았습니다.")
            else:
                raise ValueError(f"지원하지 않는 파일 형식: {format}")
            
            # 파일 크기 측정 후
            final_size = file_path.stat().st_size
            compression_ratio = (original_size - final_size) / original_size * 100 if original_size > 0 else 0
            
            # 처리 시간 계산
            processing_time = time.time() - start_time
            
            # 통계 업데이트
            self.stats.serialization_speed = original_size / processing_time / 1024 / 1024  # MB/s
            self.stats.compression_ratio = compression_ratio
            
            logger.info(f"Arrow 파일 저장 완료: {file_path}, "
                       f"원본 크기: {original_size/1024/1024:.2f}MB, "
                       f"저장 크기: {final_size/1024/1024:.2f}MB, "
                       f"압축률: {compression_ratio:.1f}%, "
                       f"처리 시간: {processing_time:.3f}s")
            
        except Exception as e:
            logger.error(f"Arrow 파일 저장 오류: {file_path}, {str(e)}")
            raise
    
    async def load_arrow_file(self, file_path: str, format: str = 'auto') -> Any:
        """파일을 Arrow Table로 로드"""
        start_time = time.time()
        
        try:
            file_path = Path(file_path)
            
            if not file_path.exists():
                raise FileNotFoundError(f"파일을 찾을 수 없음: {file_path}")
            
            # 파일 확장자에 따른 형식 결정
            if format == 'auto':
                format = file_path.suffix.lower().lstrip('.')
            
            # 파일 크기 측정
            file_size = file_path.stat().st_size
            
            # 파일 로드
            if format == 'parquet':
                if pq:
                    table = pq.read_table(
                        file_path,
                        memory_map=True,
                        **self._get_parquet_read_options()
                    )
                else:
                    raise ImportError("Apache Arrow(pyarrow)가 설치되지 않았습니다.")
            elif format == 'feather':
                if feather:
                    table = feather.read_table(
                        file_path,
                        memory_map=True,
                        **self._get_feather_read_options()
                    )
                else:
                    raise ImportError("Apache Arrow(pyarrow)가 설치되지 않았습니다.")
            elif format == 'arrow':
                # 메모리 매핑 기반 로드
                if self.enable_memory_mapping:
                    table = self._load_with_memory_mapping(file_path)
                else:
                    if pa:
                        if pa:
                            if pa:
                                with pa.memory_map(str(file_path), 'rb') as source:
                                    table = pa.ipc.open_file(source).read_all()
                            else:
                                raise ImportError("Apache Arrow(pyarrow)가 설치되지 않았습니다.")
                        else:
                            raise ImportError("Apache Arrow(pyarrow)가 설치되지 않았습니다.")
                    else:
                        raise ImportError("Apache Arrow(pyarrow)가 설치되지 않았습니다.")
            elif format == 'csv':
                table = csv.read_csv(
                    file_path,
                    memory_map=True,
                    **self._get_csv_read_options()
                )
            elif format == 'json':
                table = json_arrow.read_json(
                    file_path,
                    memory_map=True,
                    **self._get_json_read_options()
                )
            else:
                raise ValueError(f"지원하지 않는 파일 형식: {format}")
            
            # 처리 시간 계산
            processing_time = time.time() - start_time
            
            # 통계 업데이트
            self.stats.deserialization_speed = table.nbytes / processing_time / 1024 / 1024  # MB/s
            
            logger.info(f"Arrow 파일 로드 완료: {file_path}, "
                       f"테이블 크기: {table.nbytes/1024/1024:.2f}MB, "
                       f"행 수: {len(table)}, "
                       f"처리 시간: {processing_time:.3f}s")
            
            return table
            
        except Exception as e:
            logger.error(f"Arrow 파일 로드 오류: {file_path}, {str(e)}")
            raise
    
    def _get_compression_options(self, compression: str) -> Any:
        """압축 옵션 가져오기"""
        if compression not in self.compression_profiles:
            raise ValueError(f"지원하지 않는 압축 알고리즘: {compression}")
        
        profile = self.compression_profiles[compression]
        if not profile.enabled:
            raise ValueError(f"비활성화된 압축 알고리즘: {compression}")
        
        # Arrow 압축 옵션 설정
        if profile.algorithm == 'zstd':
            return 'ZSTD'
        elif profile.algorithm == 'lz4':
            return 'LZ4'
        elif profile.algorithm == 'snappy':
            return 'SNAPPY'
        elif profile.algorithm == 'gzip':
            return 'GZIP'
        elif profile.algorithm == 'brotli':
            return 'BROTLI'
        else:
            return None
    
    def _get_parquet_write_options(self) -> Dict[str, Any]:
        """Parquet 쓰기 옵션"""
        return {
            'write_statistics': True,
            'dictionary_encoding': True,
            'compression': 'ZSTD',
            'use_dictionary': True,
            'allow_truncated_timestamps': True,
            'coerce_timestamps': 'ms'
        }
    
    def _get_feather_write_options(self) -> Dict[str, Any]:
        """Feather 쓰기 옵션"""
        return {
            'compression': 'ZSTD',
            'chunksize': 1024 * 1024  # 1MB chunks
        }
    
    def _get_parquet_read_options(self) -> Dict[str, Any]:
        """Parquet 읽기 옵션"""
        return {
            'use_threads': True,
            'memory_map': True,
            'pre_buffer': True,
            'buffer_size': 1024 * 1024  # 1MB
        }
    
    def _get_feather_read_options(self) -> Dict[str, Any]:
        """Feather 읽기 옵션"""
        return {
            'use_threads': True,
            'memory_map': True,
            'pre_buffer': True
        }
    
    def _get_csv_read_options(self) -> Dict[str, Any]:
        """CSV 읽기 옵션"""
        return {
            'memory_map': True,
            'block_size': 1024 * 1024,  # 1MB
            'encoding': 'utf-8',
            'ignore_empty_lines': True,
            'skip_rows': 0,
            'autogenerate_column_names': False
        }
    
    def _get_json_read_options(self) -> Dict[str, Any]:
        """JSON 읽기 옵션"""
        return {
            'memory_map': True,
            'block_size': 1024 * 1024,  # 1MB
            'encoding': 'utf-8',
            'ignore_empty_lines': True
        }
    
    def get_memory_stats(self) -> Dict[str, float]:
        """메모리 통계 반환"""
        current_memory = self.process.memory_info().rss / 1024 / 1024  # MB
        self.peak_memory = max(self.peak_memory, current_memory)
        
        return {
            'current_memory_mb': current_memory,
            'peak_memory_mb': self.peak_memory,
            'start_memory_mb': self.start_memory,
            'memory_increase_mb': current_memory - self.start_memory,
            'available_memory_mb': psutil.virtual_memory().available / 1024 / 1024
        }
    
    def get_performance_stats(self) -> ArrowStats:
        """성능 통계 반환"""
        if self.stats.total_conversions > 0:
            self.stats.average_conversion_time = (
                self.stats.total_processing_time / self.stats.total_conversions
            )
        
        # 메모리 통계
        memory_stats = self.get_memory_stats()
        self.stats.peak_memory_usage = memory_stats['peak_memory_mb']
        
        return self.stats
    
    # 성능 최적화 메서드
    def _load_with_memory_mapping(self, file_path: str) -> Any:
        """메모리 매핑 기반 Arrow 파일 로드"""
        try:
            # 파일 크기 확인
            file_size = os.path.getsize(file_path)
            
            # 대용량 파일인 경우 청크 기반 로드
            if file_size > self.memory_threshold:
                return self._load_large_file_with_chunks(file_path)
            else:
                # 일반 파일은 한 번에 로드
                if pa:
                    with pa.memory_map(str(file_path), 'rb') as source:
                        return pa.ipc.open_file(source).read_all()
                else:
                    raise ImportError("Apache Arrow(pyarrow)가 설치되지 않았습니다.")
                    
        except Exception as e:
            logger.error(f"메모리 매핑 로드 오류: {file_path}, {str(e)}")
            raise
    
    def _load_large_file_with_chunks(self, file_path: str) -> Any:
        """대용량 파일 청크 기반 로드"""
        try:
            # 메모리 매핑을 통한 효율적 로드
            with pa.memory_mapped_file(file_path) as source:
                # 메모리 매핑을 통한 효율적 로드
                if pa:
                    table = pa.ipc.open_file(source).read_all()
                else:
                    raise ImportError("Apache Arrow(pyarrow)가 설치되지 않았습니다.")
                
                # 필요한 경우 청크로 분할
                if len(table) > self.chunk_size:
                    return self._process_large_table_in_chunks(table)
                else:
                    return table
                    
        except Exception as e:
            logger.error(f"대용량 파일 로드 오류: {file_path}, {str(e)}")
            raise
    
    def _process_large_table_in_chunks(self, table: Any) -> Any:
        """대용량 테이블 청크 기반 처리"""
        try:
            chunks = []
            for i in range(0, len(table), self.chunk_size):
                chunk = table.slice(i, min(self.chunk_size, len(table) - i))
                chunks.append(chunk)
            
            # 청크별 병렬 처리
            processed_chunks = []
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = [executor.submit(self._process_chunk, chunk) for chunk in chunks]
                
                for future in as_completed(futures):
                    try:
                        processed_chunk = future.result()
                        processed_chunks.append(processed_chunk)
                    except Exception as e:
                        logger.error(f"청크 처리 오류: {e}")
            
            # 처리된 청크 병합
            return pa.concat_tables(processed_chunks)
            
        except Exception as e:
            logger.error(f"대용량 테이블 처리 오류: {e}")
            raise
    
    def _process_chunk(self, chunk: Any) -> Any:
        """테이블 청크 처리"""
        try:
            # 스키마 최적화 적용
            if self.schema_optimizer:
                chunk = self.schema_optimizer.apply_compression_optimization(chunk)
            
            return chunk
            
        except Exception as e:
            logger.error(f"청크 처리 오류: {e}")
            return chunk
    
    def _calculate_optimal_chunk_size(self, table: Any) -> int:
        """최적 청크 크기 계산"""
        try:
            # 테이블 크기와 메모리 상태에 따라 동적 계산
            table_size = len(table)
            available_memory = psutil.virtual_memory().available
            
            # 기본 청크 크기 설정
            base_chunk_size = 100000  # 10만 행
            
            # 사용 가능한 메모리에 따라 조정
            if available_memory < 2 * 1024 * 1024 * 1024:  # 2GB 미만
                chunk_size = min(base_chunk_size, table_size // 4)
            elif available_memory < 4 * 1024 * 1024 * 1024:  # 4GB 미만
                chunk_size = min(base_chunk_size * 2, table_size // 2)
            else:
                chunk_size = min(base_chunk_size * 4, table_size)
            
            return max(1000, chunk_size)  # 최소 1000행 보장
            
        except Exception as e:
            logger.error(f"청크 크기 계산 오류: {e}")
            return 100000  # 기본값
    
    def _calculate_memory_savings(self) -> float:
        """메모리 절감량 계산"""
        try:
            if not hasattr(self, 'memory_stats'):
                return 0.0
            
            original_memory = self.memory_stats.get('original_memory', 0)
            optimized_memory = self.memory_stats.get('optimized_memory', 0)
            
            if original_memory > 0:
                return (original_memory - optimized_memory) / original_memory * 100
            return 0.0
            
        except Exception as e:
            logger.error(f"메모리 절감량 계산 오류: {e}")
            return 0.0
    
    def optimize_memory_usage(self) -> None:
        """메모리 사용량 최적화"""
        try:
            # 메모리 풀 최적화
            if self.memory_pool:
                self.memory_pool.clear()
            
            # 캐시 정리
            if len(self.arrow_tables) > 10:  # 테이블이 10개 이상이면
                # 가장 오래된 테이블 제거
                oldest_key = next(iter(self.arrow_tables))
                del self.arrow_tables[oldest_key]
                logger.info(f"메모리 최적화: 오래된 테이블 제거 - {oldest_key}")
            
            # 가비지 컬렉션 강제 실행
            gc.collect()
            
            logger.info("메모리 사용량 최적화 완료")
            
        except Exception as e:
            logger.error(f"메모리 최적화 오류: {e}")
    
    def enable_memory_mapping(self, enable: bool = True) -> None:
        """메모리 매핑 활성화/비활성화"""
        self.enable_memory_mapping = enable
        logger.info(f"메모리 매핑 {'활성화' if enable else '비활성화'}")
    
    def set_chunk_size(self, chunk_size: int) -> None:
        """청크 크기 설정"""
        self.chunk_size = max(1000, chunk_size)  # 최소 1000행 보장
        logger.info(f"청크 크기 설정: {self.chunk_size}")
    
    def set_memory_threshold(self, threshold: int) -> None:
        """메모리 임계값 설정 (MB)"""
        self.memory_threshold = threshold * 1024 * 1024  # MB to bytes
        logger.info(f"메모리 임계값 설정: {threshold}MB")
    
    # 상호운용성 지원 메서드
    def save_parquet_file(self, table: Any, file_path: str, compression: str = 'snappy') -> None:
        """Parquet 파일로 저장"""
        try:
            start_time = time.time()
            
            # 메모리 풀 관리
            if self.memory_pool:
                with self.memory_pool:
                    # Parquet 파일로 저장
                    pq.write_table(
                        table,
                        file_path,
                        compression=compression,
                        **self._get_parquet_write_options()
                    )
            else:
                # 기본 방식으로 저장
                pq.write_table(
                    table,
                    file_path,
                    compression=compression,
                    **self._get_parquet_write_options()
                )
            
            # 성능 모니터링
            save_duration = time.time() - start_time
            file_size = os.path.getsize(file_path) / 1024 / 1024  # MB
            
            self.performance_stats['save_operations'] += 1
            self.performance_stats['total_save_time'] += save_duration
            self.performance_stats['save_file_sizes'].append(file_size)
            
            logger.info(f"Parquet 파일 저장 완료: {file_path} ({file_size:.2f}MB, {save_duration:.3f}s)")
            
        except Exception as e:
            logger.error(f"Parquet 파일 저장 오류: {file_path}, {str(e)}")
            raise
    
    def save_feather_file(self, table: Any, file_path: str) -> None:
        """Feather 파일로 저장"""
        try:
            start_time = time.time()
            
            # 메모리 풀 관리
            if self.memory_pool:
                with self.memory_pool:
                    # Feather 파일로 저장
                    feather.write_table(
                        table,
                        file_path,
                        **self._get_feather_write_options()
                    )
            else:
                # 기본 방식으로 저장
                feather.write_table(
                    table,
                    file_path,
                    **self._get_feather_write_options()
                )
            
            # 성능 모니터링
            save_duration = time.time() - start_time
            file_size = os.path.getsize(file_path) / 1024 / 1024  # MB
            
            self.performance_stats['save_operations'] += 1
            self.performance_stats['total_save_time'] += save_duration
            self.performance_stats['save_file_sizes'].append(file_size)
            
            logger.info(f"Feather 파일 저장 완료: {file_path} ({file_size:.2f}MB, {save_duration:.3f}s)")
            
        except Exception as e:
            logger.error(f"Feather 파일 저장 오류: {file_path}, {str(e)}")
            raise
    
    def load_parquet_file(self, file_path: str) -> Any:
        """Parquet 파일에서 로드"""
        try:
            start_time = time.time()
            
            # 메모리 매핑 기반 로드
            if self.enable_memory_mapping:
                table = pq.read_table(
                    file_path,
                    memory_map=True,
                    **self._get_parquet_read_options()
                )
            else:
                # 메모리 풀 관리
                if self.memory_pool:
                    with self.memory_pool:
                        table = pq.read_table(
                            file_path,
                            memory_map=True,
                            **self._get_parquet_read_options()
                        )
                else:
                    # 기본 방식으로 로드
                    table = pq.read_table(
                        file_path,
                        memory_map=True,
                        **self._get_parquet_read_options()
                    )
            
            # 성능 모니터링
            load_duration = time.time() - start_time
            table_size = table.nbytes / 1024 / 1024  # MB
            
            self.performance_stats['load_operations'] += 1
            self.performance_stats['total_load_time'] += load_duration
            self.performance_stats['load_table_sizes'].append(table_size)
            
            logger.info(f"Parquet 파일 로드 완료: {file_path} ({table_size:.2f}MB, {load_duration:.3f}s)")
            
            return table
            
        except Exception as e:
            logger.error(f"Parquet 파일 로드 오류: {file_path}, {str(e)}")
            raise
    
    def load_feather_file(self, file_path: str) -> Any:
        """Feather 파일에서 로드"""
        try:
            start_time = time.time()
            
            # 메모리 매핑 기반 로드
            if self.enable_memory_mapping:
                table = feather.read_table(
                    file_path,
                    memory_map=True,
                    **self._get_feather_read_options()
                )
            else:
                # 메모리 풀 관리
                if self.memory_pool:
                    with self.memory_pool:
                        table = feather.read_table(
                            file_path,
                            memory_map=True,
                            **self._get_feather_read_options()
                        )
                else:
                    # 기본 방식으로 로드
                    table = feather.read_table(
                        file_path,
                        memory_map=True,
                        **self._get_feather_read_options()
                    )
            
            # 성능 모니터링
            load_duration = time.time() - start_time
            table_size = table.nbytes / 1024 / 1024  # MB
            
            self.performance_stats['load_operations'] += 1
            self.performance_stats['total_load_time'] += load_duration
            self.performance_stats['load_table_sizes'].append(table_size)
            
            logger.info(f"Feather 파일 로드 완료: {file_path} ({table_size:.2f}MB, {load_duration:.3f}s)")
            
            return table
            
        except Exception as e:
            logger.error(f"Feather 파일 로드 오류: {file_path}, {str(e)}")
            raise
    
    def convert_to_parquet(self, table: Any, output_path: str, compression: str = 'snappy') -> None:
        """Arrow 테이블을 Parquet로 변환"""
        try:
            start_time = time.time()
            
            # 스키마 최적화 적용
            if self.schema_optimizer:
                table = self.schema_optimizer.apply_compression_optimization(table)
            
            # Parquet로 변환 및 저장
            self.save_parquet_file(table, output_path, compression)
            
            # 성능 모니터링
            conversion_duration = time.time() - start_time
            original_size = table.nbytes
            converted_size = os.path.getsize(output_path)
            compression_ratio = (original_size - converted_size) / original_size * 100 if original_size > 0 else 0
            
            self.performance_stats['conversion_operations'] += 1
            self.performance_stats['total_conversion_time'] += conversion_duration
            self.performance_stats['compression_ratios'].append(compression_ratio)
            
            logger.info(f"Parquet 변환 완료: {output_path} ({compression_ratio:.1f}% 압축률, {conversion_duration:.3f}s)")
            
        except Exception as e:
            logger.error(f"Parquet 변환 오류: {output_path}, {str(e)}")
            raise
    
    def convert_to_feather(self, table: Any, output_path: str) -> None:
        """Arrow 테이블을 Feather로 변환"""
        try:
            start_time = time.time()
            
            # 스키마 최적화 적용
            if self.schema_optimizer:
                table = self.schema_optimizer.apply_compression_optimization(table)
            
            # Feather로 변환 및 저장
            self.save_feather_file(table, output_path)
            
            # 성능 모니터링
            conversion_duration = time.time() - start_time
            original_size = table.nbytes
            converted_size = os.path.getsize(output_path)
            compression_ratio = (original_size - converted_size) / original_size * 100 if original_size > 0 else 0
            
            self.performance_stats['conversion_operations'] += 1
            self.performance_stats['total_conversion_time'] += conversion_duration
            self.performance_stats['compression_ratios'].append(compression_ratio)
            
            logger.info(f"Feather 변환 완료: {output_path} ({compression_ratio:.1f}% 압축률, {conversion_duration:.3f}s)")
            
        except Exception as e:
            logger.error(f"Feather 변환 오류: {output_path}, {str(e)}")
            raise
    
    def _get_parquet_write_options(self) -> Dict[str, Any]:
        """Parquet 쓰기 옵션 반환"""
        return {
            'compression': self.compression_type,
            'write_statistics': True,
            'use_dictionary': True,
            'allow_truncated_timestamps': True,
            'coerce_timestamps': 'ms'
        }
    
    def _get_parquet_read_options(self) -> Dict[str, Any]:
        """Parquet 읽기 옵션 반환"""
        return {
            'use_pandas_metadata': True,
            'memory_map': True,
            'pre_buffer': True,
            'buffer_size': 1024 * 1024  # 1MB
        }
    
    def _get_feather_write_options(self) -> Dict[str, Any]:
        """Feather 쓰기 옵션 반환"""
        return {
            'compression': self.compression_type,
            'use_pandas_metadata': True,
            'version': 2  # 최신 버전
        }
    
    def _get_feather_read_options(self) -> Dict[str, Any]:
        """Feather 읽기 옵션 반환"""
        return {
            'use_pandas_metadata': True,
            'memory_map': True,
            'pre_buffer': True,
            'buffer_size': 1024 * 1024  # 1MB
        }
    
    def validate_schema_compatibility(self, table: Any, target_format: str) -> bool:
        """스키마 호환성 검증"""
        try:
            if target_format.lower() == 'parquet':
                # Parquet 호환성 검증
                for field in table.schema:
                    # Parquet가 지원하지 않는 데이터 타입 확인
                    if pa.types.is_binary(field.type) or pa.types.is_fixed_size_binary(field.type):
                        logger.warning(f"Parquet 호환성 문제: {field.name} - {field.type}")
                        return False
            elif target_format.lower() == 'feather':
                # Feather 호환성 검증
                for field in table.schema:
                    # Feather가 지원하지 않는 데이터 타입 확인
                    if pa.types.is_timestamp(field.type, 'ns'):
                        logger.warning(f"Feather 호환성 문제: {field.name} - {field.type}")
                        return False
            
            return True
            
        except Exception as e:
            logger.error(f"스키마 호환성 검증 오류: {e}")
            return False
    
    def clear_cache(self) -> None:
        """캐시 정리"""
        self.arrow_tables.clear()
        self.schema_cache.clear()
        
        # 메모리 풀 정리
        if hasattr(self.memory_pool, 'clear'):
            self.memory_pool.clear()
        
        # 가비지 컬렉션
        gc.collect()
        
        logger.info("Arrow 캐시 정리 완료")
    
    def optimize_memory_usage(self) -> None:
        """메모리 사용량 최적화"""
        try:
            # 메모리 풀 최적화
            if hasattr(self.memory_pool, 'release_unused'):
                self.memory_pool.release_unused()
            
            # Arrow 테이블 메모리 최적화
            for table_name, table in self.arrow_tables.items():
                if hasattr(table, 'release'):
                    table.release()
            
            # 가비지 컬렉션
            gc.collect()
            
            logger.info("Arrow 메모리 사용량 최적화 완료")
            
        except Exception as e:
            logger.error(f"메모리 최적화 오류: {str(e)}")
    
    def __del__(self):
        """소멸자"""
        try:
            self.clear_cache()
        except:
            pass

# 유틸리티 함수
def create_arrow_manager(memory_pool_size: int = None, compression_type: str = 'zstd') -> ArrowDataManager:
    """ArrowDataManager 인스턴스 생성"""
    return ArrowDataManager(memory_pool_size=memory_pool_size, compression_type=compression_type)

async def convert_pandas_to_arrow(df: pd.DataFrame, file_path: str, 
                                compression: str = 'zstd', format: str = 'parquet') -> Any:
    """pandas DataFrame을 Arrow 파일로 변환"""
    manager = create_arrow_manager()
    
    try:
        # DataFrame을 Arrow Table로 변환
        table = await manager.pandas_to_arrow(df)
        
        # 파일로 저장
        await manager.save_arrow_file(table, file_path, compression, format)
        
        return table
    finally:
        manager.clear_cache()

async def convert_arrow_to_pandas(file_path: str, format: str = 'auto') -> pd.DataFrame:
    """Arrow 파일을 pandas DataFrame으로 변환"""
    manager = create_arrow_manager()
    
    try:
        # 파일을 Arrow Table로 로드
        table = await manager.load_arrow_file(file_path, format)
        
        # DataFrame으로 변환
        df = await manager.arrow_to_pandas(table)
        
        return df
    finally:
        manager.clear_cache()

if __name__ == "__main__":
    # 테스트 코드
    async def test_arrow_manager():
        """ArrowDataManager 테스트"""
        try:
            # 테스트 데이터 생성
            test_data = {
                'id': range(1000),
                'name': [f'Item_{i}' for i in range(1000)],
                'value': np.random.rand(1000) * 100,
                'category': np.random.choice(['A', 'B', 'C'], 1000),
                'timestamp': pd.date_range('2025-01-01', periods=1000, freq='h')
            }
            
            df = pd.DataFrame(test_data)
            
            # ArrowManager 생성
            manager = create_arrow_manager(memory_pool_size=512, compression_type='zstd')
            
            # DataFrame → Arrow 변환 테스트
            print("pandas → Arrow 변환 테스트...")
            arrow_table = await manager.pandas_to_arrow(df, 'test_table')
            print(f"변환 완료: {len(arrow_table)}행, {len(arrow_table.schema)}열")
            
            # Arrow → DataFrame 변환 테스트
            print("Arrow → pandas 변환 테스트...")
            converted_df = await manager.arrow_to_pandas(arrow_table, 'test_table')
            print(f"변환 완료: {len(converted_df)}행")
            
            # 파일 저장 테스트
            print("파일 저장 테스트...")
            await manager.save_arrow_file(arrow_table, 'test_data.parquet', compression='zstd', format='parquet')
            print("Parquet 저장 완료")
            
            await manager.save_arrow_file(arrow_table, 'test_data.feather', compression='lz4', format='feather')
            print("Feather 저장 완료")
            
            # 파일 로드 테스트
            print("파일 로드 테스트...")
            loaded_table = await manager.load_arrow_file('test_data.parquet', format='parquet')
            print(f"Parquet 로드 완료: {len(loaded_table)}행")
            
            loaded_table = await manager.load_arrow_file('test_data.feather', format='feather')
            print(f"Feather 로드 완료: {len(loaded_table)}행")
            
            # 성능 통계 출력
            stats = manager.get_performance_stats()
            print("\n성능 통계:")
            print(f"총 변환 횟수: {stats.total_conversions}")
            print(f"성공 변환: {stats.successful_conversions}")
            print(f"실패 변환: {stats.failed_conversions}")
            print(f"평균 변환 시간: {stats.average_conversion_time:.3f}s")
            print(f"직렬화 속도: {stats.serialization_speed:.2f}MB/s")
            print(f"역직렬화 속도: {stats.deserialization_speed:.2f}MB/s")
            print(f"압축률: {stats.compression_ratio:.1f}%")
            
            # 메모리 통계 출력
            memory_stats = manager.get_memory_stats()
            print("\n메모리 통계:")
            print(f"현재 메모리: {memory_stats['current_memory_mb']:.2f}MB")
            print(f"최대 메모리: {memory_stats['peak_memory_mb']:.2f}MB")
            print(f"메모리 증가: {memory_stats['memory_increase_mb']:.2f}MB")
            
            # 정리
            manager.clear_cache()
            
        except Exception as e:
            print(f"테스트 오류: {str(e)}")
            import traceback
            traceback.print_exc()
    
    # 테스트 실행
    asyncio.run(test_arrow_manager())