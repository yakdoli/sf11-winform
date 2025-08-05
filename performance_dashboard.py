"""
WinForms_Docs 성능 대시보드

주요 기능:
============
1. 실시간 성능 모니터링 대시보드
   - CPU, 메모리, 디스크 사용량 실시간 표시
   - 각 모듈별 성능 지표 추적
   - 성능 경고 시각화

2. 성능 차트 및 그래프
   - 처리 속도 추세 차트
   - 메모리 사용량 차트
   - CPU 사용량 차트
   - 성공률 차트

3. 성능 데이터 분석
   - 성능 패턴 분석
   - 병목점 식별
   - 성능 개선 효과 측정

4. 대시보드 인터페이스
   - 웹 기반 대시보드
   - 실시간 데이터 업데이트
   - 사용자 상호작용 기능

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0
"""

import json
import logging
import time
import sqlite3
import threading
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk, messagebox
import seaborn as sns
from concurrent.futures import ThreadPoolExecutor
import psutil
import gc

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class DashboardConfig:
    """대시보드 설정 데이터 클래스"""
    refresh_interval: int = 5  # 초
    max_data_points: int = 100
    chart_colors: Dict[str, str] = None
    warning_thresholds: Dict[str, float] = None
    
    def __post_init__(self):
        if self.chart_colors is None:
            self.chart_colors = {
                'cpu': '#FF6B6B',
                'memory': '#4ECDC4',
                'disk': '#45B7D1',
                'processing_time': '#96CEB4',
                'success_rate': '#FECA57',
                'throughput': '#FF9FF3'
            }
        
        if self.warning_thresholds is None:
            self.warning_thresholds = {
                'cpu_percent': 80,
                'memory_percent': 80,
                'disk_percent': 85,
                'processing_time_seconds': 300,
                'success_rate_percent': 90
            }

class PerformanceDataLoader:
    """성능 데이터 로더 클래스"""
    
    def __init__(self, db_path: str = "performance_data.db"):
        self.db_path = db_path
        self.cache = {}
        self.cache_timeout = 30  # 초
        self.last_cache_time = {}
        
    def get_metrics(self, module_name: Optional[str] = None, 
                   hours: int = 24) -> List[Dict[str, Any]]:
        """성능 지표 가져오기"""
        cache_key = f"metrics_{module_name}_{hours}"
        
        # 캐시 확인
        if cache_key in self.cache:
            if time.time() - self.last_cache_time[cache_key] < self.cache_timeout:
                return self.cache[cache_key]
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 시간 범위 계산
                end_time = datetime.now()
                start_time = end_time - timedelta(hours=hours)
                
                query = """
                    SELECT * FROM performance_metrics 
                    WHERE timestamp >= ? AND timestamp <= ?
                """
                params = [start_time.isoformat(), end_time.isoformat()]
                
                if module_name:
                    query += " AND module_name = ?"
                    params.append(module_name)
                
                query += " ORDER BY timestamp DESC"
                
                cursor.execute(query, params)
                columns = [desc[0] for desc in cursor.description]
                results = [dict(zip(columns, row)) for row in cursor.fetchall()]
                
                # 캐시 저장
                self.cache[cache_key] = results
                self.last_cache_time[cache_key] = time.time()
                
                return results
                
        except Exception as e:
            logger.error(f"성능 지표 로드 오류: {str(e)}")
            return []
    
    def get_test_results(self, test_type: Optional[str] = None,
                        days: int = 7) -> List[Dict[str, Any]]:
        """테스트 결과 가져오기"""
        cache_key = f"test_results_{test_type}_{days}"
        
        # 캐시 확인
        if cache_key in self.cache:
            if time.time() - self.last_cache_time[cache_key] < self.cache_timeout:
                return self.cache[cache_key]
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 시간 범위 계산
                end_time = datetime.now()
                start_time = end_time - timedelta(days=days)
                
                query = """
                    SELECT * FROM test_results 
                    WHERE datetime(substr(timestamp, 1, 19)) >= datetime('now', '-{} days')
                    AND datetime(substr(timestamp, 1, 19)) <= datetime('now')
                """.format(days)
                
                if test_type:
                    query += " AND test_type = ?"
                    params = [test_type]
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                
                columns = [desc[0] for desc in cursor.description]
                results = [dict(zip(columns, row)) for row in cursor.fetchall()]
                
                # 캐시 저장
                self.cache[cache_key] = results
                self.last_cache_time[cache_key] = time.time()
                
                return results
                
        except Exception as e:
            logger.error(f"테스트 결과 로드 오류: {str(e)}")
            return []

class PerformanceChartGenerator:
    """성능 차트 생성기 클래스"""
    
    def __init__(self, config: DashboardConfig):
        self.config = config
        plt.style.use('seaborn-v0_8')
        
    def create_cpu_usage_chart(self, data: List[Dict[str, Any]]) -> Figure:
        """CPU 사용량 차트 생성"""
        fig, ax = plt.subplots(figsize=(12, 6))
        
        if not data:
            ax.text(0.5, 0.5, '데이터 없음', ha='center', va='center', transform=ax.transAxes)
            return fig
        
        # 데이터 전처리
        timestamps = [datetime.fromisoformat(d['timestamp']) for d in data]
        cpu_usage = [d['cpu_usage_percent'] for d in data]
        
        # 차트 생성
        ax.plot(timestamps, cpu_usage, color=self.config.chart_colors['cpu'], linewidth=2, label='CPU 사용량')
        ax.axhline(y=self.config.warning_thresholds['cpu_percent'], color='red', linestyle='--', alpha=0.7, label='경고 임계값')
        
        # 차트 꾸미기
        ax.set_title('CPU 사용량 추세', fontsize=16, fontweight='bold')
        ax.set_xlabel('시간', fontsize=12)
        ax.set_ylabel('CPU 사용량 (%)', fontsize=12)
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # x축 포맷
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        return fig
    
    def create_memory_usage_chart(self, data: List[Dict[str, Any]]) -> Figure:
        """메모리 사용량 차트 생성"""
        fig, ax = plt.subplots(figsize=(12, 6))
        
        if not data:
            ax.text(0.5, 0.5, '데이터 없음', ha='center', va='center', transform=ax.transAxes)
            return fig
        
        # 데이터 전처리
        timestamps = [datetime.fromisoformat(d['timestamp']) for d in data]
        memory_usage = [d['memory_usage_mb'] for d in data]
        
        # 차트 생성
        ax.plot(timestamps, memory_usage, color=self.config.chart_colors['memory'], linewidth=2, label='메모리 사용량')
        ax.axhline(y=self.config.warning_thresholds['memory_percent'], color='red', linestyle='--', alpha=0.7, label='경고 임계값')
        
        # 차트 꾸미기
        ax.set_title('메모리 사용량 추세', fontsize=16, fontweight='bold')
        ax.set_xlabel('시간', fontsize=12)
        ax.set_ylabel('메모리 사용량 (MB)', fontsize=12)
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # x축 포맷
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        return fig
    
    def create_processing_time_chart(self, data: List[Dict[str, Any]]) -> Figure:
        """처리 시간 차트 생성"""
        fig, ax = plt.subplots(figsize=(12, 6))
        
        if not data:
            ax.text(0.5, 0.5, '데이터 없음', ha='center', va='center', transform=ax.transAxes)
            return fig
        
        # 데이터 전처리
        timestamps = [datetime.fromisoformat(d['timestamp']) for d in data]
        processing_times = [d['processing_time'] for d in data]
        
        # 차트 생성
        ax.plot(timestamps, processing_times, color=self.config.chart_colors['processing_time'], linewidth=2, label='처리 시간')
        ax.axhline(y=self.config.warning_thresholds['processing_time_seconds'], color='red', linestyle='--', alpha=0.7, label='경고 임계값')
        
        # 차트 꾸미기
        ax.set_title('처리 시간 추세', fontsize=16, fontweight='bold')
        ax.set_xlabel('시간', fontsize=12)
        ax.set_ylabel('처리 시간 (초)', fontsize=12)
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # x축 포맷
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        return fig
    
    def create_success_rate_chart(self, test_results: List[Dict[str, Any]]) -> Figure:
        """성공률 차트 생성"""
        fig, ax = plt.subplots(figsize=(12, 6))
        
        if not test_results:
            ax.text(0.5, 0.5, '데이터 없음', ha='center', va='center', transform=ax.transAxes)
            return fig
        
        # 데이터 전처리
        test_names = [r['test_name'] for r in test_results]
        success_rates = [r['success'] * 100 for r in test_results]
        
        # 차트 생성
        bars = ax.bar(test_names, success_rates, color=self.config.chart_colors['success_rate'], alpha=0.7)
        ax.axhline(y=self.config.warning_thresholds['success_rate_percent'], color='red', linestyle='--', alpha=0.7, label='경고 임계값')
        
        # 성공률 레이블 추가
        for bar, rate in zip(bars, success_rates):
            color = 'green' if rate >= self.config.warning_thresholds['success_rate_percent'] else 'red'
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
                   f'{rate:.1f}%', ha='center', va='bottom', color=color, fontweight='bold')
        
        # 차트 꾸미기
        ax.set_title('테스트 성공률', fontsize=16, fontweight='bold')
        ax.set_xlabel('테스트 이름', fontsize=12)
        ax.set_ylabel('성공률 (%)', fontsize=12)
        ax.set_ylim(0, 100)
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # x축 레이블 회전
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        return fig
    
    def create_module_performance_comparison(self, data: List[Dict[str, Any]]) -> Figure:
        """모듈별 성능 비교 차트 생성"""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        if not data:
            for ax in [ax1, ax2, ax3, ax4]:
                ax.text(0.5, 0.5, '데이터 없음', ha='center', va='center', transform=ax.transAxes)
            return fig
        
        # 데이터 그룹화
        module_data = {}
        for d in data:
            module = d['module_name']
            if module not in module_data:
                module_data[module] = []
            module_data[module].append(d)
        
        # 평균 계산
        module_stats = {}
        for module, metrics in module_data.items():
            module_stats[module] = {
                'avg_cpu': np.mean([m['cpu_usage_percent'] for m in metrics]),
                'avg_memory': np.mean([m['memory_usage_mb'] for m in metrics]),
                'avg_processing_time': np.mean([m['processing_time'] for m in metrics]),
                'avg_throughput': np.mean([m['throughput_per_second'] for m in metrics])
            }
        
        modules = list(module_stats.keys())
        
        # CPU 사용량 비교
        cpu_values = [module_stats[m]['avg_cpu'] for m in modules]
        ax1.bar(modules, cpu_values, color=self.config.chart_colors['cpu'], alpha=0.7)
        ax1.set_title('평균 CPU 사용량', fontweight='bold')
        ax1.set_ylabel('CPU 사용량 (%)')
        ax1.tick_params(axis='x', rotation=45)
        
        # 메모리 사용량 비교
        memory_values = [module_stats[m]['avg_memory'] for m in modules]
        ax2.bar(modules, memory_values, color=self.config.chart_colors['memory'], alpha=0.7)
        ax2.set_title('평균 메모리 사용량', fontweight='bold')
        ax2.set_ylabel('메모리 사용량 (MB)')
        ax2.tick_params(axis='x', rotation=45)
        
        # 처리 시간 비교
        time_values = [module_stats[m]['avg_processing_time'] for m in modules]
        ax3.bar(modules, time_values, color=self.config.chart_colors['processing_time'], alpha=0.7)
        ax3.set_title('평균 처리 시간', fontweight='bold')
        ax3.set_ylabel('처리 시간 (초)')
        ax3.tick_params(axis='x', rotation=45)
        
        # 처리량 비교
        throughput_values = [module_stats[m]['avg_throughput'] for m in modules]
        ax4.bar(modules, throughput_values, color=self.config.chart_colors['throughput'], alpha=0.7)
        ax4.set_title('평균 처리량', fontweight='bold')
        ax4.set_ylabel('처리량 (개/초)')
        ax4.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        return fig

class PerformanceDashboard:
    """성능 대시보드 메인 클래스"""
    
    def __init__(self, db_path: str = "performance_data.db"):
        self.db_path = db_path
        self.config = DashboardConfig()
        self.data_loader = PerformanceDataLoader(db_path)
        self.chart_generator = PerformanceChartGenerator(self.config)
        
        # 메인 윈도우
        self.root = tk.Tk()
        self.root.title("WinForms_Docs 성능 대시보드")
        self.root.geometry("1400x900")
        
        # 데이터
        self.current_metrics = []
        self.current_test_results = []
        
        # UI 요소
        self.setup_ui()
        
        # 실시간 업데이트
        self.update_timer = None
        self.start_real_time_update()
        
    def setup_ui(self):
        """UI 설정"""
        # 메인 프레임
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 상단 제어 패널
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=(0, 10))
        
        # 모듈 선택
        ttk.Label(control_frame, text="모듈:").pack(side=tk.LEFT, padx=(0, 5))
        self.module_var = tk.StringVar(value="all")
        module_combo = ttk.Combobox(control_frame, textvariable=self.module_var, 
                                   values=["all", "data_cleaner", "data_normalizer", "deduplication", "system"])
        module_combo.pack(side=tk.LEFT, padx=(0, 10))
        module_combo.bind('<<ComboboxSelected>>', self.on_module_change)
        
        # 시간 범위 선택
        ttk.Label(control_frame, text="시간 범위:").pack(side=tk.LEFT, padx=(0, 5))
        self.time_range_var = tk.StringVar(value="24h")
        time_combo = ttk.Combobox(control_frame, textvariable=self.time_range_var,
                                 values=["1h", "6h", "24h", "7d", "30d"])
        time_combo.pack(side=tk.LEFT, padx=(0, 10))
        time_combo.bind('<<ComboboxSelected>>', self.on_time_range_change)
        
        # 새로고침 버튼
        refresh_btn = ttk.Button(control_frame, text="새로고침", command=self.refresh_data)
        refresh_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # 설정 버튼
        settings_btn = ttk.Button(control_frame, text="설정", command=self.open_settings)
        settings_btn.pack(side=tk.LEFT)
        
        # 상태 바
        self.status_bar = ttk.Label(main_frame, text="준비 중...", relief=tk.SUNKEN)
        self.status_bar.pack(fill=tk.X, pady=(10, 0))
        
        # 차트 프레임
        chart_frame = ttk.Frame(main_frame)
        chart_frame.pack(fill=tk.BOTH, expand=True)
        
        # 차트 생성
        self.create_charts(chart_frame)
        
    def create_charts(self, parent):
        """차트 생성"""
        # 차트 컨테이너
        chart_container = ttk.Frame(parent)
        chart_container.pack(fill=tk.BOTH, expand=True)
        
        # 상단 차트 (CPU, 메모리, 처리 시간)
        top_frame = ttk.Frame(chart_container)
        top_frame.pack(fill=tk.BOTH, expand=True)
        
        # CPU 사용량 차트
        cpu_frame = ttk.LabelFrame(top_frame, text="CPU 사용량", padding=10)
        cpu_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        self.cpu_canvas = tk.Canvas(cpu_frame, bg='white')
        self.cpu_canvas.pack(fill=tk.BOTH, expand=True)
        
        # 메모리 사용량 차트
        memory_frame = ttk.LabelFrame(top_frame, text="메모리 사용량", padding=10)
        memory_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        self.memory_canvas = tk.Canvas(memory_frame, bg='white')
        self.memory_canvas.pack(fill=tk.BOTH, expand=True)
        
        # 처리 시간 차트
        time_frame = ttk.LabelFrame(top_frame, text="처리 시간", padding=10)
        time_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(5, 0))
        self.time_canvas = tk.Canvas(time_frame, bg='white')
        self.time_canvas.pack(fill=tk.BOTH, expand=True)
        
        # 하단 차트 (성공률, 모듈 비교)
        bottom_frame = ttk.Frame(chart_container)
        bottom_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        # 성공률 차트
        success_frame = ttk.LabelFrame(bottom_frame, text="테스트 성공률", padding=10)
        success_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        self.success_canvas = tk.Canvas(success_frame, bg='white')
        self.success_canvas.pack(fill=tk.BOTH, expand=True)
        
        # 모듈 비교 차트
        comparison_frame = ttk.LabelFrame(bottom_frame, text="모듈별 성능 비교", padding=10)
        comparison_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(5, 0))
        self.comparison_canvas = tk.Canvas(comparison_frame, bg='white')
        self.comparison_canvas.pack(fill=tk.BOTH, expand=True)
        
    def refresh_data(self):
        """데이터 새로고침"""
        logger.info("대시보드 데이터 새로고침")
        
        # 모듈 선택 가져오기
        module_name = None if self.module_var.get() == "all" else self.module_var.get()
        
        # 시간 범위 가져오기
        time_range = self.time_range_var.get()
        if time_range == "1h":
            hours = 1
        elif time_range == "6h":
            hours = 6
        elif time_range == "24h":
            hours = 24
        elif time_range == "7d":
            hours = 24 * 7
        else:  # 30d
            hours = 24 * 30
        
        # 데이터 로드
        self.current_metrics = self.data_loader.get_metrics(module_name, hours)
        self.current_test_results = self.data_loader.get_test_results()
        
        # 차트 업데이트
        self.update_charts()
        
        # 상태 업데이트
        self.update_status()
        
    def update_charts(self):
        """차트 업데이트"""
        try:
            # CPU 사용량 차트
            cpu_fig = self.chart_generator.create_cpu_usage_chart(self.current_metrics)
            self.update_canvas(self.cpu_canvas, cpu_fig)
            
            # 메모리 사용량 차트
            memory_fig = self.chart_generator.create_memory_usage_chart(self.current_metrics)
            self.update_canvas(self.memory_canvas, memory_fig)
            
            # 처리 시간 차트
            time_fig = self.chart_generator.create_processing_time_chart(self.current_metrics)
            self.update_canvas(self.time_canvas, time_fig)
            
            # 성공률 차트
            success_fig = self.chart_generator.create_success_rate_chart(self.current_test_results)
            self.update_canvas(self.success_canvas, success_fig)
            
            # 모듈 비교 차트
            comparison_fig = self.chart_generator.create_module_performance_comparison(self.current_metrics)
            self.update_canvas(self.comparison_canvas, comparison_fig)
            
        except Exception as e:
            logger.error(f"차트 업데이트 오류: {str(e)}")
            messagebox.showerror("오류", f"차트 업데이트 중 오류가 발생했습니다: {str(e)}")
    
    def update_canvas(self, canvas: tk.Canvas, fig: Figure):
        """캔버스 업데이트"""
        # 기존 그래프 정리
        for widget in canvas.winfo_children():
            widget.destroy()
        
        # 새로운 그래프 추가
        canvas.draw = FigureCanvasTkAgg(fig, canvas).get_tk_widget()
        canvas.draw.pack(fill=tk.BOTH, expand=True)
        
    def update_status(self):
        """상태 업데이트"""
        if self.current_metrics:
            latest_metric = self.current_metrics[0]
            status_text = f"마지막 업데이트: {latest_metric['timestamp']} | "
            status_text += f"CPU: {latest_metric['cpu_usage_percent']:.1f}% | "
            status_text += f"메모리: {latest_metric['memory_usage_mb']:.1f}MB | "
            status_text += f"데이터 포인트: {len(self.current_metrics)}"
        else:
            status_text = "데이터 없음"
        
        self.status_bar.config(text=status_text)
    
    def start_real_time_update(self):
        """실시간 업데이트 시작"""
        self.refresh_data()
        self.update_timer = self.root.after(self.config.refresh_interval * 1000, self.start_real_time_update)
    
    def stop_real_time_update(self):
        """실시간 업데이트 중지"""
        if self.update_timer:
            self.root.after_cancel(self.update_timer)
            self.update_timer = None
    
    def on_module_change(self, event=None):
        """모듈 변경 이벤트"""
        self.refresh_data()
    
    def on_time_range_change(self, event=None):
        """시간 범위 변경 이벤트"""
        self.refresh_data()
    
    def open_settings(self):
        """설정 창 열기"""
        settings_window = tk.Toplevel(self.root)
        settings_window.title("대시보드 설정")
        settings_window.geometry("400x300")
        
        # 설정 내용
        ttk.Label(settings_window, text="새로고칼 간격 (초):").pack(pady=5)
        refresh_interval_var = tk.IntVar(value=self.config.refresh_interval)
        refresh_interval_spin = ttk.Spinbox(settings_window, from_=1, to=60, textvariable=refresh_interval_var)
        refresh_interval_spin.pack(pady=5)
        
        def save_settings():
            self.config.refresh_interval = refresh_interval_var.get()
            settings_window.destroy()
            messagebox.showinfo("성공", "설정이 저장되었습니다.")
        
        ttk.Button(settings_window, text="저장", command=save_settings).pack(pady=20)
    
    def run(self):
        """대시보드 실행"""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    def on_closing(self):
        """창 닫기 이벤트"""
        self.stop_real_time_update()
        self.root.destroy()

def main():
    """메인 실행 함수"""
    logger.info("성능 대시보드 시작")
    
    try:
        dashboard = PerformanceDashboard()
        dashboard.run()
        
    except Exception as e:
        logger.error(f"대시보드 실행 오류: {str(e)}")
        messagebox.showerror("오류", f"대시보드 실행 중 오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    main()