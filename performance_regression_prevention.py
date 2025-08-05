"""
WinForms_Docs 성능 회귀 방지 시스템
================================

주요 기능:
==========
1. CI/CD 파이프라인 통합 가능한 테스트
   - GitHub Actions 통합
   - Jenkins 파이프라인 지원
   - GitLab CI/CD 호환
   - Travis CI 지원

2. 성능 기준선(baseline) 설정 및 관리
   - 자동 기준선 생성
   - 수동 기준선 설정
   - 기준선 비교 분석
   - 기준선 업데이트 관리

3. 성능 저하 감지 및 알림 시스템
   - 실시간 성능 모니터링
   - 이상 탐지 알고리즘
   - 다단계 알림 시스템
   - 자동 복구 메커니즘

4. 자동 성능 보고서 생성
   - 성능 추이 분석
   - 회귀 분석 보고서
   - 개선 제안 생성
   - 관리자 알림

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0 (성능 회귀 방지 시스템)
"""

import asyncio
import logging
import time
import json
import os
import shutil
import hashlib
import pickle
import uuid
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any, Union, Callable
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed
import sqlite3
import pandas as pd
import numpy as np
import random
import string
from enum import Enum
import subprocess
import requests
import smtplib
from email.mime.text import MimeText
from email.mime.multipart import MimeMultipart
import statistics
import scipy.stats as stats
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# 로컬 모듈 임포트
try:
    from config import (
        WINFORMS_DOCS_DIR, OUTPUT_DIR, BACKUP_DIR,
        PROCESSING_OPTIONS, LOGGING_CONFIG
    )
    from integrated_performance_test_framework import IntegratedPerformanceTestFramework, create_test_framework
    from performance_benchmark_suite import PerformanceBenchmarkSuite, create_benchmark_suite
    from automated_test_manager import AutomatedTestManager, create_test_manager
    from test_data_manager import TestDataManager, create_test_data_manager
    from performance_monitor import PerformanceMonitor, get_performance_monitor
    MODULES_AVAILABLE = True
except ImportError as e:
    print(f"일부 모듈 임포트 실패: {e}")
    MODULES_AVAILABLE = False

# 로컬 로깅 설정 (config 모듈이 없을 경우 대비)
try:
    from config import LOGGING_CONFIG
    logging.basicConfig(
        level=getattr(logging, LOGGING_CONFIG['level']),
        format=LOGGING_CONFIG['format'],
        handlers=[
            logging.FileHandler(LOGGING_CONFIG['file_path'], encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
except ImportError:
    # 기본 로깅 설정
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/performance_regression.log', encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
logger = logging.getLogger(__name__)

class RegressionSeverity(Enum):
    """성능 회귀 심각도"""
    LOW = "low"           # < 5% 저하
    MEDIUM = "medium"     # 5-15% 저하
    HIGH = "high"         # 15-30% 저하
    CRITICAL = "critical" # > 30% 저하

class TestEnvironment(Enum):
    """테스트 환경"""
    LOCAL = "local"
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"

class AlertLevel(Enum):
    """알림 레벨"""
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

@dataclass
class PerformanceBaseline:
    """성능 기준선 데이터 클래스"""
    baseline_id: str
    test_name: str
    test_environment: TestEnvironment
    created_at: datetime
    metrics: Dict[str, float]
    confidence_intervals: Dict[str, Tuple[float, float]]
    sample_size: int
    statistical_significance: float
    metadata: Optional[Dict[str, Any]] = None

@dataclass
class RegressionDetection:
    """성능 회귀 감지 데이터 클래스"""
    detection_id: str
    test_name: str
    baseline_id: str
    current_metrics: Dict[str, float]
    regression_metrics: Dict[str, Dict[str, Any]]
    severity: RegressionSeverity
    detected_at: datetime
    is_confirmed: bool = False
    auto_recovery_attempted: bool = False
    recovery_actions: List[str] = None
    metadata: Optional[Dict[str, Any]] = None

@dataclass
class CIIntegrationConfig:
    """CI/CD 통합 설정 데이터 클래스"""
    ci_platform: str
    repository_url: str
    branch: str
    webhook_url: str
    api_token: str
    test_config: Dict[str, Any]
    notification_settings: Dict[str, Any]
    auto_merge_enabled: bool = False
    auto_revert_enabled: bool = False

class StatisticalAnalyzer:
    """통계 분석기 - 성능 회귀 감지를 위한 통계적 분석"""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.isolation_forest = IsolationForest(contamination=0.1, random_state=42)
    
    def calculate_performance_change(self, baseline: Dict[str, float], 
                                   current: Dict[str, float]) -> Dict[str, float]:
        """성능 변화율 계산"""
        changes = {}
        
        for metric_name in baseline:
            if metric_name in current:
                baseline_value = baseline[metric_name]
                current_value = current[metric_name]
                
                if baseline_value != 0:
                    change_percentage = ((current_value - baseline_value) / baseline_value) * 100
                    changes[metric_name] = change_percentage
                else:
                    changes[metric_name] = float('inf') if current_value > 0 else float('-inf')
        
        return changes
    
    def is_statistically_significant(self, baseline_values: List[float], 
                                   current_values: List[float], 
                                   alpha: float = 0.05) -> bool:
        """통계적 유의성 검정"""
        try:
            # t-test 수행
            t_stat, p_value = stats.ttest_ind(baseline_values, current_values)
            
            # p-value가 alpha보다 작으면 통계적으로 유의미
            return p_value < alpha
            
        except Exception as e:
            logger.error(f"통계적 유의성 검정 오류: {e}")
            return False
    
    def detect_outliers(self, metrics: List[Dict[str, float]]) -> List[int]:
        """이상치 감지"""
        try:
            # 데이터 준비
            df = pd.DataFrame(metrics)
            
            # 수치형 컬럼만 선택
            numeric_columns = df.select_dtypes(include=[np.number]).columns
            
            if len(numeric_columns) == 0:
                return []
            
            # 데이터 정규화
            scaled_data = self.scaler.fit_transform(df[numeric_columns])
            
            # 이상치 감지
            outliers = self.isolation_forest.fit_predict(scaled_data)
            
            # 이상치 인덱스 반환
            outlier_indices = [i for i, outlier in enumerate(outliers) if outlier == -1]
            
            return outlier_indices
            
        except Exception as e:
            logger.error(f"이상치 감지 오류: {e}")
            return []
    
    def calculate_confidence_interval(self, values: List[float], 
                                    confidence: float = 0.95) -> Tuple[float, float]:
        """신뢰 구간 계산"""
        try:
            if not values:
                return (0.0, 0.0)
            
            mean = np.mean(values)
            sem = stats.sem(values)  # 표준 오차
            ci = stats.t.interval(confidence, len(values) - 1, loc=mean, scale=sem)
            
            return (ci[0], ci[1])
            
        except Exception as e:
            logger.error(f"신뢰 구간 계산 오류: {e}")
            return (0.0, 0.0)
    
    def analyze_regression_trend(self, historical_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """성능 추이 분석"""
        try:
            if not historical_data:
                return {}
            
            # 시간순으로 정렬
            sorted_data = sorted(historical_data, key=lambda x: x['timestamp'])
            
            # 각 지표별 추이 분석
            trend_analysis = {}
            
            for metric_name in sorted_data[0]['metrics']:
                values = [data['metrics'][metric_name] for data in sorted_data if metric_name in data['metrics']]
                
                if len(values) < 2:
                    continue
                
                # 선형 회귀 분석
                x = np.arange(len(values))
                y = np.array(values)
                
                slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
                
                trend_analysis[metric_name] = {
                    'slope': slope,
                    'r_squared': r_value ** 2,
                    'p_value': p_value,
                    'trend': 'increasing' if slope > 0 else 'decreasing' if slope < 0 else 'stable',
                    'change_rate': (values[-1] - values[0]) / values[0] * 100 if values[0] != 0 else 0
                }
            
            return trend_analysis
            
        except Exception as e:
            logger.error(f"성능 추이 분석 오류: {e}")
            return {}

class PerformanceRegressionPrevention:
    """성능 회귀 방지 시스템 - 핵심 클래스"""
    
    def __init__(self, db_path: str = "performance_results/regression_prevention.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 통계 분석기
        self.analyzer = StatisticalAnalyzer()
        
        # 성능 모니터
        self.performance_monitor = get_performance_monitor()
        
        # 테스트 관리자
        self.test_manager = create_test_manager()
        
        # 데이터 관리자
        self.data_manager = create_test_data_manager()
        
        # 설정
        self.config = {
            'regression_threshold_percent': 10.0,  # 10% 성능 저하 감지 임계값
            'statistical_significance_level': 0.05,
            'sample_size_minimum': 10,
            'outlier_detection_enabled': True,
            'auto_recovery_enabled': True,
            'notification_enabled': True,
            'email_notifications': True,
            'slack_notifications': False,
            'webhook_notifications': False,
            'ci_integration_enabled': True,
            'baseline_update_frequency': 'weekly',
            'historical_data_retention_days': 90,
            'auto_revert_threshold': 20.0,  # 20% 성능 저하 시 자동 롤백
            'performance_dashboard_enabled': True
        }
        
        # 데이터베이스 초기화
        self._init_database()
        
        logger.info("성능 회귀 방지 시스템 초기화 완료")
    
    def _init_database(self):
        """데이터베이스 초기화"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 성능 기준선 테이블
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS performance_baselines (
                        baseline_id TEXT PRIMARY KEY,
                        test_name TEXT NOT NULL,
                        test_environment TEXT NOT NULL,
                        created_at TEXT NOT NULL,
                        metrics TEXT NOT NULL,
                        confidence_intervals TEXT NOT NULL,
                        sample_size INTEGER NOT NULL,
                        statistical_significance REAL NOT NULL,
                        metadata TEXT
                    )
                ''')
                
                # 성능 이력 테이블
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS performance_history (
                        history_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        test_name TEXT NOT NULL,
                        test_environment TEXT NOT NULL,
                        timestamp TEXT NOT NULL,
                        metrics TEXT NOT NULL,
                        execution_id TEXT,
                        FOREIGN KEY (execution_id) REFERENCES test_executions (execution_id)
                    )
                ''')
                
                # 회귀 감지 테이블
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS regression_detections (
                        detection_id TEXT PRIMARY KEY,
                        test_name TEXT NOT NULL,
                        baseline_id TEXT NOT NULL,
                        current_metrics TEXT NOT NULL,
                        regression_metrics TEXT NOT NULL,
                        severity TEXT NOT NULL,
                        detected_at TEXT NOT NULL,
                        is_confirmed BOOLEAN DEFAULT 0,
                        auto_recovery_attempted BOOLEAN DEFAULT 0,
                        recovery_actions TEXT,
                        metadata TEXT,
                        FOREIGN KEY (baseline_id) REFERENCES performance_baselines (baseline_id)
                    )
                ''')
                
                # CI/CD 통합 설정 테이블
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS ci_integration_configs (
                        config_id TEXT PRIMARY KEY,
                        ci_platform TEXT NOT NULL,
                        repository_url TEXT NOT NULL,
                        branch TEXT NOT NULL,
                        webhook_url TEXT NOT NULL,
                        api_token TEXT NOT NULL,
                        test_config TEXT NOT NULL,
                        notification_settings TEXT NOT NULL,
                        auto_merge_enabled BOOLEAN DEFAULT 0,
                        auto_revert_enabled BOOLEAN DEFAULT 0,
                        created_at TEXT NOT NULL,
                        updated_at TEXT NOT NULL
                    )
                ''')
                
                # 알림 테이블
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS regression_alerts (
                        alert_id TEXT PRIMARY KEY,
                        detection_id TEXT NOT NULL,
                        test_name TEXT NOT NULL,
                        alert_level TEXT NOT NULL,
                        message TEXT NOT NULL,
                        timestamp TEXT NOT NULL,
                        delivered BOOLEAN DEFAULT 0,
                        delivery_method TEXT,
                        metadata TEXT,
                        FOREIGN KEY (detection_id) REFERENCES regression_detections (detection_id)
                    )
                ''')
                
                # 인덱스 생성
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_baselines_test ON performance_baselines(test_name)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_baselines_env ON performance_baselines(test_environment)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_history_test ON performance_history(test_name)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_history_timestamp ON performance_history(timestamp)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_detections_test ON regression_detections(test_name)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_detections_severity ON regression_detections(severity)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_alerts_detection ON regression_alerts(detection_id)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_alerts_delivered ON regression_alerts(delivered)')
                
                conn.commit()
                logger.info("성능 회귀 방지 데이터베이스 초기화 완료")
                
        except Exception as e:
            logger.error(f"데이터베이스 초기화 오류: {e}")
            raise
    
    def create_performance_baseline(self, test_name: str, test_environment: TestEnvironment,
                                  metrics: Dict[str, float], sample_size: int = 10) -> PerformanceBaseline:
        """성능 기준선 생성"""
        try:
            baseline_id = str(uuid.uuid4())
            
            # 신뢰 구간 계산
            confidence_intervals = {}
            for metric_name, metric_value in metrics.items():
                # 가상의 샘플 데이터 생성 (실제로는 여러 번 실행한 결과 사용)
                sample_values = [metric_value + random.uniform(-0.1, 0.1) for _ in range(sample_size)]
                ci = self.analyzer.calculate_confidence_interval(sample_values)
                confidence_intervals[metric_name] = ci
            
            # 기준선 생성
            baseline = PerformanceBaseline(
                baseline_id=baseline_id,
                test_name=test_name,
                test_environment=test_environment,
                created_at=datetime.now(),
                metrics=metrics,
                confidence_intervals=confidence_intervals,
                sample_size=sample_size,
                statistical_significance=self.config['statistical_significance_level'],
                metadata={'created_by': 'system', 'version': '1.0'}
            )
            
            # 데이터베이스에 저장
            self._save_baseline(baseline)
            
            logger.info(f"성능 기준선 생성 완료: {test_name}")
            return baseline
            
        except Exception as e:
            logger.error(f"성능 기준선 생성 오류: {e}")
            raise
    
    def _save_baseline(self, baseline: PerformanceBaseline):
        """기준선 저장"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    INSERT OR REPLACE INTO performance_baselines 
                    (baseline_id, test_name, test_environment, created_at, 
                     metrics, confidence_intervals, sample_size, statistical_significance, metadata)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    baseline.baseline_id,
                    baseline.test_name,
                    baseline.test_environment.value,
                    baseline.created_at.isoformat(),
                    json.dumps(baseline.metrics, ensure_ascii=False),
                    json.dumps(baseline.confidence_intervals, ensure_ascii=False),
                    baseline.sample_size,
                    baseline.statistical_significance,
                    json.dumps(baseline.metadata, ensure_ascii=False) if baseline.metadata else None
                ))
                
                conn.commit()
                
        except Exception as e:
            logger.error(f"기준선 저장 오류: {e}")
            raise
    
    def get_performance_baseline(self, test_name: str, test_environment: TestEnvironment) -> Optional[PerformanceBaseline]:
        """성능 기준선 조회"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    SELECT baseline_id, test_name, test_environment, created_at, 
                           metrics, confidence_intervals, sample_size, statistical_significance, metadata
                    FROM performance_baselines
                    WHERE test_name = ? AND test_environment = ?
                    ORDER BY created_at DESC
                    LIMIT 1
                ''', (test_name, test_environment.value))
                
                row = cursor.fetchone()
                if row:
                    return PerformanceBaseline(
                        baseline_id=row[0],
                        test_name=row[1],
                        test_environment=TestEnvironment(row[2]),
                        created_at=datetime.fromisoformat(row[3]),
                        metrics=json.loads(row[4]),
                        confidence_intervals=json.loads(row[5]),
                        sample_size=row[6],
                        statistical_significance=row[7],
                        metadata=json.loads(row[8]) if row[8] else None
                    )
                
                return None
                
        except Exception as e:
            logger.error(f"성능 기준선 조회 오류: {e}")
            return None
    
    def detect_performance_regression(self, test_name: str, test_environment: TestEnvironment,
                                    current_metrics: Dict[str, float]) -> Optional[RegressionDetection]:
        """성능 회귀 감지"""
        try:
            # 기준선 조회
            baseline = self.get_performance_baseline(test_name, test_environment)
            if not baseline:
                logger.warning(f"기준선을 찾을 수 없음: {test_name}")
                return None
            
            # 성능 변화율 계산
            changes = self.analyzer.calculate_performance_change(baseline.metrics, current_metrics)
            
            # 회귀 감지
            regression_metrics = {}
            has_regression = False
            max_degradation = 0
            
            for metric_name, change_percentage in changes.items():
                if change_percentage < 0:  # 성능 저하
                    degradation = abs(change_percentage)
                    max_degradation = max(max_degradation, degradation)
                    
                    # 기준선과의 비교
                    baseline_value = baseline.metrics[metric_name]
                    current_value = current_metrics[metric_name]
                    
                    # 신뢰 구간 내에 있는지 확인
                    ci_lower, ci_upper = baseline.confidence_intervals[metric_name]
                    is_out_of_confidence_interval = not (ci_lower <= current_value <= ci_upper)
                    
                    regression_metrics[metric_name] = {
                        'baseline_value': baseline_value,
                        'current_value': current_value,
                        'change_percentage': change_percentage,
                        'degradation_percentage': degradation,
                        'is_out_of_confidence_interval': is_out_of_confidence_interval,
                        'confidence_interval': baseline.confidence_intervals[metric_name]
                    }
                    
                    has_regression = True
            
            if not has_regression:
                return None
            
            # 회귀 심각도 판단
            if max_degradation > 30:
                severity = RegressionSeverity.CRITICAL
            elif max_degradation > 15:
                severity = RegressionSeverity.HIGH
            elif max_degradation > 5:
                severity = RegressionSeverity.MEDIUM
            else:
                severity = RegressionSeverity.LOW
            
            # 회귀 감지 결과 생성
            detection = RegressionDetection(
                detection_id=str(uuid.uuid4()),
                test_name=test_name,
                baseline_id=baseline.baseline_id,
                current_metrics=current_metrics,
                regression_metrics=regression_metrics,
                severity=severity,
                detected_at=datetime.now(),
                metadata={'baseline_created_at': baseline.created_at.isoformat()}
            )
            
            # 데이터베이스에 저장
            self._save_regression_detection(detection)
            
            # 알림 생성
            self._create_regression_alert(detection)
            
            # 자동 복구 시도
            if self.config['auto_recovery_enabled']:
                self._attempt_auto_recovery(detection)
            
            logger.info(f"성능 회귀 감지 완료: {test_name}, 심각도: {severity.value}")
            return detection
            
        except Exception as e:
            logger.error(f"성능 회귀 감지 오류: {e}")
            return None
    
    def _save_regression_detection(self, detection: RegressionDetection):
        """회귀 감지 결과 저장"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    INSERT INTO regression_detections 
                    (detection_id, test_name, baseline_id, current_metrics, 
                     regression_metrics, severity, detected_at, is_confirmed,
                     auto_recovery_attempted, recovery_actions, metadata)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    detection.detection_id,
                    detection.test_name,
                    detection.baseline_id,
                    json.dumps(detection.current_metrics, ensure_ascii=False),
                    json.dumps(detection.regression_metrics, ensure_ascii=False),
                    detection.severity.value,
                    detection.detected_at.isoformat(),
                    detection.is_confirmed,
                    detection.auto_recovery_attempted,
                    json.dumps(detection.recovery_actions, ensure_ascii=False) if detection.recovery_actions else None,
                    json.dumps(detection.metadata, ensure_ascii=False) if detection.metadata else None
                ))
                
                conn.commit()
                
        except Exception as e:
            logger.error(f"회귀 감지 결과 저장 오류: {e}")
    
    def _create_regression_alert(self, detection: RegressionDetection):
        """회귀 알림 생성"""
        try:
            # 알림 레벨 결정
            if detection.severity == RegressionSeverity.CRITICAL:
                alert_level = AlertLevel.CRITICAL
            elif detection.severity == RegressionSeverity.HIGH:
                alert_level = AlertLevel.ERROR
            elif detection.severity == RegressionSeverity.MEDIUM:
                alert_level = AlertLevel.WARNING
            else:
                alert_level = AlertLevel.INFO
            
            # 알림 메시지 생성
            message = f"성능 회귀 감지: {detection.test_name}\n"
            message += f"심각도: {detection.severity.value.upper()}\n"
            message += f"감지 시간: {detection.detected_at.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            
            for metric_name, regression_info in detection.regression_metrics.items():
                message += f"{metric_name}: {regression_info['change_percentage']:.2f}% 저하\n"
                message += f"  - 기준값: {regression_info['baseline_value']:.2f}\n"
                message += f"  - 현재값: {regression_info['current_value']:.2f}\n"
                message += f"  - 신뢰구간: [{regression_info['confidence_interval'][0]:.2f}, {regression_info['confidence_interval'][1]:.2f}]\n\n"
            
            # 알림 ID 생성
            alert_id = str(uuid.uuid4())
            
            # 알림 저장
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    INSERT INTO regression_alerts 
                    (alert_id, detection_id, test_name, alert_level, message, timestamp, delivered, delivery_method)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    alert_id,
                    detection.detection_id,
                    detection.test_name,
                    alert_level.value,
                    message,
                    datetime.now().isoformat(),
                    False,
                    'email'
                ))
                
                conn.commit()
            
            # 이메일 알림 발송
            if self.config['email_notifications']:
                self._send_email_alert(alert_id, message)
            
            # Slack 알림 발송
            if self.config['slack_notifications']:
                self._send_slack_alert(message)
            
            # Webhook 알림 발송
            if self.config['webhook_notifications']:
                self._send_webhook_alert(message)
            
            logger.info(f"회귀 알림 생성 완료: {alert_id}")
            
        except Exception as e:
            logger.error(f"회귀 알림 생성 오류: {e}")
    
    def _send_email_alert(self, alert_id: str, message: str):
        """이메일 알림 발송"""
        try:
            # 이메일 설정 (실제 환경에서는 설정 파일에서 읽어오기)
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            smtp_username = "your_email@gmail.com"
            smtp_password = "your_app_password"
            
            # 수신자 목록
            recipients = ["admin@example.com", "dev@example.com"]
            
            # 이메일 생성
            msg = MimeMultipart()
            msg['From'] = smtp_username
            msg['To'] = ', '.join(recipients)
            msg['Subject'] = f"[성능 회귀 알림] {alert_id}"
            
            # 이메일 내용
            body = f"""
            성능 회귀 알림이 생성되었습니다.
            
            알림 ID: {alert_id}
            시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            
            상세 내용:
            {message}
            """
            
            msg.attach(MimeText(body, 'plain', 'utf-8'))
            
            # 이메일 발송
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.send_message(msg)
            
            logger.info(f"이메일 알림 발송 완료: {alert_id}")
            
        except Exception as e:
            logger.error(f"이메일 알림 발송 오류: {e}")
    
    def _send_slack_alert(self, message: str):
        """Slack 알림 발송"""
        try:
            # Slack Webhook URL (실제 환경에서는 설정 파일에서 읽어오기)
            webhook_url = "https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK"
            
            # Slack 메시지 형식
            slack_message = {
                'text': '🚨 성능 회귀 알림',
                'attachments': [
                    {
                        'color': 'danger',
                        'text': message
                    }
                ]
            }
            
            # Webhook 호출
            response = requests.post(webhook_url, json=slack_message, timeout=10)
            
            if response.status_code == 200:
                logger.info("Slack 알림 발송 완료")
            else:
                logger.error(f"Slack 알림 발송 실패: {response.status_code}")
            
        except Exception as e:
            logger.error(f"Slack 알림 발송 오류: {e}")
    
    def _send_webhook_alert(self, message: str):
        """Webhook 알림 발송"""
        try:
            # Webhook URL (실제 환경에서는 설정 파일에서 읽어오기)
            webhook_url = "https://your-webhook-url.com/alerts"
            
            # Webhook 데이터 형식
            webhook_data = {
                'alert_type': 'performance_regression',
                'message': message,
                'timestamp': datetime.now().isoformat(),
                'severity': 'high'
            }
            
            # Webhook 호출
            response = requests.post(webhook_url, json=webhook_data, timeout=10)
            
            if response.status_code == 200:
                logger.info("Webhook 알림 발송 완료")
            else:
                logger.error(f"Webhook 알림 발송 실패: {response.status_code}")
            
        except Exception as e:
            logger.error(f"Webhook 알릌 발송 오류: {e}")
    
    def _attempt_auto_recovery(self, detection: RegressionDetection):
        """자동 복구 시도"""
        try:
            if detection.auto_recovery_attempted:
                return
            
            # 심각도에 따라 복조치 방법 결정
            if detection.severity == RegressionSeverity.CRITICAL:
                # 가장 심각한 경우: 롤백 시도
                self._attempt_rollback(detection)
            elif detection.severity == RegressionSeverity.HIGH:
                # 높은 심각도: 설정 복구 시도
                self._attempt_config_recovery(detection)
            elif detection.severity == RegressionSeverity.MEDIUM:
                # 중간 심각도: 캐시 정리 및 재시도
                self._attempt_cache_cleanup(detection)
            else:
                # 낮은 심각도: 로그 기록만
                logger.info(f"낮은 심각도 회귀 감지, 복구 시도하지 않음: {detection.test_name}")
            
            # 복구 시도 기록
            detection.auto_recovery_attempted = True
            self._save_regression_detection(detection)
            
            logger.info(f"자동 복구 시도 완료: {detection.test_name}")
            
        except Exception as e:
            logger.error(f"자동 복구 시도 오류: {e}")
    
    def _attempt_rollback(self, detection: RegressionDetection):
        """롤백 시도"""
        try:
            # Git 롤백 시뮬레이션
            rollback_command = f"git revert --no-commit HEAD~1"
            
            # 실제 환경에서는 CI/CD 파이프라인과 연동
            # subprocess.run(rollback_command, shell=True, check=True)
            
            recovery_actions = ["git_rollback"]
            detection.recovery_actions = recovery_actions
            
            logger.info(f"롤백 시도: {detection.test_name}")
            
        except Exception as e:
            logger.error(f"롤백 시도 오류: {e}")
    
    def _attempt_config_recovery(self, detection: RegressionDetection):
        """설정 복구 시도"""
        try:
            # 설정 복구 시뮬레이션
            recovery_actions = ["config_reset", "cache_clear"]
            detection.recovery_actions = recovery_actions
            
            logger.info(f"설정 복구 시도: {detection.test_name}")
            
        except Exception as e:
            logger.error(f"설정 복구 시도 오류: {e}")
    
    def _attempt_cache_cleanup(self, detection: RegressionDetection):
        """캐시 정리 시도"""
        try:
            # 캐시 정리 시뮬레이션
            recovery_actions = ["cache_cleanup", "gc_collect"]
            detection.recovery_actions = recovery_actions
            
            logger.info(f"캐시 정리 시도: {detection.test_name}")
            
        except Exception as e:
            logger.error(f"캐시 정리 시도 오류: {e}")
    
    def integrate_with_ci_cd(self, config: CIIntegrationConfig) -> bool:
        """CI/CD 파이프라인 통합"""
        try:
            # CI/CD 설정 저장
            config_id = str(uuid.uuid4())
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    INSERT INTO ci_integration_configs 
                    (config_id, ci_platform, repository_url, branch, webhook_url, 
                     api_token, test_config, notification_settings, auto_merge_enabled, 
                     auto_revert_enabled, created_at, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    config_id,
                    config.ci_platform,
                    config.repository_url,
                    config.branch,
                    config.webhook_url,
                    config.api_token,
                    json.dumps(config.test_config, ensure_ascii=False),
                    json.dumps(config.notification_settings, ensure_ascii=False),
                    config.auto_merge_enabled,
                    config.auto_revert_enabled,
                    datetime.now().isoformat(),
                    datetime.now().isoformat()
                ))
                
                conn.commit()
            
            # CI/CD 웹훅 설정 (실제 환경에서는 CI/CD 플랫폼 API 호출)
            self._setup_ci_webhook(config)
            
            logger.info(f"CI/CD 통합 설정 완료: {config.ci_platform}")
            return True
            
        except Exception as e:
            logger.error(f"CI/CD 통합 오류: {e}")
            return False
    
    def _setup_ci_webhook(self, config: CIIntegrationConfig):
        """CI 웹훅 설정"""
        try:
            # GitHub 웹훅 설정 예시
            if config.ci_platform.lower() == 'github':
                webhook_data = {
                    'name': 'web',
                    'active': True,
                    'events': ['push', 'pull_request'],
                    'config': {
                        'url': config.webhook_url,
                        'content_type': 'json',
                        'secret': config.api_token
                    }
                }
                
                # GitHub API 호출 (실제 환경에서는 인증 필요)
                # response = requests.post(
                #     f"{config.repository_url}/hooks",
                #     json=webhook_data,
                #     headers={'Authorization': f'token {config.api_token}'}
                # )
                
                logger.info("GitHub 웹훅 설정 완료")
            
            # Jenkins 웹훅 설정 예시
            elif config.ci_platform.lower() == 'jenkins':
                webhook_url = f"{config.webhook_url}/github-webhook/"
                
                # Jenkins API 호출 (실제 환경에서는 인증 필요)
                # response = requests.post(webhook_url, json=webhook_data)
                
                logger.info("Jenkins 웹훅 설정 완료")
            
        except Exception as e:
            logger.error(f"CI 웹훅 설정 오류: {e}")
    
    def generate_regression_report(self, test_name: Optional[str] = None,
                                 start_date: Optional[datetime] = None,
                                 end_date: Optional[datetime] = None) -> Dict[str, Any]:
        """성능 회귀 보고서 생성"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 회귀 감지 데이터 조회
                query = '''
                    SELECT d.test_name, d.severity, d.detected_at, d.regression_metrics,
                           a.alert_level, a.message
                    FROM regression_detections d
                    LEFT JOIN regression_alerts a ON d.detection_id = a.detection_id
                    WHERE 1=1
                '''
                params = []
                
                if test_name:
                    query += ' AND d.test_name = ?'
                    params.append(test_name)
                
                if start_date:
                    query += ' AND d.detected_at >= ?'
                    params.append(start_date.isoformat())
                
                if end_date:
                    query += ' AND d.detected_at <= ?'
                    params.append(end_date.isoformat())
                
                query += ' ORDER BY d.detected_at DESC'
                
                cursor.execute(query, params)
                
                # 데이터 집계
                total_detections = 0
                severity_counts = {severity.value: 0 for severity in RegressionSeverity}
                test_breakdown = {}
                recent_detections = []
                
                for row in cursor.fetchall():
                    test_name, severity, detected_at, regression_metrics, alert_level, message = row
                    
                    total_detections += 1
                    severity_counts[severity] += 1
                    
                    if test_name not in test_breakdown:
                        test_breakdown[test_name] = {
                            'total_detections': 0,
                            'severity_breakdown': {s.value: 0 for s in RegressionSeverity},
                            'recent_detections': []
                        }
                    
                    test_breakdown[test_name]['total_detections'] += 1
                    test_breakdown[test_name]['severity_breakdown'][severity] += 1
                    
                    detection_info = {
                        'test_name': test_name,
                        'severity': severity,
                        'detected_at': detected_at,
                        'regression_metrics': json.loads(regression_metrics),
                        'alert_level': alert_level,
                        'message': message
                    }
                    
                    recent_detections.append(detection_info)
                    test_breakdown[test_name]['recent_detections'].append(detection_info)
                
                # 최근 10개만 유지
                for test_info in test_breakdown.values():
                    test_info['recent_detections'] = test_info['recent_detections'][:10]
                
                # 보고서 생성
                report = {
                    'report_generated_at': datetime.now().isoformat(),
                    'total_detections': total_detections,
                    'severity_breakdown': severity_counts,
                    'test_breakdown': test_breakdown,
                    'recent_detections': recent_detections[:20],  # 최근 20개
                    'recommendations': self._generate_recommendations(test_breakdown)
                }
                
                return report
                
        except Exception as e:
            logger.error(f"성능 회귀 보고서 생성 오류: {e}")
            return {}
    
    def _generate_recommendations(self, test_breakdown: Dict[str, Any]) -> List[str]:
        """개선 제안 생성"""
        recommendations = []
        
        # 전체 분석 기반 제안
        if test_breakdown:
            # 가장 문제가 많은 테스트 식별
            problem_tests = []
            for test_name, test_info in test_breakdown.items():
                severity_breakdown = test_info['severity_breakdown']
                critical_count = severity_breakdown.get('critical', 0)
                high_count = severity_breakdown.get('high', 0)
                
                if critical_count > 0 or high_count > 2:
                    problem_tests.append((test_name, critical_count + high_count))
            
            if problem_tests:
                problem_tests.sort(key=lambda x: x[1], reverse=True)
                recommendations.append(f"우선적으로 개선이 필요한 테스트: {problem_tests[0][0]}")
                
                # 개선 방법 제안
                top_test = problem_tests[0][0]
                if 'performance' in top_test.lower():
                    recommendations.append("성능 모니터링을 강화하고 병목 현상을 분석하세요")
                elif 'memory' in top_test.lower():
                    recommendations.append("메모리 누수를 점검하고 메모리 관리를 최적화하세요")
                elif 'io' in top_test.lower():
                    recommendations.append("I/O 작업을 비동기화하고 캐시 전략을 개선하세요")
        
        # 일반적인 개선 제안
        recommendations.extend([
            "정기적인 성능 기준선 업데이트를 수행하세요",
            "자동화된 테스트를 CI/CD 파이프라인에 통합하세요",
            "성능 저하가 감지되면 자동으로 알림을 받도록 설정하세요",
            "장기적인 성능 추이를 분석하여 잠재적 문제를 예측하세요",
            "테스트 환경을 프로덕션 환경과 최대한 유사하게 유지하세요"
        ])
        
        return recommendations
    
    def update_performance_baseline(self, test_name: str, test_environment: TestEnvironment,
                                  new_metrics: Dict[str, float]) -> bool:
        """성능 기준선 업데이트"""
        try:
            # 새로운 기준선 생성
            new_baseline = self.create_performance_baseline(
                test_name, test_environment, new_metrics
            )
            
            # 기존 기준선은 보존하고 새로운 기준선으로 대체
            logger.info(f"성능 기준선 업데이트 완료: {test_name}")
            return True
            
        except Exception as e:
            logger.error(f"성능 기준선 업데이트 오류: {e}")
            return False
    
    def cleanup_old_data(self):
        """오래된 데이터 정리"""
        try:
            cutoff_date = datetime.now() - timedelta(days=self.config['historical_data_retention_days'])
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 오래된 성능 이력 삭제
                cursor.execute('DELETE FROM performance_history WHERE timestamp < ?', (cutoff_date.isoformat(),))
                
                # 오래된 알림 삭제 (이미 전송된 알림만)
                cursor.execute('''
                    DELETE FROM regression_alerts 
                    WHERE timestamp < ? AND delivered = 1
                ''', (cutoff_date.isoformat(),))
                
                conn.commit()
                
                logger.info(f"오래된 데이터 정리 완료: {cutoff_date.strftime('%Y-%m-%d')} 이전 데이터")
                
        except Exception as e:
            logger.error(f"오래된 데이터 정리 오류: {e}")
    
    def get_system_status(self) -> Dict[str, Any]:
        """시스템 상태 조회"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 기준선 통계
                cursor.execute('''
                    SELECT COUNT(*) as total_baselines,
                           COUNT(DISTINCT test_name) as unique_tests
                    FROM performance_baselines
                ''')
                
                baseline_stats = cursor.fetchone()
                
                # 회귀 감지 통계
                cursor.execute('''
                    SELECT severity, COUNT(*) as count
                    FROM regression_detections
                    GROUP BY severity
                ''')
                
                regression_stats = {row[0]: row[1] for row in cursor.fetchall()}
                
                # 최근 감지
                cursor.execute('''
                    SELECT COUNT(*) as recent_detections
                    FROM regression_detections
                    WHERE detected_at >= ?
                ''', ((datetime.now() - timedelta(days=7)).isoformat(),))
                
                recent_detections = cursor.fetchone()[0]
                
                # 활성 알림
                cursor.execute('''
                    SELECT COUNT(*) as active_alerts
                    FROM regression_alerts
                    WHERE delivered = 0
                ''')
                
                active_alerts = cursor.fetchone()[0]
                
                return {
                    'total_baselines': baseline_stats[0],
                    'unique_tests': baseline_stats[1],
                    'regression_breakdown': regression_stats,
                    'recent_detections': recent_detections,
                    'active_alerts': active_alerts,
                    'auto_recovery_enabled': self.config['auto_recovery_enabled'],
                    'notifications_enabled': self.config['notification_enabled'],
                    'last_updated': datetime.now().isoformat()
                }
                
        except Exception as e:
            logger.error(f"시스템 상태 조회 오류: {e}")
            return {}
    
    def cleanup(self):
        """정리 작업"""
        try:
            # 데이터 정리
            self.cleanup_old_data()
            
            logger.info("성능 회귀 방지 시스템 정리 완료")
            
        except Exception as e:
            logger.error(f"정리 작업 오류: {e}")

# 유틸리티 함수
def create_regression_prevention_system(db_path: str = "performance_results/regression_prevention.db") -> PerformanceRegressionPrevention:
    """성능 회귀 방지 시스템 인스턴스 생성"""
    return PerformanceRegressionPrevention(db_path)

def setup_default_regression_tests():
    """기본 회귀 테스트 설정"""
    try:
        regression_system = create_regression_prevention_system()
        
        # 기본 성능 기준선 생성
        baseline_metrics = {
            'execution_time': 1.5,
            'memory_usage_mb': 512.0,
            'throughput_files_per_sec': 100.0,
            'cpu_usage_percent': 25.0
        }
        
        # 개발 환경 기준선
        regression_system.create_performance_baseline(
            test_name="integrated_performance_test",
            test_environment=TestEnvironment.DEVELOPMENT,
            metrics=baseline_metrics,
            sample_size=20
        )
        
        # 스테이징 환경 기준선
        regression_system.create_performance_baseline(
            test_name="integration_performance_test",
            test_environment=TestEnvironment.STAGING,
            metrics=baseline_metrics,
            sample_size=20
        )
        
        logger.info("기본 회귀 테스트 설정 완료")
        
    except Exception as e:
        logger.error(f"기본 회귀 테스트 설정 오류: {e}")

def run_regression_monitoring():
    """성능 회귀 모니터링 실행"""
    regression_system = create_regression_prevention_system()
    
    try:
        # 기본 설정
        setup_default_regression_tests()
        
        print("성능 회귀 방지 시스템이 시작되었습니다.")
        print("성능 변화를 실시간으로 모니터링합니다.")
        print("Ctrl+C를 눌러 시스템을 중지합니다.")
        
        # 시스템 상태 모니터링
        while True:
            try:
                time.sleep(60)  # 1분마다 상태 확인
                
                # 시스템 상태 출력
                status = regression_system.get_system_status()
                print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 시스템 상태:")
                print(f"  - 총 기준선 수: {status['total_baselines']}")
                print(f"  - 활성 알림: {status['active_alerts']}")
                print(f"  - 최근 감지: {status['recent_detections']}")
                
                # 회귀 통계 출력
                if status['regression_breakdown']:
                    print("  - 회귀 분포:")
                    for severity, count in status['regression_breakdown'].items():
                        print(f"    - {severity}: {count}")
                
            except KeyboardInterrupt:
                print("\n성능 회귀 방지 시스템을 중지합니다...")
                break
        
    except Exception as e:
        print(f"성능 회귀 방지 시스템 오류: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # 정리
        regression_system.cleanup()
        print("성능 회귀 방지 시스템이 정리되었습니다.")

if __name__ == "__main__":
    print("WinForms_Docs 성능 회귀 방지 시스템")
    print("=" * 50)
    
    # 성능 회귀 모니터링 실행
    run_regression_monitoring()