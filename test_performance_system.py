#!/usr/bin/env python3
"""
성능 모니터링 시스템 테스트 스크립트
"""

from performance_monitor import get_performance_monitor
import time
import json

def main():
    try:
        # 성능 모니터 초기화
        monitor = get_performance_monitor()
        
        # 테스트 데이터 생성
        test_modules = ['data_cleaner', 'data_normalizer', 'deduplication']
        test_operations = ['process_file', 'normalize_data', 'check_duplicates']
        
        print('성능 테스트 데이터 생성 시작...')
        
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
            
            print(f'테스트 {i+1}: {module}.{operation} - {processing_time:.3f}초')
        
        print('성능 테스트 데이터 생성 완료')
        
        # 성능 보고서 생성
        report = monitor.get_performance_report()
        
        if report['status'] == 'success':
            print('\n성능 보고서 생성 완료')
            summary = report['data']['summary']
            print(f'총 작업 수: {summary["total_operations"]}')
            print(f'평균 처리 시간: {summary["average_processing_time"]:.3f}초')
            print(f'최대 메모리 사용: {summary["peak_memory_usage"]:.2f}MB')
            print(f'총 오류 수: {summary["total_errors"]}')
            print(f'총 경고 수: {summary["total_warnings"]}')
            
            # 개선 사항 출력
            if report['data']['recommendations']:
                print('\n개선 사항:')
                for rec in report['data']['recommendations']:
                    print(f'  - {rec}')
            
            # 보고서 파일로 저장
            report_path = 'performance_results/performance_report.json'
            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            print(f'\n보고서가 {report_path}에 저장되었습니다')
            
            return True
        else:
            print(f'보고서 생성 실패: {report["message"]}')
            return False
            
    except Exception as e:
        print(f'오류 발생: {str(e)}')
        return False

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)