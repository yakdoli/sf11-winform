"""
WinForms_Docs 병렬 처리 성능 테스트 결과 보고서

병렬 처리 모듈들의 성능을 테스트하고 결과를 분석, 보고서를 생성합니다.
기존 처리 방식과 병렬 처리 방식의 성능 비교를 제공합니다.
"""

import time
import os
import json
import logging
import psutil
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, List, Set, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime
import traceback

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class TestResult:
    """테스트 결과 데이터 클래스"""
    test_name: str
    test_type: str
    execution_time: float
    memory_usage: float
    cpu_usage: float
    processed_items: int
    success_rate: float
    error_count: int
    throughput: float
    timestamp: str

@dataclass
class PerformanceComparison:
    """성능 비교 데이터 클래스"""
    test_name: str
    sequential_time: float
    parallel_time: float
    speedup_ratio: float
    memory_improvement: float
    cpu_improvement: float
    throughput_improvement: float
    efficiency: float

class PerformanceTester:
    """성능 테스트 클래스"""
    
    def __init__(self):
        self.test_results: List[TestResult] = []
        self.comparisons: List[PerformanceComparison] = []
        self.test_data = self._generate_test_data()
        
        # 로깅
        self.logger = logging.getLogger(__name__)
    
    def _generate_test_data(self) -> Dict[str, Any]:
        """테스트 데이터 생성"""
        # 테스트용 텍스트 데이터 생성
        sample_texts = []
        for i in range(1000):
            text = f"""
            # 문서 {i}
            
            이것은 테스트 문서 {i}입니다.
            
            ## 섹션 1
            여기에 내용이 들어갑니다.
            
            ```python
            def test_function_{i}():
                print("Hello, World!")
                return i * 2
            ```
            
            ## 섹션 2
            추가 내용입니다.
            
            [D2H]이것은 D2H 관련 텍스트입니다.[/D2H]
            
            package:[이것은 패키지 URL입니다]
            
            | 헤더1 | 헤더2 | 헤더3 |
            |-------|-------|-------|
            | 데이터1 | 데이터2 | 데이터3 |
            | 데이터4 | 데이터5 | 데이터6 |
            
            TODO: 이것은 TODO 주석입니다.
            FIXME: 이것은 FIXME 주석입니다.
            """
            sample_texts.append(text)
        
        # 테스트용 파일 경로 생성
        test_files = []
        for i in range(100):
            test_files.append(Path(f"test_file_{i}.txt"))
        
        return {
            'texts': sample_texts,
            'files': test_files,
            'mixed_content': sample_texts[:50] + test_files
        }
    
    def test_data_cleaner_performance(self) -> Dict[str, Any]:
        """데이터 정제기 성능 테스트"""
        self.logger.info("데이터 정제기 성능 테스트 시작")
        
        # 기존 방식 테스트
        sequential_result = self._test_sequential_data_cleaning()
        
        # 병렬 처리 방식 테스트
        parallel_result = self._test_parallel_data_cleaning()
        
        # 성능 비교
        comparison = self._compare_performance(
            sequential_result, parallel_result, "data_cleaner"
        )
        
        return {
            'sequential': sequential_result,
            'parallel': parallel_result,
            'comparison': comparison
        }
    
    def _test_sequential_data_cleaning(self) -> TestResult:
        """순차적 데이터 정제 테스트"""
        start_time = time.time()
        start_memory = psutil.Process().memory_info().rss / 1024 / 1024
        
        try:
            # 기존 데이터 정제 로직 시뮬레이션
            processed_count = 0
            error_count = 0
            
            for text in self.test_data['texts']:
                try:
                    # 간단한 텍스트 정제
                    cleaned = self._simple_text_cleaning(text)
                    processed_count += 1
                except Exception as e:
                    error_count += 1
                    continue
            
            end_time = time.time()
            end_memory = psutil.Process().memory_info().rss / 1024 / 1024
            
            execution_time = end_time - start_time
            memory_usage = end_memory - start_memory
            cpu_usage = psutil.Process().cpu_percent()
            success_rate = (processed_count / len(self.test_data['texts'])) * 100
            throughput = processed_count / execution_time if execution_time > 0 else 0
            
            return TestResult(
                test_name="sequential_data_cleaning",
                test_type="data_cleaning",
                execution_time=execution_time,
                memory_usage=memory_usage,
                cpu_usage=cpu_usage,
                processed_items=processed_count,
                success_rate=success_rate,
                error_count=error_count,
                throughput=throughput,
                timestamp=datetime.now().isoformat()
            )
            
        except Exception as e:
            self.logger.error(f"순차적 데이터 정제 테스트 오류: {str(e)}")
            return TestResult(
                test_name="sequential_data_cleaning",
                test_type="data_cleaning",
                execution_time=0,
                memory_usage=0,
                cpu_usage=0,
                processed_items=0,
                success_rate=0,
                error_count=1,
                throughput=0,
                timestamp=datetime.now().isoformat()
            )
    
    def _test_parallel_data_cleaning(self) -> TestResult:
        """병렬 데이터 정제 테스트"""
        start_time = time.time()
        start_memory = psutil.Process().memory_info().rss / 1024 / 1024
        
        try:
            # 병렬 처리 시뮬레이션
            processed_count = 0
            error_count = 0
            
            # 여러 스레드로 병렬 처리 시뮬레이션
            import threading
            import queue
            
            result_queue = queue.Queue()
            text_queue = queue.Queue()
            
            # 텍스트 큐에 데이터 추가
            for text in self.test_data['texts']:
                text_queue.put(text)
            
            # 워커 스레드 함수
            def worker():
                while not text_queue.empty():
                    try:
                        text = text_queue.get_nowait()
                        cleaned = self._simple_text_cleaning(text)
                        result_queue.put(('success', cleaned))
                    except queue.Empty:
                        break
                    except Exception as e:
                        result_queue.put(('error', str(e)))
            
            # 워커 스레드 시작
            workers = []
            num_workers = min(4, len(self.test_data['texts']))
            
            for _ in range(num_workers):
                worker_thread = threading.Thread(target=worker)
                worker_thread.start()
                workers.append(worker_thread)
            
            # 워커 스레드 대기
            for worker_thread in workers:
                worker_thread.join()
            
            # 결과 처리
            while not result_queue.empty():
                result_type, _ = result_queue.get()
                if result_type == 'success':
                    processed_count += 1
                else:
                    error_count += 1
            
            end_time = time.time()
            end_memory = psutil.Process().memory_info().rss / 1024 / 1024
            
            execution_time = end_time - start_time
            memory_usage = end_memory - start_memory
            cpu_usage = psutil.Process().cpu_percent()
            success_rate = (processed_count / len(self.test_data['texts'])) * 100
            throughput = processed_count / execution_time if execution_time > 0 else 0
            
            return TestResult(
                test_name="parallel_data_cleaning",
                test_type="data_cleaning",
                execution_time=execution_time,
                memory_usage=memory_usage,
                cpu_usage=cpu_usage,
                processed_items=processed_count,
                success_rate=success_rate,
                error_count=error_count,
                throughput=throughput,
                timestamp=datetime.now().isoformat()
            )
            
        except Exception as e:
            self.logger.error(f"병렬 데이터 정제 테스트 오류: {str(e)}")
            return TestResult(
                test_name="parallel_data_cleaning",
                test_type="data_cleaning",
                execution_time=0,
                memory_usage=0,
                cpu_usage=0,
                processed_items=0,
                success_rate=0,
                error_count=1,
                throughput=0,
                timestamp=datetime.now().isoformat()
            )
    
    def _simple_text_cleaning(self, text: str) -> str:
        """간단한 텍스트 정제"""
        # HTML 태그 제거
        import re
        text = re.sub(r'<[^>]+>', '', text)
        
        # D2H 관련 텍스트 제거
        text = re.sub(r'\[D2H\][^\]]*\]', '', text)
        text = re.sub(r'package:\[.*?\]', '', text)
        
        # 테이블 테두기 제거
        text = re.sub(r'\|[-+]+\|', '', text)
        
        # TODO/FIXME 주석 제거
        text = re.sub(r'TODO:.*|FIXME:.*', '', text)
        
        # 여러 공백 정리
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()
    
    def test_data_normalizer_performance(self) -> Dict[str, Any]:
        """데이터 정규화기 성능 테스트"""
        self.logger.info("데이터 정규화기 성능 테스트 시작")
        
        # 기존 방식 테스트
        sequential_result = self._test_sequential_data_normalization()
        
        # 병렬 처리 방식 테스트
        parallel_result = self._test_parallel_data_normalization()
        
        # 성능 비교
        comparison = self._compare_performance(
            sequential_result, parallel_result, "data_normalizer"
        )
        
        return {
            'sequential': sequential_result,
            'parallel': parallel_result,
            'comparison': comparison
        }
    
    def _test_sequential_data_normalization(self) -> TestResult:
        """순차적 데이터 정규화 테스트"""
        start_time = time.time()
        start_memory = psutil.Process().memory_info().rss / 1024 / 1024
        
        try:
            processed_count = 0
            error_count = 0
            
            for text in self.test_data['texts']:
                try:
                    # 간단한 텍스트 정규화
                    normalized = self._simple_text_normalization(text)
                    processed_count += 1
                except Exception as e:
                    error_count += 1
                    continue
            
            end_time = time.time()
            end_memory = psutil.Process().memory_info().rss / 1024 / 1024
            
            execution_time = end_time - start_time
            memory_usage = end_memory - start_memory
            cpu_usage = psutil.Process().cpu_percent()
            success_rate = (processed_count / len(self.test_data['texts'])) * 100
            throughput = processed_count / execution_time if execution_time > 0 else 0
            
            return TestResult(
                test_name="sequential_data_normalization",
                test_type="data_normalization",
                execution_time=execution_time,
                memory_usage=memory_usage,
                cpu_usage=cpu_usage,
                processed_items=processed_count,
                success_rate=success_rate,
                error_count=error_count,
                throughput=throughput,
                timestamp=datetime.now().isoformat()
            )
            
        except Exception as e:
            self.logger.error(f"순차적 데이터 정규화 테스트 오류: {str(e)}")
            return TestResult(
                test_name="sequential_data_normalization",
                test_type="data_normalization",
                execution_time=0,
                memory_usage=0,
                cpu_usage=0,
                processed_items=0,
                success_rate=0,
                error_count=1,
                throughput=0,
                timestamp=datetime.now().isoformat()
            )
    
    def _test_parallel_data_normalization(self) -> TestResult:
        """병렬 데이터 정규화 테스트"""
        start_time = time.time()
        start_memory = psutil.Process().memory_info().rss / 1024 / 1024
        
        try:
            processed_count = 0
            error_count = 0
            
            # 병렬 처리 시뮬레이션
            import threading
            import queue
            
            result_queue = queue.Queue()
            text_queue = queue.Queue()
            
            # 텍스트 큐에 데이터 추가
            for text in self.test_data['texts']:
                text_queue.put(text)
            
            # 워커 스레드 함수
            def worker():
                while not text_queue.empty():
                    try:
                        text = text_queue.get_nowait()
                        normalized = self._simple_text_normalization(text)
                        result_queue.put(('success', normalized))
                    except queue.Empty:
                        break
                    except Exception as e:
                        result_queue.put(('error', str(e)))
            
            # 워커 스레드 시작
            workers = []
            num_workers = min(4, len(self.test_data['texts']))
            
            for _ in range(num_workers):
