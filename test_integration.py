"""
WinForms_Docs 데이터 정제 및 정규화 시스템 통합 테스트
"""

import sys
import os
sys.path.append('.')

def test_data_cleaner():
    """데이터 정제기 기능 테스트"""
    print("=== 데이터 정제기 기능 테스트 ===")
    
    try:
        from data_cleaner import DataCleaner
        cleaner = DataCleaner()
        
        # 샘플 테스트 데이터
        test_content = """::: {style="DISPLAY: none"}
[](ms-xhelp:///?Id=d2h_url_template){#d2h_url_template}
## Test Document

This is a test document with some HTML content.

```csharp
public void TestMethod()
{
    Console.WriteLine("Hello World");
}
```

Some text with special characters."""
        
        # 텍스트 정제 테스트
        cleaned_content = cleaner.clean_text_content(test_content)
        print(f"✓ 텍스트 정제 기능 테스트 성공")
        print(f"  - 원본 길이: {len(test_content)}")
        print(f"  - 정제된 길이: {len(cleaned_content)}")
        print(f"  - 정제된 내용 (첫 100자): {cleaned_content[:100]}...")
        
        # 코드 블록 추출 테스트
        cleaned_content, code_snippets = cleaner.extract_code_blocks(test_content)
        print(f"  - 추출된 코드 블록 수: {len(code_snippets)}")
        if code_snippets:
            print(f"  - 첫 번째 코드 언어: {code_snippets[0]['language']}")
            print(f"  - 첫 번째 코드 해시: {code_snippets[0]['hash'][:8]}...")
        
        return True
        
    except Exception as e:
        print(f"✗ 데이터 정제기 기능 테스트 실패: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_data_normalizer():
    """데이터 정규화 기능 테스트"""
    print("\n=== 데이터 정규화 기능 테스트 ===")
    
    try:
        from data_normalizer import DataNormalizer
        normalizer = DataNormalizer()
        
        # 샘플 문서 데이터
        test_doc = {
            'file_path': 'test/path/document.md',
            'cleaned_content': 'This is a test document content for normalization.',
            'metadata': {
                'category': '01_Getting_Started',
                'subcategory': '',
                'title': 'Test Document Title',
                'tags': ['test', 'document', 'example'],
                'description': 'This is a test description for the document.'
            },
            'code_snippets': [
                {
                    'language': 'csharp',
                    'code': 'Console.WriteLine("Hello World");',
                    'line_start': 1,
                    'line_end': 1,
                    'hash': 'test_hash_123'
                }
            ]
        }
        
        # 문서 정규화 테스트
        normalized_doc = normalizer.normalize_document(test_doc)
        if normalized_doc:
            print(f"✓ 데이터 정규화 기능 테스트 성공")
            print(f"  - 정규화된 ID: {normalized_doc.id[:8]}...")
            print(f"  - 정규화된 카테고리: {normalized_doc.category}")
            print(f"  - 정규화된 제목: {normalized_doc.normalized_title}")
            print(f"  - 정규화된 태그: {normalized_doc.normalized_tags}")
            print(f"  - 품질 점수: {normalized_doc.quality_score:.2f}")
            return True
        else:
            print("✗ 데이터 정규화 결과 없음")
            return False
            
    except Exception as e:
        print(f"✗ 데이터 정규화 기능 테스트 실패: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_deduplication():
    """중복 제거 기능 테스트"""
    print("\n=== 중복 제거 기능 테스트 ===")
    
    try:
        from deduplication import Deduplicator
        deduplicator = Deduplicator()
        
        # 샘플 문서 목록
        test_docs = [
            {
                'id': 'doc1',
                'file_path': 'doc1.md',
                'normalized_content': 'This is the first document content.',
                'normalized_filename': 'document_one',
                'metadata': {'category': 'test', 'title': 'First Document'},
                'normalized_code_snippets': [],
                'updated_date': '2023-01-01'
            },
            {
                'id': 'doc2',
                'file_path': 'doc2.md',
                'normalized_content': 'This is the first document content.',
                'normalized_filename': 'document_two',
                'metadata': {'category': 'test', 'title': 'Second Document'},
                'normalized_code_snippets': [],
                'updated_date': '2023-01-02'
            }
        ]
        
        # 중복 검사 테스트
        duplicate_groups = deduplicator.find_duplicates(test_docs)
        print(f"✓ 중복 제거 기능 테스트 성공")
        print(f"  - 중복 그룹 수: {len(duplicate_groups)}")
        if duplicate_groups:
            print(f"  - 첫 번째 그룹 유사도: {duplicate_groups[0].similarity_score:.3f}")
            print(f"  - 첫 번째 그룹 문서 수: {len(duplicate_groups[0].documents)}")
        return True
        
    except Exception as e:
        print(f"✗ 중복 제거 기능 테스트 실패: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_config():
    """설정 모듈 테스트"""
    print("\n=== 설정 모듈 테스트 ===")
    
    try:
        import config
        print(f"✓ 설정 모듈 임포트 성공")
        print(f"  - WinForms_Docs 경로: {config.WINFORMS_DOCS_DIR}")
        print(f"  - 출력 디렉토리: {config.OUTPUT_DIR}")
        print(f"  - 백업 디렉토리: {config.BACKUP_DIR}")
        print(f"  - 카테고리 매핑: {len(config.CATEGORY_MAPPING)}개")
        print(f"  - 서브 카테고리 매핑: {len(config.SUBCATEGORY_MAPPING)}개")
        return True
        
    except Exception as e:
        print(f"✗ 설정 모듈 테스트 실패: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """메인 테스트 함수"""
    print("WinForms_Docs 데이터 정제 및 정규화 시스템 통합 테스트")
    print("=" * 60)
    
    # 테스트 실행
    tests = [
        ("설정 모듈", test_config),
        ("데이터 정제기", test_data_cleaner),
        ("데이터 정규화", test_data_normalizer),
        ("중복 제거", test_deduplication)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"✗ {test_name} 테스트 실행 중 오류 발생: {e}")
            results.append((test_name, False))
    
    # 테스트 결과 요약
    print("\n" + "=" * 60)
    print("테스트 결과 요약")
    print("=" * 60)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "PASS" if result else "FAIL"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\n통계: {passed}/{total} 테스트 성공 ({passed/total*100:.1f}%)")
    
    if passed == total:
        print("🎉 모든 테스트를 통과했습니다!")
        return True
    else:
        print("⚠️ 일부 테스트가 실패했습니다.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)