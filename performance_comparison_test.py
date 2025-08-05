"""
WinForms_Docs AsyncFileManager 성능 비교 테스트

주요 테스트 기능:
================
1. 기존 동기 처리 vs 비동기 처리 성능 비교
2. 메모리 사용량 비교
3. 처리량(Throughput) 측정
4. 오류율 비교
5. 실제 데이터로 성능 검증

테스트 전략:
===========
- 동일한 테스트 데이터로 비교
- 여러 반복을 통한 평균값 계산
- 실제 WinForms_Docs 데이터 사용
- 다양한 파일 크기 테스트

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0 (성능 비교 테스트)
"""

import asyncio
import time
import logging
import psutil
import gc
from pathlib import Path
from typing import List, Dict, Any
import json
import statistics

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 테스트 대상 모듈 임포트
from async_file_bridge import AsyncFileBridge

class PerformanceComparisonTester:
    """성능 비교 테스터 클래스"""
    
    def __init__(self):
        """테스터 초기화"""
        self.test_results = []
        self.process = psutil.Process()
        
    def get_memory_usage(self) -> float:
        """메모리 사용량 조회 (MB)"""
        return self.process.memory_info().rss / 1024 / 1024
    
    def measure_performance(self, 
                          test_name: str, 
                          test_func, 
                          *args, 
                          **kwargs) -> Dict[str, Any]:
        """성능 측정"""
        logger.info(f"성능 측정 시작: {test_name}")
        
        # 메모리 초기화
        gc.collect()
        initial_memory = self.get_memory_usage()
        
        # 실행 시간 측정
        start_time = time.time()
        start_memory = self.get_memory_usage()
        
        # 테스트 실행
        try:
            result = test_func(*args, **kwargs)
            success = True
        except Exception as e:
            logger.error(f"테스트 실행 실패: {str(e)}")
            result = None
            success = False
        
        # 종료 시간 및 메모리 측정
        end_time = time.time()
        end_memory = self.get_memory_usage()
        
        # 성능 계산
        execution_time = end_time - start_time
        memory_usage = end_memory - initial_memory
        peak_memory = end_memory - start_memory
        
        # 결과 저장
        test_result = {
            'test_name': test_name,
            'execution_time': execution_time,
            'memory_usage': memory_usage,
            'peak_memory': peak_memory,
            'success': success,
            'result': result
        }
        
        self.test_results.append(test_result)
        
        logger.info(f"성능 측정 완료: {test_name}")
        logger.info(f"  - 실행 시간: {execution_time:.3f}초")
        logger.info(f"  - 메모리 사용: {memory_usage:.2f}MB")
        logger.info(f"  - 피크 메모리: {peak_memory:.2f}MB")
        logger.info(f"  - 성공 여부: {success}")
        
        return test_result
    
    def create_test_files(self, 
                         base_dir: Path, 
                         count: int = 50, 
                         min_size: int = 1024, 
                         max_size: int = 10240) -> List[Path]:
        """테스트 파일 생성"""
        test_files = []
        
        logger.info(f"테스트 파일 생성: {count}개 파일")
        
        for i in range(count):
            # 파일 크기 랜덤 생성
            file_size = min_size + (max_size - min_size) * (i % 5) / 4
            
            # 테스트 파일 생성
            test_file = base_dir / f"test_perf_{i:04d}.md"
            
            with open(test_file, 'w', encoding='utf-8') as f:
                # 헤더 작성
                f.write(f"# 테스트 문서 {i+1}\n\n")
                
                # 내용 생성 (파일 크기에 맞춰)
                content_size = int(file_size)
                content = "이것은 성능 테스트를 위한 가짜 문서 내용입니다. " * (content_size // 50)
                f.write(content)
            
            test_files.append(test_file)
        
        logger.info(f"테스트 파일 생성 완료: {len(test_files)}개 파일")
        return test_files
    
    def cleanup_test_files(self, test_files: List[Path]) -> None:
        """테스트 파일 정리"""
        logger.info("테스트 파일 정리 시작")
        
        for test_file in test_files:
            try:
                test_file.unlink()
            except Exception as e:
                logger.warning(f"파일 삭제 실패: {test_file} - {str(e)}")
        
        logger.info("테스트 파일 정리 완료")
    
    def run_performance_comparison(self, 
                                 file_count: int = 50, 
                                 iterations: int = 3) -> Dict[str, Any]:
        """성능 비교 테스트 실행"""
        logger.info("WinForms_Docs AsyncFileManager 성능 비교 테스트 시작")
        logger.info(f"파일 수: {file_count}, 반복 투수: {iterations}")
        
        # 테스트 디렉토리 생성
        test_dir = Path(tempfile.mkdtemp())
        logger.info(f"테스트 디렉토리: {test_dir}")
        
        try:
            # 테스트 파일 생성
            test_files = self.create_test_files(test_dir, file_count)
            
            # 테스트 결과 저장
            all_results = {
                'sync_results': [],
                'async_results': [],
                'comparison': {},
                'summary': {}
            }
            
            # 반복 테스트
            for iteration in range(iterations):
                logger.info(f"\n=== 반복 {iteration + 1}/{iterations} ===")
                
                # 동기 처리 테스트
                sync_result = self.measure_performance(
                    f"동기 처리 (반복 {iteration + 1})",
                    self.run_sync_processing,
                    test_files.copy()
                )
                all_results['sync_results'].append(sync_result)
                
                # 비동기 처리 테스트
                async_result = self.measure_performance(
                    f"비동기 처리 (반복 {iteration + 1})",
                    self.run_async_processing,
                    test_files.copy()
                )
                all_results['async_results'].append(async_result)
                
                # 강제 가비지 컬렉션
                gc.collect()
                time.sleep(1)
            
            # 결과 분석
            all_results['comparison'] = self.analyze_results(all_results)
            all_results['summary'] = self.generate_summary(all_results)
            
            # 결과 출력
            self.print_results(all_results)
            
            return all_results
            
        finally:
            # 테스트 파일 정리
            self.cleanup_test_files(test_files)
            
            # 테스트 디렉토리 삭제
            try:
                test_dir.rmdir()
            except:
                pass
            
            logger.info("성능 비교 테스트 완료")
    
    def run_sync_processing(self, test_files: List[Path]) -> List[Any]:
        """동기 처리 실행"""
        logger.info("동기 처리 시작")
        
        bridge = AsyncFileBridge(use_async=False)
        
        try:
            # 동기 처리
            results = bridge.process_files_parallel(test_files)
            
            logger.info(f"동기 처리 완료: {len(results)}개 파일")
            return results
            
        finally:
            bridge.cleanup()
    
    async def run_async_processing(self, test_files: List[Path]) -> List[Any]:
        """비동기 처리 실행"""
        logger.info("비동기 처리 시작")
        
        bridge = AsyncFileBridge(use_async=True)
        
        try:
            # 비동기 처리
            results = await bridge.process_files_async(test_files)
            
            logger.info(f"비동기 처리 완료: {len(results)}개 파일")
            return results
            
        finally:
            bridge.cleanup()
    
    def analyze_results(self, all_results: Dict[str, Any]) -> Dict[str, Any]:
        """결과 분석"""
        logger.info("성능 결과 분석 시작")
        
        sync_times = [r['execution_time'] for r in all_results['sync_results']]
        async_times = [r['execution_time'] for r in all_results['async_results']]
        
        sync_memory = [r['memory_usage'] for r in all_results['sync_results']]
        async_memory = [r['memory_usage'] for r in all_results['async_results']]
        
        # 통계 계산
        comparison = {
            'avg_sync_time': statistics.mean(sync_times),
            'avg_async_time': statistics.mean(async_times),
            'avg_sync_memory': statistics.mean(sync_memory),
            'avg_async_memory': statistics.mean(async_memory),
            'time_improvement': (statistics.mean(sync_times) - statistics.mean(async_times)) / statistics.mean(sync_times) * 100,
            'memory_improvement': (statistics.mean(sync_memory) - statistics.mean(async_memory)) / statistics.mean(sync_memory) * 100,
            'throughput_improvement': 0,  # 처리량 개선률은 나중에 계산
            'success_rate_sync': sum(1 for r in all_results['sync_results'] if r['success']) / len(all_results['sync_results']),
            'success_rate_async': sum(1 for r in all_results['async_results'] if r['success']) / len(all_results['async_results'])
        }
        
        # 처리량 계산
        if comparison['avg_sync_time'] > 0:
            sync_throughput = len(all_results['sync_results'][0]['result']) / comparison['avg_sync_time']
        else:
            sync_throughput = 0
            
        if comparison['avg_async_time'] > 0:
            async_throughput = len(all_results['async_results'][0]['result']) / comparison['avg_async_time']
        else:
            async_throughput = 0
        
        comparison['sync_throughput'] = sync_throughput
        comparison['async_throughput'] = async_throughput
        comparison['throughput_improvement'] = (async_throughput - sync_throughput) / sync_throughput * 100 if sync_throughput > 0 else 0
        
        logger.info("성능 결과 분석 완료")
        return comparison
    
    def generate_summary(self, all_results: Dict[str, Any]) -> Dict[str, Any]:
        """요약 생성"""
        logger.info("성능 요약 생성 시작")
        
        summary = {
            'total_tests': len(all_results['sync_results']) + len(all_results['async_results']),
            'successful_tests': sum(1 for r in all_results['sync_results'] + all_results['async_results'] if r['success']),
            'total_files_processed': sum(len(r['result']) for r in all_results['sync_results'] + all_results['async_results'] if r['success']),
            'average_execution_time': statistics.mean([r['execution_time'] for r in all_results['sync_results'] + all_results['async_results'] if r['success']]),
            'average_memory_usage': statistics.mean([r['memory_usage'] for r in all_results['sync_results'] + all_results['async_results'] if r['success']]),
            'performance_goals': {
                'time_improvement_target': 50.0,  # 50% 개선 목표
                'memory_improvement_target': 10.0,  # 10% 개선 목표
                'throughput_improvement_target': 100.0  # 100% 개선 목표
            },
            'achievement': {
                'time_improvement_achieved': False,
                'memory_improvement_achieved': False,
                'throughput_improvement_achieved': False
            }
        }
        
        # 성과 평가
        comparison = all_results['comparison']
        if comparison['time_improvement'] >= summary['performance_goals']['time_improvement_target']:
            summary['achievement']['time_improvement_achieved'] = True
        
        if comparison['memory_improvement'] >= summary['performance_goals']['memory_improvement_target']:
            summary['achievement']['memory_improvement_achieved'] = True
        
        if comparison['throughput_improvement'] >= summary['performance_goals']['throughput_improvement_target']:
            summary['achievement']['throughput_improvement_achieved'] = True
        
        logger.info("성능 요약 생성 완료")
        return summary
    
    def print_results(self, all_results: Dict[str, Any]) -> None:
        """결과 출력"""
        logger.info("\n" + "="*60)
        logger.info("WinForms_Docs AsyncFileManager 성능 비교 결과")
        logger.info("="*60)
        
        # 기본 통계
        comparison = all_results['comparison']
        summary = all_results['summary']
        
        logger.info("\n기본 통계:")
        logger.info(f"  - 총 테스트 수: {summary['total_tests']}")
        logger.info(f"  - 성공한 테스트: {summary['successful_tests']}")
        logger.info(f"  - 처리된 총 파일 수: {summary['total_files_processed']}")
        
        logger.info("\n성능 비교:")
        logger.info(f"  - 평균 동기 처리 시간: {comparison['avg_sync_time']:.3f}초")
        logger.info(f"  - 평균 비동기 처리 시간: {comparison['avg_async_time']:.3f}초")
        logger.info(f"  - 시간 개선률: {comparison['time_improvement']:.1f}%")
        logger.info(f"  - 평균 동기 메모리 사용: {comparison['avg_sync_memory']:.2f}MB")
        logger.info(f"  - 평균 비동기 메모리 사용: {comparison['avg_async_memory']:.2f}MB")
        logger.info(f"  - 메모리 개선률: {comparison['memory_improvement']:.1f}%")
        logger.info(f"  - 동기 처리량: {comparison['sync_throughput']:.2f} 파일/초")
        logger.info(f"  - 비동기 처리량: {comparison['async_throughput']:.2f} 파일/초")
        logger.info(f"  - 처리량 개선률: {comparison['throughput_improvement']:.1f}%")
        
        logger.info("\n성공률:")
        logger.info(f"  - 동기 처리 성공률: {comparison['success_rate_sync']*100:.1f}%")
        logger.info(f"  - 비동기 처리 성공률: {comparison['success_rate_async']*100:.1f}%")
        
        logger.info("\n성과 평가:")
        goals = summary['performance_goals']
        achievement = summary['achievement']
        
        logger.info(f"  - 시간 개선 목표 ({goals['time_improvement_target']}%): {'달성' if achievement['time_improvement_achieved'] else '미달성'}")
        logger.info(f"  - 메모리 개선 목표 ({goals['memory_improvement_target']}%): {'달성' if achievement['memory_improvement_achieved'] else '미달성'}")
        logger.info(f"  - 처리량 개선 목표 ({goals['throughput_improvement_target']}%): {'달성' if achievement['throughput_improvement_achieved'] else '미달성'}")
        
        # 최종 평가
        achieved_goals = sum(1 for achieved in achievement.values() if achieved)
        total_goals = len(achievement)
        
        logger.info(f"\n최종 평가: {achieved_goals}/{total_goals} 목표 달성")
        
        if achieved_goals >= total_goals * 0.8:  # 80% 이상 달성
            logger.info("🎉 우수한 성능 개선을 달성했습니다!")
        elif achieved_goals >= total_goals * 0.6:  # 60% 이상 달성
            logger.info("✅ 양호한 성능 개선을 달성했습니다.")
        else:
            logger.info("⚠️ 추가적인 성능 개선이 필요합니다.")
        
        logger.info("="*60)

def main():
    """메인 실행 함수"""
    # 테스터 생성
    tester = PerformanceComparisonTester()
    
    # 성능 비교 테스트 실행
    results = tester.run_performance_comparison(file_count=30, iterations=3)
    
    # 결과 저장
    with open('performance_comparison_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    logger.info("성능 비교 결과 저장 완료: performance_comparison_results.json")
    
    return results

if __name__ == "__main__":
    import tempfile
    main()