"""
WinForms_Docs 중복 제거 모듈
"""

import json
import logging
import hashlib
import re
from pathlib import Path
from typing import Dict, List, Set, Optional, Any, Tuple, Union
from dataclasses import dataclass, asdict
from datetime import datetime
from collections import defaultdict, Counter
import math
import difflib
from concurrent.futures import ThreadPoolExecutor, as_completed

from config import (
    OUTPUT_DIR, DEDUPLICATION_CONFIG, PROCESSING_OPTIONS
)

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class DuplicateGroup:
    """중복 그룹 데이터 클래스"""
    group_id: str
    documents: List[Dict[str, Any]]
    similarity_score: float
    is_exact_duplicate: bool
    duplicate_type: str  # 'content', 'filename', 'code_snippet', 'metadata'
    created_date: str

@dataclass
class DuplicateResult:
    """중복 검사 결과 데이터 클래스"""
    document_id: str
    file_path: str
    is_duplicate: bool
    duplicate_group_id: Optional[str]
    similarity_score: float
    duplicate_type: str
    confidence: float

@dataclass
class DeduplicationStats:
    """중복 제거 통계 데이터 클래스"""
    total_documents: int = 0
    duplicate_documents: int = 0
    unique_documents: int = 0
    exact_duplicates: int = 0
    content_duplicates: int = 0
    filename_duplicates: int = 0
    code_duplicates: int = 0
    metadata_duplicates: int = 0
    duplicate_groups: int = 0
    total_similarity_score: float = 0.0
    average_similarity: float = 0.0
    processing_time: float = 0.0

class ContentComparator:
    """내용 비교 클래스"""
    
    def __init__(self, threshold: float = 0.85):
        self.threshold = threshold
        self.stop_words = set([
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
            'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 
            'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should',
            'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they'
        ])
    
    def calculate_similarity(self, text1: str, text2: str) -> float:
        """두 텍스트 간의 유사도 계산"""
        if not text1 or not text2:
            return 0.0
        
        # 토큰화
        tokens1 = self._tokenize(text1)
        tokens2 = self._tokenize(text2)
        
        if not tokens1 or not tokens2:
            return 0.0
        
        # 자카드 유사도 계산
        set1 = set(tokens1)
        set2 = set(tokens2)
        
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        
        if union == 0:
            return 0.0
        
        jaccard_similarity = intersection / union
        
        # 코사인 유사도 계산
        cosine_similarity = self._calculate_cosine_similarity(tokens1, tokens2)
        
        # 가중 평균
        final_similarity = 0.6 * jaccard_similarity + 0.4 * cosine_similarity
        
        return min(1.0, final_similarity)
    
    def _tokenize(self, text: str) -> List[str]:
        """텍스트 토큰화"""
        # 소문자 변환
        text = text.lower()
        
        # 특수 문자 제거
        text = re.sub(r'[^\w\s가-힣]', ' ', text)
        
        # 토큰 분리
        tokens = text.split()
        
        # 불용어 제거
        tokens = [token for token in tokens if token not in self.stop_words and len(token) > 2]
        
        return tokens
    
    def _calculate_cosine_similarity(self, tokens1: List[str], tokens2: List[str]) -> float:
        """코사인 유사도 계산"""
        # 단어 빈도 계산
        word_counts1 = Counter(tokens1)
        word_counts2 = Counter(tokens2)
        
        # 모든 고유 단어
        all_words = set(word_counts1.keys()).union(set(word_counts2.keys()))
        
        # 벡터 생성
        vector1 = [word_counts1.get(word, 0) for word in all_words]
        vector2 = [word_counts2.get(word, 0) for word in all_words]
        
        # 벡터 크기 계산
        magnitude1 = math.sqrt(sum(x * x for x in vector1))
        magnitude2 = math.sqrt(sum(x * x for x in vector2))
        
        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0
        
        # 내적 계산
        dot_product = sum(x * y for x, y in zip(vector1, vector2))
        
        # 코사인 유사도
        cosine_similarity = dot_product / (magnitude1 * magnitude2)
        
        return cosine_similarity
    
    def is_exact_duplicate(self, text1: str, text2: str) -> bool:
        """완전 중복 확인"""
        if not text1 or not text2:
            return False
        
        # 정규화 후 비교
        normalized1 = self._normalize_text(text1)
        normalized2 = self._normalize_text(text2)
        
        return normalized1 == normalized2
    
    def _normalize_text(self, text: str) -> str:
        """텍스트 정규화"""
        # 유니코드 정규화
        text = text.lower()
        
        # 여러 공백 제거
        text = re.sub(r'\s+', ' ', text)
        
        # 특수 문자 제거
        text = re.sub(r'[^\w\s가-힣]', ' ', text)
        
        # 앞뒤 공백 제거
        text = text.strip()
        
        return text

class CodeComparator:
    """코드 비교 클래스"""
    
    def __init__(self, threshold: float = 0.95):
        self.threshold = threshold
    
    def calculate_code_similarity(self, code1: str, code2: str) -> float:
        """코드 유사도 계산"""
        if not code1 or not code2:
            return 0.0
        
        # 정규화된 코드 비교
        normalized1 = self._normalize_code(code1)
        normalized2 = self._normalize_code(code2)
        
        # 완전 중복 확인
        if normalized1 == normalized2:
            return 1.0
        
        # 시퀀스 매칭을 이용한 유사도 계산
        similarity = self._sequence_similarity(normalized1, normalized2)
        
        return similarity
    
    def _normalize_code(self, code: str) -> str:
        """코드 정규화"""
        if not code:
            return ''
        
        # 줄바꿈 정리
        code = re.sub(r'\r\n', '\n', code)
        code = re.sub(r'\n+', '\n', code)
        
        # 주석 제거
        code = re.sub(r'//.*?$|/\*.*?\*/', '', code, flags=re.MULTILINE | re.DOTALL)
        
        # 불필요한 공백 정리
        lines = code.split('\n')
        normalized_lines = []
        
        for line in lines:
            line = line.rstrip()
            if line:
                normalized_lines.append(line)
        
        return '\n'.join(normalized_lines)
    
    def _sequence_similarity(self, text1: str, text2: str) -> float:
        """시퀀스 유사도 계산"""
        # difflib를 이용한 시퀀스 매칭
        matcher = difflib.SequenceMatcher(None, text1, text2)
        similarity = matcher.ratio()
        
        return similarity

class FilenameComparator:
    """파일명 비교 클래스"""
    
    def __init__(self, threshold: float = 0.9):
        self.threshold = threshold
    
    def calculate_filename_similarity(self, filename1: str, filename2: str) -> float:
        """파일명 유사도 계산"""
        if not filename1 or not filename2:
            return 0.0
        
        # 파일명 정규화
        normalized1 = self._normalize_filename(filename1)
        normalized2 = self._normalize_filename(filename2)
        
        # 시퀀스 유사도 계산
        similarity = difflib.SequenceMatcher(None, normalized1, normalized2).ratio()
        
        return similarity
    
    def _normalize_filename(self, filename: str) -> str:
        """파일명 정규화"""
        # 확장자 제거
        name = Path(filename).stem
        
        # 소문자 변환
        name = name.lower()
        
        # 특수 문자 제거
        name = re.sub(r'[^\w\s가-힣]', ' ', name)
        
        # 여러 공백 제거
        name = re.sub(r'\s+', ' ', name)
        
        # 앞뒤 공백 제거
        name = name.strip()
        
        return name

class MetadataComparator:
    """메타데이터 비교 클래스"""
    
    def __init__(self, threshold: float = 0.8):
        self.threshold = threshold
    
    def calculate_metadata_similarity(self, metadata1: Dict[str, Any], metadata2: Dict[str, Any]) -> float:
        """메타데이터 유사도 계산"""
        if not metadata1 or not metadata2:
            return 0.0
        
        similarity_score = 0.0
        max_score = 0.0
        
        # 카테고리 비교
        if 'category' in metadata1 and 'category' in metadata2:
            if metadata1['category'] == metadata2['category']:
                similarity_score += 1.0
            max_score += 1.0
        
        # 서브 카테고리 비교
        if 'subcategory' in metadata1 and 'subcategory' in metadata2:
            if metadata1['subcategory'] == metadata2['subcategory']:
                similarity_score += 0.5
            max_score += 0.5
        
        # 태그 비교
        if 'tags' in metadata1 and 'tags' in metadata2:
            tags1 = set(metadata1['tags'])
            tags2 = set(metadata2['tags'])
            
            if tags1 and tags2:
                intersection = len(tags1.intersection(tags2))
                union = len(tags1.union(tags2))
                
                if union > 0:
                    tag_similarity = intersection / union
                    similarity_score += tag_similarity
                    max_score += 1.0
        
        # 제목 비교
        if 'title' in metadata1 and 'title' in metadata2:
            title_similarity = difflib.SequenceMatcher(
                None, metadata1['title'], metadata2['title']
            ).ratio()
            similarity_score += title_similarity * 0.5
            max_score += 0.5
        
        if max_score == 0:
            return 0.0
        
        return similarity_score / max_score

class Deduplicator:
    """중복 제거 클래스"""
    
    def __init__(self):
        self.content_comparator = ContentComparator(DEDUPLICATION_CONFIG['similarity_threshold'])
        self.code_comparator = CodeComparator(DEDUPLICATION_CONFIG['code_similarity_threshold'])
        self.filename_comparator = FilenameComparator()
        self.metadata_comparator = MetadataComparator()
        
        self.stats = DeduplicationStats()
        self.duplicate_groups: List[DuplicateGroup] = []
        self.duplicate_results: List[DuplicateResult] = []
        
    def find_duplicates(self, documents: List[Dict[str, Any]]) -> List[DuplicateGroup]:
        """중복 문서 찾기"""
        logger.info(f"중복 검사 시작: {len(documents)}개 문서")
        
        start_time = datetime.now()
        self.stats.total_documents = len(documents)
        
        # 중복 그룹 저장
        duplicate_groups = []
        processed_pairs = set()
        
        # 모든 문서 쌍 비교
        for i in range(len(documents)):
            for j in range(i + 1, len(documents)):
                doc1 = documents[i]
                doc2 = documents[j]
                
                # 이미 처리된 쌍 건너뛰기
                pair_key = tuple(sorted([doc1.get('id', ''), doc2.get('id', '')]))
                if pair_key in processed_pairs:
                    continue
                
                processed_pairs.add(pair_key)
                
                # 중복 유형별 비교
                duplicate_info = self._compare_documents(doc1, doc2)
                
                if duplicate_info['is_duplicate']:
                    # 중복 그룹에 추가
                    self._add_to_duplicate_group(duplicate_groups, doc1, doc2, duplicate_info)
        
        # 중복 그룹 후처리
        duplicate_groups = self._post_process_duplicate_groups(duplicate_groups)
        
        self.duplicate_groups = duplicate_groups
        self.stats.duplicate_groups = len(duplicate_groups)
        self.stats.processing_time = (datetime.now() - start_time).total_seconds()
        
        logger.info(f"중복 검사 완료: {len(duplicate_groups)}개 중복 그룹 발견")
        
        return duplicate_groups
    
    def _compare_documents(self, doc1: Dict[str, Any], doc2: Dict[str, Any]) -> Dict[str, Any]:
        """두 문서 비교"""
        result = {
            'is_duplicate': False,
            'similarity_score': 0.0,
            'duplicate_type': '',
            'confidence': 0.0
        }
        
        max_similarity = 0.0
        best_type = ''
        
        # 1. 내용 비교
        content1 = doc1.get('normalized_content', '')
        content2 = doc2.get('normalized_content', '')
        
        if content1 and content2:
            content_similarity = self.content_comparator.calculate_similarity(content1, content2)
            
            # 완전 중복 확인
            if self.content_comparator.is_exact_duplicate(content1, content2):
                result.update({
                    'is_duplicate': True,
                    'similarity_score': 1.0,
                    'duplicate_type': 'content',
                    'confidence': 1.0
                })
                return result
            
            if content_similarity > max_similarity:
                max_similarity = content_similarity
                best_type = 'content'
        
        # 2. 코드 스니펫 비교
        code_snippets1 = doc1.get('normalized_code_snippets', [])
        code_snippets2 = doc2.get('normalized_code_snippets', [])
        
        if code_snippets1 and code_snippets2:
            code_similarity = self._compare_code_snippets(code_snippets1, code_snippets2)
            
            if code_similarity > max_similarity:
                max_similarity = code_similarity
                best_type = 'code'
        
        # 3. 파일명 비교
        filename1 = doc1.get('normalized_filename', '')
        filename2 = doc2.get('normalized_filename', '')
        
        if filename1 and filename2:
            filename_similarity = self.filename_comparator.calculate_filename_similarity(filename1, filename2)
            
            if filename_similarity > max_similarity:
                max_similarity = filename_similarity
                best_type = 'filename'
        
        # 4. 메타데이터 비교
        metadata1 = doc1.get('metadata', {})
        metadata2 = doc2.get('metadata', {})
        
        if metadata1 and metadata2:
            metadata_similarity = self.metadata_comparator.calculate_metadata_similarity(metadata1, metadata2)
            
            if metadata_similarity > max_similarity:
                max_similarity = metadata_similarity
                best_type = 'metadata'
        
        # 임계값 확인
        if max_similarity >= DEDUPLICATION_CONFIG['similarity_threshold']:
            result.update({
                'is_duplicate': True,
                'similarity_score': max_similarity,
                'duplicate_type': best_type,
                'confidence': max_similarity
            })
        
        return result
    
    def _compare_code_snippets(self, snippets1: List[Dict[str, Any]], snippets2: List[Dict[str, Any]]) -> float:
        """코드 스니펫 비교"""
        if not snippets1 or not snippets2:
            return 0.0
        
        max_similarity = 0.0
        
        # 모든 코드 조합 비교
        for snippet1 in snippets1:
            for snippet2 in snippets2:
                code1 = snippet1.get('normalized_code', '')
                code2 = snippet2.get('normalized_code', '')
                
                if code1 and code2:
                    similarity = self.code_comparator.calculate_code_similarity(code1, code2)
                    
                    if similarity > max_similarity:
                        max_similarity = similarity
        
        return max_similarity
    
    def _add_to_duplicate_group(self, duplicate_groups: List[DuplicateGroup], doc1: Dict[str, Any], 
                               doc2: Dict[str, Any], duplicate_info: Dict[str, Any]):
        """중복 그룹에 문서 추가"""
        # 기존 그룹에서 일치하는 그룹 찾기
        for group in duplicate_groups:
            if doc1.get('id') in [doc['id'] for doc in group.documents]:
                group.documents.append(doc2)
                group.similarity_score = max(group.similarity_score, duplicate_info['similarity_score'])
                return
            elif doc2.get('id') in [doc['id'] for doc in group.documents]:
                group.documents.append(doc1)
                group.similarity_score = max(group.similarity_score, duplicate_info['similarity_score'])
                return
        
        # 새 그룹 생성
        new_group = DuplicateGroup(
            group_id=f"dup_{len(duplicate_groups) + 1}",
            documents=[doc1, doc2],
            similarity_score=duplicate_info['similarity_score'],
            is_exact_duplicate=duplicate_info['similarity_score'] >= 0.99,
            duplicate_type=duplicate_info['duplicate_type'],
            created_date=datetime.now().isoformat()
        )
        duplicate_groups.append(new_group)
    
    def _post_process_duplicate_groups(self, duplicate_groups: List[DuplicateGroup]) -> List[DuplicateGroup]:
        """중복 그룹 후처리"""
        # 그룹 병합 (교집합이 있는 경우)
        merged_groups = []
        used_indices = set()
        
        for i, group1 in enumerate(duplicate_groups):
            if i in used_indices:
                continue
            
            merged_group = group1
            used_indices.add(i)
            
            for j, group2 in enumerate(duplicate_groups[i+1:], i+1):
                if j in used_indices:
                    continue
                
                # 교집합 확인
                ids1 = set(doc.get('id') for doc in merged_group.documents)
                ids2 = set(doc.get('id') for doc in group2.documents)
                
                if ids1.intersection(ids2):
                    # 그룹 병합
                    merged_group.documents.extend(group2.documents)
                    merged_group.similarity_score = max(merged_group.similarity_score, group2.similarity_score)
                    used_indices.add(j)
            
            merged_groups.append(merged_group)
        
        # 그룹 크기별 정렬
        merged_groups.sort(key=lambda x: len(x.documents), reverse=True)
        
        return merged_groups
    
    def resolve_duplicates(self, duplicate_groups: List[DuplicateGroup], 
                          strategy: str = 'keep_newest') -> List[Dict[str, Any]]:
        """중복 해결"""
        logger.info(f"중복 해결 시작: {len(duplicate_groups)}개 그룹")
        
        unique_documents = []
        removed_documents = []
        
        for group in duplicate_groups:
            if len(group.documents) <= 1:
                continue
            
            # 중복 그룹에서 유일한 문서 선택
            selected_doc = self._select_document_from_group(group, strategy)
            
            # 선택된 문서는 유지
            unique_documents.append(selected_doc)
            
            # 나머지 문서는 제거 목록에 추가
            for doc in group.documents:
                if doc.get('id') != selected_doc.get('id'):
                    removed_documents.append({
                        'document_id': doc.get('id'),
                        'file_path': doc.get('file_path'),
                        'reason': f'Duplicate of {selected_doc.get("id")} (type: {group.duplicate_type})',
                        'similarity_score': group.similarity_score
                    })
        
        # 중복이 아닌 문서 추가
        all_doc_ids = set()
        for group in duplicate_groups:
            all_doc_ids.update(doc.get('id') for doc in group.documents)
        
        # 여기서는 이미 처리된 문서들을 제외하고 추가하는 로직이 필요합니다
        # 실제 구현에서는 입력 문서 목록과 비교하여 중복이 아닌 문서를 찾아야 합니다
        
        self.stats.duplicate_documents = len(removed_documents)
        self.stats.unique_documents = len(unique_documents)
        
        logger.info(f"중복 해결 완료: {len(removed_documents)}개 중복 문서 제거")
        
        return unique_documents
    
    def _select_document_from_group(self, group: DuplicateGroup, strategy: str) -> Dict[str, Any]:
        """중복 그룹에서 문서 선택"""
        documents = group.documents
        
        if strategy == 'keep_newest':
            # 수정 날짜가 최신인 문서 선택
            return max(documents, key=lambda x: x.get('updated_date', ''))
        elif strategy == 'keep_longest':
            # 내용이 가장 긴 문서 선택
            return max(documents, key=lambda x: len(x.get('normalized_content', '')))
        elif strategy == 'keep_highest_quality':
            # 품질 점수가 가장 높은 문서 선택
            return max(documents, key=lambda x: x.get('quality_score', 0))
        else:
            # 기본: 첫 번째 문서 선택
            return documents[0]
    
    def generate_deduplication_report(self, output_dir: Path = None):
        """중복 제거 보고서 생성"""
        if output_dir is None:
            output_dir = OUTPUT_DIR / 'reports'
        
        report_dir = output_dir / 'deduplication_reports'
        report_dir.mkdir(parents=True, exist_ok=True)
        
        # 텍스트 보고서
        report_content = f"""
WinForms_Docs 중복 제거 보고서
=============================

중복 제거 일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

기본 통계:
- 총 문서 수: {self.stats.total_documents}
- 중복 문서 수: {self.stats.duplicate_documents}
- 유일 문서 수: {self.stats.unique_documents}
- 중복 그룹 수: {self.stats.duplicate_groups}
- 중복 제거율: {(self.stats.duplicate_documents / max(self.stats.total_documents, 1) * 100):.1f}%

중복 유형별 통계:
- 완전 중복: {self.stats.exact_duplicates}개
- 내용 중복: {self.stats.content_duplicates}개
- 파일명 중복: {self.stats.filename_duplicates}개
- 코드 중복: {self.stats.code_duplicates}개
- 메타데이터 중복: {self.stats.metadata_duplicates}개

유사도 통계:
- 평균 유사도: {self.stats.average_similarity:.3f}
- 최대 유사도: {max([g.similarity_score for g in self.duplicate_groups], default=0):.3f}
- 최소 유사도: {min([g.similarity_score for g in self.duplicate_groups], default=0):.3f}

중복 그룹 상세 정보:
"""
        
        for i, group in enumerate(self.duplicate_groups[:20]):  # 상위 20개 그룹만 표시
            report_content += f"""
그룹 {i+1}: {group.group_id}
- 문서 수: {len(group.documents)}
- 유사도: {group.similarity_score:.3f}
- 중복 유형: {group.duplicate_type}
- 완전 중복: {'예' if group.is_exact_duplicate else '아니오'}
"""
            
            for doc in group.documents:
                report_content += f"  - {doc.get('file_path', 'Unknown')}\n"
        
        # 보고서 파일 저장
        with open(report_dir / 'deduplication_report.txt', 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        # 중복 그룹 정보 JSON 저장
        duplicate_groups_data = [asdict(group) for group in self.duplicate_groups]
        with open(report_dir / 'duplicate_groups.json', 'w', encoding='utf-8') as f:
            json.dump(duplicate_groups_data, f, ensure_ascii=False, indent=2)
        
        logger.info(f"중복 제거 보고서 생성 완료: {report_dir}")

def main():
    """메인 실행 함수"""
    logger.info("WinForms_Docs 중복 제거 시작")
    
    # 중복 제거기 초기화
    deduplicator = Deduplicator()
    
    # 정규화된 데이터 파일 경로
    input_file = OUTPUT_DIR / 'normalized_data' / 'normalized_documents.json'
    
    if not input_file.exists():
        logger.error(f"입력 파일을 찾을 수 없습니다: {input_file}")
        return
    
    # 데이터 읽기
    with open(input_file, 'r', encoding='utf-8') as f:
        documents = json.load(f)
    
    # 중복 검사
    duplicate_groups = deduplicator.find_duplicates(documents)
    
    # 중복 해결
    unique_documents = deduplicator.resolve_duplicates(duplicate_groups)
    
    # 결과 저장
    output_dir = OUTPUT_DIR / 'deduplicated_data'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    with open(output_dir / 'unique_documents.json', 'w', encoding='utf-8') as f:
        json.dump(unique_documents, f, ensure_ascii=False, indent=2)
    
    # 중복 제거 보고서 생성
    deduplicator.generate_deduplication_report()
    
    # 최종 로그
    logger.info(f"중복 제거 완료. 유일 문서: {deduplicator.stats.unique_documents}, 중복 문서: {deduplicator.stats.duplicate_documents}")

if __name__ == "__main__":
    main()