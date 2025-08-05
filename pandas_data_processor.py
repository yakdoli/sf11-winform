"""
WinForms_Docs Pandas 데이터 처리기 - 벡터화된 데이터 처리 성능 최적화

주요 기능:
==========
1. 파일-DataFrame 변환
   - AsyncFileManager에서 읽은 파일 데이터를 효율적으로 pandas DataFrame으로 변환
   - 청크 기반 대용량 파일 처리 지원
   - 메모리 매핑을 통한 효율적인 데이터 로딩

2. 벡터화 텍스트 처리
   - pandas.Series.str 메서드를 활용한 벡터화된 텍스트 처리
   - 정규식 패턴의 벡터화된 적용
   - 배치 기반 텍스트 정규화 작업

3. 메모리 최적화
   - 효율적인 데이터 타입 선택 (category, int32 등)
   - DataFrame 청크 처리를 통한 메모리 관리
   - 가비지 컬렉션 최적화

4. 성능 모니터링
   - pandas 처리 성능 지표 수집
   - 메모리 사용량 실시간 추적
   - 벡터화 연산 효율성 측정

성능 향상 목표:
=============
- 텍스트 처리 속도: 기존 대비 200-300% 향상
- 메모리 사용량: 30-50% 감소
- 중복 검출 속도: 기존 대비 400-500% 향상
- 대용량 파일 처리: 기존 대비 150-200% 향상

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0 (Pandas 벡터화 처리 시스템)
"""

import pandas as pd
import numpy as np
import re
import logging
import time
import hashlib
import gc
import psutil
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any, Generator, Union, Callable
from dataclasses import dataclass, asdict
from datetime import datetime
import asyncio
from concurrent.futures import ThreadPoolExecutor, as_completed
import multiprocessing as mp
from functools import lru_cache

# 로컬 모듈 임포트 (지연 로딩)
try:
    from async_file_manager import AsyncFileManager
    ASYNC_FILE_MANAGER_AVAILABLE = True
except ImportError:
    ASYNC_FILE_MANAGER_AVAILABLE = False
    AsyncFileManager = None

# Arrow 모듈 임포트 (지연 로딩)
try:
    from arrow_data_manager import ArrowDataManager, create_arrow_manager
    from arrow_schema_optimizer import ArrowSchemaOptimizer, create_schema_optimizer
    ARROW_INTEGRATION_AVAILABLE = True
except ImportError:
    ARROW_INTEGRATION_AVAILABLE = False
    ArrowDataManager = None
    create_arrow_manager = None
    ArrowSchemaOptimizer = None
    create_schema_optimizer = None

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
class ProcessingStats:
    """처리 통계 데이터 클래스"""
    total_files: int = 0
    processed_files: int = 0
    failed_files: int = 0
    total_processing_time: float = 0.0
    peak_memory_usage: float = 0.0
    average_processing_time: float = 0.0
    vectorization_speedup: float = 0.0
    memory_reduction: float = 0.0
    throughput: float = 0.0

@dataclass
class DataFrameChunk:
    """DataFrame 청크 데이터 클래스"""
    chunk_id: int
    data: pd.DataFrame
    file_paths: List[str]
    row_count: int
    memory_usage: float
    processing_time: float

class MemoryManager:
    """메모리 관리 클래스"""
    
    def __init__(self):
        self.process = psutil.Process()
        self.start_memory = self.process.memory_info().rss / 1024 / 1024  # MB
        self.peak_memory = self.start_memory
        self.monitoring = True
        
    def update_memory_usage(self) -> float:
        """메모리 사용량 업데이트"""
        current_memory = self.process.memory_info().rss / 1024 / 1024  # MB
        self.peak_memory = max(self.peak_memory, current_memory)
        return current_memory
    
    def get_memory_stats(self) -> Dict[str, float]:
        """메모리 통계 반환"""
        current_memory = self.update_memory_usage()
        return {
            'current_memory_mb': current_memory,
            'peak_memory_mb': self.peak_memory,
            'start_memory_mb': self.start_memory,
            'memory_increase_mb': current_memory - self.start_memory
        }
    
    def optimize_dtypes(self, df: pd.DataFrame) -> pd.DataFrame:
        """DataFrame 데이터 타입 최적화"""
        original_memory = df.memory_usage(deep=True).sum() / 1024 / 1024  # MB
        
        # 수치형 데이터 타입 최적화
        for col in df.select_dtypes(include=['int64']).columns:
            df[col] = pd.to_numeric(df[col], downcast='integer')
        
        for col in df.select_dtypes(include=['float64']).columns:
            df[col] = pd.to_numeric(df[col], downcast='float')
        
        # 문자열 데이터 타입 최적화
        for col in df.select_dtypes(include=['object']).columns:
            if df[col].nunique() / len(df[col]) < 0.5:  # 고유값 비율이 50% 미만이면
                df[col] = df[col].astype('category')
        
        optimized_memory = df.memory_usage(deep=True).sum() / 1024 / 1024  # MB
        reduction_ratio = (original_memory - optimized_memory) / original_memory if original_memory > 0 else 0
        
        logger.debug(f"데이터 타입 최적화: {original_memory:.2f}MB -> {optimized_memory:.2f}MB ({reduction_ratio*100:.1f}% 감소)")
        
        return df
    
    def optimize_memory_usage_advanced(self, df: pd.DataFrame) -> pd.DataFrame:
        """고급 메모리 사용량 최적화"""
        try:
            original_memory = df.memory_usage(deep=True).sum()
            
            # 데이터 타입 최적화
            for col in df.columns:
                if df[col].dtype == 'object':
                    # 문자열 데이터 타입 최적화
                    if df[col].nunique() / len(df[col]) < 0.5:  # 고유 값 비율이 50% 미만이면
                        df[col] = df[col].astype('category')
                    elif df[col].str.len().max() < 50:  # 문자열 길이가 50 미만이면
                        df[col] = df[col].astype('string')
                
                elif df[col].dtype in ['int64', 'float64']:
                    # 수치 데이터 타입 최적화
                    if df[col].dtype == 'int64':
                        df[col] = pd.to_numeric(df[col], downcast='integer')
                    elif df[col].dtype == 'float64':
                        df[col] = pd.to_numeric(df[col], downcast='float')
                
                elif df[col].dtype == 'bool':
                    # 불리언 타입 최적화
                    df[col] = df[col].astype('int8')
            
            # 중복 데이터 제거
            if len(df) > 1000:  # 1000행 이상인 경우에만 적용
                df = df.drop_duplicates()
            
            # 인덱스 메모리 최적화
            if df.index.nunique() == len(df):
                df = df.reset_index(drop=True)
            
            optimized_memory = df.memory_usage(deep=True).sum()
            reduction_ratio = (original_memory - optimized_memory) / original_memory * 100
            
            logger.info(f"고급 메모리 최적화 완료: {reduction_ratio:.1f}% 감소 ({original_memory/1024/1024:.1f}MB -> {optimized_memory/1024/1024:.1f}MB)")
            
            return df
            
        except Exception as e:
            logger.error(f"메모리 최적화 오류: {str(e)}")
            return df
    
    def manage_memory_chunks(self, df: pd.DataFrame, max_chunk_size: int = 10000) -> List[pd.DataFrame]:
        """대용량 DataFrame을 청크로 분할하여 메모리 관리"""
        try:
            chunks = []
            total_rows = len(df)
            
            if total_rows <= max_chunk_size:
                chunks.append(df)
                return chunks
            
            # 행 기반 청크 분할
            for i in range(0, total_rows, max_chunk_size):
                chunk = df.iloc[i:i + max_chunk_size].copy()
                chunks.append(chunk)
                
                # 각 청크에 대해 메모리 최적화 적용
                chunk = self.optimize_memory_usage_advanced(chunk)
                
                # 명시적 메모리 정리
                del chunk
            
            logger.info(f"DataFrame을 {len(chunks)}개 청크로 분할 완료 (총 {total_rows}행)")
            return chunks
            
        except Exception as e:
            logger.error(f"메모리 청크 분할 오류: {str(e)}")
            return [df]
    
    def cleanup_memory(self) -> None:
        """메모리 정리"""
        try:
            # gc 수동 호출
            gc.collect()
            
            # pandas 메모리 풀 정리
            pd.options.mode.chained_assignment = None
            pd.reset_option('mode.chained_assignment')
            
            # 임시 파일 정리
            if hasattr(self, 'temp_files'):
                for temp_file in self.temp_files:
                    try:
                        Path(temp_file).unlink(missing_ok=True)
                    except:
                        pass
                self.temp_files.clear()
            
            logger.info("메모리 정리 완료")
            
        except Exception as e:
            logger.error(f"메모리 정리 오류: {str(e)}")
    
    def get_memory_usage(self) -> Dict[str, float]:
        """현재 메모리 사용량 정보 반환"""
        try:
            memory_info = psutil.Process().memory_info()
            return {
                'rss': memory_info.rss / 1024 / 1024,  # MB
                'vms': memory_info.vms / 1024 / 1024,  # MB
                'percent': psutil.Process().memory_percent(),
                'available': psutil.virtual_memory().available / 1024 / 1024,  # MB
                'total': psutil.virtual_memory().total / 1024 / 1024  # MB
            }
        except Exception as e:
            logger.error(f"메모리 정보 조회 오류: {str(e)}")
            return {}
    
    def monitor_memory_usage(self, interval: float = 1.0) -> None:
        """메모리 사용량 모니터링"""
        try:
            start_time = time.time()
            peak_memory = 0
            
            while True:
                memory_info = self.get_memory_usage()
                current_memory = memory_info['rss']
                
                if current_memory > peak_memory:
                    peak_memory = current_memory
                
                logger.debug(f"메모리 사용량: {current_memory:.1f}MB (최대: {peak_memory:.1f}MB)")
                
                # 메모리 임계값 확인
                if memory_info['percent'] > 80:  # 80% 이상이면 경고
                    logger.warning(f"메모리 사용량 임계값 초과: {memory_info['percent']:.1f}%")
                
                time.sleep(interval)
                
        except KeyboardInterrupt:
            logger.info(f"메모리 모니터링 종료 (최대 메모리 사용량: {peak_memory:.1f}MB)")
        except Exception as e:
            logger.error(f"메모리 모니터링 오류: {str(e)}")
    
    def integrate_performance_monitor(self, monitor_interval: float = 5.0) -> None:
        """성능 모니터링 연동"""
        try:
            # 성능 모니터링 스레드 시작
            import threading
            
            def monitor_performance():
                """성능 모니터링 스레드"""
                while True:
                    try:
                        # 메모리 사용량 수집
                        memory_info = self.get_memory_usage()
                        
                        # 처리 통계 수집
                        processing_stats = self.get_processing_stats()
                        
                        # 성능 지표 로깅
                        logger.info(f"성능 모니터링 - 메모리: {memory_info['rss']:.1f}MB, "
                                   f"처리 시간: {processing_stats.total_processing_time:.2f}s, "
                                   f"처리량: {processing_stats.throughput:.2f} 행/초")
                        
                        # 성능 임계값 확인
                        if memory_info['percent'] > 85:  # 85% 이상이면 경고
                            logger.warning(f"메모리 사용량 임계값 초과: {memory_info['percent']:.1f}%")
                        
                        if processing_stats.total_processing_time > 300:  # 5분 이상이면 경고
                            logger.warning(f"처리 시간 임계값 초과: {processing_stats.total_processing_time:.2f}s")
                        
                        time.sleep(monitor_interval)
                        
                    except Exception as e:
                        logger.error(f"성능 모니터링 오류: {str(e)}")
                        time.sleep(monitor_interval)
            
            # 모니터링 스레드 시작
            monitor_thread = threading.Thread(target=monitor_performance, daemon=True)
            monitor_thread.start()
            
            logger.info(f"성능 모니터링 연동 완료 (간격: {monitor_interval}초)")
            
        except Exception as e:
            logger.error(f"성능 모니터링 연동 오류: {str(e)}")
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """성능 지표 수집"""
        try:
            # 메모리 사용량
            memory_info = self.get_memory_usage()
            
            # 처리 통계
            processing_stats = self.get_processing_stats()
            
            # 벡터화 연산 통계
            vectorized_stats = {
                'cache_hits': getattr(self, 'cache_hits', 0),
                'cache_misses': getattr(self, 'cache_misses', 0),
                'compiled_patterns_count': len(self.compiled_patterns),
                'vectorized_operations_count': len(self.vectorized_operations)
            }
            
            # 메모리 관리 통계
            memory_stats = {
                'total_memory_allocated': getattr(self, 'total_memory_allocated', 0),
                'peak_memory_usage': getattr(self, 'peak_memory_usage', 0),
                'garbage_collections': getattr(self, 'garbage_collections', 0)
            }
            
            return {
                'timestamp': time.time(),
                'memory': memory_info,
                'processing': processing_stats,
                'vectorized_operations': vectorized_stats,
                'memory_management': memory_stats,
                'system_info': {
                    'cpu_count': mp.cpu_count(),
                    'python_version': platform.python_version(),
                    'pandas_version': pd.__version__,
                    'numpy_version': np.__version__
                }
            }
            
        except Exception as e:
            logger.error(f"성능 지표 수집 오류: {str(e)}")
            return {}
    
    def log_performance_report(self) -> None:
        """성능 보고서 생성"""
        try:
            metrics = self.get_performance_metrics()
            
            # 성능 보고서 생성
            report = {
                'timestamp': datetime.now().isoformat(),
                'performance_metrics': metrics,
                'recommendations': self._generate_performance_recommendations(metrics)
            }
            
            # 보고서 파일에 저장
            report_file = f"performance_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            
            logger.info(f"성능 보고서 생성 완료: {report_file}")
            
        except Exception as e:
            logger.error(f"성능 보고서 생성 오류: {str(e)}")
    
    def _generate_performance_recommendations(self, metrics: Dict[str, Any]) -> List[str]:
        """성능 개선 권장사항 생성"""
        recommendations = []
        
        try:
            # 메모리 사용량 기반 권장사항
            if metrics['memory']['percent'] > 80:
                recommendations.append("메모리 사용량이 높습니다. 데이터 타입 최적화 또는 청크 처리를 고려하세요.")
            
            # 처리 시간 기반 권장사항
            if metrics['processing']['total_processing_time'] > 300:
                recommendations.append("처리 시간이 길어집니다. 병렬 처리 또는 벡터화 연산을 적용하세요.")
            
            # 벡터화 연산 기반 권장사항
            if metrics['vectorized_operations']['cache_misses'] > metrics['vectorized_operations']['cache_hits']:
                recommendations.append("벡터화 연산 캐시 히트율이 낮습니다. 패턴을 미리 컴파일하세요.")
            
            # 메모리 관리 기반 권장사항
            if metrics['memory_management']['peak_memory_usage'] > 1024:  # 1GB 이상
                recommendations.append("메모리 사용량이 1GB를 초과합니다. 청크 처리를 적용하세요.")
            
            return recommendations
            
        except Exception as e:
            logger.error(f"성능 권장사항 생성 오류: {str(e)}")
            return []
    
    def trigger_gc(self) -> None:
        """가비지 컬렉션 트리거"""
        gc.collect()
        logger.debug("가비지 컬렉션 실행")

class ChunkProcessor:
    """청크 처리 클래스"""
    
    def __init__(self, chunk_size: int = 1000, max_workers: int = 4):
        self.chunk_size = chunk_size
        self.max_workers = max_workers
        self.memory_manager = MemoryManager()
        
    def create_chunks(self, data: pd.DataFrame) -> Generator[DataFrameChunk, None, None]:
        """DataFrame을 청크로 분할"""
        total_rows = len(data)
        for i in range(0, total_rows, self.chunk_size):
            chunk_data = data.iloc[i:i + self.chunk_size]
            
            # 메모리 사용량 측정
            memory_usage = chunk_data.memory_usage(deep=True).sum() / 1024 / 1024
            
            chunk = DataFrameChunk(
                chunk_id=i // self.chunk_size,
                data=chunk_data,
                file_paths=[],  # 실제 구현에서는 파일 경로 설정
                row_count=len(chunk_data),
                memory_usage=memory_usage,
                processing_time=0.0
            )
            
            yield chunk
    
    def process_chunk(self, chunk: DataFrameChunk, operations: List[Callable]) -> DataFrameChunk:
        """청크 처리"""
        start_time = time.time()
        
        try:
            # 메모리 사용량 측정 전
            memory_before = self.memory_manager.update_memory_usage()
            
            # 연산 적용
            for operation in operations:
                chunk.data = operation(chunk.data)
            
            # 메모리 사용량 측정 후
            memory_after = self.memory_manager.update_memory_usage()
            memory_increase = memory_after - memory_before
            
            # 처리 시간 계산
            processing_time = time.time() - start_time
            chunk.processing_time = processing_time
            
            logger.debug(f"청크 {chunk.chunk_id} 처리 완료: {processing_time:.3f}s, 메모리 증가: {memory_increase:.2f}MB")
            
            return chunk
            
        except Exception as e:
            logger.error(f"청크 {chunk.chunk_id} 처리 오류: {str(e)}")
            raise

class PandasDataProcessor:
    """Pandas 데이터 처리 클래스 - 핵심 데이터 처리 시스템"""
    
    def __init__(self, max_workers: int = None, chunk_size: int = 1000, enable_arrow: bool = True):
        self.max_workers = max_workers or min(mp.cpu_count(), 8)
        self.chunk_size = chunk_size
        self.enable_arrow = enable_arrow
        self.dataframe_cache: Dict[str, pd.DataFrame] = {}
        self.processing_stats = ProcessingStats()
        self.memory_manager = MemoryManager()
        self.chunk_processor = ChunkProcessor(chunk_size, self.max_workers)
        
        # 벡터화된 연산 캐시
        self.vectorized_operations: Dict[str, Callable] = {}
        self.compiled_patterns: Dict[str, re.Pattern] = {}
        
        # 성능 모니터링
        self.start_time = time.time()
        self.processing_times: List[float] = []
        
        # Arrow 통합 초기화
        self.arrow_manager = None
        self.schema_optimizer = None
        if ARROW_INTEGRATION_AVAILABLE and enable_arrow:
            try:
                self.arrow_manager = create_arrow_manager()
                self.schema_optimizer = create_schema_optimizer()
                logger.info("Apache Arrow 통합 활성화")
            except Exception as e:
                logger.warning(f"Apache Arrow 통합 초기화 실패: {str(e)}")
                self.enable_arrow = False
        
        # Windows 11 최적화
        self._windows_optimization()
        
        # 초기화
        self._initialize_operations()
    
    # Arrow 통합 메서드
    async def optimize_dataframe_with_arrow(self, df: pd.DataFrame, table_name: str = None) -> pd.DataFrame:
        """Arrow를 활용한 DataFrame 최적화"""
        if not self.enable_arrow or not self.arrow_manager or not self.schema_optimizer:
            logger.warning("Arrow 통합이 비활성화되어 있습니다.")
            return df
        
        try:
            start_time = time.time()
            
            # 1. 스키마 최적화
            schema_result = self.schema_optimizer.optimize_schema(df, table_name)
            
            # 2. Arrow Table로 변환
            arrow_table = await self.arrow_manager.pandas_to_arrow(df, table_name)
            
            # 3. 최적화된 스키마 적용
            optimized_table = arrow_table.cast(schema_result.optimized_schema)
            
            # 4. 다시 pandas DataFrame으로 변환
            optimized_df = await self.arrow_manager.arrow_to_pandas(optimized_table, table_name)
            
            # 5. 성능 통계 업데이트
            processing_time = time.time() - start_time
            memory_reduction = schema_result.memory_reduction
            
            logger.info(f"Arrow 최적화 완료: {table_name or 'unnamed'}")
            logger.info(f"처리 시간: {processing_time:.3f}s")
            logger.info(f"메모리 감소: {memory_reduction:.1f}%")
            logger.info(f"타입 최적화: {len(schema_result.type_optimizations)}개")
            
            # 통계 저장
            if hasattr(self.processing_stats, 'arrow_optimizations'):
                self.processing_stats.arrow_optimizations += 1
            else:
                self.processing_stats.arrow_optimizations = 1
            
            return optimized_df
            
        except Exception as e:
            logger.error(f"Arrow 최적화 오류: {str(e)}")
            return df
    
    async def save_dataframe_as_arrow(self, df: pd.DataFrame, file_path: str,
                                    compression: str = 'zstd', format: str = 'parquet') -> str:
        """DataFrame을 Arrow 파일로 저장"""
        if not self.enable_arrow or not self.arrow_manager:
            logger.warning("Arrow 통합이 비활성화되어 있습니다.")
            return file_path
        
        try:
            # Arrow Table로 변환
            arrow_table = await self.arrow_manager.pandas_to_arrow(df)
            
            # Arrow 파일로 저장
            await self.arrow_manager.save_arrow_file(arrow_table, file_path, compression, format)
            
            logger.info(f"Arrow 파일 저장 완료: {file_path}")
            return file_path
            
        except Exception as e:
            logger.error(f"Arrow 파일 저장 오류: {str(e)}")
            raise
    
    async def load_dataframe_from_arrow(self, file_path: str, format: str = 'auto') -> pd.DataFrame:
        """Arrow 파일에서 DataFrame 로드"""
        if not self.enable_arrow or not self.arrow_manager:
            logger.warning("Arrow 통합이 비활성화되어 있습니다.")
            # 기존 방식으로 로드 시도
            return await self._load_dataframe_legacy(file_path)
        
        try:
            # Arrow 파일 로드
            arrow_table = await self.arrow_manager.load_arrow_file(file_path, format)
            
            # DataFrame으로 변환
            df = await self.arrow_manager.arrow_to_pandas(arrow_table)
            
            logger.info(f"Arrow 파일 로드 완료: {file_path}")
            return df
            
        except Exception as e:
            logger.error(f"Arrow 파일 로드 오류: {str(e)}")
            # 기존 방식으로 로드 시도
            return await self._load_dataframe_legacy(file_path)
    
    async def _load_dataframe_legacy(self, file_path: str) -> pd.DataFrame:
        """기존 방식으로 DataFrame 로드 (Arrow 실패 시 대체)"""
        try:
            file_path = Path(file_path)
            
            if file_path.suffix.lower() == '.csv':
                return pd.read_csv(file_path)
            elif file_path.suffix.lower() == '.json':
                return pd.read_json(file_path)
            elif file_path.suffix.lower() == '.parquet':
                return pd.read_parquet(file_path)
            elif file_path.suffix.lower() == '.feather':
                return pd.read_feather(file_path)
            else:
                # 기본적으로 CSV로 시도
                return pd.read_csv(file_path)
                
        except Exception as e:
            logger.error(f"기존 방식으로 DataFrame 로드 실패: {str(e)}")
            raise
    
    def get_arrow_performance_stats(self) -> Dict[str, Any]:
        """Arrow 성능 통계 반환"""
        if not self.enable_arrow or not self.arrow_manager:
            return {}
        
        arrow_stats = self.arrow_manager.get_performance_stats()
        schema_stats = self.schema_optimizer.get_memory_stats() if self.schema_optimizer else {}
        
        return {
            'arrow_stats': arrow_stats,
            'schema_stats': schema_stats,
            'enabled': self.enable_arrow
        }
    
    def optimize_arrow_memory_usage(self) -> None:
        """Arrow 메모리 사용량 최적화"""
        if self.enable_arrow:
            if self.arrow_manager:
                self.arrow_manager.optimize_memory_usage()
            if self.schema_optimizer:
                self.schema_optimizer.optimize_memory_usage()
    
    def clear_arrow_cache(self) -> None:
        """Arrow 캐시 정리"""
        if self.enable_arrow:
            if self.arrow_manager:
                self.arrow_manager.clear_cache()
            if self.schema_optimizer:
                self.schema_optimizer.clear_cache()
        
    def _windows_optimization(self) -> None:
        """Windows 11 환경 최적화"""
        try:
            # Windows 환경에서 pandas 최적화 설정
            import ctypes
            kernel32 = ctypes.windll.kernel32
            
            # 메모리 관리 최적화
            if hasattr(kernel32, 'SetProcessWorkingSetSize'):
                kernel32.SetProcessWorkingSetSize(
                    kernel32.GetCurrentProcess(),
                    -1,  # 최소 작업 집합 크기
                    -1   # 최대 작업 집합 크기
                )
                logger.info("Windows 11 메모리 관리 최적화 적용")
            
        except Exception as e:
            logger.warning(f"Windows 최적화 적용 실패: {str(e)}")
    
    def _initialize_operations(self) -> None:
        """벡터화된 연산 초기화"""
        # 컴파일된 정규식 패턴
        self.compiled_patterns = {
            'html_tags': re.compile(r'<[^>]+>', re.IGNORECASE),
            'extra_spaces': re.compile(r'\s+', re.UNICODE),
            'empty_lines': re.compile(r'\n\s*\n', re.MULTILINE),
            'special_chars': re.compile(r'[^\w\s가-힣]', re.UNICODE),
            'code_blocks': re.compile(r'```[a-zA-Z0-9+]*\s*\n(.*?)\n```', re.DOTALL),
            'urls': re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'),
            'email': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
            'markdown_headers': re.compile(r'^#{1,6}\s+(.+)$', re.MULTILINE)
        }
        
        # 벡터화된 연산 함수
        self.vectorized_operations = {
            'remove_html': self._vectorized_remove_html,
            'normalize_spaces': self._vectorized_normalize_spaces,
            'remove_special_chars': self._vectorized_remove_special_chars,
            'extract_code_blocks': self._vectorized_extract_code_blocks,
            'normalize_text': self._vectorized_normalize_text,
            'extract_metadata': self._vectorized_extract_metadata
        }
        
        logger.info("벡터화된 연산 초기화 완료")
    
    async def process_file_to_dataframe(self, file_path: str, async_manager: AsyncFileManager = None) -> pd.DataFrame:
        """파일 데이터를 pandas DataFrame으로 변환"""
        try:
            start_time = time.time()
            
            # AsyncFileManager가 제공되면 비동기 파일 읽기 사용
            if async_manager:
                content = await async_manager.read_file(file_path)
                content = content.decode('utf-8', errors='ignore')
            else:
                # 동기 파일 읽기
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
            
            # DataFrame 생성
            df = self._create_dataframe_from_content(content, file_path)
            
            # 메모리 최적화
            df = self.memory_manager.optimize_dtypes(df)
            
            # 처리 시간 계산
            processing_time = time.time() - start_time
            self.processing_times.append(processing_time)
            
            # 통계 업데이트
            self.processing_stats.processed_files += 1
            self.processing_stats.total_processing_time += processing_time
            
            logger.debug(f"파일 처리 완료: {file_path} ({processing_time:.3f}s)")
            
            return df
            
        except Exception as e:
            logger.error(f"파일 처리 오류: {file_path}, {str(e)}")
            self.processing_stats.failed_files += 1
            raise
    
    def _create_dataframe_from_content(self, content: str, file_path: str) -> pd.DataFrame:
        """콘텐츠에서 DataFrame 생성"""
        # 파일 경로에서 메타데이터 추출
        path = Path(file_path)
        
        # 기본 데이터 구조 생성
        data = {
            'file_path': [str(file_path)],
            'filename': [path.name],
            'content': [content],
            'content_length': [len(content)],
            'line_count': [content.count('\n') + 1],
            'word_count': [len(content.split())],
            'char_count': [len(content)],
            'has_code': ['```' in content],
            'has_links': ['](' in content],
            'has_images': ['![' in content],
            'has_tables': ['|' in content],
            'processing_date': [datetime.now().isoformat()]
        }
        
        # DataFrame 생성
        df = pd.DataFrame(data)
        
        # 벡터화된 메타데이터 추적
        df = self._vectorized_extract_metadata(df)
        
        return df
    
    def _vectorized_extract_metadata(self, df: pd.DataFrame) -> pd.DataFrame:
        """벡터화된 메타데이터 추출"""
        # 카테고리 추출
        df['category'] = df['filename'].apply(self._extract_category_vectorized)
        
        # 서브 카테고리 추출
        df['subcategory'] = df['filename'].apply(self._extract_subcategory_vectorized)
        
        # 제목 추출
        df['title'] = df['content'].apply(self._extract_title_vectorized)
        
        # 태그 추출
        df['tags'] = df['content'].apply(self._extract_tags_vectorized)
        
        # 설명 추출
        df['description'] = df['content'].apply(self._extract_description_vectorized)
        
        return df
    
    def _extract_category_vectorized(self, filename: str) -> str:
        """벡터화된 카테고리 추출"""
        category_map = {
            '01_Getting_Started': '01_Getting_Started',
            '02_Concepts': '02_Concepts',
            '03_Data_Binding': '03_Data_Binding',
            '04_Controls': '04_Controls',
            '05_Features': '05_Features',
            '99_Uncategorized': '99_Uncategorized'
        }
        
        for category in category_map.keys():
            if category in filename:
                return category_map[category]
        return '99_Uncategorized'
    
    def _extract_subcategory_vectorized(self, filename: str) -> str:
        """벡터화된 서브 카테고리 추출"""
        subcategory_map = {
            'Chart': 'Chart',
            'Diagram': 'Diagram',
            'Editors': 'Editors',
            'Gauge': 'Gauge',
            'Grid': 'Grid',
            'Ribbon': 'Ribbon'
        }
        
        for subcategory in subcategory_map.keys():
            if subcategory in filename:
                return subcategory_map[subcategory]
        return ''
    
    def _extract_title_vectorized(self, content: str) -> str:
        """벡터화된 제목 추출"""
        # 정규식으로 헤더 찾기
        header_pattern = self.compiled_patterns['markdown_headers']
        matches = header_pattern.findall(content)
        
        if matches:
            return matches[0].strip()
        
        # 헤더가 없으면 첫 번째 줄 사용
        first_line = content.split('\n')[0].strip()
        if first_line and len(first_line) < 100:
            return first_line
        
        return 'Untitled'
    
    def _extract_tags_vectorized(self, content: str) -> List[str]:
        """벡터화된 태그 추출"""
        keyword_map = {
            'control': ['control', 'controls'],
            'data': ['data', 'database', 'datasource'],
            'binding': ['binding', 'bindings'],
            'grid': ['grid', 'grids'],
            'chart': ['chart', 'charts'],
            'diagram': ['diagram', 'diagrams'],
            'editor': ['editor', 'editors'],
            'gauge': ['gauge', 'gauges'],
            'ribbon': ['ribbon', 'ribbons'],
            'feature': ['feature', 'features'],
            'concept': ['concept', 'concepts'],
            'getting-started': ['getting', 'started', 'beginner', 'basic']
        }
        
        content_lower = content.lower()
        tags = []
        
        for tag, keywords in keyword_map.items():
            for keyword in keywords:
                if keyword in content_lower:
                    tags.append(tag)
                    break
        
        return list(set(tags))
    
    def _extract_description_vectorized(self, content: str) -> str:
        """벡터화된 설명 추출"""
        # 첫 번째 문장 추출
        sentences = re.split(r'[.!?]', content)
        for sentence in sentences:
            sentence = sentence.strip()
            if 10 < len(sentence) < 200:
                return sentence
        
        return content[:100] + '...' if len(content) > 100 else content
    
    def vectorize_text_operations(self, df: pd.DataFrame) -> pd.DataFrame:
        """벡터화된 텍스트 처리 연산 적용"""
        try:
            start_time = time.time()
            
            # HTML 태그 제거
            df['cleaned_content'] = self._vectorized_remove_html(df['content'])
            
            # 여러 공백 정리
            df['cleaned_content'] = self._vectorized_normalize_spaces(df['cleaned_content'])
            
            # 특수 문자 정리
            df['cleaned_content'] = self._vectorized_remove_special_chars(df['cleaned_content'])
            
            # 코드 블록 추출
            df['cleaned_content'], df['code_blocks'] = self._vectorized_extract_code_blocks(df['cleaned_content'])
            
            # 텍스트 정규화
            df['cleaned_content'] = self._vectorized_normalize_text(df['cleaned_content'])
            
            # 처리 시간 계산
            processing_time = time.time() - start_time
            
            # 통계 업데이트
            self.processing_stats.total_processing_time += processing_time
            self.processing_times.append(processing_time)
            
            logger.info(f"벡터화된 텍스트 처리 완료: {processing_time:.3f}s")
            
            return df
            
        except Exception as e:
            logger.error(f"벡터화된 텍스트 처리 오류: {str(e)}")
            raise
    
    def _vectorized_remove_html(self, series: pd.Series) -> pd.Series:
        """벡터화된 HTML 태그 제거"""
        return series.str.replace(self.compiled_patterns['html_tags'], '', regex=True)
    
    def _vectorized_normalize_spaces(self, series: pd.Series) -> pd.Series:
        """벡터화된 공백 정규화"""
        return series.str.replace(self.compiled_patterns['extra_spaces'], ' ', regex=True)
    
    def _vectorized_remove_special_chars(self, series: pd.Series) -> pd.Series:
        """벡터화된 특수 문자 제거"""
        return series.str.replace(self.compiled_patterns['special_chars'], ' ', regex=True)
    
    def _vectorized_extract_code_blocks(self, series: pd.Series) -> Tuple[pd.Series, pd.Series]:
        """벡터화된 코드 블록 추출"""
        code_blocks = series.str.extractall(self.compiled_patterns['code_blocks'])[0]
        cleaned_content = series.str.replace(self.compiled_patterns['code_blocks'], '[CODE_BLOCK]', regex=True)
        return cleaned_content, code_blocks
    
    def _vectorized_normalize_text(self, series: pd.Series) -> pd.Series:
        """벡터화된 텍스트 정규화"""
        # 여러 줄바꿈 정리
        normalized = series.str.replace(r'\n\s*\n', '\n\n', regex=True)
        
        # 앞뒤 공백 제거
        normalized = normalized.str.strip()
        
        # 빈 문자열 처리
        normalized = normalized.replace('', 'EMPTY')
        
        return normalized
    
    def apply_batch_operations(self, df: pd.DataFrame, operations: List[str]) -> pd.DataFrame:
        """배치 연산 적용"""
        try:
            start_time = time.time()
            
            # 청크로 분할하여 처리
            chunks = list(self.chunk_processor.create_chunks(df))
            
            # 병렬 처리
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                # 연산 함수 생성
                operation_functions = [self.vectorized_operations[op] for op in operations]
                
                # 청크 병렬 처리
                future_to_chunk = {
                    executor.submit(self.chunk_processor.process_chunk, chunk, operation_functions): chunk
                    for chunk in chunks
                }
                
                # 결과 수집
                processed_chunks = []
                for future in as_completed(future_to_chunk):
                    try:
                        processed_chunk = future.result()
                        processed_chunks.append(processed_chunk)
                    except Exception as e:
                        logger.error(f"청크 처리 오류: {str(e)}")
                        continue
            
            # 청크 병합
            if processed_chunks:
                result_df = pd.concat([chunk.data for chunk in processed_chunks], ignore_index=True)
            else:
                result_df = df
            
            # 메모리 최적화
            result_df = self.memory_manager.optimize_dtypes(result_df)
            
            # 처리 시간 계산
            processing_time = time.time() - start_time
            
            logger.info(f"배치 연산 완료: {len(chunks)}개 청크, {processing_time:.3f}s")
            
            return result_df
            
        except Exception as e:
            logger.error(f"배치 연산 오류: {str(e)}")
            raise
    
    def optimize_memory_usage(self, df: pd.DataFrame) -> pd.DataFrame:
        """메모리 사용량 최적화"""
        try:
            start_time = time.time()
            
            # 메모리 사용량 측정
            before_memory = df.memory_usage(deep=True).sum() / 1024 / 1024  # MB
            
            # 데이터 타입 최적화
            df = self.memory_manager.optimize_dtypes(df)
            
            # 중복 데이터 제거
            df = df.drop_duplicates(subset=['file_path'], keep='first')
            
            # 메모리 사용량 측정 후
            after_memory = df.memory_usage(deep=True).sum() / 1024 / 1024  # MB
            
            # 메모리 감소율 계산
            memory_reduction = (before_memory - after_memory) / before_memory * 100 if before_memory > 0 else 0
            
            # 처리 시간 계산
            processing_time = time.time() - start_time
            
            logger.info(f"메모리 최적화 완료: {before_memory:.2f}MB -> {after_memory:.2f}MB ({memory_reduction:.1f}% 감소, {processing_time:.3f}s)")
            
            # 통계 업데이트
            self.processing_stats.memory_reduction = memory_reduction
            
            return df
            
        except Exception as e:
            logger.error(f"메모리 최적화 오류: {str(e)}")
            raise
    
    def get_processing_stats(self) -> ProcessingStats:
        """처리 통계 정보 반환"""
        if self.processing_stats.processed_files > 0:
            self.processing_stats.average_processing_time = (
                self.processing_stats.total_processing_time / self.processing_stats.processed_files
            )
        
        # 처리량 계산
        elapsed_time = time.time() - self.start_time
        self.processing_stats.throughput = self.processing_stats.processed_files / max(elapsed_time, 0.001)
        
        # 메모리 통계
        memory_stats = self.memory_manager.get_memory_stats()
        self.processing_stats.peak_memory_usage = memory_stats['peak_memory_mb']
        
        return self.processing_stats
    
    def clear_cache(self) -> None:
        """캐시 정리"""
        self.dataframe_cache.clear()
        self.memory_manager.trigger_gc()
        logger.info("캐시 정리 완료")
    
    def __del__(self):
        """소멸자"""
        try:
            self.clear_cache()
        except:
            pass

# 유틸리티 함수
def create_pandas_processor(max_workers: int = None, chunk_size: int = 1000) -> PandasDataProcessor:
    """PandasDataProcessor 인스턴스 생성"""
    return PandasDataProcessor(max_workers=max_workers, chunk_size=chunk_size)

async def process_files_with_pandas(file_paths: List[str], async_manager: AsyncFileManager = None, 
                                   max_workers: int = None, chunk_size: int = 1000) -> pd.DataFrame:
    """PandasDataProcessor를 사용한 파일 처리"""
    processor = create_pandas_processor(max_workers, chunk_size)
    
    # DataFrame 리스트 생성
    dataframes = []
    for file_path in file_paths:
        try:
            df = await processor.process_file_to_dataframe(file_path, async_manager)
            dataframes.append(df)
        except Exception as e:
            logger.error(f"파일 처리 실패: {file_path}, {str(e)}")
            continue
    
    # 모든 DataFrame 병합
    if dataframes:
        result_df = pd.concat(dataframes, ignore_index=True)
        
        # 벡터화된 텍스트 처리 적용
        result_df = processor.vectorize_text_operations(result_df)
        
        # 메모리 최적화
        result_df = processor.optimize_memory_usage(result_df)
        
        # 통계 정보
        stats = processor.get_processing_stats()
        
        logger.info(f"처리 완료: {stats.processed_files}개 파일, {stats.average_processing_time:.3f}s 평균")
        
        return result_df
    else:
        return pd.DataFrame()

if __name__ == "__main__":
    # 테스트 코드
    async def test_pandas_processor():
        """PandasDataProcessor 테스트"""
        test_files = [
            "test_file1.txt",
            "test_file2.txt",
            "test_file3.txt"
        ]
        
        # 테스트 파일 생성
        for i, file_path in enumerate(test_files):
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"# 테스트 파일 {i+1}\n\n")
                f.write("이것은 테스트 파일입니다.\n\n")
                f.write("```python\nprint('Hello, World!')\n```\n\n")
                f.write("여러 공백과    특수문자 @#$% 테스트\n")
        
        try:
            # AsyncFileManager 생성
            async_manager = AsyncFileManager()
            
            # PandasDataProcessor 테스트
            result_df = await process_files_with_pandas(test_files, async_manager)
            
            print("처리 결과:")
            print(f"처리된 파일 수: {len(result_df)}")
            print(f"평균 처리 시간: {result_df['processing_time'].mean():.3f}s")
            print(f"메모리 사용량: {result_df.memory_usage(deep=True).sum() / 1024 / 1024:.2f}MB")
            print("\n샘플 데이터:")
            print(result_df[['filename', 'title', 'category', 'word_count']].head())
            
        finally:
            # 테스트 파일 삭제
            for file_path in test_files:
                try:
                    Path(file_path).unlink()
                except:
                    pass
    
    # 테스트 실행
    asyncio.run(test_pandas_processor())