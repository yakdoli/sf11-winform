"""
WinForms_Docs 성능 모니터링 시스템

주요 기능:
1. 실시간 성능 모니터링
2. 성능 데이터 수집 및 저장
3. 성능 분석 및 보고서 생성
4. 경고 시스템
5. 대시보드 데이터 제공

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0
"""

import os
import json
import time
import logging
import sqlite3
import threading
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, asdict
from contextlib import contextmanager
import psutil
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/performance_monitor.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class PerformanceMetrics:
    """성능 지표 데이터 클래스"""
    timestamp: str
    module_name: str
    operation_type: str
    processing_time: float
    memory_usage_mb: float
    cpu_usage_percent: float
    disk_io_read_mb: float = 0.0
    disk_io_write_mb: float = 0.0
    network_io_bytes: float = 0.0
    error_count: int = 0
    warning_count: int = 0
    custom_metrics: Optional[Dict[str, Any]] = None
    
    def __post_init__(self):
        if self.custom_metrics is None:
            self.custom_metrics = {}

@dataclass
class SystemResource:
    """시스템 리소스 데이터 클래스"""
    timestamp: str
    cpu_usage_percent: float
    memory_usage_percent: float
    memory_available_mb: float
    disk_usage_percent: float
    network_io_bytes: float
    process_count: int
    thread_count: int

@dataclass
class TestResult:
    """테스트 결과 데이터 클래스"""
    test_name: str
    module_name: str
    test_type: str
    execution_time: float
    memory_usage_mb: float
    cpu_usage_percent: float
    success: bool
    error_message: Optional[str] = None
    data_size: Optional[int] = None
    throughput: Optional[float] = None

@dataclass
class PerformanceDatabase:
    """성능 데이터베이스 관리 클래스"""
    db_path: str
    connection: Optional[sqlite3.Connection] = None
    
    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
    
    def execute_query(self, query: str, params: tuple = ()) -> List[tuple]:
        """쿼리 실행"""
        if not self.connection:
            raise ConnectionError("데이터베이스 연결이 설정되지 않았습니다")
        
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    
    def execute_update(self, query: str, params: tuple = ()) -> int:
        """업데이트 쿼리 실행"""
        if not self.connection:
            raise ConnectionError("데이터베이스 연결이 설정되지 않았습니다")
        
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor.rowcount

@dataclass
class PerformanceAlert:
    """성능 경고 데이터 클래스"""
    id: str
    timestamp: str
    level: str  # 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
    module_name: str
    message: str
    metrics: Dict[str, Any]
    resolved: bool = False

class PerformanceMonitor:
    """성능 모니터링 클래스"""
    
    def __init__(self, db_path: str = "performance_results/performance_metrics.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 스레드 관리
        self.monitoring_thread = None
        self.monitoring_active = False
        self.monitoring_lock = threading.Lock()
        
        # 성능 데이터 저장소
        self.metrics_buffer: List[PerformanceMetrics] = []
        self.system_resources: List[SystemResource] = []
        self.alerts: List[PerformanceAlert] = []
        
        # 설정
        self.config = {
            'monitoring_interval': 5,  # 초
            'buffer_size': 1000,
            'alert_thresholds': {
                'cpu_usage_percent': 85.0,
                'memory_usage_percent': 80.0,
                'disk_usage_percent': 90.0,
                'processing_time_seconds': 300.0,
                'error_count_threshold': 10
            },
            'data_retention_days': 30,
            'enable_real_time_monitoring': True,
            'enable_alerting': True,
            'enable_system_monitoring': True
        }
        
        # 데이터베이스 초기화
        self._init_database()
        
        # 성능 통계
        self.performance_stats = {
            'total_operations': 0,
            'total_processing_time': 0.0,
            'average_processing_time': 0.0,
            'peak_memory_usage': 0.0,
            'total_errors': 0,
            'total_warnings': 0
        }
        
        logger.info("성능 모니터링 시스템 초기화 완료")
    
    def _init_database(self):
        """데이터베이스 초기화"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 성능 지표 테이블
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS performance_metrics (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp TEXT NOT NULL,
                        module_name TEXT NOT NULL,
                        operation_type TEXT NOT NULL,
                        processing_time REAL NOT NULL,
                        memory_usage_mb REAL NOT NULL,
                        cpu_usage_percent REAL NOT NULL,
                        disk_io_read_mb REAL DEFAULT 0.0,
                        disk_io_write_mb REAL DEFAULT 0.0,
                        network_io_bytes REAL DEFAULT 0.0,
                        error_count INTEGER DEFAULT 0,
                        warning_count INTEGER DEFAULT 0,
                        custom_metrics TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # 시스템 리소스 테이블
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS system_resources (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp TEXT NOT NULL,
                        cpu_usage_percent REAL NOT NULL,
                        memory_usage_percent REAL NOT NULL,
                        memory_available_mb REAL NOT NULL,
                        disk_usage_percent REAL NOT NULL,
                        network_io_bytes REAL NOT NULL,
                        process_count INTEGER NOT NULL,
                        thread_count INTEGER NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # 성능 경고 테이블
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS performance_alerts (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        alert_id TEXT UNIQUE NOT NULL,
                        timestamp TEXT NOT NULL,
                        level TEXT NOT NULL,
                        module_name TEXT NOT NULL,
                        message TEXT NOT NULL,
                        metrics TEXT,
                        resolved BOOLEAN DEFAULT FALSE,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        resolved_at TIMESTAMP NULL
                    )
                ''')
                
                # 인덱스 생성
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_metrics_timestamp ON performance_metrics(timestamp)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_resources_timestamp ON system_resources(timestamp)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_alerts_timestamp ON performance_alerts(timestamp)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_alerts_resolved ON performance_alerts(resolved)')
                
                conn.commit()
                logger.info("데이터베이스 초기화 완료")
                
        except Exception as e:
            logger.error(f"데이터베이스 초기화 오류: {str(e)}")
            raise
    
    def start_monitoring(self):
        """모니터링 시작"""
        if not self.monitoring_active:
            self.monitoring_active = True
            self.monitoring_thread = threading.Thread(target=self._monitoring_loop, daemon=True)
            self.monitoring_thread.start()
            logger.info("성능 모니터링 시작")
    
    def stop_monitoring(self):
        """모니터링 중지"""
        self.monitoring_active = False
        if self.monitoring_thread:
            self.monitoring_thread.join()
        logger.info("성능 모니터링 중지")
    
    def _monitoring_loop(self):
        """모니터링 루프"""
        while self.monitoring_active:
            try:
                # 시스템 리소스 모니터링
                if self.config['enable_system_monitoring']:
                    self._monitor_system_resources()
                
                # 버퍼 데이터 저장
                self._flush_buffer()
                
                # 데이터 정리
                self._cleanup_old_data()
                
                # 대기
                time.sleep(self.config['monitoring_interval'])
                
            except Exception as e:
                logger.error(f"모니터링 루프 오류: {str(e)}")
                time.sleep(self.config['monitoring_interval'])
    
    def _monitor_system_resources(self):
        """시스템 리소스 모니터링"""
        try:
            process = psutil.Process()
            
            # 현재 프로세스 리소스
            cpu_percent = process.cpu_percent()
            memory_info = process.memory_info()
            memory_mb = memory_info.rss / 1024 / 1024
            
            # 시스템 전체 리소스
            system_cpu = psutil.cpu_percent()
            system_memory = psutil.virtual_memory()
            disk_usage = psutil.disk_usage('/')
            
            # 네트워크 I/O
            network_io = psutil.net_io_counters()
            
            # 시스템 리소스 데이터 생성
            resource_data = SystemResource(
                timestamp=datetime.now().isoformat(),
                cpu_usage_percent=system_cpu,
                memory_usage_percent=system_memory.percent,
                memory_available_mb=system_memory.available / 1024 / 1024,
                disk_usage_percent=disk_usage.percent,
                network_io_bytes=network_io.bytes_sent + network_io.bytes_recv,
                process_count=len(psutil.pids()),
                thread_count=process.num_threads()
            )
            
            with self.monitoring_lock:
                self.system_resources.append(resource_data)
                
                # 최근 1000개만 유지
                if len(self.system_resources) > 1000:
                    self.system_resources = self.system_resources[-1000:]
                
                # 데이터베이스 저장
                self._save_system_resource(resource_data)
                
                # 경고 체크
                if self.config['enable_alerting']:
                    self._check_system_alerts(resource_data)
                    
        except Exception as e:
            logger.error(f"시스템 리소스 모니터링 오류: {str(e)}")
    
    def _check_system_alerts(self, resource_data: SystemResource):
        """시스템 경고 체크"""
        thresholds = self.config['alert_thresholds']
        
        alerts = []
        
        # CPU 사용량 경고
        if resource_data.cpu_usage_percent > thresholds['cpu_usage_percent']:
            alerts.append(PerformanceAlert(
                id=f"cpu_high_{int(time.time())}",
                timestamp=datetime.now().isoformat(),
                level='WARNING',
                module_name='SYSTEM',
                message=f"CPU 사용량 높음: {resource_data.cpu_usage_percent:.1f}%",
                metrics={'cpu_usage_percent': resource_data.cpu_usage_percent}
            ))
        
        # 메모리 사용량 경고
        if resource_data.memory_usage_percent > thresholds['memory_usage_percent']:
            alerts.append(PerformanceAlert(
                id=f"memory_high_{int(time.time())}",
                timestamp=datetime.now().isoformat(),
                level='WARNING',
                module_name='SYSTEM',
                message=f"메모리 사용량 높음: {resource_data.memory_usage_percent:.1f}%",
                metrics={'memory_usage_percent': resource_data.memory_usage_percent}
            ))
        
        # 디스크 사용량 경고
        if resource_data.disk_usage_percent > thresholds['disk_usage_percent']:
            alerts.append(PerformanceAlert(
                id=f"disk_high_{int(time.time())}",
                timestamp=datetime.now().isoformat(),
                level='ERROR',
                module_name='SYSTEM',
                message=f"디스크 사용량 높음: {resource_data.disk_usage_percent:.1f}%",
                metrics={'disk_usage_percent': resource_data.disk_usage_percent}
            ))
        
        # 경고 저장
        for alert in alerts:
            self._save_alert(alert)
            with self.monitoring_lock:
                self.alerts.append(alert)
                logger.warning(f"성능 경고: {alert.message}")
    
    def record_performance_metrics(self, module_name: str, operation_type: str,
                                 processing_time: float, **kwargs):
        """성능 지표 기록"""
        try:
            # 현재 시스템 상태 가져오기
            process = psutil.Process()
            memory_info = process.memory_info()
            cpu_percent = process.cpu_percent()
            
            # 성능 지표 생성
            metrics = PerformanceMetrics(
                timestamp=datetime.now().isoformat(),
                module_name=module_name,
                operation_type=operation_type,
                processing_time=processing_time,
                memory_usage_mb=memory_info.rss / 1024 / 1024,
                cpu_usage_percent=cpu_percent,
                disk_io_read_mb=kwargs.get('disk_io_read_mb', 0.0),
                disk_io_write_mb=kwargs.get('disk_io_write_mb', 0.0),
                network_io_bytes=kwargs.get('network_io_bytes', 0.0),
                error_count=kwargs.get('error_count', 0),
                warning_count=kwargs.get('warning_count', 0),
                custom_metrics=kwargs.get('custom_metrics', {})
            )
            
            # 버퍼에 추가
            with self.monitoring_lock:
                self.metrics_buffer.append(metrics)
                
                # 버퍼 크기 제한
                if len(self.metrics_buffer) > self.config['buffer_size']:
                    self.metrics_buffer = self.metrics_buffer[-self.config['buffer_size']:]
                
                # 성능 통계 업데이트
                self._update_performance_stats(metrics)
                
                # 실시간 모니터링 활성화 시 바로 저장
                if self.config['enable_real_time_monitoring']:
                    self._save_metrics(metrics)
                
                # 경고 체크
                if self.config['enable_alerting']:
                    self._check_performance_alerts(metrics)
            
            logger.debug(f"성능 지표 기록: {module_name}.{operation_type} - {processing_time:.3f}초")
            
        except Exception as e:
            logger.error(f"성능 지표 기록 오류: {str(e)}")
    
    def _update_performance_stats(self, metrics: PerformanceMetrics):
        """성능 통계 업데이트"""
        stats = self.performance_stats
        
        stats['total_operations'] += 1
        stats['total_processing_time'] += metrics.processing_time
        stats['total_errors'] += metrics.error_count
        stats['total_warnings'] += metrics.warning_count
        
        # 평균 처리 시간 계산
        if stats['total_operations'] > 0:
            stats['average_processing_time'] = stats['total_processing_time'] / stats['total_operations']
        
        # 최대 메모리 사용량 업데이트
        if metrics.memory_usage_mb > stats['peak_memory_usage']:
            stats['peak_memory_usage'] = metrics.memory_usage_mb
    
    def _check_performance_alerts(self, metrics: PerformanceMetrics):
        """성능 경고 체크"""
        thresholds = self.config['alert_thresholds']
        alerts = []
        
        # 처리 시간 경고
        if metrics.processing_time > thresholds['processing_time_seconds']:
            alerts.append(PerformanceAlert(
                id=f"slow_operation_{int(time.time())}",
                timestamp=datetime.now().isoformat(),
                level='WARNING',
                module_name=metrics.module_name,
                message=f"처리 시간 길음: {metrics.operation_type} - {metrics.processing_time:.2f}초",
                metrics={'processing_time': metrics.processing_time}
            ))
        
        # 오류 수 경고
        if metrics.error_count > thresholds['error_count_threshold']:
            alerts.append(PerformanceAlert(
                id=f"high_errors_{int(time.time())}",
                timestamp=datetime.now().isoformat(),
                level='ERROR',
                module_name=metrics.module_name,
                message=f"오류 수 많음: {metrics.error_count}개",
                metrics={'error_count': metrics.error_count}
            ))
        
        # 경고 저장
        for alert in alerts:
            self._save_alert(alert)
            with self.monitoring_lock:
                self.alerts.append(alert)
                logger.warning(f"성능 경고: {alert.message}")
    
    def _flush_buffer(self):
        """버퍼 데이터 데이터베이스에 저장"""
        if not self.metrics_buffer:
            return
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                for metrics in self.metrics_buffer:
                    cursor.execute('''
                        INSERT INTO performance_metrics 
                        (timestamp, module_name, operation_type, processing_time, 
                         memory_usage_mb, cpu_usage_percent, disk_io_read_mb, 
                         disk_io_write_mb, network_io_bytes, error_count, 
                         warning_count, custom_metrics)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        metrics.timestamp,
                        metrics.module_name,
                        metrics.operation_type,
                        metrics.processing_time,
                        metrics.memory_usage_mb,
                        metrics.cpu_usage_percent,
                        metrics.disk_io_read_mb,
                        metrics.disk_io_write_mb,
                        metrics.network_io_bytes,
                        metrics.error_count,
                        metrics.warning_count,
                        json.dumps(metrics.custom_metrics, ensure_ascii=False)
                    ))
                
                conn.commit()
                
            # 버퍼 초기화
            with self.monitoring_lock:
                self.metrics_buffer.clear()
                
        except Exception as e:
            logger.error(f"버퍼 플러시 오류: {str(e)}")
    
    def _save_metrics(self, metrics: PerformanceMetrics):
        """개별 성능 지표 저장"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO performance_metrics 
                    (timestamp, module_name, operation_type, processing_time, 
                     memory_usage_mb, cpu_usage_percent, disk_io_read_mb, 
                     disk_io_write_mb, network_io_bytes, error_count, 
                     warning_count, custom_metrics)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    metrics.timestamp,
                    metrics.module_name,
                    metrics.operation_type,
                    metrics.processing_time,
                    metrics.memory_usage_mb,
                    metrics.cpu_usage_percent,
                    metrics.disk_io_read_mb,
                    metrics.disk_io_write_mb,
                    metrics.network_io_bytes,
                    metrics.error_count,
                    metrics.warning_count,
                    json.dumps(metrics.custom_metrics, ensure_ascii=False)
                ))
                conn.commit()
                
        except Exception as e:
            logger.error(f"성능 지표 저장 오류: {str(e)}")
    
    def _save_system_resource(self, resource: SystemResource):
        """시스템 리소스 저장"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO system_resources 
                    (timestamp, cpu_usage_percent, memory_usage_percent, 
                     memory_available_mb, disk_usage_percent, network_io_bytes, 
                     process_count, thread_count)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    resource.timestamp,
                    resource.cpu_usage_percent,
                    resource.memory_usage_percent,
                    resource.memory_available_mb,
                    resource.disk_usage_percent,
                    resource.network_io_bytes,
                    resource.process_count,
                    resource.thread_count
                ))
                conn.commit()
                
        except Exception as e:
            logger.error(f"시스템 리소스 저장 오류: {str(e)}")
    
    def _save_alert(self, alert: PerformanceAlert):
        """성능 경고 저장"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT OR REPLACE INTO performance_alerts 
                    (alert_id, timestamp, level, module_name, message, metrics, resolved, resolved_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    alert.id,
                    alert.timestamp,
                    alert.level,
                    alert.module_name,
                    alert.message,
                    json.dumps(alert.metrics, ensure_ascii=False),
                    alert.resolved,
                    datetime.now().isoformat() if alert.resolved else None
                ))
                conn.commit()
                
        except Exception as e:
            logger.error(f"성능 경고 저장 오류: {str(e)}")
    
    def _cleanup_old_data(self):
        """오래된 데이터 정리"""
        try:
            retention_days = self.config['data_retention_days']
            cutoff_date = datetime.now() - timedelta(days=retention_days)
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 성능 지표 정리
                cursor.execute('''
                    DELETE FROM performance_metrics 
                    WHERE timestamp < ?
                ''', (cutoff_date.isoformat(),))
                
                # 시스템 리소스 정리
                cursor.execute('''
                    DELETE FROM system_resources 
                    WHERE timestamp < ?
                ''', (cutoff_date.isoformat(),))
                
                # 해결된 경고 정리
                cursor.execute('''
                    DELETE FROM performance_alerts 
                    WHERE resolved = 1 AND resolved_at < ?
                ''', (cutoff_date.isoformat(),))
                
                conn.commit()
                
            logger.debug(f"오래된 데이터 정리 완료 (보관 기간: {retention_days}일)")
            
        except Exception as e:
            logger.error(f"데이터 정리 오류: {str(e)}")
    
    def get_performance_report(self, start_date: Optional[str] = None, 
                             end_date: Optional[str] = None,
                             module_name: Optional[str] = None) -> Dict[str, Any]:
        """성능 보고서 생성"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 기본 쿼리
                query = '''
                    SELECT timestamp, module_name, operation_type, processing_time,
                           memory_usage_mb, cpu_usage_percent, error_count, warning_count
                    FROM performance_metrics
                    WHERE 1=1
                '''
                params = []
                
                # 필터 조건 추가
                if start_date:
                    query += ' AND timestamp >= ?'
                    params.append(start_date)
                
                if end_date:
                    query += ' AND timestamp <= ?'
                    params.append(end_date)
                
                if module_name:
                    query += ' AND module_name = ?'
                    params.append(module_name)
                
                query += ' ORDER BY timestamp DESC'
                
                # 데이터 조회
                cursor.execute(query, params)
                rows = cursor.fetchall()
                
                # 데이터프레임 변환
                df = pd.DataFrame(rows, columns=[
                    'timestamp', 'module_name', 'operation_type', 'processing_time',
                    'memory_usage_mb', 'cpu_usage_percent', 'error_count', 'warning_count'
                ])
                
                if df.empty:
                    return {
                        'status': 'error',
                        'message': '조회된 데이터가 없습니다.',
                        'data': None
                    }
                
                # 보고서 데이터 생성
                report = {
                    'generated_at': datetime.now().isoformat(),
                    'period': {
                        'start': start_date or df['timestamp'].min(),
                        'end': end_date or df['timestamp'].max()
                    },
                    'summary': {
                        'total_operations': len(df),
                        'total_processing_time': df['processing_time'].sum(),
                        'average_processing_time': df['processing_time'].mean(),
                        'peak_memory_usage': df['memory_usage_mb'].max(),
                        'total_errors': df['error_count'].sum(),
                        'total_warnings': df['warning_count'].sum()
                    },
                    'module_breakdown': {},
                    'operation_breakdown': {},
                    'performance_trends': {},
                    'recommendations': []
                }
                
                # 모듈별 분석
                module_stats = df.groupby('module_name').agg({
                    'processing_time': ['count', 'sum', 'mean', 'std'],
                    'memory_usage_mb': ['max', 'mean'],
                    'error_count': 'sum',
                    'warning_count': 'sum'
                }).round(3)
                
                for module, stats in module_stats.iterrows():
                    report['module_breakdown'][module] = {
                        'operation_count': stats[('processing_time', 'count')],
                        'total_processing_time': stats[('processing_time', 'sum')],
                        'average_processing_time': stats[('processing_time', 'mean')],
                        'processing_time_std': stats[('processing_time', 'std')],
                        'peak_memory_usage': stats[('memory_usage_mb', 'max')],
                        'average_memory_usage': stats[('memory_usage_mb', 'mean')],
                        'total_errors': stats[('error_count', 'sum')],
                        'total_warnings': stats[('warning_count', 'sum')]
                    }
                
                # 작업 유형별 분석
                operation_stats = df.groupby(['module_name', 'operation_type']).agg({
                    'processing_time': ['count', 'mean', 'max'],
                    'memory_usage_mb': ['mean', 'max']
                }).round(3)
                
                # operation_stats의 인덱스를 튜플로 변환하여 반복
                for idx in operation_stats.index:
                    module, operation = idx
                    stats = operation_stats.loc[idx]
                    # module과 operation은 모두 문자열이므로 해시 가능
                    if module not in report['operation_breakdown']:
                        report['operation_breakdown'][module] = {}
                    
                    report['operation_breakdown'][module][operation] = {
                        'operation_count': stats[('processing_time', 'count')],
                        'average_processing_time': stats[('processing_time', 'mean')],
                        'max_processing_time': stats[('processing_time', 'max')],
                        'average_memory_usage': stats[('memory_usage_mb', 'mean')],
                        'max_memory_usage': stats[('memory_usage_mb', 'max')]
                    }
                
                # 성능 추세 분석
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                df['date'] = df['timestamp'].dt.date
                
                daily_stats = df.groupby('date').agg({
                    'processing_time': ['mean', 'sum'],
                    'memory_usage_mb': ['mean', 'max'],
                    'error_count': 'sum'
                }).round(3)
                
                report['performance_trends'] = {
                    'daily_average_processing_time': daily_stats[('processing_time', 'mean')].to_dict(),
                    'daily_total_processing_time': daily_stats[('processing_time', 'sum')].to_dict(),
                    'daily_average_memory_usage': daily_stats[('memory_usage_mb', 'mean')].to_dict(),
                    'daily_peak_memory_usage': daily_stats[('memory_usage_mb', 'max')].to_dict(),
                    'daily_error_count': daily_stats[('error_count', 'sum')].to_dict()
                }
                
                # 개선 사항 생성
                recommendations = self._generate_recommendations(df, report)
                report['recommendations'] = recommendations
                
                return {
                    'status': 'success',
                    'message': '성능 보고서 생성 완료',
                    'data': report
                }
                
        except Exception as e:
            logger.error(f"성능 보고서 생성 오류: {str(e)}")
            return {
                'status': 'error',
                'message': f'성능 보고서 생성 실패: {str(e)}',
                'data': None
            }
    
    def _generate_recommendations(self, df: pd.DataFrame, report: Dict[str, Any]) -> List[str]:
        """개선 사항 생성"""
        recommendations = []
        
        # 평균 처리 시기가 긴 모듈
        slow_modules = df.groupby('module_name')['processing_time'].mean().sort_values(ascending=False)
        for module, avg_time in slow_modules.head(3).items():
            if avg_time > 10:  # 10초 이상
                recommendations.append(f"모듈 '{module}'의 평균 처리 시간이 {avg_time:.2f}초로 길어 성능 개선이 필요합니다.")
        
        # 메모리 사용량이 높은 모듈
        memory_intensive_modules = df.groupby('module_name')['memory_usage_mb'].max().sort_values(ascending=False)
        for module, max_memory in memory_intensive_modules.head(3).items():
            if max_memory > 1000:  # 1GB 이상
                recommendations.append(f"모듈 '{module}'의 최대 메모리 사용량이 {max_memory:.2f}MB로 높습니다. 메모리 누수 확인이 필요합니다.")
        
        # 오류가 많은 모듈
        error_prone_modules = df.groupby('module_name')['error_count'].sum().sort_values(ascending=False)
        for module, total_errors in error_prone_modules.head(3).items():
            if total_errors > 10:  # 10개 이상
                recommendations.append(f"모듈 '{module}'에서 총 {total_errors}개의 오류가 발생했습니다. 오류 로그를 확인하고 개선이 필요합니다.")
        
        # 처리 시간 변동성이 큰 모듈
        time_variability = df.groupby('module_name')['processing_time'].std().sort_values(ascending=False)
        for module, std_time in time_variability.head(3).items():
            if std_time > 5:  # 5초 이상 표준편차
                recommendations.append(f"모듈 '{module}'의 처리 시간 변동성이 큽니다({std_time:.2f}초). 안정성 개선이 필요합니다.")
        
        return recommendations
    
    def get_system_status(self) -> Dict[str, Any]:
        """시스템 상태 조회"""
        try:
            # 현재 시스템 리소스
            process = psutil.Process()
            memory_info = process.memory_info()
            
            # 최근 시스템 리소스 데이터
            recent_resources = None
            if self.system_resources:
                recent_resources = self.system_resources[-1]
            
            # 활성 경고
            active_alerts = [alert for alert in self.alerts if not alert.resolved]
            
            # 성능 통계
            stats = self.performance_stats.copy()
            
            return {
                'status': 'healthy',
                'timestamp': datetime.now().isoformat(),
                'current_resources': {
                    'cpu_usage_percent': process.cpu_percent(),
                    'memory_usage_mb': memory_info.rss / 1024 / 1024,
                    'memory_usage_percent': process.memory_percent(),
                    'thread_count': process.num_threads(),
                    'open_files': len(process.open_files()),
                    'connections': len(process.connections())
                },
                'recent_resources': asdict(recent_resources) if recent_resources else None,
                'active_alerts': len(active_alerts),
                'performance_stats': stats,
                'monitoring_status': {
                    'active': self.monitoring_active,
                    'buffer_size': len(self.metrics_buffer),
                    'system_resources_count': len(self.system_resources)
                }
            }
            
        except Exception as e:
            logger.error(f"시스템 상태 조회 오류: {str(e)}")
            return {
                'status': 'error',
                'message': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    def get_alerts(self, level: Optional[str] = None, 
                   module_name: Optional[str] = None,
                   resolved: Optional[bool] = None,
                   limit: int = 100) -> List[Dict[str, Any]]:
        """경고 목록 조회"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 쿼리
                query = '''
                    SELECT alert_id, timestamp, level, module_name, message, 
                           metrics, resolved, resolved_at
                    FROM performance_alerts
                    WHERE 1=1
                '''
                params = []
                
                # 필터 조건
                if level:
                    query += ' AND level = ?'
                    params.append(level)
                
                if module_name:
                    query += ' AND module_name = ?'
                    params.append(module_name)
                
                if resolved is not None:
                    query += ' AND resolved = ?'
                    params.append(resolved)
                
                query += ' ORDER BY timestamp DESC LIMIT ?'
                params.append(limit)
                
                cursor.execute(query, params)
                rows = cursor.fetchall()
                
                alerts = []
                for row in rows:
                    alert = {
                        'id': row[0],
                        'timestamp': row[1],
                        'level': row[2],
                        'module_name': row[3],
                        'message': row[4],
                        'metrics': json.loads(row[5]) if row[5] else {},
                        'resolved': bool(row[6]),
                        'resolved_at': row[7]
                    }
                    alerts.append(alert)
                
                return alerts
                
        except Exception as e:
            logger.error(f"경고 목록 조회 오류: {str(e)}")
            return []
    
    def resolve_alert(self, alert_id: str) -> bool:
        """경고 해결"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE performance_alerts 
                    SET resolved = 1, resolved_at = ?
                    WHERE alert_id = ?
                ''', (datetime.now().isoformat(), alert_id))
                conn.commit()
                
                # 메모리 내 경고 업데이트
                with self.monitoring_lock:
                    for alert in self.alerts:
                        if alert.id == alert_id:
                            alert.resolved = True
                            break
                
                return cursor.rowcount > 0
                
        except Exception as e:
            logger.error(f"경고 해결 오류: {str(e)}")
            return False
    
    def export_performance_data(self, output_path: str, 
                               format: str = 'json',
                               start_date: Optional[str] = None,
                               end_date: Optional[str] = None) -> bool:
        """성능 데이터 내보내기"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 데이터 조회
                query = '''
                    SELECT timestamp, module_name, operation_type, processing_time,
                           memory_usage_mb, cpu_usage_percent, error_count, warning_count
                    FROM performance_metrics
                    WHERE 1=1
                '''
                params = []
                
                if start_date:
                    query += ' AND timestamp >= ?'
                    params.append(start_date)
                
                if end_date:
                    query += ' AND timestamp <= ?'
                    params.append(end_date)
                
                query += ' ORDER BY timestamp'
                
                cursor.execute(query, params)
                rows = cursor.fetchall()
                
                # 데이터 변환
                data = []
                for row in rows:
                    record = {
                        'timestamp': row[0],
                        'module_name': row[1],
                        'operation_type': row[2],
                        'processing_time': row[3],
                        'memory_usage_mb': row[4],
                        'cpu_usage_percent': row[5],
                        'error_count': row[6],
                        'warning_count': row[7]
                    }
                    data.append(record)
                
                # 파일 저장
                output_path_obj = Path(output_path)
                output_path_obj.parent.mkdir(parents=True, exist_ok=True)
                
                if format.lower() == 'json':
                    with open(output_path, 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)
                elif format.lower() == 'csv':
                    df = pd.DataFrame(data)
                    df.to_csv(output_path, index=False, encoding='utf-8')
                else:
                    raise ValueError(f"지원하지 않는 형식: {format}")
                
                logger.info(f"성능 데이터 내보내기 완료: {output_path}")
                return True
                
        except Exception as e:
            logger.error(f"성능 데이터 내보내기 오류: {str(e)}")
            return False
    
    def cleanup(self):
        """정리 작업"""
        try:
            self.stop_monitoring()
            
            # 남은 버퍼 데이터 저장
            if self.metrics_buffer:
                self._flush_buffer()
            
            logger.info("성능 모니터링 시스템 정리 완료")
            
        except Exception as e:
            logger.error(f"정리 작업 오류: {str(e)}")

# 전역 인스턴스
_performance_monitor = None

def get_performance_monitor() -> PerformanceMonitor:
    """전역 성능 모니터 인스턴스 반환"""
    global _performance_monitor
    if _performance_monitor is None:
        _performance_monitor = PerformanceMonitor()
    return _performance_monitor

def initialize_performance_monitor(db_path: Optional[str] = None) -> PerformanceMonitor:
    """성능 모니터 초기화"""
    global _performance_monitor
    _performance_monitor = PerformanceMonitor(db_path or "performance_results/performance_metrics.db")
    return _performance_monitor

@contextmanager
def performance_monitoring(module_name: str, operation_type: str):
    """성능 모니터링 컨텍스트 매니저"""
    monitor = get_performance_monitor()
    start_time = time.time()
    
    try:
        yield
    except Exception as e:
        monitor.record_performance_metrics(
            module_name=module_name,
            operation_type=operation_type,
            processing_time=time.time() - start_time,
            error_count=1,
            error_message=str(e)
        )
        raise
    else:
        monitor.record_performance_metrics(
            module_name=module_name,
            operation_type=operation_type,
            processing_time=time.time() - start_time
        )

# 데코레이터
def monitor_performance(operation_type: str):
    """성능 모니터링 데코레이터"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            monitor = get_performance_monitor()
            start_time = time.time()
            
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                monitor.record_performance_metrics(
                    module_name=func.__module__,
                    operation_type=operation_type,
                    processing_time=time.time() - start_time,
                    error_count=1,
                    error_message=str(e)
                )
                raise
            else:
                monitor.record_performance_metrics(
                    module_name=func.__module__,
                    operation_type=operation_type,
                    processing_time=time.time() - start_time
                )
        
        return wrapper
    return decorator

if __name__ == "__main__":
    # 테스트 코드
    print("성능 모니터링 시스템 테스트 시작")
    
    # 모니터 초기화
    monitor = initialize_performance_monitor()
    
    # 모니터링 시작
    monitor.start_monitoring()
    
    # 테스트 데이터 생성
    test_modules = ['data_cleaner', 'data_normalizer', 'deduplication']
    test_operations = ['process_file', 'normalize_data', 'check_duplicates']
    
    for i in range(10):
        module = test_modules[i % len(test_modules)]
        operation = test_operations[i % len(test_operations)]
        
        # 성능 측정
        start_time = time.time()
        time.sleep(0.1 + (i % 5) * 0.1)  # 가변 처리 시간
        processing_time = time.time() - start_time
        
        # 성능 지표 기록
        monitor.record_performance_metrics(
            module_name=module,
            operation_type=operation,
            processing_time=processing_time,
            memory_usage_mb=100 + i * 10,
            cpu_usage_percent=20 + i * 5,
            error_count=0 if i % 3 != 0 else 1,
            custom_metrics={'test_iteration': i}
        )
        
        print(f"테스트 {i+1}: {module}.{operation} - {processing_time:.3f}초")
    
    # 시스템 상태 조회
    status = monitor.get_system_status()
    print(f"시스템 상태: {status}")
    
    # 성능 보고서 생성
    report = monitor.get_performance_report()
    if report['status'] == 'success':
        print(f"성능 보고서 생성 완료")
        print(f"총 작업 수: {report['data']['summary']['total_operations']}")
        print(f"평균 처리 시간: {report['data']['summary']['average_processing_time']:.3f}초")
        print(f"최대 메모리 사용: {report['data']['summary']['peak_memory_usage']:.2f}MB")
        
        # 개선 사항 출력
        if report['data']['recommendations']:
            print("\n개선 사항:")
            for rec in report['data']['recommendations']:
                print(f"  - {rec}")
    
    # 모니터링 중지
    monitor.stop_monitoring()
    print("성능 모니터링 시스템 테스트 완료")
