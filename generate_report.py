#!/usr/bin/env python3
"""
성능 보고서 생성 스크립트
"""

from performance_monitor import get_performance_monitor
import json
import sys

def main():
    try:
        # 성능 모니터 인스턴스 가져오기
        monitor = get_performance_monitor()
        
        # 성능 보고서 생성
        report = monitor.get_performance_report()
        
        if report['status'] == 'success':
            print('성능 보고서 생성 완료')
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
    sys.exit(0 if success else 1)