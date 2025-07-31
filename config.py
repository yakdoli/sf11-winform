"""
WinForms_Docs 데이터 정제 및 정규화 설정 파일
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Set, Optional

# 기본 경로 설정
PROJECT_ROOT = Path(__file__).parent
WINFORMS_DOCS_DIR = PROJECT_ROOT / "WinForms_Docs"
OUTPUT_DIR = PROJECT_ROOT / "cleaned_data"
BACKUP_DIR = PROJECT_ROOT / "backup"

# 출력 디렉토리 구조
OUTPUT_SUBDIRS = {
    'json': 'json_data',
    'logs': 'logs',
    'reports': 'reports',
    'backup': 'backup'
}

# 정규화된 카테고리 매핑
CATEGORY_MAPPING = {
    '01_Getting_Started': 'getting-started',
    '02_Concepts': 'concepts',
    '03_Data_Binding': 'data-binding',
    '04_Controls': 'controls',
    '05_Features': 'features',
    '99_Uncategorized': 'uncategorized'
}

# 서브 카테고리 매핑
SUBCATEGORY_MAPPING = {
    'Chart': 'chart',
    'Diagram': 'diagram', 
    'Editors': 'editors',
    'Gauge': 'gauge',
    'Grid': 'grid',
    'Ribbon': 'ribbon'
}

# 정규식 패턴
CLEANING_PATTERNS = {
    'html_tags': re.compile(r'<[^>]+>'),
    'html_entities': re.compile(r'&[^;]+;'),
    'style_attributes': re.compile(r'style="[^"]*"'),
    'class_attributes': re.compile(r'class="[^"]*"'),
    'id_attributes': re.compile(r'id="[^"]*"'),
    'display_none': re.compile(r'DISPLAY:\s*none'),
    'ms_xhelp_links': re.compile(r'ms-xhelp:///\?Id=[^}]+'),
    'package_url': re.compile(r'!package_url!'),
    'd2h_prefixes': re.compile(r'::+:|:::|\{#[^}]+\}'),
    'color_styles': re.compile(r'style="[^"]*COLOR:[^"]*"'),
    'font_styles': re.compile(r'style="[^"]*FONT-FAMILY:[^"]*"'),
    'size_styles': re.compile(r'style="[^"]*FONT-SIZE:[^"]*"'),
    'extra_spaces': re.compile(r'\s+'),
    'empty_lines': re.compile(r'\n\s*\n'),
    'markdown_links': re.compile(r'\[([^\]]+)\]\([^)]+\)'),
    'code_block_start': re.compile(r'```([a-zA-Z0-9+]*)\s*$'),
    'code_block_end': re.compile(r'^```$'),
    'image_tags': re.compile(r'!\[.*?\]\(.*?\)'),
    'table_borders': re.compile(r'\+[-+]+\+')
}

# 코드 블록 언식 식별자
CODE_BLOCK_LANGUAGES = {
    'csharp', 'C#', 'c#', 'cs',
    'vb', 'vb.net', 'VB.NET', 'vb.net',
    'asp', 'aspx', 'ASPX',
    'xml', 'XML',
    'html', 'HTML',
    'css', 'CSS',
    'js', 'javascript', 'JavaScript',
    'sql', 'SQL',
    'json', 'JSON',
    'plain', 'text', 'plaintext'
}

# 허용되는 특수 문자
ALLOWED_SPECIAL_CHARS = {
    '!', '?', '.', ',', ';', ':', '-', '(', ')', '[', ']', '{', '}', 
    '#', '@', '$', '%', '&', '*', '+', '=', '|', '/', '\\', '<', '>'
}

# 불필요한 키워드 목록
UNWANTED_KEYWORDS = {
    'd2h_', 'nsbanner', 'nstext', 'ienav', 'titlerow',
    'breadcrumbs', 'package_url', 'related-topics',
    'display', 'none', 'position', 'relative', 'absolute',
    'font-family', 'font-size', 'color', 'background',
    'padding', 'margin', 'border', 'width', 'height'
}

# 문서 메타데이터 필드
DOCUMENT_METADATA_FIELDS = {
    'title', 'category', 'subcategory', 'tags', 'description',
    'version', 'author', 'created_date', 'updated_date',
    'related_topics', 'code_examples', 'images'
}

# 코드 스니펫 메타데이터
CODE_SNIPPET_METADATA_FIELDS = {
    'language', 'description', 'purpose', 'dependencies',
    'requirements', 'output', 'notes'
}

# 중복 탐지 설정
DEDUPLICATION_CONFIG = {
    'similarity_threshold': 0.85,
    'code_similarity_threshold': 0.95,
    'min_content_length': 100,
    'max_file_size_mb': 10,
    'file_extensions': {'.md', '.markdown'}
}

# 데이터 품질 체크리스트
QUALITY_CHECKLIST = {
    'remove_html_tags': True,
    'normalize_whitespace': True,
    'extract_code_blocks': True,
    'validate_links': True,
    'check_metadata': True,
    'remove_duplicates': True,
    'standardize_categories': True,
    'extract_keywords': True,
    'validate_structure': True
}

# 로깅 설정
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file_path': 'logs/data_cleaning.log',
    'max_file_size': '10MB',
    'backup_count': 5
}

# 출력 파일 형식
OUTPUT_FORMATS = {
    'json': {
        'indent': 2,
        'ensure_ascii': False,
        'encoding': 'utf-8'
    },
    'csv': {
        'encoding': 'utf-8',
        'delimiter': ',',
        'quotechar': '"'
    }
}

# 처리 옵션
PROCESSING_OPTIONS = {
    'create_backup': True,
    'validate_output': True,
    'generate_reports': True,
    'parallel_processing': True,
    'max_workers': 4,
    'chunk_size': 100
}

# 유효성 검사 규칙
VALIDATION_RULES = {
    'file_path': {
        'required': True,
        'type': 'str',
        'pattern': r'^[a-zA-Z0-9_\-/\\]+$'
    },
    'content': {
        'required': True,
        'type': 'str',
        'min_length': 1
    },
    'category': {
        'required': True,
        'type': 'str',
        'allowed_values': list(CATEGORY_MAPPING.values())
    },
    'subcategory': {
        'required': False,
        'type': 'str',
        'allowed_values': list(SUBCATEGORY_MAPPING.values())
    }
}

def get_config_value(key: str, default=None):
    """설정 값 가져오기"""
    return globals().get(key, default)

def get_output_path(subdir: str, filename: str = None) -> Path:
    """출력 파일 경로 생성"""
    output_dir = OUTPUT_DIR / OUTPUT_SUBDIRS.get(subdir, subdir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if filename:
        return output_dir / filename
    return output_dir

def ensure_directories():
    """필요한 디렉토리 생성"""
    for subdir in OUTPUT_SUBDIRS.values():
        get_output_path(subdir).mkdir(parents=True, exist_ok=True)
    
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

def normalize_category(category: str) -> str:
    """카테고리 이름 정규화"""
    return CATEGORY_MAPPING.get(category, category.lower().replace('_', '-'))

def normalize_subcategory(subcategory: str) -> str:
    """서브 카테고리 이름 정규화"""
    return SUBCATEGORY_MAPPING.get(subcategory, subcategory.lower().replace('_', '-'))

def is_valid_file_extension(file_path: str) -> bool:
    """파일 확장자 유효성 검사"""
    return any(file_path.lower().endswith(ext) for ext in DEDUPLICATION_CONFIG['file_extensions'])

def initialize_config():
    """초기화 설정"""
    ensure_directories()
    
    # 로깅 디렉토리 생성
    log_dir = Path(LOGGING_CONFIG['file_path']).parent
    log_dir.mkdir(parents=True, exist_ok=True)

# 모듈 로드 시 초기화
initialize_config()