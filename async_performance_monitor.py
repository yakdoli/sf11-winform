"""
WinForms_Docs 비동기 성능 모니터링 시스템

주요 기능:
==========
1. 실시간 성능 모니터링
   - 파일 I/O 성능 지표 수집
   - 비동기 처리 통계 추적
   - 시스템 리소스 모니터링

2. 성능 분석 및 보고
   - 성능 병목점 식별
   - 최적화 기회 발견
   - 자동 보고서 생성

3. 경고 및 알림
   - 성능 임계값 모니터링
   - 이상 감지 및 알림
   - 자동 복구 제안

4. 성능 히스토리 관리
   - 성능 데이터 저장
   - 장기 추이 분석
   - 성능 개선 효과 측정

통합 전략:
==========
- 기존 PerformanceMonitor와의 호환성 유지
- AsyncFileManager 내장 모니터링 강화
- 실시간 대시보드 지원
- 데이터베이스 저장 및 분석

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0 (통합 성능 모니터링)
"""

import asyncio
import logging
import time
import json
import sqlite3
import threading
from pathlib import Path
from typing import Dict, List, Optional, Any, Union, Callable
from dataclasses import dataclass, asdict, field
from datetime import datetime, timedelta
from enum import Enum
import psutil
import gc
import statistics
from collections import deque
import threading

# 로깅 설정
logger = logging.getLogger(__name__)

class MetricType(Enum):
    """성능 지표 유형"""
    THROUGHPUT = "throughput"
    LATENCY = "latency"
    MEMORY = "memory"
    CPU = "cpu"
    DISK_IO = "disk_io"
    NETWORK_IO = "network_io"
    ERROR_RATE = "error_rate"

@dataclass
class PerformanceMetric:
    """성능 지표 데이터 클래스"""
    timestamp: float
    metric_type: MetricType
    value: float
    unit: str
    file_path: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """딕셔너리 변환"""
        return {
            'timestamp': self.timestamp,
            'metric_type': self.metric_type.value,
            'value': self.value,
            'unit': self.unit,
            'file_path': self.file_path,
            'metadata': self.metadata
        }

@dataclass
class PerformanceAlert:
    """성능 알림 데이터 클래스"""
    alert_id: str
    timestamp: float
    metric_type: MetricType
    current_value: float
    threshold: float
    severity: str  # 'low', 'medium', 'high', 'critical'
    message: str
    suggested_action: Optional[str] = None
    resolved: bool = False
    
    def to_dict(self) -> Dict[str, Any]:
        """딕셔너리 변환"""
        return {
            'alert_id': self.alert_id,
            'timestamp': self.timestamp,
            'metric_type': self.metric_type.value,
            'current_value': self.current_value,
            'threshold': self.threshold,
            'severity': self.severity,
            'message': self.message,
            'suggested_action': self.suggested_action,
            'resolved': self.resolved
        }

class AsyncPerformanceMonitor:
    """비동기 성능 모니터링 시스템"""
    
    def __init__(self, 
                 db_path: Optional[str] = None,
                 max_history_size: int = 10000,
                 alert_thresholds: Optional[Dict[str, Dict[str, float]]] = None):
        """
        성능 모니터링 초기화
        
        Args:
            db_path: 성능 데이터베이스 경로
            max_history_size: 최대 히스토리 크기
            alert_thresholds: 알림 임계값 설정
        """
        self.db_path = db_path or "performance_data.db"
        self.max_history_size = max_history_size
        self.alert_thresholds = alert_thresholds or self._default_alert_thresholds()
        
        # 성능 지표 히스토리
        self.metrics_history: Dict[str, deque] = {}
        self.alerts: List[PerformanceAlert] = []
        
        # 실시간 모니터링 상태
        self.monitoring_active = False
        self.monitoring_thread = None
        
        # 콜백 함수
        self.alert_callbacks: List[Callable[[PerformanceAlert], None]] = []
        
        # 데이터베이스 초기화
        self._init_database()
        
        # 성능 측정 변수
        self.start_time = time.time()
        self.processed_files = 0
        self.total_processing_time = 0.0
        self.error_count = 0
        
        logger.info("AsyncPerformanceMonitor 초기화 완료")
    
    def _default_alert_thresholds(self) -> Dict[str, Dict[str, float]]:
        """기본 알림 임계값 설정"""
        return {
            'cpu_usage': {
                'warning': 80.0,
                'critical': 95.0
            },
            'memory_usage': {
                'warning': 80.0,
                'critical': 95.0
            },
            'processing_time': {
                'warning': 5.0,  # 5초
                'critical': 10.0  # 10초
            },
            'error_rate': {
                'warning': 0.05,  # 5%
                'critical': 0.10  # 10%
            },
            'throughput': {
                'warning': 1.0,  # 1 파일/초
                'critical': 0.5  # 0.5 파일/초
            }
        }
    
    def _init_database(self) -> None:
        """데이터베이스 초기화"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # 성능 지표 테이블
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS performance_metrics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp REAL NOT NULL,
                    metric_type TEXT NOT NULL,
                    value REAL NOT NULL,
                    unit TEXT NOT NULL,
                    file_path TEXT,
                    metadata TEXT,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # 알림 테이블
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS performance_alerts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    alert_id TEXT UNIQUE NOT NULL,
                    timestamp REAL NOT NULL,
                    metric_type TEXT NOT NULL,
                    current_value REAL NOT NULL,
                    threshold REAL NOT NULL,
                    severity TEXT NOT NULL,
                    message TEXT NOT NULL,
                    suggested_action TEXT,
                    resolved BOOLEAN DEFAULT FALSE,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    resolved_at DATETIME
                )
            ''')
            
            # 성능 요약 테이블
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS performance_summary (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date DATE NOT NULL,
                    total_files INTEGER NOT NULL,
                    total_processing_time REAL NOT NULL,
                    average_processing_time REAL NOT NULL,
                    throughput REAL NOT NULL,
                    error_rate REAL NOT NULL,
                    peak_memory_mb REAL NOT NULL,
                    average_cpu_usage REAL NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(date)
                )
            ''')
            
            conn.commit()
            conn.close()
            
            logger.info(f"성능 데이터베이스 초기화 완료: {self.db_path}")
            
        except Exception as e:
            logger.error(f"데이터베이스 초기화 오류: {str(e)}")
    
    def record_metric(self, metric: PerformanceMetric) -> None:
        """성능 지표 기록"""
        try:
            # 히스토리에 추가
            metric_key = f"{metric.metric_type.value}_{metric.file_path or 'global'}"
            if metric_key not in self.metrics_history:
                self.metrics_history[metric_key] = deque(maxlen=self.max_history_size)
            
            self.metrics_history[metric_key].append(metric)
            
            # 데이터베이스에 저장
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO performance_metrics 
                (timestamp, metric_type, value, unit, file_path, metadata)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                metric.timestamp,
                metric.metric_type.value,
                metric.value,
                metric.unit,
                metric.file_path,
                json.dumps(metric.metadata)
            ))
            
            conn.commit()
            conn.close()
            
            # 알림 체크
            self._check_alerts(metric)
            
        except Exception as e:
            logger.error(f"성능 지표 기록 오류: {str(e)}")
    
    def _check_alerts(self, metric: PerformanceMetric) -> None:
        """알림 조건 체크"""
        try:
            if metric.metric_type.value not in self.alert_thresholds:
                return
            
            thresholds = self.alert_thresholds[metric.metric_type.value]
            
            # 경고 임계값 체크
            if metric.value >= thresholds.get('warning', float('inf')):
                severity = 'medium'
                if metric.value >= thresholds.get('critical', float('inf')):
                    severity = 'critical'
                else:
                    severity = 'low'
                
                alert = PerformanceAlert(
                    alert_id=f"{metric.metric_type.value}_{int(metric.timestamp)}",
                    timestamp=metric.timestamp,
                    metric_type=metric.metric_type,
                    current_value=metric.value,
                    threshold=thresholds['warning'],
                    severity=severity,
                    message=f"{metric.metric_type.value} 임계값 초과: {metric.value} {metric.unit}",
                    suggested_action=self._get_suggested_action(metric.metric_type, severity)
                )
                
                self._trigger_alert(alert)
                
        except Exception as e:
            logger.error(f"알림 체크 오류: {str(e)}")
    
    def _get_suggested_action(self, metric_type: MetricType, severity: str) -> str:
        """제안 조치 반환"""
        actions = {
            'cpu_usage': {
                'low': 'CPU 사용량이 증가하고 있습니다. 시스템 리소스를 확인하세요.',
                'medium': 'CPU 사용량이 높습니다. 워커 수를 조정하거나 비효율적인 작업을 최적화하세요.',
                'critical': 'CPU 사용량이 임계치를 초과했습니다. 즉시 워커 수를 줄이고 시스템을 점검하세요.'
            },
            'memory_usage': {
                'low': '메모리 사용량이 증가하고 있습니다. 메모리 누수를 확인하세요.',
                'medium': '메모리 사용량이 높습니다. 메모리 관리를 개선하세요.',
                'critical': '메모리 사용량이 임계치를 초과했습니다. 즉시 메모리를 확보하고 애플리케이션을 재시작하세요.'
            },
            'processing_time': {
                'low': '처리 시간이 증가하고 있습니다. 병목점을 확인하세요.',
                'medium': '처리 시간이 길어지고 있습니다. 알고리즘을 최적화하세요.',
                'critical': '처리 시간이 임계치를 초과했습니다. 시스템을 점검하고 작업을 분할하세요.'
            }
        }
        
        return actions.get(metric_type.value, {}).get(severity, '시스템 관리자에게 문의하세요.')
    
    def _trigger_alert(self, alert: PerformanceAlert) -> None:
        """알림 트리거"""
        try:
            # 알림 목록에 추가
            self.alerts.append(alert)
            
            # 데이터베이스에 저장
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT OR REPLACE INTO performance_alerts 
                (alert_id, timestamp, metric_type, current_value, threshold, severity, message, suggested_action)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                alert.alert_id,
                alert.timestamp,
                alert.metric_type.value,
                alert.current_value,
                alert.threshold,
                alert.severity,
                alert.message,
                alert.suggested_action
            ))
            
            conn.commit()
            conn.close()
            
            # 콜백 실행
            for callback in self.alert_callbacks:
                try:
                    callback(alert)
                except Exception as e:
                    logger.error(f"알림 콜백 오류: {str(e)}")
            
            logger.warning(f"성능 알림: {alert.message}")
            
        except Exception as e:
            logger.error(f"알림 트리거 오류: {str(e)}")
    
    def add_alert_callback(self, callback: Callable[[PerformanceAlert], None]) -> None:
        """알림 콜백 추가"""
        self.alert_callbacks.append(callback)
    
    def record_file_processing(self, 
                             file_path: str, 
                             processing_time: float,
                             memory_usage: float,
                             success: bool = True) -> None:
        """파일 처리 성능 기록"""
        try:
            # 처리 시간 지표
            self.record_metric(PerformanceMetric(
                timestamp=time.time(),
                metric_type=MetricType.LATENCY,
                value=processing_time,
                unit="seconds",
                file_path=file_path,
                metadata={'success': success}
            ))
            
            # 메모리 사용량 지표
            self.record_metric(PerformanceMetric(
                timestamp=time.time(),
                metric_type=MetricType.MEMORY,
                value=memory_usage,
                unit="MB",
                file_path=file_path
            ))
            
            # 통계 업데이트
            self.processed_files += 1
            self.total_processing_time += processing_time
            if not success:
                self.error_count += 1
            
        except Exception as e:
            logger.error(f"파일 처리 성능 기록 오류: {str(e)}")
    
    def record_system_metrics(self) -> None:
        """시스템 메트릭 기록"""
        try:
            # CPU 사용량
            cpu_usage = psutil.cpu_percent(interval=1)
            self.record_metric(PerformanceMetric(
                timestamp=time.time(),
                metric_type=MetricType.CPU,
                value=cpu_usage,
                unit="percent"
            ))
            
            # 메모리 사용량
            memory = psutil.virtual_memory()
            self.record_metric(PerformanceMetric(
                timestamp=time.time(),
                metric_type=MetricType.MEMORY,
                value=memory.percent,
                unit="percent"
            ))
            
            # 디스크 I/O
            disk_io = psutil.disk_io_counters()
            if disk_io:
                self.record_metric(PerformanceMetric(
                    timestamp=time.time(),
                    metric_type=MetricType.DISK_IO,
                    value=disk_io.read_bytes + disk_io.write_bytes,
                    unit="bytes"
                ))
            
        except Exception as e:
            logger.error(f"시스템 메트릭 기록 오류: {str(e)}")
    
    def get_performance_summary(self, 
                               hours: int = 24) -> Dict[str, Any]:
        """성능 요약 정보 반환"""
        try:
            end_time = time.time()
            start_time = end_time - (hours * 3600)
            
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # 기본 통계
            cursor.execute('''
                SELECT 
                    COUNT(*) as total_files,
                    AVG(value) as avg_processing_time,
                    MAX(value) as max_processing_time,
                    MIN(value) as min_processing_time
                FROM performance_metrics 
                WHERE metric_type = 'latency' AND timestamp >= ? AND timestamp <= ?
            ''', (start_time, end_time))
            
            stats = cursor.fetchone()
            total_files, avg_time, max_time, min_time = stats
            
            # 처리량 계산
            time_span = end_time - start_time
            throughput = total_files / max(time_span, 0.001)
            
            # 오류율 계산
            cursor.execute('''
                SELECT COUNT(*) as error_count
                FROM performance_metrics 
                WHERE metric_type = 'latency' AND metadata LIKE '%\"success\": false%' 
                AND timestamp >= ? AND timestamp <= ?
            ''', (start_time, end_time))
            
            error_count = cursor.fetchone()[0]
            error_rate = error_count / max(total_files, 1)
            
            # 메모리 사용량
            cursor.execute('''
                SELECT AVG(value) as avg_memory, MAX(value) as max_memory
                FROM performance_metrics 
                WHERE metric_type = 'memory' AND timestamp >= ? AND timestamp <= ?
            ''', (start_time, end_time))
            
            memory_stats = cursor.fetchone()
            avg_memory, max_memory = memory_stats
            
            # CPU 사용량
            cursor.execute('''
                SELECT AVG(value) as avg_cpu, MAX(value) as max_cpu
                FROM performance_metrics 
                WHERE metric_type = 'cpu' AND timestamp >= ? AND timestamp <= ?
            ''', (start_time, end_time))
            
            cpu_stats = cursor.fetchone()
            avg_cpu, max_cpu = cpu_stats
            
            conn.close()
            
            return {
                'period_hours': hours,
                'total_files': total_files,
                'average_processing_time': avg_time or 0,
                'max_processing_time': max_time or 0,
                'min_processing_time': min_time or 0,
                'throughput': throughput,
                'error_rate': error_rate,
                'average_memory_usage': avg_memory or 0,
                'peak_memory_usage': max_memory or 0,
                'average_cpu_usage': avg_cpu or 0,
                'peak_cpu_usage': max_cpu or 0,
                'start_time': start_time,
                'end_time': end_time
            }
            
        except Exception as e:
            logger.error(f"성능 요약 조회 오류: {str(e)}")
            return {}
    
    def get_active_alerts(self) -> List[Dict[str, Any]]:
        """활성 알림 목록 반환"""
        try:
            return [alert.to_dict() for alert in self.alerts if not alert.resolved]
        except Exception as e:
            logger.error(f"활성 알림 조회 오류: {str(e)}")
            return []
    
    def resolve_alert(self, alert_id: str) -> bool:
        """알림 해결"""
        try:
            for alert in self.alerts:
                if alert.alert_id == alert_id:
                    alert.resolved = True
                    return True
            return False
        except Exception as e:
            logger.error(f"알림 해결 오류: {str(e)}")
            return False
    
    def start_monitoring(self, interval: int = 60) -> None:
        """실시간 모니터링 시작"""
        if self.monitoring_active:
            logger.warning("모니터링이 이미 활성화되어 있습니다")
            return
        
        self.monitoring_active = True
        self.monitoring_thread = threading.Thread(target=self._monitoring_loop, args=(interval,))
        self.monitoring_thread.daemon = True
        self.monitoring_thread.start()
        
        logger.info(f"실시간 모니터링 시작 (간격: {interval}초)")
    
    def _monitoring_loop(self, interval: int) -> None:
        """모니터링 루프"""
        while self.monitoring_active:
            try:
                self.record_system_metrics()
                time.sleep(interval)
            except Exception as e:
                logger.error(f"모니터링 루프 오류: {str(e)}")
                time.sleep(interval)
    
    def stop_monitoring(self) -> None:
        """실시간 모니터링 중지"""
        self.monitoring_active = False
        if self.monitoring_thread:
            self.monitoring_thread.join(timeout=5)
        
        logger.info("실시간 모니터링 중지")
    
    def generate_performance_report(self, 
                                  output_path: Optional[str] = None,
                                  hours: int = 24) -> str:
        """성능 보고서 생성"""
        try:
            summary = self.get_performance_summary(hours)
            alerts = self.get_active_alerts()
            
            # 보고서 생성
            report = f"""
WinForms_Docs 성능 보고서
==========================

생성 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
분석 기간: 최근 {hours}시간

기본 통계:
- 총 처리 파일 수: {summary.get('total_files', 0):,}
- 평균 처리 시간: {summary.get('average_processing_time', 0):.3f}초
- 최대 처리 시간: {summary.get('max_processing_time', 0):.3f}초
- 최소 처리 시간: {summary.get('min_processing_time', 0):.3f}초
- 처리량: {summary.get('throughput', 0):.2f} 파일/초
- 오류율: {summary.get('error_rate', 0):.2%}

리소스 사용량:
- 평균 메모리 사용량: {summary.get('average_memory_usage', 0):.2f}MB
- 최대 메모리 사용량: {summary.get('peak_memory_usage', 0):.2f}MB
- 평균 CPU 사용량: {summary.get('average_cpu_usage', 0):.1f}%
- 최대 CPU 사용량: {summary.get('peak_cpu_usage', 0):.1f}%

활성 알림: {len(alerts)}개
"""
            
            # 알림 상세 정보
            if alerts:
                report += "\n알림 상세:\n"
                for alert in alerts:
                    report += f"- {alert['message']} (심각도: {alert['severity']})\n"
            
            # 최적화 제안
            report += "\n최적화 제안:\n"
            if summary.get('throughput', 0) < 1.0:
                report += "- 처리량이 낮습니다. 워커 수를 늘리거나 I/O 작업을 최적화하세요.\n"
            if summary.get('error_rate', 0) > 0.05:
                report += "- 오류율이 높습니다. 오류 처리 로직을 개선하세요.\n"
            if summary.get('average_cpu_usage', 0) > 80:
                report += "- CPU 사용량이 높습니다. 워커 수를 조정하세요.\n"
            if summary.get('average_memory_usage', 0) > 1000:
                report += "- 메모리 사용량이 높습니다. 메모리 누수를 확인하세요.\n"
            
            # 파일 저장
            if output_path:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(report)
                logger.info(f"성능 보고서 저장 완료: {output_path}")
            
            return report
            
        except Exception as e:
            logger.error(f"성능 보고서 생성 오류: {str(e)}")
            return f"보고서 생성 오류: {str(e)}"
    
    def cleanup(self) -> None:
        """자원 정리"""
        try:
            self.stop_monitoring()
            
            # 데이터베이스 정리 (오래된 데이터 삭제)
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # 30일 이상된 데이터 삭제
            cutoff_date = datetime.now() - timedelta(days=30)
            cursor.execute('''
                DELETE FROM performance_metrics 
                WHERE created_at < ?
            ''', (cutoff_date,))
            
            cursor.execute('''
                DELETE FROM performance_alerts 
                WHERE created_at < ? AND resolved = TRUE
            ''', (cutoff_date,))
            
            conn.commit()
            conn.close()
            
            logger.info("성능 모니터링 자원 정리 완료")
            
        except Exception as e:
            logger.error(f"자원 정리 오류: {str(e)}")

# 유틸리티 함수
def create_async_performance_monitor(db_path: Optional[str] = None) -> AsyncPerformanceMonitor:
    """AsyncPerformanceMonitor 인스턴스 생성"""
    return AsyncPerformanceMonitor(db_path=db_path)

# 테스트 함수
def test_async_performance_monitor():
    """AsyncPerformanceMonitor 테스트"""
    monitor = create_async_performance_monitor()
    
    try:
        # 실시간 모니터링 시작
        monitor.start_monitoring(interval=5)
        
        # 가짜 파일 처리 성능 기록
        for i in range(10):
            time.sleep(1)
            monitor.record_file_processing(
                file_path=f"test_file_{i}.md",
                processing_time=0.1 + (i * 0.05),
                memory_usage=100 + (i * 10),
                success=True
            )
        
        # 성능 요약 조회
        summary = monitor.get_performance_summary(hours=1)
        print("성능 요약:")
        print(f"총 처리 파일: {summary.get('total_files', 0)}")
        print(f"평균 처리 시간: {summary.get('average_processing_time', 0):.3f}초")
        print(f"처리량: {summary.get('throughput', 0):.2f} 파일/초")
        
        # 성능 보고서 생성
        report = monitor.generate_performance_report()
        print("\n성능 보고서:")
        print(report)
        
    finally:
        # 모니터링 중지
        monitor.stop_monitoring()
        monitor.cleanup()

if __name__ == "__main__":
    test_async_performance_monitor()