#!/usr/bin/env python3
"""
개선된 Unsloth/Alpaca 형식 데이터셋 생성 스크립트
- 코드 스니펫/자연어 지침 구분 개선
- 데이터셋 품질 향상
- 데이터 구조 최적화
"""

import json
import yaml
import re
import os
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import unicodedata
import difflib
import string
from collections import Counter
import unicodedata

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/improved_dataset_creation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class ImprovedDatasetConfig:
    """개선된 데이터셋 생성 설정"""
    input_dir: str = "WinForms_Docs_structured"
    output_dir: str = "unsloth_alpaca_datasets"
    max_workers: int = 4
    min_content_length: int = 50
    max_content_length: int = 8192
    deduplication_threshold: float = 0.95
    code_block_threshold: int = 5  # 코드 블록으로 간주할 최소 줄 수
    
    # 카테고리 매핑
    category_mapping = {
        '01_Getting_Started': 'getting-started',
        '02_Concepts': 'concepts', 
        '03_Data_Binding': 'data-binding',
        '04_Controls': 'controls',
        '99_Uncategorized': 'uncategorized'
    }
    
    # 서브 카테고리 매핑
    subcategory_mapping = {
        'Chart': 'chart',
        'Diagram': 'diagram',
        'Editors': 'editors', 
        'Gauge': 'gauge',
        'Grid': 'grid',
        'Ribbon': 'ribbon'
    }
    
    # 코드 언어 식별을 위한 키워드
    code_language_keywords = {
        'csharp': ['c#', 'csharp', 'cs', '.cs'],
        'vb': ['vb.net', 'visual basic', 'vb', '.vb'],
        'xml': ['xml', '.xml'],
        'html': ['html', '.html'],
        'css': ['css', '.css'],
        'javascript': ['javascript', 'js', '.js'],
        'python': ['python', 'py', '.py'],
        'sql': ['sql', '.sql'],
        'json': ['json', '.json'],
        'markdown': ['markdown', 'md', '.md']
    }

@dataclass
class ImprovedDatasetItem:
    """개선된 데이터셋 항목"""
    instruction: str
    input: str
    output: str
    text: str
    category: str
    subcategory: str
    difficulty: str = "medium"
    language: str = "ko"
    metadata: Dict[str, Any] = None
    code_blocks: List[Dict[str, Any]] = None
    description: str = ""
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}
        if self.code_blocks is None:
            self.code_blocks = []

class ImprovedDatasetGenerator:
    """개선된 데이터셋 생성기"""
    
    def __init__(self, config: ImprovedDatasetConfig):
        self.config = config
        self.seen_hashes = set()
        self.content_similarity_cache = {}
        self.stats = {
            'total_files': 0,
            'processed_files': 0,
            'skipped_files': 0,
            'total_items': 0,
            'duplicate_items': 0,
            'code_block_items': 0,
            'category_counts': {},
            'subcategory_counts': {},
            'quality_issues': []
        }
        
        # 출력 디렉토리 생성
        Path(self.config.output_dir).mkdir(parents=True, exist_ok=True)
        Path("logs").mkdir(parents=True, exist_ok=True)
    
    def extract_yaml_frontmatter(self, content: str) -> Dict[str, Any]:
        """YAML 프론트매터 추출"""
        if not content.strip().startswith('---'):
            return {}
        
        try:
            frontmatter_end = content.find('---', 3)
            if frontmatter_end == -1:
                return {}
            
            frontmatter_text = content[3:frontmatter_end].strip()
            # YAML 파싱 대신 간단한 키-값 추출
            frontmatter = {}
            for line in frontmatter_text.split('\n'):
                line = line.strip()
                if ':' in line and not line.startswith('#'):
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip().strip('"\'')
                    frontmatter[key] = value
            return frontmatter
        except Exception as e:
            logger.warning(f"YAML 파싱 오류: {e}")
            return {}
    
    def clean_content(self, content: str) -> str:
        """콘텐츠 정제"""
        # YAML 프론트매터 제거
        content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
        
        # 여러 공백 줄바꿈 정리
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        # 양쪽 공백 제거
        content = content.strip()
        
        return content
    
    def extract_code_blocks(self, content: str) -> Tuple[List[Dict[str, Any]], str]:
        """코드 블록 추출 및 설명 분리"""
        code_blocks = []
        remaining_content = content
        
        # 코드 블록 패턴 매칭
        code_pattern = r'```(\w+)?\s*\n(.*?)```'
        matches = re.findall(code_pattern, content, re.DOTALL)
        
        for language, code in matches:
            # 코드 블록 정보 저장
            code_info = {
                'language': language or 'unknown',
                'code': code.strip(),
                'line_count': len(code.split('\n')),
                'is_complete': self._is_complete_code_block(code)
            }
            code_blocks.append(code_info)
            
            # 원본 내용에서 코드 블록 제거
            remaining_content = re.sub(code_pattern, '', remaining_content, flags=re.DOTALL, count=1)
        
        # 설명 분리
        description = self._extract_description(remaining_content)
        
        return code_blocks, description
    
    def _is_complete_code_block(self, code: str) -> bool:
        """코드 블록의 완전성 검사"""
        lines = code.split('\n')
        if len(lines) < 2:
            return False
        
        # 클래스, 메서드, 함수 등의 구조적 요소 확인
        first_line = lines[0].strip()
        last_line = lines[-1].strip()
        
        # 구조적 요소가 있는지 확인
        structural_patterns = [
            r'class\s+\w+',  # 클래스 정의
            r'def\s+\w+',   # 함수 정의
            r'namespace\s+\w+',  # 네임스페이스
            r'public\s+class', r'private\s+class',  # 접근자 있는 클래스
            r'interface\s+\w+',  # 인터페이스
            r'struct\s+\w+',  # 구조체
        ]
        
        for pattern in structural_patterns:
            if re.search(pattern, code, re.IGNORECASE):
                return True
        
        return len(lines) >= self.config.code_block_threshold
    
    def _extract_description(self, content: str) -> str:
        """설명 텍스트 추출"""
        # 헤더 제거
        content = re.sub(r'^#+\s.*$', '', content, flags=re.MULTILINE)
        
        # 코드 블록 잔여물 제거
        content = re.sub(r'`[^`]*`', '', content)
        
        # 여러 공백 줄바꿈 정리
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        # 양쪽 공백 제거
        content = content.strip()
        
        return content
    
    def generate_instruction_output(self, content: str, title: str, category: str, 
                                   code_blocks: List[Dict[str, Any]], description: str) -> tuple[str, str]:
        """개선된 instruction과 output 생성"""
        content = self.clean_content(content)
        
        if len(content) < self.config.min_content_length:
            return "", ""
        
        # 코드 블록이 있는 경우 instruction 생성
        if code_blocks:
            self.stats['code_block_items'] += 1
            if category == 'getting-started':
                instruction = f"WinForms {title}에 대한 설치 및 시작 가이드를 제공해주세요. 코드 예시를 포함해주세요."
            elif category == 'concepts':
                instruction = f"WinForms {title}의 개념과 주요 기능에 대해 설명해주세요. 관련 코드 예시를 제공해주세요."
            elif category == 'data-binding':
                instruction = f"WinForms {title}의 데이터 바인딩 방법과 사용법을 설명해주세요. 코드 예시를 포함해주세요."
            elif category == 'controls':
                instruction = f"WinForms {title} 컨트롤의 사용 방법과 예제를 제공해주세요. 코드 예시를 포함해주세요."
            else:
                instruction = f"WinForms {title}에 대해 설명해주세요. 코드 예시를 포함해주세요."
        else:
            # 코드 블록이 없는 경우 기존 instruction 생성
            if category == 'getting-started':
                instruction = f"WinForms {title}에 대한 설치 및 시작 가이드를 제공해주세요."
            elif category == 'concepts':
                instruction = f"WinForms {title}의 개념과 주요 기능에 대해 설명해주세요."
            elif category == 'data-binding':
                instruction = f"WinForms {title}의 데이터 바인딩 방법과 사용법을 설명해주세요."
            elif category == 'controls':
                instruction = f"WinForms {title} 컨트롤의 사용 방법과 예제를 제공해주세요."
            else:
                instruction = f"WinForms {title}에 대해 설명해주세요."
        
        # 개선된 output 생성
        output_parts = []
        
        # 설명 부분 추가
        if description:
            output_parts.append(description)
        
        # 코드 블록 추가
        if code_blocks:
            output_parts.append("\n## 코드 예시\n")
            for i, code_block in enumerate(code_blocks, 1):
                output_parts.append(f"### 예제 {i}\n")
                output_parts.append(f"```{code_block['language']}\n")
                output_parts.append(code_block['code'])
                output_parts.append("\n```\n")
        
        # 내용이 너무 길면 자르기
        output = "\n".join(output_parts)
        if len(output) > self.config.max_content_length:
            output = output[:self.config.max_content_length] + "... [내용이 길어서 잘렸습니다]"
        
        return instruction, output
    
    def get_content_hash(self, instruction: str, output: str) -> str:
        """내용 해시 생성 (중복 검사용)"""
        content = f"{instruction}\n{output}"
        return hashlib.md5(content.encode('utf-8')).hexdigest()
    
    def is_similar_content(self, content1: str, content2: str) -> bool:
        """유사한 내용 판단"""
        # 정규화
        content1 = self.normalize_content(content1)
        content2 = self.normalize_content(content2)
        
        # 해시 기반 빠른 검사
        hash1 = hashlib.md5(content1.encode('utf-8')).hexdigest()
        hash2 = hashlib.md5(content2.encode('utf-8')).hexdigest()
        
        if hash1 == hash2:
            return True
        
        # 유사도 계산
        similarity = difflib.SequenceMatcher(None, content1, content2).ratio()
        return similarity >= self.config.deduplication_threshold
    
    def normalize_content(self, content: str) -> str:
        """내용 정규화"""
        # 소문자 변환
        content = content.lower()
        
        # 구두점 제거
        content = content.translate(str.maketrans('', '', string.punctuation))
        
        # 여러 공백 제거
        content = re.sub(r'\s+', ' ', content)
        
        # 양쪽 공백 제거
        content = content.strip()
        
        return content
    
    def categorize_content(self, file_path: str, content: str) -> tuple[str, str]:
        """카테고리 분류"""
        path_parts = Path(file_path).parts
        
        # 메인 카테고리 확인
        main_category = "uncategorized"
        for part in path_parts:
            if part in self.config.category_mapping:
                main_category = self.config.category_mapping[part]
                break
        
        # 서브 카테고리 확인
        sub_category = ""
        for part in path_parts:
            if part in self.config.subcategory_mapping:
                sub_category = self.config.subcategory_mapping[part]
                break
        
        # 내용 기반 추가 분류
        content_lower = content.lower()
        if any(keyword in content_lower for keyword in ['install', 'setup', 'deployment', 'getting started']):
            main_category = "getting-started"
        elif any(keyword in content_lower for keyword in ['concept', 'feature', 'overview', 'introduction']):
            main_category = "concepts"
        elif any(keyword in content_lower for keyword in ['bind', 'data', 'source', 'databinding']):
            main_category = "data-binding"
        elif any(keyword in content_lower for keyword in ['control', 'component', 'widget', 'user interface']):
            main_category = "controls"
        
        return main_category, sub_category
    
    def detect_code_language(self, code: str) -> str:
        """코드 언어 감지"""
        code_lower = code.lower()
        
        # 키워드 기반 언어 감지
        for language, keywords in self.config.code_language_keywords.items():
            if any(keyword in code_lower for keyword in keywords):
                return language
        
        # 파일 확장자 기반 언어 감지
        if code_lower.startswith('<') and code_lower.endswith('>'):
            return 'xml'
        elif code_lower.startswith('{') and code_lower.endswith('}'):
            return 'json'
        elif '.' in code_lower and '@' in code_lower:
            return 'csharp'
        elif 'public class' in code_lower or 'private class' in code_lower:
            return 'csharp'
        elif 'function' in code_lower or 'def ' in code_lower:
            return 'python'
        
        return 'unknown'
    
    def process_file(self, file_path: Path) -> Optional[List[Dict[str, Any]]]:
        """개별 파일 처리"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # YAML 프론트매터 추출
            frontmatter = self.extract_yaml_frontmatter(content)
            title = frontmatter.get('title', file_path.stem)
            
            # 실제 콘텐츠 추출
            main_content = self.clean_content(content)
            
            if len(main_content) < self.config.min_content_length:
                self.stats['skipped_files'] += 1
                return None
            
            # 코드 블록 추출
            code_blocks, description = self.extract_code_blocks(main_content)
            
            # 카테고리 분류
            category, subcategory = self.categorize_content(str(file_path), main_content)
            
            # instruction과 output 생성
            instruction, output = self.generate_instruction_output(
                main_content, title, category, code_blocks, description
            )
            
            if not instruction or not output:
                self.stats['skipped_files'] += 1
                return None
            
            # 중복 검사
            content_hash = self.get_content_hash(instruction, output)
            if content_hash in self.seen_hashes:
                self.stats['duplicate_items'] += 1
                return None
            
            self.seen_hashes.add(content_hash)
            
            # 데이터셋 항목 생성
            dataset_item = {
                "instruction": instruction,
                "input": "",
                "output": output,
                "text": f"{instruction}\n{output}",
                "category": category,
                "subcategory": subcategory,
                "difficulty": self._determine_difficulty(output),
                "language": "ko",
                "metadata": {
                    "title": title,
                    "original_path": str(file_path),
                    "file_size": len(content),
                    "created_at": frontmatter.get('created_at', '2025-08-05'),
                    "content_length": len(output),
                    "has_code_blocks": len(code_blocks) > 0,
                    "code_block_count": len(code_blocks),
                    "description_length": len(description)
                },
                "code_blocks": code_blocks,
                "description": description
            }
            
            # 통계 업데이트
            self.stats['total_items'] += 1
            self.stats['category_counts'][category] = self.stats['category_counts'].get(category, 0) + 1
            self.stats['subcategory_counts'][subcategory] = self.stats['subcategory_counts'].get(subcategory, 0) + 1
            
            return [dataset_item]
            
        except Exception as e:
            logger.error(f"파일 처리 오류 {file_path}: {e}")
            self.stats['skipped_files'] += 1
            self.stats['quality_issues'].append(f"파일 처리 오류: {file_path} - {e}")
            return None
    
    def _determine_difficulty(self, content: str) -> str:
        """난이도 판단"""
        length = len(content)
        code_blocks = re.findall(r'```.*?```', content, re.DOTALL)
        code_ratio = len(''.join(code_blocks)) / length if length > 0 else 0
        
        if length < 200:
            return "easy"
        elif length < 800:
            return "medium"
        else:
            return "hard"
    
    def generate_dataset(self) -> Dict[str, Any]:
        """개선된 데이터셋 생성"""
        logger.info("개선된 데이터셋 생성 시작...")
        
        input_path = Path(self.config.input_dir)
        all_files = list(input_path.rglob("*.md"))
        self.stats['total_files'] = len(all_files)
        
        dataset_items = []
        
        # 병렬 처리
        with ThreadPoolExecutor(max_workers=self.config.max_workers) as executor:
            future_to_file = {executor.submit(self.process_file, file_path): file_path 
                            for file_path in all_files}
            
            for future in as_completed(future_to_file):
                result = future.result()
                if result:
                    dataset_items.extend(result)
        
        self.stats['processed_files'] = len(dataset_items)
        
        # 데이터셋 분할
        unsloth_dataset = []
        alpaca_dataset = []
        unified_dataset = []
        
        for item in dataset_items:
            # Unsloth 형식
            unsloth_item = {
                "instruction": item["instruction"],
                "input": item["input"],
                "output": item["output"],
                "category": item["category"],
                "metadata": item["metadata"]
            }
            unsloth_dataset.append(unsloth_item)
            
            # Alpaca 형식
            alpaca_item = {
                "instruction": item["instruction"],
                "input": item["input"],
                "output": item["output"]
            }
            alpaca_dataset.append(alpaca_item)
            
            # 통합 형식
            unified_item = {
                "instruction": item["instruction"],
                "input": item["input"],
                "output": item["output"],
                "text": item["text"],
                "category": item["category"],
                "subcategory": item["subcategory"],
                "difficulty": item["difficulty"],
                "language": item["language"],
                "metadata": item["metadata"],
                "code_blocks": item["code_blocks"],
                "description": item["description"]
            }
            unified_dataset.append(unified_item)
        
        # 데이터셋 저장 (JSON 유효성 검증 추가)
        self._save_dataset_with_validation(unsloth_dataset, "improved_unsloth_format.json")
        self._save_dataset_with_validation(alpaca_dataset, "improved_alpaca_format.json")
        self._save_dataset_with_validation(unified_dataset, "improved_unified_format.json")
        
        # 통계 정보 저장
        stats_info = {
            "generation_info": {
                "timestamp": datetime.now().isoformat(),
                "total_files_processed": self.stats['total_files'],
                "successfully_processed": self.stats['processed_files'],
                "skipped_files": self.stats['skipped_files'],
                "total_items": self.stats['total_items'],
                "duplicate_items_removed": self.stats['duplicate_items'],
                "code_block_items": self.stats['code_block_items'],
                "quality_issues_count": len(self.stats['quality_issues'])
            },
            "category_distribution": self.stats['category_counts'],
            "subcategory_distribution": self.stats['subcategory_counts'],
            "dataset_sizes": {
                "unsloth_format": len(unsloth_dataset),
                "alpaca_format": len(alpaca_dataset),
                "unified_format": len(unified_dataset)
            },
            "quality_issues": self.stats['quality_issues'][:10]  # 상위 10개만
        }
        
        # JSON 직렬화 가능하도록 날짜 객체 문자열로 변환
        def convert_dates(obj):
            if isinstance(obj, dict):
                return {k: convert_dates(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_dates(item) for item in obj]
            elif hasattr(obj, 'isoformat'):
                return obj.isoformat()
            else:
                return obj
        
        stats_info = convert_dates(stats_info)
        
        self._save_dataset(stats_info, "improved_dataset_statistics.json")
        
        logger.info("개선된 데이터셋 생성 완료!")
        return stats_info
    
    def _save_dataset(self, data: List[Dict[str, Any]], filename: str):
        """데이터셋 저장"""
        output_path = Path(self.config.output_dir) / filename
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.info(f"데이터셋 저장 완료: {output_path}")
    
    def _save_dataset_with_validation(self, data: List[Dict[str, Any]], filename: str):
        """데이터셋 저장 (JSON 유효성 검증 포함)"""
        output_path = Path(self.config.output_dir) / filename
        
        # 데이터 유효성 검증
        validated_data = []
        for i, item in enumerate(data):
            try:
                # JSON 직렬화 테스트
                json_str = json.dumps(item, ensure_ascii=False, indent=2)
                json.loads(json_str)  # 다시 파싱하여 유효성 검증
                validated_data.append(item)
            except (json.JSONDecodeError, TypeError) as e:
                logger.warning(f"항목 {i} JSON 유효성 검증 실패: {e}")
                logger.warning(f"문제의 항목: {item}")
                # 문제가 있는 항목 제외
                continue
        
        # 검증된 데이터 저장
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(validated_data, f, ensure_ascii=False, indent=2)
        
        logger.info(f"데이터셋 저장 완료 (유효성 검증 포함): {output_path}")
        logger.info(f"원본 데이터 항목 수: {len(data)}, 유효한 데이터 항목 수: {len(validated_data)}")

def main():
    """메인 함수"""
    config = ImprovedDatasetConfig()
    generator = ImprovedDatasetGenerator(config)
    
    try:
        stats = generator.generate_dataset()
        
        print("\n" + "="*60)
        print("개선된 데이터셋 생성 완료!")
        print("="*60)
        print(f"처리된 파일 수: {stats['generation_info']['total_files_processed']}")
        print(f"생성된 데이터 항목 수: {stats['generation_info']['total_items']}")
        print(f"중복 항목 제거 수: {stats['generation_info']['duplicate_items_removed']}")
        print(f"코드 블록 포함 항목 수: {stats['generation_info']['code_block_items']}")
        print(f"품질 이슈 수: {stats['generation_info']['quality_issues_count']}")
        print(f"카테고리 분포: {stats['category_distribution']}")
        print(f"데이터셋 크기:")
        print(f"  - Unsloth 형식: {stats['dataset_sizes']['unsloth_format']}")
        print(f"  - Alpaca 형식: {stats['dataset_sizes']['alpaca_format']}")
        print(f"  - 통합 형식: {stats['dataset_sizes']['unified_format']}")
        print("="*60)
        
    except Exception as e:
        logger.error(f"개선된 데이터셋 생성 실패: {e}")
        raise

if __name__ == "__main__":
    main()