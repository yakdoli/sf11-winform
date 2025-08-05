"""
WinForms_Docs 병렬 처리 성능 테스트 실행 스크립트

이 스크립트는 병렬 처리가 적용된 각 모듈의 성능을 테스트하고 결과를 보고합니다.
"""

import sys
import os
import time
import logging
import json
from pathlib import Path
from typing import Dict, List, Any

# 프로젝트 루트 추가
sys.path.append(str(Path(__file__).parent))

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_data_cleaner_performance():
    """데이터 정제기 성능 테스트"""
    logger.info("데이터 정제기 성능 테스트 시작")
    
    try:
        from data_cleaner import DataCleaner
        
        # 데이터 정제기 초기화
        cleaner = DataCleaner()
        
        # 테스트용 데이터 생성
        test_files = []
        test_dir = Path("test_data_cleaner")
        test_dir.mkdir(exist_ok=True)
        
        # 테스트 파일 생성
        for i in range(10):
            test_file = test_dir / f"test_file_{i}.md"
            test_content = f"""# 테스트 문서 {i}

이것은 테스트 문서입니다.

## 섹션 1
여기에 내용이 들어갑니다.

```python
def test_function_{i}():
    print("Hello, World!")
    return i * 2
```

[D2H]이것은 D2H 관련 텍스트입니다.[/D2H]

package:[이것은 패키지 URL입니다]

| 헤더1 | 헤더2 | 헤더3 |
|-------|-------|-------|
| 데이터1 | 데이터2 | 데이터3 |
| 데이터4 | 데이터5 | 데이터6 |

TODO: 이것은 TODO 주석입니다.
FIXME: 이것은 FIXME 주석입니다.
"""
            with open(test_file, 'w', encoding='utf-8') as f:
                f.write(test_content)
            test_files.append(test_file)
        
        # 순차 처리 테스트
        start_time = time.time()
        sequential_results = cleaner.process_files(test_files)
        sequential_time = time.time() - start_time
        
        # 병렬 처리 테스트
        start_time = time.time()
        parallel_results = cleaner.process_files_parallel(test_files)
        parallel_time = time.time() - start_time
        
        # 결과 정리
        result = {
            'test_name': 'data_cleaner',
            'sequential_time': sequential_time,
            'parallel_time': parallel_time,
            'speedup_ratio': sequential_time / parallel_time if parallel_time > 0 else 0,
            'processed_files': len(parallel_results),
            'success_rate': len(parallel_results) / len(test_files) * 100
        }
        
        # 테스트 파일 정리
        for file in test_files:
            file.unlink()
        test_dir.rmdir()
        
        logger.info(f"데이터 정제기 테스트 완료: {result}")
        return result
        
    except Exception as e:
        logger.error(f"데이터 정제기 테스트 오류: {str(e)}")
        return {
            'test_name': 'data_cleaner',
            'error': str(e),
            'sequential_time': 0,
            'parallel_time': 0,
            'speedup_ratio': 0,
            'processed_files': 0,
            'success_rate': 0
        }

def test_data_normalizer_performance():
    """데이터 정규화기 성능 테스트"""
    logger.info("데이터 정규화기 성능 테스트 시작")
    
    try:
        from data_normalizer import DataNormalizer
        
        # 데이터 정규화기 초기화
        normalizer = DataNormalizer()
        
        # 테스트용 데이터 생성
        test_texts = []
        for i in range(100):
            text = f"""문서 {i} - 이것은 테스트 문서입니다.

## 카테고리: 테스트
### 서브카테고리: 데이터 정규화

이 문서는 데이터 정규화 테스트를 위한 것입니다.

```python
def test_function_{i}():
    # 이것은 테스트 함수입니다
    print(f"테스트 {i}")
    return True
```

[D2H]D2H 텍스트[/D2H]

package:[테스트 패키지]

| 테스트1 | 테스트2 | 테스트3 |
|---------|---------|---------|
| 데이터1 | 데이터2 | 데이터3 |

태그: 테스트, 데이터, 정규화
"""
            test_texts.append(text)
        
        # 순차 처리 테스트
        start_time = time.time()
        sequential_results = []
        for text in test_texts:
            try:
                normalized = normalizer.normalize_document(text)
                sequential_results.append(normalized)
            except Exception as e:
                logger.warning(f"순차 처리 오류: {str(e)}")
        sequential_time = time.time() - start_time
        
        # 병렬 처리 테스트
        start_time = time.time()
        parallel_results = normalizer.normalize_documents_parallel(test_texts)
        parallel_time = time.time() - start_time
        
        # 결과 정리
        result = {
            'test_name': 'data_normalizer',
            'sequential_time': sequential_time,
            'parallel_time': parallel_time,
            'speedup_ratio': sequential_time / parallel_time if parallel_time > 0 else 0,
            'processed_texts': len(parallel_results),
            'success_rate': len(parallel_results) / len(test_texts) * 100
        }
        
        logger.info(f"데이터 정규화기 테스트 완료: {result}")
        return result
        
    except Exception as e:
        logger.error(f"데이터 정규화기 테스트 오류: {str(e)}")
        return {
            'test_name': 'data_normalizer',
            'error': str(e),
            'sequential_time': 0,
            'parallel_time': 0,
            'speedup_ratio': 0,
            'processed_texts': 0,
            'success_rate': 0
        }

def test_deduplication_performance():
    """중복 검사 성능 테스트"""
    logger.info("중복 검사 성능 테스트 시작")
    
    try:
        from deduplication import Deduplicator
        
        # 중복 검사기 초기화
        deduplicator = Deduplicator()
        
        # 테스트용 문서 생성
        test_documents = []
        base_content = """이것은 테스트 문서입니다.

## 섹션 1
여기에 내용이 들어갑니다.

```python
def test_function():
    print("Hello, World!")
    return True
```

[D2H]이것은 D2H 관련 텍스트입니다.[/D2H]

package:[이것은 패키지 URL입니다]

| 헤더1 | 헤더2 | 헤더3 |
|-------|-------|-------|
| 데이터1 | 데이터2 | 데이터3 |
| 데이터4 | 데이터5 | 데이터6 |

태그: 테스트, 데이터, 중복검사
"""
        
        # 유사한 문서 생성 (중복 테스트용)
        for i in range(50):
            doc = {
                'id': f'doc_{i}',
                'file_path': f'test_doc_{i}.md',
                'normalized_filename': f'test_doc_{i}',
                'category': '테스트',
                'subcategory': '중복검사',
                'title': f'테스트 문서 {i}',
                'normalized_title': f'테스트 문서 {i}',
                'description': f'이것은 테스트 문서 {i}입니다.',
                'tags': ['테스트', '데이터', '중복검사'],
                'normalized_tags': ['테스트', '데이터', '중복검사'],
                'content': base_content + f'\n\n## 추가 내용 {i}\n여기에 추가 내용이 들어갑니다.',
                'normalized_content': base_content + f'\n\n## 추가 내용 {i}\n여기에 추가 내용이 들어갑니다.',
                'word_count': len(base_content.split()) + 10,
                'char_count': len(base_content) + 50,
                'language': 'ko',
                'code_snippets': [
                    {
                        'language': 'python',
                        'code': 'def test_function():\n    print("Hello, World!")\n    return True',
                        'normalized_code': 'def test_function():\n    print("Hello, World!")\n    return True',
                        'hash': 'test_hash'
                    }
                ],
                'normalized_code_snippets': [
                    {
                        'language': 'python',
                        'code': 'def test_function():\n    print("Hello, World!")\n    return True',
                        'normalized_code': 'def test_function():\n    print("Hello, World!")\n    return True',
                        'hash': 'test_hash'
                    }
                ],
                'metadata': {
                    'category': '테스트',
                    'subcategory': '중복검사',
                    'tags': ['테스트', '데이터', '중복검사']
                },
                'relationships': [],
                'quality_score': 0.8,
                'created_date': '2024-01-01T00:00:00',
                'updated_date': '2024-01-01T00:00:00'
            }
            test_documents.append(doc)
        
        # 순차 처리 테스트
        start_time = time.time()
        sequential_groups = deduplicator.find_duplicates(test_documents)
        sequential_time = time.time() - start_time
        
        # 병렬 처리 테스트
        start_time = time.time()
        parallel_groups = deduplicator.find_duplicates_parallel(test_documents)
        parallel_time = time.time() - start_time
        
        # 결과 정리
        result = {
            'test_name': 'deduplication',
            'sequential_time': sequential_time,
            'parallel_time': parallel_time,
            'speedup_ratio': sequential_time / parallel_time if parallel_time > 0 else 0,
            'processed_documents': len(parallel_groups),
            'duplicate_groups': len(parallel_groups),
            'success_rate': 100  # 중복 검사는 항상 성공
        }
        
        logger.info(f"중복 검사 테스트 완료: {result}")
        return result
        
    except Exception as e:
        logger.error(f"중복 검사 테스트 오류: {str(e)}")
        return {
            'test_name': 'deduplication',
            'error': str(e),
            'sequential_time': 0,
            'parallel_time': 0,
            'speedup_ratio': 0,
            'processed_documents': 0,
            'duplicate_groups': 0,
            'success_rate': 0
        }

def run_all_performance_tests():
    """모든 성능 테스트 실행"""
    logger.info("모든 성능 테스트 시작")
    
    test_results = []
    
    # 데이터 정제기 테스트
    cleaner_result = test_data_cleaner_performance()
    test_results.append(cleaner_result)
    
    # 데이터 정규화기 테스트
    normalizer_result = test_data_normalizer_performance()
    test_results.append(normalizer_result)
    
    # 중복 검사 테스트
    deduplication_result = test_deduplication_performance()
    test_results.append(deduplication_result)
    
    # 종합 결과 생성
    summary = {
        'test_timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'total_tests': len(test_results),
        'successful_tests': len([r for r in test_results if 'error' not in r]),
        'failed_tests': len([r for r in test_results if 'error' in r]),
        'average_speedup': sum(r.get('speedup_ratio', 0) for r in test_results) / len(test_results),
        'test_results': test_results
    }
    
    # 결과 저장
    output_dir = Path("performance_results")
    output_dir.mkdir(exist_ok=True)
    
    with open(output_dir / "performance_test_results.json", 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    # 결과 출력
    logger.info("=" * 50)
    logger.info("성능 테스트 결과 요약")
    logger.info("=" * 50)
    
    for result in test_results:
        if 'error' in result:
            logger.error(f"{result['test_name']}: 테스트 실패 - {result['error']}")
        else:
            logger.info(f"{result['test_name']}:")
            logger.info(f"  순차 처리 시간: {result['sequential_time']:.3f}초")
            logger.info(f"  병렬 처리 시간: {result['parallel_time']:.3f}초")
            logger.info(f"  속도 향상 비율: {result['speedup_ratio']:.2f}x")
            logger.info(f"  처리 항목 수: {result.get('processed_files', result.get('processed_texts', result.get('processed_documents', 0)))}")
            logger.info(f"  성공률: {result.get('success_rate', 0):.1f}%")
    
    logger.info(f"\n종합 평균 속도 향상: {summary['average_speedup']:.2f}x")
    logger.info(f"성공한 테스트: {summary['successful_tests']}/{summary['total_tests']}")
    
    return summary

if __name__ == "__main__":
    try:
        run_all_performance_tests()
    except Exception as e:
        logger.error(f"성능 테스트 실행 오류: {str(e)}")
        sys.exit(1)