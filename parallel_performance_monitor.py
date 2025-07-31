"""
WinForms_Docs 병렬 처리 성능 모니터링 시스템

병렬 처리 환경에서의 성능 모니터링, 로깅, 통계 분석을 제공합니다.
실시간 성능 지표 수집, 성능 병목점 분석, 최적화 제안을 제공합니다.
"""

import time
import psutil
import threading
import logging
import json
import csv
from datetime import datetime, timedelta
from typing import Dict, List, Set, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path
from collections import defaultdict, deque
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class PerformanceMetrics:
    """성능 지표 데이터 클래스"""
    timestamp: str
    cpu_usage: float
    memory_usage: float
    memory_available: float
    disk_usage: float
    network_io: Dict[str, float]
    process_count: int
    thread_count: int
    load_average: List[float]
    
    def to_dict(self) -> Dict[str, Any]:
        """딕셔너리로 변환"""
        return asdict(self)

@dataclass
class ProcessingMetrics:
    """처리 성능 지표 데이터 클래스"""
    task_id: str
    task_type: str
    start_time: str
    end_time: str
    duration: float
    input_size: int
    output_size: int
    worker_count: int
    chunk_size: int
    memory_peak: float
    cpu_peak: float
    success: bool
    error_message: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """딕셔너리로 변환"""
        return asdict(self)

class PerformanceMonitor:
    """성능 모니터링 클래스"""
    
    def __init__(self, max_history: int = 1000):
        self.max_history = max_history
        self.metrics_history: deque = deque(maxlen=max_history)
        self.processing_metrics: List[ProcessingMetrics] = []
        self.is_monitoring = False
        self.monitor_thread = None
        self.monitor_interval = 1.0  # 1초 간격
        
        # 성능 통계
        self.total_processing_time = 0.0
        self.total_processed_items = 0
        self.successful_tasks = 0
        self.failed_tasks = 0
        
        # 병목점 분석
        self.bottleneck_analysis = {
            'cpu_bottlenecks': [],
            'memory_bottlenecks': [],
            'disk_bottlenecks': [],
            'network_bottlenecks': []
        }
        
        # 알림 설정
        self.alert_thresholds = {
            'cpu_usage': 80.0,
            'memory_usage': 85.0,
            'disk_usage': 90.0,
            'temperature': 70.0
        }
        
        # 로깅
        self.logger = logging.getLogger(__name__)
        
        # 시작 시간
        self.start_time = time.time()
    
    def start_monitoring(self):
        """모니터링 시작"""
        if self.is_monitoring:
            return
        
        self.is_monitoring = True
        self.monitor_thread = threading.Thread(target=self._monitor_loop)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()
        
        self.logger.info("성능 모니터링 시작")
    
    def stop_monitoring(self):
        """모니터링 중지"""
        self.is_monitoring = False
        if self.monitor_thread:
            self.monitor_thread.join()
        
        self.logger.info("성능 모니터링 중지")
    
    def _monitor_loop(self):
        """모니터링 루프"""
        while self.is_monitoring:
            try:
                # 시스템 지표 수집
                metrics = self._collect_system_metrics()
                self.metrics_history.append(metrics)
                
                # 병목점 분석
                self._analyze_bottlenecks(metrics)
                
                # 알림 확인
                self._check_alerts(metrics)
                
                # 대기
                time.sleep(self.monitor_interval)
                
            except Exception as e:
                self.logger.error(f"모니터링 오류: {str(e)}")
                time.sleep(self.monitor_interval)
    
    def _collect_system_metrics(self) -> PerformanceMetrics:
        """시스템 지표 수집"""
        # CPU 사용량
        cpu_usage = psutil.cpu_percent(interval=None)
        
        # 메모리 사용량
        memory = psutil.virtual_memory()
        memory_usage = memory.percent
        memory_available = memory.available / (1024 * 1024)  # MB
        
        # 디스크 사용량
        disk = psutil.disk_usage('/')
        disk_usage = disk.percent
        
        # 네트워크 I/O
        network = psutil.net_io_counters()
        network_io = {
            'bytes_sent': network.bytes_sent,
            'bytes_recv': network.bytes_recv,
            'packets_sent': network.packets_sent,
            'packets_recv': network.packets_recv
        }
        
        # 프로세스 및 스레드 수
        process_count = len(psutil.pids())
        thread_count = sum(p.num_threads() for p in psutil.process_iter(['num_threads']) if p.info['num_threads'])
        
        # 부하 평균 (Linux에서만 사용 가능)
        try:
            load_average = list(psutil.getloadavg())
        except (AttributeError, OSError):
            load_average = [0.0, 0.0, 0.0]
        
        return PerformanceMetrics(
            timestamp=datetime.now().isoformat(),
            cpu_usage=cpu_usage,
            memory_usage=memory_usage,
            memory_available=memory_available,
            disk_usage=disk_usage,
            network_io=network_io,
            process_count=process_count,
            thread_count=thread_count,
            load_average=load_average
        )
    
    def _analyze_bottlenecks(self, metrics: PerformanceMetrics):
        """병목점 분석"""
        # CPU 병목점
        if metrics.cpu_usage > self.alert_thresholds['cpu_usage']:
            self.bottleneck_analysis['cpu_bottlenecks'].append({
                'timestamp': metrics.timestamp,
                'cpu_usage': metrics.cpu_usage,
                'severity': 'high' if metrics.cpu_usage > 90 else 'medium'
            })
        
        # 메모리 병목점
        if metrics.memory_usage > self.alert_thresholds['memory_usage']:
            self.bottleneck_analysis['memory_bottlenecks'].append({
                'timestamp': metrics.timestamp,
                'memory_usage': metrics.memory_usage,
                'severity': 'high' if metrics.memory_usage > 95 else 'medium'
            })
        
        # 디스크 병목점
        if metrics.disk_usage > self.alert_thresholds['disk_usage']:
            self.bottleneck_analysis['disk_bottlenecks'].append({
                'timestamp': metrics.timestamp,
                'disk_usage': metrics.disk_usage,
                'severity': 'high' if metrics.disk_usage > 95 else 'medium'
            })
    
    def _check_alerts(self, metrics: PerformanceMetrics):
        """알림 확인"""
        alerts = []
        
        if metrics.cpu_usage > self.alert_thresholds['cpu_usage']:
            alerts.append(f"CPU 사용량 높음: {metrics.cpu_usage:.1f}%")
        
        if metrics.memory_usage > self.alert_thresholds['memory_usage']:
            alerts.append(f"메모리 사용량 높음: {metrics.memory_usage:.1f}%")
        
        if metrics.disk_usage > self.alert_thresholds['disk_usage']:
            alerts.append(f"디스크 사용량 높음: {metrics.disk_usage:.1f}%")
        
        if alerts:
            self.logger.warning(f"성능 알림: {'; '.join(alerts)}")
    
    def record_processing_metrics(self, task_id: str, task_type: str, start_time: float, 
                                 end_time: float, input_size: int, output_size: int,
                                 worker_count: int, chunk_size: int, memory_peak: float,
                                 cpu_peak: float, success: bool, error_message: str = None):
        """처리 성능 지표 기록"""
        duration = end_time - start_time
        
        processing_metrics = ProcessingMetrics(
            task_id=task_id,
            task_type=task_type,
            start_time=datetime.fromtimestamp(start_time).isoformat(),
            end_time=datetime.fromtimestamp(end_time).isoformat(),
            duration=duration,
            input_size=input_size,
            output_size=output_size,
            worker_count=worker_count,
            chunk_size=chunk_size,
            memory_peak=memory_peak,
            cpu_peak=cpu_peak,
            success=success,
            error_message=error_message
        )
        
        self.processing_metrics.append(processing_metrics)
        
        # 통계 업데이트
        self.total_processing_time += duration
        self.total_processed_items += input_size
        
        if success:
            self.successful_tasks += 1
        else:
            self.failed_tasks += 1
    
    def get_system_performance_summary(self) -> Dict[str, Any]:
        """시스템 성능 요약"""
        if not self.metrics_history:
            return {}
        
        # 최근 지표
        recent_metrics = list(self.metrics_history)[-60:]  # 최근 1분
        
        # 평균 및 최대값 계산
        avg_cpu = sum(m.cpu_usage for m in recent_metrics) / len(recent_metrics)
        max_cpu = max(m.cpu_usage for m in recent_metrics)
        
        avg_memory = sum(m.memory_usage for m in recent_metrics) / len(recent_metrics)
        max_memory = max(m.memory_usage for m in recent_metrics)
        
        avg_disk = sum(m.disk_usage for m in recent_metrics) / len(recent_metrics)
        max_disk = max(m.disk_usage for m in recent_metrics)
        
        return {
            'monitoring_duration': len(recent_metrics) * self.monitor_interval,
            'average_cpu_usage': avg_cpu,
            'peak_cpu_usage': max_cpu,
            'average_memory_usage': avg_memory,
            'peak_memory_usage': max_memory,
            'average_disk_usage': avg_disk,
            'peak_disk_usage': max_disk,
            'current_memory_available': recent_metrics[-1].memory_available,
            'process_count': recent_metrics[-1].process_count,
            'thread_count': recent_metrics[-1].thread_count
        }
    
    def get_processing_performance_summary(self) -> Dict[str, Any]:
        """처리 성능 요약"""
        if not self.processing_metrics:
            return {}
        
        # 성공 및 실패 작업 수
        total_tasks = len(self.processing_metrics)
        success_rate = (self.successful_tasks / total_tasks) * 100 if total_tasks > 0 else 0
        
        # 평균 처리 시간
        avg_processing_time = self.total_processing_time / total_tasks if total_tasks > 0 else 0
        
        # 처리 속도
        avg_processing_rate = self.total_processed_items / self.total_processing_time if self.total_processing_time > 0 else 0
        
        # 작업 유형별 통계
        task_type_stats = defaultdict(lambda: {'count': 0, 'total_time': 0, 'total_items': 0})
        
        for metrics in self.processing_metrics:
            task_type_stats[metrics.task_type]['count'] += 1
            task_type_stats[metrics.task_type]['total_time'] += metrics.duration
            task_type_stats[metrics.task_type]['total_items'] += metrics.input_size
        
        # 작업 유형별 평균 계산
        for task_type, stats in task_type_stats.items():
            if stats['count'] > 0:
                stats['avg_time'] = stats['total_time'] / stats['count']
                stats['avg_items'] = stats['total_items'] / stats['count']
                stats['avg_rate'] = stats['total_items'] / stats['total_time'] if stats['total_time'] > 0 else 0
        
        return {
            'total_tasks': total_tasks,
            'successful_tasks': self.successful_tasks,
            'failed_tasks': self.failed_tasks,
            'success_rate': success_rate,
            'total_processing_time': self.total_processing_time,
            'total_processed_items': self.total_processed_items,
            'average_processing_time': avg_processing_time,
            'average_processing_rate': avg_processing_rate,
            'task_type_stats': dict(task_type_stats),
            'bottleneck_analysis': self.bottleneck_analysis
        }
    
    def generate_performance_report(self, output_path: Path = None) -> Dict[str, Any]:
        """성능 보고서 생성"""
        report = {
            'report_generated': datetime.now().isoformat(),
            'system_performance': self.get_system_performance_summary(),
            'processing_performance': self.get_processing_performance_summary(),
            'recommendations': self._generate_recommendations(),
            'bottleneck_analysis': self.bottleneck_analysis
        }
        
        # 보고서 파일 저장
        if output_path:
            try:
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(report, f, indent=2, ensure_ascii=False)
                self.logger.info(f"성능 보고서 저장 완료: {output_path}")
            except Exception as e:
                self.logger.error(f"보고서 저장 오류: {str(e)}")
        
        return report
    
    def _generate_recommendations(self) -> List[str]:
        """최적화 제안 생성"""
        recommendations = []
        
        # 시스템 성능 기반 제안
        system_summary = self.get_system_performance_summary()
        
        if system_summary.get('average_cpu_usage', 0) > 80:
            recommendations.append("CPU 사용량이 높습니다. 워커 수를 줄이거나 작업을 분할하는 것을 고려하세요.")
        
        if system_summary.get('average_memory_usage', 0) > 80:
            recommendations.append("메모리 사용량이 높습니다. 메모리 정리 주기를 줄이거나 청크 크기를 조절하세요.")
        
        if system_summary.get('average_disk_usage', 0) > 80:
            recommendations.append("디스크 공간이 부족합니다. 디스크 정리를 수행하세요.")
        
        # 처리 성능 기반 제안
        processing_summary = self.get_processing_performance_summary()
        
        if processing_summary.get('success_rate', 0) < 90:
            recommendations.append("작업 실패율이 높습니다. 오류 로그를 확인하고 작업 크기를 조절하세요.")
        
        if processing_summary.get('average_processing_rate', 0) < 100:
            recommendations.append("처리 속도가 느립니다. 병렬 처리 설정을 최적화하세요.")
        
        # 병목점 기반 제안
        bottlenecks = self.bottleneck_analysis
        
        if bottlenecks['cpu_bottlenecks']:
            recommendations.append("CPU 병목점이 감지되었습니다. CPU 집약적 작업을 분산시키세요.")
        
        if bottlenecks['memory_bottlenecks']:
            recommendations.append("메모리 병목점이 감지되었습니다. 메모리 사용량을 모니터링하고 필요시 정리하세요.")
        
        if not recommendations:
            recommendations.append("시스템이 정상적으로 작동하고 있습니다.")
        
        return recommendations
    
    def export_metrics_to_csv(self, output_path: Path):
        """지표 데이터 CSV 내보내기"""
        if not self.metrics_history:
            return
        
        try:
            with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['timestamp', 'cpu_usage', 'memory_usage', 'disk_usage', 
                             'network_bytes_sent', 'network_bytes_recv', 'process_count', 'thread_count']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for metrics in self.metrics_history:
                    writer.writerow({
                        'timestamp': metrics.timestamp,
                        'cpu_usage': metrics.cpu_usage,
                        'memory_usage': metrics.memory_usage,
                        'disk_usage': metrics.disk_usage,
                        'network_bytes_sent': metrics.network_io['bytes_sent'],
                        'network_bytes_recv': metrics.network_io['bytes_recv'],
                        'process_count': metrics.process_count,
                        'thread_count': metrics.thread_count
                    })
            
            self.logger.info(f"지표 데이터 CSV 내보내기 완료: {output_path}")
        
        except Exception as e:
            self.logger.error(f"CSV 내보내기 오류: {str(e)}")
    
    def export_processing_metrics_to_csv(self, output_path: Path):
        """처리 성능 지표 CSV 내보내기"""
        if not self.processing_metrics:
            return
        
        try:
            with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['task_id', 'task_type', 'start_time', 'end_time', 'duration',
                             'input_size', 'output_size', 'worker_count', 'chunk_size',
                             'memory_peak', 'cpu_peak', 'success', 'error_message']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for metrics in self.processing_metrics:
                    writer.writerow({
                        'task_id': metrics.task_id,
                        'task_type': metrics.task_type,
                        'start_time': metrics.start_time,
                        'end_time': metrics.end_time,
                        'duration': metrics.duration,
                        'input_size': metrics.input_size,
                        'output_size': metrics.output_size,
                        'worker_count': metrics.worker_count,
                        'chunk_size': metrics.chunk_size,
                        'memory_peak': metrics.memory_peak,
                        'cpu_peak': metrics.cpu_peak,
                        'success': metrics.success,
                        'error_message': metrics.error_message or ''
                    })
            
            self.logger.info(f"처리 성능 지표 CSV 내보내기 완료: {output_path}")
        
        except Exception as e:
            self.logger.error(f"처리 성능 지표 CSV 내보내기 오류: {str(e)}")

# 전역 인스턴스
_default_performance_monitor = None

def get_default_performance_monitor() -> PerformanceMonitor:
    """기본 성능 모니터 인스턴스 반환"""
    global _default_performance_monitor
    if _default_performance_monitor is None:
        _default_performance_monitor = PerformanceMonitor()
    return _default_performance_monitor