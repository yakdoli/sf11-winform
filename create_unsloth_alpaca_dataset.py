#!/usr/bin/env python3
"""
Unsloth/Alpaca 형식 데이터셋 생성 스크립트
"""

import json
import yaml
import re
import os
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from datetime import datetime
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import unicodedata

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/dataset_creation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class DatasetConfig:
    """데이터셋 생성 설정"""
    input_dir: str = "WinForms_Docs_structured"
    output_dir: str = "unsloth_alpaca_datasets"
    max_workers: int = 4
    min_content_length: int = 50
    max_content_length: int = 8192
    deduplication_threshold: float = 0.95
    
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

@dataclass
class DatasetItem:
    """데이터셋 항목"""
    instruction: str
    input: str
    output: str
    text: str
    category: str
    subcategory: str
    difficulty: str = "medium"
    language: str = "ko"
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}

class DatasetGenerator:
    """데이터셋 생성기"""
    
    def __init__(self, config: DatasetConfig):
        self.config = config
        self.seen_hashes = set()
        self.stats = {
            'total_files': 0,
            'processed_files': 0,
            'skipped_files': 0,
            'total_items': 0,
            'duplicate_items': 0,
            'category_counts': {},
            'subcategory_counts': {}
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
    
    def generate_instruction_output(self, content: str, title: str, category: str) -> tuple[str, str]:
        """instruction과 output 생성"""
        content = self.clean_content(content)
        
        if len(content) < self.config.min_content_length:
            return "", ""
        
        # 카테고리 기반 instruction 생성
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
        
        # 내용이 너무 길면 자르기
        if len(content) > self.config.max_content_length:
            content = content[:self.config.max_content_length] + "... [내용이 길어서 잘렸습니다]"
        
        output = content
        return instruction, output
    
    def get_content_hash(self, instruction: str, output: str) -> str:
        """내용 해시 생성 (중복 검사용)"""
        content = f"{instruction}\n{output}"
        return hashlib.md5(content.encode('utf-8')).hexdigest()
    
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
        
        # 내용 기난 추가 분류
        if any(keyword in content.lower() for keyword in ['install', 'setup', 'deployment']):
            main_category = "getting-started"
        elif any(keyword in content.lower() for keyword in ['concept', 'feature', 'overview']):
            main_category = "concepts"
        elif any(keyword in content.lower() for keyword in ['bind', 'data', 'source']):
            main_category = "data-binding"
        elif any(keyword in content.lower() for keyword in ['control', 'component', 'widget']):
            main_category = "controls"
        
        return main_category, sub_category
    
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
            
            # 카테고리 분류
            category, subcategory = self.categorize_content(str(file_path), main_content)
            
            # instruction과 output 생성
            instruction, output = self.generate_instruction_output(main_content, title, category)
            
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
                    "content_length": len(output)
                }
            }
            
            # 통계 업데이트
            self.stats['total_items'] += 1
            self.stats['category_counts'][category] = self.stats['category_counts'].get(category, 0) + 1
            self.stats['subcategory_counts'][subcategory] = self.stats['subcategory_counts'].get(subcategory, 0) + 1
            
            return [dataset_item]
            
        except Exception as e:
            logger.error(f"파일 처리 오류 {file_path}: {e}")
            self.stats['skipped_files'] += 1
            return None
    
    def _determine_difficulty(self, content: str) -> str:
        """난이도 판단"""
        length = len(content)
        if length < 200:
            return "easy"
        elif length < 800:
            return "medium"
        else:
            return "hard"
    
    def generate_dataset(self) -> Dict[str, Any]:
        """데이터셋 생성"""
        logger.info("데이터셋 생성 시작...")
        
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
                "metadata": item["metadata"]
            }
            unified_dataset.append(unified_item)
        
        # 데이터셋 저장
        self._save_dataset(unsloth_dataset, "unsloth_format.json")
        self._save_dataset(alpaca_dataset, "alpaca_format.json")
        self._save_dataset(unified_dataset, "unified_format.json")
        
        # 통계 정보 저장
        stats_info = {
            "generation_info": {
                "timestamp": datetime.now().isoformat(),
                "total_files_processed": self.stats['total_files'],
                "successfully_processed": self.stats['processed_files'],
                "skipped_files": self.stats['skipped_files'],
                "total_items": self.stats['total_items'],
                "duplicate_items_removed": self.stats['duplicate_items']
            },
            "category_distribution": self.stats['category_counts'],
            "subcategory_distribution": self.stats['subcategory_counts'],
            "dataset_sizes": {
                "unsloth_format": len(unsloth_dataset),
                "alpaca_format": len(alpaca_dataset),
                "unified_format": len(unified_dataset)
            }
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
        
        self._save_dataset(stats_info, "dataset_statistics.json")
        
        logger.info("데이터셋 생성 완료!")
        return stats_info
    
    def _save_dataset(self, data: List[Dict[str, Any]], filename: str):
        """데이터셋 저장"""
        output_path = Path(self.config.output_dir) / filename
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.info(f"데이터셋 저장 완료: {output_path}")

def main():
    """메인 함수"""
    config = DatasetConfig()
    generator = DatasetGenerator(config)
    
    try:
        stats = generator.generate_dataset()
        
        print("\n" + "="*60)
        print("데이터셋 생성 완료!")
        print("="*60)
        print(f"처리된 파일 수: {stats['generation_info']['total_files_processed']}")
        print(f"생성된 데이터 항목 수: {stats['generation_info']['total_items']}")
        print(f"중복 항목 제거 수: {stats['generation_info']['duplicate_items_removed']}")
        print(f"카테고리 분포: {stats['category_distribution']}")
        print(f"데이터셋 크기:")
        print(f"  - Unsloth 형식: {stats['dataset_sizes']['unsloth_format']}")
        print(f"  - Alpaca 형식: {stats['dataset_sizes']['alpaca_format']}")
        print(f"  - 통합 형식: {stats['dataset_sizes']['unified_format']}")
        print("="*60)
        
    except Exception as e:
        logger.error(f"데이터셋 생성 실패: {e}")
        raise

if __name__ == "__main__":
    main()