# WinForms_Docs 통합 병렬 처리 설정 및 관리 모듈

## 개요

WinForms_Docs 데이터 처리 시스템을 위한 통합 병렬 처리 설정 및 관리 모듈로, 세 개의 핵심 모듈(data_cleaner.py, data_normalizer.py, deduplication.py)을 통합 관리합니다.

## 주요 기능

### 1. 통합 설정 관리 시스템
- 세 개 모듈의 병렬 처리 파라미터 중앙 관리
- 환경별 설정 파일 지원 (JSON/YAML)
- 설정 값 검증 및 자동 조정
- 실시간 설정 업데이트

### 2. 동적 리소스 관리
- CPU 코어 수 실시간 감지
- 메모리 사용량 모니터링
- 최적 워커 수 계산 및 할당
- 시스템 부하 기반 자동 스케일링

### 3. 작업 큐 관리 시스템
- 세 개 모듈의 작업 통합 큐
- 우선순위 기반 작업 스케줄링
- 작업 상태 추적 및 관리
- 작업 통계 및 모니터링

### 4. 성능 모니터링 및 로깅
- 시스템 전체 성능 지표 수집
- 병렬 처리 상태 실시간 모니터링
- 성능 로그 중앙 관리
- 성능 보고서 생성

### 5. 오류 처리 및 복구 시스템
- 다중 모듈 오류 처리
- 자동 복구 메커니즘
- 실패 작업 재시도 로직
- 상세 오류 로깅

## 설치 및 설정

### 1. 의존성 설치

```bash
pip install psutil pyyaml
```

### 2. 설정 파일 준비

기본 설정 파일 `parallel_config.json`이 함께 제공됩니다. 필요에 따라 수정하여 사용합니다.

```json
{
  "global": {
    "log_level": "INFO",
    "max_concurrent_tasks": 4,
    "enable_auto_scaling": true
  },
  "modules": {
    "data_cleaner": {
      "max_workers": 8,
      "chunk_size": 100,
      "memory_limit_mb": 2048,
      "enabled": true
    },
    "data_normalizer": {
      "max_workers": 6,
      "chunk_size": 50,
      "memory_limit_mb": 1536,
      "enabled": true
    },
    "deduplication": {
      "max_workers": 12,
      "chunk_size": 30,
      "memory_limit_mb": 3072,
      "enabled": true
    }
  }
}
```

### 3. 모듈 초기화

```python
from parallel_config import ParallelConfigManager, ProcessingModule, TaskPriority

# 설정 관리자 초기화
config_manager = ParallelConfigManager()

# 커스텀 설정 파일로 초기화
config_manager = ParallelConfigManager(config_file=Path("my_config.json"))
```

## 사용 방법

### 1. 기본 사용 예제

```python
from parallel_config import ParallelConfigManager, ProcessingModule, TaskPriority
import time

# 설정 관리자 초기화
manager = ParallelConfigManager()

# 작업 추가
task_id1 = manager.add_task(
    ProcessingModule.DATA_CLEANER,
    {"input_path": "data/raw", "output_path": "data/cleaned"},
    TaskPriority.HIGH
)

task_id2 = manager.add_task(
    ProcessingModule.DATA_NORMALIZER,
    {"input_file": "data/cleaned/output.json"},
    TaskPriority.NORMAL
)

task_id3 = manager.add_task(
    ProcessingModule.DEDUPLICATION,
    {"input_directory": "data/normalized"},
    TaskPriority.CRITICAL
)

# 시스템 상태 확인
status = manager.get_system_status()
print(f"CPU 사용률: {status['cpu_usage_percent']:.1f}%")
print(f"메모리 사용량: {status['memory_used_mb']:.1f}MB")

# 작업 실행 (별도 스레드에서 실행)
import threading
execution_thread = threading.Thread(target=manager.execute_tasks, args=(4,))
execution_thread.start()

# 성능 모니터링
while True:
    report = manager.get_performance_report()
    print(f"완료된 작업: {report['performance_metrics']['completed_tasks']}")
    print(f"실패한 작업: {report['performance_metrics']['failed_tasks']}")
    time.sleep(5)
```

### 2. 설정 관리 예제

```python
from parallel_config import ParallelConfigManager, ProcessingModule

# 설정 관리자 초기화
manager = ParallelConfigManager()

# 특정 모듈 설정 조회
cleaner_config = manager.get_module_config(ProcessingModule.DATA_CLEANER)
print(f"DataCleaner 최대 워커 수: {cleaner_config.max_workers}")

# 설정 동적 업데이트
manager.update_module_config(
    ProcessingModule.DATA_CLEANER,
    max_workers=12,
    chunk_size=150,
    memory_limit_mb=4096
)

# 설정 파일 저장
manager.save_config()
```

### 3. 성능 모니터링 예제

```python
from parallel_config import ParallelConfigManager
import json

# 설정 관리자 초기화
manager = ParallelConfigManager()

# 성능 보고서 생성
report = manager.get_performance_report()

# 보고서 출력
print("=== 성능 보고서 ===")
print(f"총 작업 수: {report['performance_metrics']['total_tasks']}")
print(f"완료된 작업: {report['performance_metrics']['completed_tasks']}")
print(f"실패한 작업: {report['performance_metrics']['failed_tasks']}")
print(f"평균 처리 시간: {report['performance_metrics']['average_processing_time']:.2f}초")
print(f"최대 메모리 사용: {report['performance_metrics']['peak_memory_usage_mb']:.1f}MB")

# 시스템 상태 출력
status = report['system_status']
print(f"\n=== 시스템 상태 ===")
print(f"CPU 사용률: {status['cpu_usage_percent']:.1f}%")
print(f"메모리 사용량: {status['memory_used_mb']:.1f}MB / {status['memory_total_mb']:.1f}MB")
print(f"디스크 사용률: {status['disk_usage_percent']:.1f}%")

# 보고서 파일로 저장
with open("performance_report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=2, ensure_ascii=False)
```

### 4. 고급 사용 예제

```python
from parallel_config import ParallelConfigManager, ProcessingModule, TaskPriority
from pathlib import Path
import threading
import time

class DataProcessingPipeline:
    """데이터 처리 파이프라인 클래스"""
    
    def __init__(self, config_file=None):
        self.manager = ParallelConfigManager(config_file)
        self.running = False
        
    def start_pipeline(self):
        """파이프라인 시작"""
        self.running = True
        
        # 작업 실행 스레드 시작
        self.execution_thread = threading.Thread(target=self._execute_tasks, daemon=True)
        self.execution_thread.start()
        
        # 모니터링 스레드 시작
        self.monitoring_thread = threading.Thread(target=self._monitor_performance, daemon=True)
        self.monitoring_thread.start()
        
        print("데이터 처리 파이프라인 시작")
    
    def stop_pipeline(self):
        """파이프라인 중지"""
        self.running = False
        self.manager.cleanup()
        print("데이터 처리 파이프라인 중지")
    
    def add_batch_tasks(self, tasks_data):
        """배치 작업 추가"""
        for task_data in tasks_data:
            priority = TaskPriority(task_data.get('priority', 2))
            self.manager.add_task(
                ProcessingModule(task_data['module']),
                task_data['data'],
                priority
            )
    
    def _execute_tasks(self):
        """작업 실행 루프"""
        while self.running:
            try:
                self.manager.execute_tasks(max_concurrent_tasks=6)
                time.sleep(1)
            except Exception as e:
                print(f"작업 실행 오류: {e}")
                time.sleep(5)
    
    def _monitor_performance(self):
        """성능 모니터링 루프"""
        while self.running:
            try:
                report = self.manager.get_performance_report()
                
                # 성능 경고 체크
                if report['performance_metrics']['failed_tasks'] > 0:
                    print(f"⚠️  실패한 작업 발생: {report['performance_metrics']['failed_tasks']}")
                
                if report['system_status']['cpu_usage_percent'] > 90:
                    print(f"⚠️  CPU 사용률 높음: {report['system_status']['cpu_usage_percent']:.1f}%")
                
                if report['system_status']['memory_used_mb'] / report['system_status']['memory_total_mb'] * 100 > 85:
                    print(f"⚠️  메모리 사용량 높음: {report['system_status']['memory_used_mb']:.1f}MB")
                
                time.sleep(10)
                
            except Exception as e:
                print(f"성능 모니터링 오류: {e}")
                time.sleep(10)

# 사용 예시
if __name__ == "__main__":
    # 파이프라인 초기화
    pipeline = DataProcessingPipeline("parallel_config.json")
    
    # 작업 데이터 준비
    tasks = [
        {
            'module': 'data_cleaner',
            'priority': 3,
            'data': {'input_path': 'WinForms_Docs', 'output_path': 'cleaned_data'}
        },
        {
            'module': 'data_normalizer', 
            'priority': 2,
            'data': {'input_file': 'cleaned_data/output.json'}
        },
        {
            'module': 'deduplication',
            'priority': 4,
            'data': {'input_directory': 'normalized_data'}
        }
    ]
    
    # 파이프라인 시작
    pipeline.start_pipeline()
    
    # 작업 추가
    pipeline.add_batch_tasks(tasks)
    
    # 잠시 대기
    try:
        time.sleep(30)
    except KeyboardInterrupt:
        pass
    finally:
        # 파이프라인 중지
        pipeline.stop_pipeline()
```

## API 참조

### ParallelConfigManager 클래스

#### 생성자
```python
ParallelConfigManager(config_file: Optional[Path] = None)
```
- `config_file`: 설정 파일 경로 (기본: parallel_config.json)

#### 주요 메서드

##### 작업 관리
- `add_task(module, data, priority)`: 작업 추가
- `get_next_task()`: 다음 작업 가져오기
- `complete_task(task_id, result)`: 작업 완료 처리
- `fail_task(task_id, error_message)`: 작업 실패 처리

##### 설정 관리
- `get_module_config(module)`: 모듈 설정 조회
- `update_module_config(module, **kwargs)`: 모듈 설정 업데이트
- `load_config()`: 설정 파일 로드
- `save_config()`: 설정 파일 저장

##### 모니터링
- `get_system_status()`: 시스템 상태 조회
- `get_performance_report()`: 성능 보고서 생성
- `start_monitoring()`: 모니터링 시작
- `stop_monitoring()`: 모니터링 중지

##### 작업 실행
- `execute_tasks(max_concurrent_tasks)`: 작업 실행
- `_execute_task(task)`: 개별 작업 실행

##### 정리
- `cleanup()`: 자원 정리

### 데이터 클래스

#### ProcessingConfig
- `module`: 처리 모듈
- `max_workers`: 최대 워커 수
- `chunk_size`: 청크 크기
- `memory_limit_mb`: 메모리 제한 (MB)
- `timeout_seconds`: 타임아웃 (초)
- `retry_count`: 재시도 횟수
- `priority`: 우선순위
- `enabled`: 활성화 여부
- `module_specific_config`: 모듈별 특정 설정

#### TaskItem
- `task_id`: 작업 ID
- `module`: 처리 모듈
- `priority`: 우선순위
- `data`: 작업 데이터
- `status`: 작업 상태
- `created_at`: 생성 시간
- `started_at`: 시작 시간
- `completed_at`: 완료 시간
- `retry_count`: 재시도 횟수
- `error_message`: 오류 메시지
- `result`: 작업 결과

#### PerformanceMetrics
- `total_tasks`: 총 작업 수
- `completed_tasks`: 완료된 작업 수
- `failed_tasks`: 실패한 작업 수
- `average_processing_time`: 평균 처리 시간
- `peak_memory_usage_mb`: 최대 메모리 사용량
- `current_memory_usage_mb`: 현재 메모리 사용량
- `cpu_usage_percent`: CPU 사용률
- `throughput_tasks_per_second`: 초당 처리량

### 열거형 타입

#### ProcessingModule
- `DATA_CLEANER`: 데이터 정제 모듈
- `DATA_NORMALIZER`: 데이터 정규화 모듈
- `DEDUPLICATION`: 중복 제거 모듈

#### TaskPriority
- `LOW`: 낮은 우선순위 (1)
- `NORMAL`: 보통 우선순위 (2)
- `HIGH`: 높은 우선순위 (3)
- `CRITICAL`: 긴급 우선순위 (4)

#### TaskStatus
- `PENDING`: 대기 중
- `RUNNING`: 실행 중
- `COMPLETED`: 완료됨
- `FAILED`: 실패함
- `RETRYING`: 재시도 중

## 성능 최적화

### 1. 시스템 리소스 최적화

```python
# CPU 코어 수에 맞춰 워커 수 조정
cpu_cores = mp.cpu_count()
optimal_workers = min(cpu_cores, 8)  # 최대 8개 워커 제한

# 메모리 사용량 모니터링
if memory_usage > memory_limit * 0.8:  # 80% 이상 사용 시
    # 워커 수 동적 조정
    manager.update_module_config(module, max_workers=optimal_workers // 2)
```

### 2. 작업 큐 최적화

```python
# 우선순위 기반 작업 할당
high_priority_tasks = [task for task in task_queue if task.priority == TaskPriority.CRITICAL]

# 작업 큐 크기 제한
if len(task_queue) > 1000:
    # 오래된 작업 제거
    task_queue = task_queue[-1000:]
```

### 3. 캐시 최적화

```python
# LRU 캐시 크기 조정
cache_size = min(10000, available_memory_mb // 10)  # 메모리의 10% 사용

# 캐시 히트율 모니터링
hit_rate = cache_hits / (cache_hits + cache_misses)
if hit_rate < 0.5:  # 50% 미만 시
    # 캐시 크기 조정
    cache_size = int(cache_size * 1.5)
```

## 문제 해결

### 1. 메모리 부족 문제

**증상**: 메모리 사용량이 지나치게 높음

**해결책**:
```python
# 메모리 제한 설정
manager.update_module_config(ProcessingModule.DATA_CLEANER, memory_limit_mb=1024)

# 청크 크기 조정
manager.update_module_config(ProcessingModule.DATA_CLEANER, chunk_size=50)

# 메모리 정주기 설정
manager.global_config['memory_cleanup_interval'] = 5
```

### 2. CPU 사용량 과다

**증상**: CPU 사용률이 90% 이상

**해결책**:
```python
# 워커 수 감소
manager.update_module_config(ProcessingModule.DATA_CLEANER, max_workers=4)

# 동적 스케일링 활성화
manager.global_config['enable_auto_scaling'] = True
```

### 3. 작업 대기 시간 길음

**증상**: 작업이 큐에서 오래 대기

**해결책**:
```python
# 우선순위 조정
manager.update_module_config(ProcessingModule.DATA_CLEANER, priority=TaskPriority.HIGH)

# 동시 작업 증가
manager.execute_tasks(max_concurrent_tasks=8)
```

## 로그 분석

### 1. 로그 파일 위치
- 기본 로그: `logs/parallel_config.log`
- 성능 로그: `logs/performance.log`
- 오류 로그: `logs/error.log`

### 2. 로그 레벨
- `DEBUG`: 상세 디버깅 정보
- `INFO`: 일반 정보
- `WARNING`: 경고 정보
- `ERROR`: 오류 정보
- `CRITICAL`: 심각한 오류

### 3. 로그 분석 예제

```python
import re
from collections import Counter

# 로그 파일 읽기
with open("logs/parallel_config.log", "r", encoding="utf-8") as f:
    logs = f.readlines()

# 오류 패턴 분석
error_pattern = re.compile(r'ERROR - (.+)')
errors = error_pattern.findall(' '.join(logs))
error_counter = Counter(errors)

print("주요 오류 유형:")
for error, count in error_counter.most_common(5):
    print(f"{error}: {count}회")

# 성능 패턴 분석
performance_pattern = re.compile(r'성능 - (.+)')
performance_logs = performance_pattern.findall(' '.join(logs))
```

## 업데이트 및 유지보수

### 1. 설정 파일 업데이트

```python
# 새로운 설정 파일로 업데이트
new_config = Path("updated_config.json")
manager.load_config(new_config)

# 설정 변경 사항 확인
report = manager.get_performance_report()
print("업데이트된 설정:")
for module, config in report['module_configs'].items():
    print(f"{module}: max_workers={config['max_workers']}")
```

### 2. 모듈 업데이트

```python
# 새 버전 모듈로 업데이트
manager.update_module_config(
    ProcessingModule.DATA_CLEANER,
    module_specific_config={
        "new_feature": True,
        "improved_algorithm": True
    }
)
```

## 기여 가이드

1. 이슈 템플릿을 사용하여 버그 리포트 작성
2. 기능 요청 시 상세한 사용 사례 제공
3. 코드 변경 시 테스트 케이스 포함
4. 문서 업데이트 필요 시 함께 제공

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.

## 지원

문의 사항이 있을 경우 다음 방법으로 연락주세요:
- 이메일: kilo@example.com
- GitHub Issues: 프로젝트 저장소의 Issues 탭
- 문서: 이 README 파일 및 코드 내 docstring