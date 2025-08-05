import pandas as pd
import numpy as np
import logging
import gc
import time
import psutil
import re
import unicodedata
from typing import Dict, List, Optional, Union, Generator, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from pathlib import Path
import hashlib
import json
import traceback
import multiprocessing as mp
from functools import lru_cache

@dataclass
class CleaningStats:
    """데이터 정제 통계 정보"""
    total_files: int = 0
    processed_files: int = 0
    total_size_mb: float = 0.0
    processed_size_mb: float = 0.0
    cleaning_time: float = 0.0
    memory_usage_mb: float = 0.0
    errors: List[str] = None
    
    def __post_init__(self):
        if self.errors is None:
            self.errors = []

class DataCleaner:
    """
    대용량 데이터 정제 및 메모리 관리를 위한 핵심 클래스
    """
    
    def __init__(self, config: Optional[Dict] = None):
        """
        DataCleaner 초기화
        
        Args:
            config: 설정 딕셔너리
        """
        self.config = config or {}
        self.logger = self._setup_logger()
        self.memory_threshold = self.config.get('memory_threshold', 80)  # 메모리 사용량 임계값 (%)
        self.chunk_size = self.config.get('chunk_size', 100000)
        self.max_workers = self.config.get('max_workers', psutil.cpu_count())
        self.enable_multiprocessing = self.config.get('enable_multiprocessing', True)
        
        # 정규식 패턴 미리 컴파일
        self.patterns = {
            'html_tags': re.compile(r'<[^>]+>'),
            'whitespace': re.compile(r'\s+'),
            'special_chars': re.compile(r'[^\w\s\u4e00-\u9fff]'),
            'urls': re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'),
            'emails': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
            'phone_numbers': re.compile(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'),
            'dates': re.compile(r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b|\b\d{4}[/-]\d{1,2}[/-]\d{1,2}\b'),
        }
        
        self.stats = CleaningStats()
        self.logger.info("DataCleaner 초기화 완료")
    
    def _setup_logger(self) -> logging.Logger:
        """로거 설정"""
        logger = logging.getLogger('DataCleaner')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def _check_memory_usage(self) -> bool:
        """
        현재 메모리 사용량 확인
        
        Returns:
            bool: 메모리 사용량이 임계값을 초과하면 True
        """
        memory = psutil.virtual_memory()
        return memory.percent > self.memory_threshold
    
    def _optimize_dtypes(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        데이터프레임의 데이터 타입을 최적화
        
        Args:
            df: 최적화할 데이터프레임
            
        Returns:
            최적화된 데이터프레임
        """
        # 수치형 데이터 타입 최적화
        for col in df.select_dtypes(include=['int64']).columns:
            df[col] = pd.to_numeric(df[col], downcast='integer')
        
        for col in df.select_dtypes(include=['float64']).columns:
            df[col] = pd.to_numeric(df[col], downcast='float')
        
        # 카테고리형 데이터 타입 변환
        for col in df.select_dtypes(include=['object']).columns:
            if df[col].nunique() / len(df[col]) < 0.5:  # 고유값 비율이 50% 미만인 경우
                df[col] = df[col].astype('category')
        
        return df
    
    def _clean_text(self, text: str) -> str:
        """
        텍스트 정제
        
        Args:
            text: 정제할 텍스트
            
        Returns:
            정제된 텍스트
        """
        if not isinstance(text, str):
            return str(text)
        
        # HTML 태그 제거
        text = self.patterns['html_tags'].sub('', text)
        
        # URL 제거
        text = self.patterns['urls'].sub('', text)
        
        # 이메일 주소 제거
        text = self.patterns['emails'].sub('', text)
        
        # 전화번호 제거
        text = self.patterns['phone_numbers'].sub('', text)
        
        # 날짜 제거
        text = self.patterns['dates'].sub('', text)
        
        # 특수문자 제거 (한글, 영문, 숫자, 공백 제외)
        text = self.patterns['special_chars'].sub('', text)
        
        # 여러 공백을 하나로
        text = self.patterns['whitespace'].sub(' ', text)
        
        # 앞뒤 공백 제거
        text = text.strip()
        
        # 유니코드 정규화
        text = unicodedata.normalize('NFKC', text)
        
        return text
    
    def _process_chunk(self, chunk: pd.DataFrame) -> pd.DataFrame:
        """
        데이터 청크별 처리
        
        Args:
            chunk: 처리할 데이터 청크
            
        Returns:
            처리된 데이터 청크
        """
        start_time = time.time()
        
        try:
            # 텍스트 컬럼 정제
            text_columns = chunk.select_dtypes(include=['object']).columns
            for col in text_columns:
                chunk[col] = chunk[col].apply(self._clean_text)
            
            # 데이터 타입 최적화
            chunk = self._optimize_dtypes(chunk)
            
            # 결측값 처리
            chunk = chunk.fillna('')  # 간단한 결측값 처리
            
            processing_time = time.time() - start_time
            self.logger.debug(f"청크 처리 완료: {processing_time:.2f}초")
            
            return chunk
            
        except Exception as e:
            self.logger.error(f"청크 처리 오류: {e}")
            self.stats.errors.append(f"청크 처리 오류: {e}")
            return chunk
    
    def _process_file_multiprocessing(self, file_path: Path) -> pd.DataFrame:
        """
        파일을 멀티프로세싱으로 처리
        
        Args:
            file_path: 처리할 파일 경로
            
        Returns:
            처리된 데이터프레임
        """
        try:
            # 파일 읽기
            if file_path.suffix == '.csv':
                df = pd.read_csv(file_path)
            elif file_path.suffix == '.json':
                df = pd.read_json(file_path)
            else:
                # 텍스트 파일 처리
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                df = pd.DataFrame({'content': [content]})
            
            # 청크 단위로 분할
            chunks = [df[i:i + self.chunk_size] for i in range(0, len(df), self.chunk_size)]
            
            # 멀티프로세싱으로 청크 처리
            with ProcessPoolExecutor(max_workers=self.max_workers) as executor:
                results = list(executor.map(self._process_chunk, chunks))
            
            # 결과 병합
            result = pd.concat(results, ignore_index=True)
            
            return result
            
        except Exception as e:
            self.logger.error(f"파일 처리 오류 ({file_path}): {e}")
            self.stats.errors.append(f"파일 처리 오류 ({file_path}): {e}")
            return pd.DataFrame()
    
    def _process_file_threading(self, file_path: Path) -> pd.DataFrame:
        """
        파일을 멀티스레딩으로 처리
        
        Args:
            file_path: 처리할 파일 경로
            
        Returns:
            처리된 데이터프레임
        """
        try:
            # 파일 읽기
            if file_path.suffix == '.csv':
                df = pd.read_csv(file_path)
            elif file_path.suffix == '.json':
                df = pd.read_json(file_path)
            else:
                # 텍스트 파일 처리
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                df = pd.DataFrame({'content': [content]})
            
            # 청크 단위로 분할
            chunks = [df[i:i + self.chunk_size] for i in range(0, len(df), self.chunk_size)]
            
            # 멀티스레딩으로 청크 처리
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                results = list(executor.map(self._process_chunk, chunks))
            
            # 결과 병합
            result = pd.concat(results, ignore_index=True)
            
            return result
            
        except Exception as e:
            self.logger.error(f"파일 처리 오류 ({file_path}): {e}")
            self.stats.errors.append(f"파일 처리 오류 ({file_path}): {e}")
            return pd.DataFrame()
    
    def _monitor_memory_usage(self):
        """메모리 사용량 모니터링"""
        while True:
            memory = psutil.virtual_memory()
            self.stats.memory_usage_mb = memory.used / (1024 * 1024)
            
            if memory.percent > self.memory_threshold:
                self.logger.warning(f"메모리 사용량 임계값 초과: {memory.percent}%")
                gc.collect()
            
            time.sleep(5)  # 5초마다 확인
    
    def clean_directory(self, directory_path: Union[str, Path], output_path: Optional[Union[str, Path]] = None) -> Dict:
        """
        디렉토리 내 모든 파일 정제
        
        Args:
            directory_path: 정제할 디렉토리 경로
            output_path: 결과 저장 경로
            
        Returns:
            정제 통계 정보
        """
        start_time = time.time()
        directory_path = Path(directory_path)
        
        if not directory_path.exists():
            raise FileNotFoundError(f"디렉토리를 찾을 수 없습니다: {directory_path}")
        
        # 출력 경로 설정
        if output_path is None:
            output_path = directory_path.parent / f"{directory_path.name}_cleaned"
        output_path = Path(output_path)
        output_path.mkdir(exist_ok=True)
        
        # 지원 파일 확장자
        supported_extensions = {'.csv', '.json', '.txt', '.md'}
        
        # 처리할 파일 목록
        files_to_process = []
        total_size = 0
        
        for file_path in directory_path.rglob('*'):
            if file_path.is_file() and file_path.suffix.lower() in supported_extensions:
                files_to_process.append(file_path)
                total_size += file_path.stat().st_size
        
        self.stats.total_files = len(files_to_process)
        self.stats.total_size_mb = total_size / (1024 * 1024)
        
        self.logger.info(f"정제 시작: {len(files_to_process)}개 파일, 총 크기: {self.stats.total_size_mb:.2f}MB")
        
        # 메모리 모니터링 스레드 시작
        import threading
        monitor_thread = threading.Thread(target=self._monitor_memory_usage, daemon=True)
        monitor_thread.start()
        
        # 파일 처리
        processed_files = 0
        for file_path in files_to_process:
            try:
                file_start_time = time.time()
                
                # 메모리 사용량 확인
                if self._check_memory_usage():
                    self.logger.warning("메모리 사용량 임계값 도달, 가비지 컬렉션 실행")
                    gc.collect()
                
                # 파일 처리 방법 선택
                if self.enable_multiprocessing:
                    processed_df = self._process_file_multiprocessing(file_path)
                else:
                    processed_df = self._process_file_threading(file_path)
                
                if not processed_df.empty:
                    # 결과 저장
                    output_file = output_path / file_path.name
                    if file_path.suffix == '.csv':
                        processed_df.to_csv(output_file, index=False)
                    elif file_path.suffix == '.json':
                        processed_df.to_json(output_file, orient='records', indent=2)
                    else:
                        # 텍스트 파일 처리
                        with open(output_file, 'w', encoding='utf-8') as f:
                            for _, row in processed_df.iterrows():
                                f.write(str(row['content']) + '\n')
                    
                    # 통계 업데이트
                    processed_files += 1
                    file_size = file_path.stat().st_size / (1024 * 1024)
                    self.stats.processed_files = processed_files
                    self.stats.processed_size_mb += file_size
                    
                    file_time = time.time() - file_start_time
                    self.logger.info(f"파일 처리 완료: {file_path.name} ({file_time:.2f}초, {file_size:.2f}MB)")
                
            except Exception as e:
                self.logger.error(f"파일 처리 중 오류 발생 ({file_path}): {e}")
                self.stats.errors.append(f"파일 처리 오류 ({file_path}): {e}")
        
        # 최종 통계 계산
        self.stats.cleaning_time = time.time() - start_time
        
        # 결과 저장
        stats_file = output_path / 'cleaning_stats.json'
        with open(stats_file, 'w', encoding='utf-8') as f:
            json.dump(asdict(self.stats), f, ensure_ascii=False, indent=2)
        
        self.logger.info(f"정제 완료: {self.stats.processed_files}/{self.stats.total_files} 파일 처리")
        self.logger.info(f"총 처리 시간: {self.stats.cleaning_time:.2f}초")
        self.logger.info(f"평균 처리 속도: {self.stats.processed_size_mb/self.stats.cleaning_time:.2f}MB/초")
        
        return asdict(self.stats)
    
    def clean_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        데이터프레임 정제
        
        Args:
            df: 정제할 데이터프레임
            
        Returns:
            정제된 데이터프레임
        """
        start_time = time.time()
        
        try:
            # 청크 단위로 분할
            chunks = [df[i:i + self.chunk_size] for i in range(0, len(df), self.chunk_size)]
            
            # 청크별 처리
            processed_chunks = []
            for chunk in chunks:
                processed_chunk = self._process_chunk(chunk)
                processed_chunks.append(processed_chunk)
                
                # 메모리 관리
                if self._check_memory_usage():
                    gc.collect()
            
            # 결과 병합
            result = pd.concat(processed_chunks, ignore_index=True)
            
            # 최종 메모리 최적화
            result = self._optimize_dtypes(result)
            
            processing_time = time.time() - start_time
            self.logger.info(f"데이터프레임 정제 완료: {processing_time:.2f}초")
            
            return result
            
        except Exception as e:
            self.logger.error(f"데이터프레임 정제 오류: {e}")
            self.stats.errors.append(f"데이터프레임 정제 오류: {e}")
            return df
    
    def get_stats(self) -> Dict:
        """
        현재 정제 통계 정보 반환
        
        Returns:
            통계 정보 딕셔너리
        """
        return asdict(self.stats)
    
    def reset_stats(self):
        """통계 정보 초기화"""
        self.stats = CleaningStats()
        self.logger.info("통계 정보 초기화 완료")


def main():
    """메인 실행 함수"""
    import argparse
    
    parser = argparse.ArgumentParser(description='데이터 정제 도구')
    parser.add_argument('input_dir', help='입력 디렉토리 경로')
    parser.add_argument('--output-dir', help='출력 디렉토리 경로')
    parser.add_argument('--memory-threshold', type=int, default=80, help='메모리 사용량 임계값 (%)')
    parser.add_argument('--chunk-size', type=int, default=100000, help='처리 청크 크기')
    parser.add_argument('--max-workers', type=int, default=psutil.cpu_count(), help='최대 작업자 수')
    
    args = parser.parse_args()
    cleaner = DataCleaner(config)
    stats = cleaner.clean_directory('input_dir', output_dir)
    print(f"정제: {stats}")
    print(json.dumps(stats, indent=2))


if __name__ == '__main__':
    if __name__ == '__main__':
        main()


[Response interrupted by user]<|im_end|>