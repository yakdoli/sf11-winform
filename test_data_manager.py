"""
WinForms_Docs 테스트 데이터 생성 및 관리 시스템
==========================================

주요 기능:
==========
1. 다양한 크기의 테스트 데이터셋 생성
   - 소규모 데이터 (< 1MB): 기본 기능 검증
   - 중규모 데이터 (1MB - 100MB): 일반적 사용 사례
   - 대규모 데이터 (100MB - 1GB): 고성능 처리 검증
   - 초대형 데이터 (> 1GB): 시스템 한계 테스트

2. 실제 사용 패턴을 반영한 데이터 구성
   - WinForms 문서 구조 모방
   - 다양한 문서 유형 생성
   - 실제 데이터 분포 반영
   - 다국어 지원 데이터 생성

3. 엣지 케이스 및 예외 상황 시나리오
   - 손상된 데이터 생성
   - 큰 파일 생성
   - 작은 파일 생성
   - 중복 데이터 생성
   - 특수 문자 포함 데이터 생성

4. 테스트 데이터 버전 관리
   - 데이터셋 버전 관리
   - 변경 이력 추적
   - 롤백 기능
   - 데이터 무결성 검증

작성자: Kilo Code
작성일: 2025-07-31
버전: 1.0 (테스트 데이터 생성 및 관리 시스템)
"""

import asyncio
import logging
import time
import json
import os
import shutil
import hashlib
import pickle
import uuid
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any, Union, Generator
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed
import sqlite3
import pandas as pd
import numpy as np
import random
import string
from enum import Enum
import zipfile
import tempfile

# 로컬 모듈 임포트
try:
    from config import (
        WINFORMS_DOCS_DIR, OUTPUT_DIR, BACKUP_DIR,
        PROCESSING_OPTIONS, LOGGING_CONFIG
    )
    MODULES_AVAILABLE = True
except ImportError as e:
    print(f"일부 모듈 임포트 실패: {e}")
    MODULES_AVAILABLE = False

# 로깅 설정
logging.basicConfig(
    level=getattr(logging, LOGGING_CONFIG['level']),
    format=LOGGING_CONFIG['format'],
    handlers=[
        logging.FileHandler(LOGGING_CONFIG['file_path'], encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DataSize(Enum):
    """데이터 크기 타입"""
    SMALL = "small"           # < 1MB
    MEDIUM = "medium"         # 1MB - 100MB
    LARGE = "large"           # 100MB - 1GB
    EXTRA_LARGE = "extra_large"  # > 1GB

class DataType(Enum):
    """데이터 타입"""
    DOCUMENT = "document"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    ARCHIVE = "archive"
    DATABASE = "database"
    LOG = "log"
    CONFIG = "config"

class DataFormat(Enum):
    """데이터 형식"""
    JSON = "json"
    XML = "xml"
    CSV = "csv"
    TXT = "txt"
    MD = "md"
    HTML = "html"
    PDF = "pdf"
    ZIP = "zip"

@dataclass
class TestDataConfig:
    """테스트 데이터 설정 데이터 클래스"""
    dataset_name: str
    data_size: DataSize
    data_type: DataType
    data_format: DataFormat
    file_count: int
    file_size_mb: float
    include_corrupted: bool = False
    include_duplicates: bool = False
    include_special_chars: bool = True
    language: str = "ko"
    compression_level: int = 6
    metadata: Optional[Dict[str, Any]] = None

@dataclass
class TestDataInfo:
    """테스트 데이터 정보 데이터 클래스"""
    dataset_id: str
    dataset_name: str
    data_size: DataSize
    data_type: DataType
    data_format: DataFormat
    file_count: int
    total_size_mb: float
    created_at: datetime
    version: str
    checksum: str
    file_list: List[str]
    metadata: Optional[Dict[str, Any]] = None

@dataclass
class DataGenerationResult:
    """데이터 생성 결과 데이터 클래스"""
    success: bool
    dataset_info: Optional[TestDataInfo] = None
    generated_files: List[str] = None
    error_message: Optional[str] = None
    generation_time: float = 0.0
    memory_usage_mb: float = 0.0

class TestDataGenerator:
    """테스트 데이터 생성기"""
    
    def __init__(self):
        self.base_content = self._load_base_content()
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?~`"
        self.languages = {
            'ko': self._generate_korean_content,
            'en': self._generate_english_content,
            'ja': self._generate_japanese_content,
            'zh': self._generate_chinese_content
        }
    
    def _load_base_content(self) -> Dict[str, List[str]]:
        """기본 콘텐츠 로드"""
        return {
            'winforms': [
                "WinForms는 Windows 애플리케이션을 개발하기 위한 UI 프레임워크입니다.",
                "이 프레임워크를 사용하면 데스크톱 애플리케이션을 쉽게 개발할 수 있습니다.",
                "다양한 컨트롤과 이벤트 처리 시스템을 제공합니다.",
                "데이터 바인딩 기능을 통해 UI와 데이터를 쉽게 연결할 수 있습니다.",
                "비동기 처리를 지원하여 사용자 경험을 향상시킬 수 있습니다.",
                "메모리 관리 시스템을 통해 안정적인 애플리케이션 실행이 가능합니다.",
                "성능 모니터링 기능을 통해 애플리케이션 성능을 실시간으로 확인할 수 있습니다.",
                "다국어 지원을 통해 글로벌 애플리케이션 개발이 가능합니다.",
                "테스트 자동화를 통해 안정적인 소프트웨어 품질을 유지할 수 있습니다.",
                "문서 변환 시스템을 통해 다양한 형식의 문서를 처리할 수 있습니다."
            ],
            'programming': [
                "객체 지향 프로그래밍은 현대 소프트웨어 개발의 핵심 패러다임입니다.",
                "디자인 패턴은 반복적으로 발생하는 문제들을 해결하기 위한 템플릿입니다.",
                "알고리즘 효율성은 프로그램 성능에 결정적인 영향을 미칩니다.",
                "데이터 구조 선택은 애플리케이션 성능에 큰 영향을 줍니다.",
                "동시성 프로그래밍은 멀티코어 프로세서를 효율적으로 활용합니다.",
                "메모리 관리는 안정적인 애플리케이션 개발의 핵심입니다.",
                "오류 처리는 소프트웨어 신뢰성을 보장합니다.",
                "테스트 주도 개발은 코드 품질을 향상시키는 효과적인 방법입니다.",
                "CI/CD 파이프라인은 소프트웨어 배포 프로세스를 자동화합니다.",
                "클라우드 컴퓨팅은 확장 가능한 인프라를 제공합니다."
            ],
            'general': [
                "기술 발전은 인류 사회에 많은 변화를 가져왔습니다.",
                "디지털 전환은 모든 산업 분야에서 중요한 화두입니다.",
                "인공지능은 미래 기술의 핵심으로 주목받고 있습니다.",
                "빅데이터 분석은 의사결정을 위한 중요한 도구입니다.",
                "사물인터넷은 일상생활에 깊숙이 들어오고 있습니다.",
                "블록체인 기술은 분산 시스템의 신뢰성을 보장합니다.",
                "사이버 보안은 디지털 시대의 필수 요소입니다.",
                "클라우드 컴퓨팅은 유연한 인프라를 제공합니다.",
                "모바일 기술은 사람들의 생활 방식을 바꾸고 있습니다.",
                "소프트웨어 개발은 끊임없이 진화하고 있습니다."
            ]
        }
    
    def _generate_korean_content(self, paragraphs: int = 10) -> str:
        """한국어 콘텐츠 생성"""
        content = []
        categories = list(self.base_content.keys())
        
        for _ in range(paragraphs):
            category = random.choice(categories)
            sentences = random.sample(self.base_content[category], 
                                    min(random.randint(1, 3), len(self.base_content[category])))
            content.extend(sentences)
        
        return "\n".join(content)
    
    def _generate_english_content(self, paragraphs: int = 10) -> str:
        """영어 콘텐츠 생성"""
        content = []
        categories = list(self.base_content.keys())
        
        for _ in range(paragraphs):
            category = random.choice(categories)
            sentences = random.sample(self.base_content[category], 
                                    min(random.randint(1, 3), len(self.base_content[category])))
            # 영어 번역 (간단한 시뮬레이션)
            translated = [f"English translation: {sentence}" for sentence in sentences]
            content.extend(translated)
        
        return "\n".join(content)
    
    def _generate_japanese_content(self, paragraphs: int = 10) -> str:
        """일본어 콘텐츠 생성"""
        content = []
        categories = list(self.base_content.keys())
        
        for _ in range(paragraphs):
            category = random.choice(categories)
            sentences = random.sample(self.base_content[category], 
                                    min(random.randint(1, 3), len(self.base_content[category])))
            # 일본어 번역 (간단한 시뮬레이션)
            translated = [f"日本語翻訳: {sentence}" for sentence in sentences]
            content.extend(translated)
        
        return "\n".join(content)
    
    def _generate_chinese_content(self, paragraphs: int = 10) -> str:
        """중국어 콘텐츠 생성"""
        content = []
        categories = list(self.base_content.keys())
        
        for _ in range(paragraphs):
            category = random.choice(categories)
            sentences = random.sample(self.base_content[category], 
                                    min(random.randint(1, 3), len(self.base_content[category])))
            # 중국어 번역 (간단한 시뮬레이션)
            translated = [f"中文翻译: {sentence}" for sentence in sentences]
            content.extend(translated)
        
        return "\n".join(content)
    
    def _generate_document_content(self, size_mb: float, language: str = "ko") -> str:
        """문서 콘텐츠 생성"""
        target_size = int(size_mb * 1024 * 1024)
        content = ""
        
        # 언어별 콘텐츠 생성 함수 선택
        generate_func = self.languages.get(language, self._generate_korean_content)
        
        while len(content.encode('utf-8')) < target_size:
            # 새로운 문단 추가
            new_paragraph = generate_func(random.randint(5, 15))
            content += new_paragraph + "\n\n"
        
        # 정확한 크기로 조정
        content = content[:target_size]
        return content
    
    def _generate_csv_content(self, size_mb: float) -> str:
        """CSV 콘텐츠 생성"""
        target_size = int(size_mb * 1024 * 1024)
        content = "id,name,description,created_at,updated_at,size\n"
        
        row_count = int(target_size / 100)  # 예상 행당 크기
        
        for i in range(row_count):
            name = f"item_{i}"
            description = f"Description for item {i}"
            created_at = datetime.now().isoformat()
            updated_at = datetime.now().isoformat()
            size = random.randint(100, 10000)
            
            row = f"{i},{name},{description},{created_at},{updated_at},{size}\n"
            content += row
        
        return content[:target_size]
    
    def _generate_json_content(self, size_mb: float) -> str:
        """JSON 콘텐츠 생성"""
        target_size = int(size_mb * 1024 * 1024)
        data = {
            "metadata": {
                "created_at": datetime.now().isoformat(),
                "version": "1.0",
                "generator": "TestDataGenerator"
            },
            "documents": []
        }
        
        # 문서 생성
        doc_count = int(target_size / 500)  # 예상 문서당 크기
        
        for i in range(doc_count):
            doc = {
                "id": i,
                "title": f"Document {i}",
                "content": self._generate_document_content(0.1),  # 0.1MB 문서
                "tags": ["tag1", "tag2", "tag3"],
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat()
            }
            data["documents"].append(doc)
        
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        return json_str[:target_size]
    
    def _generate_corrupted_content(self, size_mb: float) -> str:
        """손상된 콘텐츠 생성"""
        target_size = int(size_mb * 1024 * 1024)
        content = ""
        
        # 일반 콘텐츠 생성
        normal_content = self._generate_document_content(size_mb * 0.8)
        content += normal_content
        
        # 손상된 부분 추가
        corrupted_size = target_size - len(content.encode('utf-8'))
        if corrupted_size > 0:
            # 무작위 바이트 추가
            corrupted_bytes = bytes([random.randint(0, 255) for _ in range(corrupted_size)])
            content += corrupted_bytes.decode('latin-1', errors='ignore')
        
        return content
    
    def _generate_duplicate_content(self, size_mb: float, duplicate_ratio: float = 0.3) -> str:
        """중복 콘텐츠 생성"""
        target_size = int(size_mb * 1024 * 1024)
        content = ""
        
        # 원본 콘텐츠 생성
        original_content = self._generate_document_content(size_mb * (1 - duplicate_ratio))
        content += original_content
        
        # 중복 콘텐츠 추가
        duplicate_size = target_size - len(content.encode('utf-8'))
        if duplicate_size > 0:
            duplicate_content = original_content[:duplicate_size]
            content += duplicate_content
        
        return content
    
    def _generate_special_chars_content(self, size_mb: float) -> str:
        """특수 문자 포함 콘텐츠 생성"""
        content = self._generate_document_content(size_mb * 0.7)
        
        # 특수 문자 추가
        special_size = int(size_mb * 1024 * 1024 * 0.3)
        special_chars = ''.join(random.choice(self.special_chars) for _ in range(special_size))
        
        return content + special_chars
    
    def generate_file_content(self, config: TestDataConfig, file_index: int) -> str:
        """파일 콘텐츠 생성"""
        try:
            if config.data_format == DataFormat.JSON:
                return self._generate_json_content(config.file_size_mb)
            elif config.data_format == DataFormat.CSV:
                return self._generate_csv_content(config.file_size_mb)
            elif config.data_format == DataFormat.TXT:
                if config.include_corrupted:
                    return self._generate_corrupted_content(config.file_size_mb)
                elif config.include_duplicates:
                    return self._generate_duplicate_content(config.file_size_mb)
                elif config.include_special_chars:
                    return self._generate_special_chars_content(config.file_size_mb)
                else:
                    return self._generate_document_content(config.file_size_mb, config.language)
            elif config.data_format == DataFormat.MD:
                return self._generate_document_content(config.file_size_mb, config.language)
            elif config.data_format == DataFormat.HTML:
                # HTML 형식으로 변환
                content = self._generate_document_content(config.file_size_mb, config.language)
                html_content = f"""
                <!DOCTYPE html>
                <html lang="{config.language}">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Test Documenttitle>
                </head>
                <body>
                    <h1>Test Document</h1>
                    <div class="content">
                        {content.replace('\n', '<br>')}
                    </div>
                </body>
                </html>
                """
                return html_content
            else:
                return self._generate_document_content(config.file_size_mb, config.language)
                
        except Exception as e:
            logger.error(f"파일 콘텐츠 생성 오류: {e}")
            return ""
    
    def save_test_file(self, file_path: str, content: str, config: TestDataConfig) -> bool:
        """테스트 파일 저장"""
        try:
            # 디렉토리 생성
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)
            
            # 파일 저장
            if config.data_format == DataFormat.ZIP:
                # ZIP 파일로 저장
                with zipfile.ZipFile(file_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=config.compression_level) as zipf:
                    # 임시 파일 생성
                    temp_file = Path(file_path).with_suffix('.tmp')
                    with open(temp_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    # ZIP에 추가
                    zipf.write(temp_file, Path(temp_file).name)
                    temp_file.unlink()
            else:
                # 일반 파일로 저장
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            return True
            
        except Exception as e:
            logger.error(f"테스트 파일 저장 오류: {file_path}, {e}")
            return False
    
    def calculate_checksum(self, file_path: str) -> str:
        """파일 체크섬 계산"""
        try:
            hash_md5 = hashlib.md5()
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except Exception as e:
            logger.error(f"체크섬 계산 오류: {file_path}, {e}")
            return ""

class TestDataManager:
    """테스트 데이터 관리 시스템 - 핵심 클래스"""
    
    def __init__(self, db_path: str = "performance_results/test_data.db", base_dir: str = "test_data"):
        self.db_path = Path(db_path)
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)
        
        # 데이터 생성기
        self.generator = TestDataGenerator()
        
        # 설정
        self.config = {
            'max_concurrent_generators': 4,
            'cleanup_old_days': 30,
            'compression_enabled': True,
            'checksum_verification': True,
            'auto_backup': True,
            'backup_retention_days': 7
        }
        
        # 데이터베이스 초기화
        self._init_database()
        
        logger.info("테스트 데이터 관리 시스템 초기화 완료")
    
    def _init_database(self):
        """데이터베이스 초기화"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 데이터셋 정보 테이블
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS datasets (
                        dataset_id TEXT PRIMARY KEY,
                        dataset_name TEXT NOT NULL,
                        data_size TEXT NOT NULL,
                        data_type TEXT NOT NULL,
                        data_format TEXT NOT NULL,
                        file_count INTEGER NOT NULL,
                        total_size_mb REAL NOT NULL,
                        created_at TEXT NOT NULL,
                        version TEXT NOT NULL,
                        checksum TEXT,
                        metadata TEXT,
                        backup_path TEXT
                    )
                ''')
                
                # 파일 정보 테이블
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS dataset_files (
                        file_id TEXT PRIMARY KEY,
                        dataset_id TEXT NOT NULL,
                        file_path TEXT NOT NULL,
                        file_name TEXT NOT NULL,
                        file_size_mb REAL NOT NULL,
                        file_format TEXT NOT NULL,
                        created_at TEXT NOT NULL,
                        checksum TEXT,
                        FOREIGN KEY (dataset_id) REFERENCES datasets (dataset_id)
                    )
                ''')
                
                # 버전 관리 테이블
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS dataset_versions (
                        version_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        dataset_id TEXT NOT NULL,
                        version TEXT NOT NULL,
                        created_at TEXT NOT NULL,
                        change_description TEXT,
                        checksum TEXT,
                        FOREIGN KEY (dataset_id) REFERENCES datasets (dataset_id)
                    )
                ''')
                
                # 백업 정보 테이블
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS dataset_backups (
                        backup_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        dataset_id TEXT NOT NULL,
                        backup_path TEXT NOT NULL,
                        backup_size_mb REAL NOT NULL,
                        created_at TEXT NOT NULL,
                        checksum TEXT,
                        FOREIGN KEY (dataset_id) REFERENCES datasets (dataset_id)
                    )
                ''')
                
                # 인덱스 생성
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_datasets_name ON datasets(dataset_name)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_datasets_size ON datasets(data_size)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_datasets_created ON datasets(created_at)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_files_dataset ON dataset_files(dataset_id)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_versions_dataset ON dataset_versions(dataset_id)')
                cursor.execute('CREATE INDEX IF NOT EXISTS idx_backups_dataset ON dataset_backups(dataset_id)')
                
                conn.commit()
                logger.info("테스트 데이터 관리 데이터베이스 초기화 완료")
                
        except Exception as e:
            logger.error(f"데이터베이스 초기화 오류: {e}")
            raise
    
    def generate_test_dataset(self, config: TestDataConfig) -> DataGenerationResult:
        """테스트 데이터셋 생성"""
        start_time = time.time()
        
        try:
            # 데이터셋 ID 생성
            dataset_id = str(uuid.uuid4())
            dataset_dir = self.base_dir / dataset_id
            
            # 디렉토리 생성
            dataset_dir.mkdir(parents=True, exist_ok=True)
            
            # 파일 목록
            generated_files = []
            
            # 파일 생성
            with ThreadPoolExecutor(max_workers=self.config['max_concurrent_generators']) as executor:
                futures = []
                
                for i in range(config.file_count):
                    file_name = f"{config.dataset_name}_{i:04d}.{config.data_format.value}"
                    file_path = dataset_dir / file_name
                    
                    # 파일 콘텐츠 생성
                    future = executor.submit(
                        self.generator.generate_file_content,
                        config, i
                    )
                    futures.append((future, file_path))
                
                # 결과 저장
                for future, file_path in futures:
                    content = future.result()
                    if content:
                        if self.generator.save_test_file(str(file_path), content, config):
                            generated_files.append(str(file_path))
            
            # 총 크기 계산
            total_size_mb = sum(os.path.getsize(f) for f in generated_files) / 1024 / 1024
            
            # 체크섬 계산
            checksum = self._calculate_dataset_checksum(generated_files)
            
            # 데이터셋 정보 생성
            dataset_info = TestDataInfo(
                dataset_id=dataset_id,
                dataset_name=config.dataset_name,
                data_size=config.data_size,
                data_type=config.data_type,
                data_format=config.data_format,
                file_count=config.file_count,
                total_size_mb=total_size_mb,
                created_at=datetime.now(),
                version="1.0",
                checksum=checksum,
                file_list=generated_files,
                metadata=config.metadata
            )
            
            # 데이터베이스에 저장
            self._save_dataset_info(dataset_info)
            
            # 생성 시간 계산
            generation_time = time.time() - start_time
            
            # 메모리 사용량 계산 (간단한 시뮬레이션)
            memory_usage_mb = total_size_mb * 0.1  # 생성 과정에서 추가 메모리 사용
            
            return DataGenerationResult(
                success=True,
                dataset_info=dataset_info,
                generated_files=generated_files,
                generation_time=generation_time,
                memory_usage_mb=memory_usage_mb
            )
            
        except Exception as e:
            logger.error(f"테스트 데이터셋 생성 오류: {e}")
            return DataGenerationResult(
                success=False,
                error_message=str(e),
                generation_time=time.time() - start_time
            )
    
    def _calculate_dataset_checksum(self, file_paths: List[str]) -> str:
        """데이터셋 체크섬 계산"""
        try:
            hash_md5 = hashlib.md5()
            
            for file_path in sorted(file_paths):  # 정렬된 순서로 처리
                with open(file_path, "rb") as f:
                    for chunk in iter(lambda: f.read(4096), b""):
                        hash_md5.update(chunk)
            
            return hash_md5.hexdigest()
        except Exception as e:
            logger.error(f"데이터셋 체크섬 계산 오류: {e}")
            return ""
    
    def _save_dataset_info(self, dataset_info: TestDataInfo):
        """데이터셋 정보 저장"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    INSERT OR REPLACE INTO datasets 
                    (dataset_id, dataset_name, data_size, data_type, data_format,
                     file_count, total_size_mb, created_at, version, checksum, metadata)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    dataset_info.dataset_id,
                    dataset_info.dataset_name,
                    dataset_info.data_size.value,
                    dataset_info.data_type.value,
                    dataset_info.data_format.value,
                    dataset_info.file_count,
                    dataset_info.total_size_mb,
                    dataset_info.created_at.isoformat(),
                    dataset_info.version,
                    dataset_info.checksum,
                    json.dumps(dataset_info.metadata, ensure_ascii=False) if dataset_info.metadata else None
                ))
                
                # 파일 정보 저장
                for file_path in dataset_info.file_list:
                    file_id = str(uuid.uuid4())
                    file_name = os.path.basename(file_path)
                    file_size_mb = os.path.getsize(file_path) / 1024 / 1024
                    file_format = os.path.splitext(file_path)[1][1:] or 'txt'
                    checksum = self.generator.calculate_checksum(file_path)
                    
                    cursor.execute('''
                        INSERT INTO dataset_files 
                        (file_id, dataset_id, file_path, file_name, file_size_mb,
                         file_format, created_at, checksum)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        file_id,
                        dataset_info.dataset_id,
                        file_path,
                        file_name,
                        file_size_mb,
                        file_format,
                        datetime.now().isoformat(),
                        checksum
                    ))
                
                conn.commit()
                logger.info(f"데이터셋 정보 저장 완료: {dataset_info.dataset_name}")
                
        except Exception as e:
            logger.error(f"데이터셋 정보 저장 오류: {e}")
            raise
    
    def get_dataset_info(self, dataset_id: str) -> Optional[TestDataInfo]:
        """데이터셋 정보 조회"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    SELECT dataset_id, dataset_name, data_size, data_type, data_format,
                           file_count, total_size_mb, created_at, version, checksum, metadata
                    FROM datasets
                    WHERE dataset_id = ?
                ''', (dataset_id,))
                
                row = cursor.fetchone()
                if row:
                    return TestDataInfo(
                        dataset_id=row[0],
                        dataset_name=row[1],
                        data_size=DataSize(row[2]),
                        data_type=DataType(row[3]),
                        data_format=DataFormat(row[4]),
                        file_count=row[5],
                        total_size_mb=row[6],
                        created_at=datetime.fromisoformat(row[7]),
                        version=row[8],
                        checksum=row[9],
                        metadata=json.loads(row[10]) if row[10] else None
                    )
                
                return None
                
        except Exception as e:
            logger.error(f"데이터셋 정보 조회 오류: {e}")
            return None
    
    def list_datasets(self, data_size: Optional[DataSize] = None, 
                     data_type: Optional[DataType] = None,
                     limit: int = 100) -> List[TestDataInfo]:
        """데이터셋 목록 조회"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                query = '''
                    SELECT dataset_id, dataset_name, data_size, data_type, data_format,
                           file_count, total_size_mb, created_at, version, checksum, metadata
                    FROM datasets
                '''
                params = []
                
                if data_size:
                    query += ' WHERE data_size = ?'
                    params.append(data_size.value)
                
                if data_type and not data_size:
                    query += ' WHERE data_type = ?'
                    params.append(data_type.value)
                elif data_type and data_size:
                    query += ' AND data_type = ?'
                    params.append(data_type.value)
                
                query += ' ORDER BY created_at DESC LIMIT ?'
                params.append(limit)
                
                cursor.execute(query, params)
                
                datasets = []
                for row in cursor.fetchall():
                    dataset_info = TestDataInfo(
                        dataset_id=row[0],
                        dataset_name=row[1],
                        data_size=DataSize(row[2]),
                        data_type=DataType(row[3]),
                        data_format=DataFormat(row[4]),
                        file_count=row[5],
                        total_size_mb=row[6],
                        created_at=datetime.fromisoformat(row[7]),
                        version=row[8],
                        checksum=row[9],
                        metadata=json.loads(row[10]) if row[10] else None
                    )
                    datasets.append(dataset_info)
                
                return datasets
                
        except Exception as e:
            logger.error(f"데이터셋 목록 조회 오류: {e}")
            return []
    
    def delete_dataset(self, dataset_id: str) -> bool:
        """데이터셋 삭제"""
        try:
            # 데이터셋 정보 조회
            dataset_info = self.get_dataset_info(dataset_id)
            if not dataset_info:
                return False
            
            # 파일 삭제
            for file_path in dataset_info.file_list:
                try:
                    os.remove(file_path)
                except Exception as e:
                    logger.warning(f"파일 삭제 오류: {file_path}, {e}")
            
            # 디렉토리 삭제
            dataset_dir = Path(dataset_info.file_list[0]).parent
            try:
                shutil.rmtree(dataset_dir)
            except Exception as e:
                logger.warning(f"디렉토리 삭제 오류: {dataset_dir}, {e}")
            
            # 데이터베이스에서 삭제
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('DELETE FROM dataset_files WHERE dataset_id = ?', (dataset_id,))
                cursor.execute('DELETE FROM dataset_versions WHERE dataset_id = ?', (dataset_id,))
                cursor.execute('DELETE FROM dataset_backups WHERE dataset_id = ?', (dataset_id,))
                cursor.execute('DELETE FROM datasets WHERE dataset_id = ?', (dataset_id,))
                
                conn.commit()
            
            logger.info(f"데이터셋 삭제 완료: {dataset_info.dataset_name}")
            return True
            
        except Exception as e:
            logger.error(f"데이터셋 삭제 오류: {e}")
            return False
    
    def backup_dataset(self, dataset_id: str) -> bool:
        """데이터셋 백업"""
        try:
            # 데이터셋 정보 조회
            dataset_info = self.get_dataset_info(dataset_id)
            if not dataset_info:
                return False
            
            # 백업 디렉토리 생성
            backup_dir = self.base_dir / "backups" / dataset_id
            backup_dir.mkdir(parents=True, exist_ok=True)
            
            # 백업 파일 생성
            backup_files = []
            for file_path in dataset_info.file_list:
                file_name = os.path.basename(file_path)
                backup_path = backup_dir / file_name
                
                shutil.copy2(file_path, backup_path)
                backup_files.append(str(backup_path))
            
            # 백업 정보 생성
            backup_size_mb = sum(os.path.getsize(f) for f in backup_files) / 1024 / 1024
            checksum = self._calculate_dataset_checksum(backup_files)
            
            # 백업 정보 저장
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    INSERT INTO dataset_backups 
                    (dataset_id, backup_path, backup_size_mb, created_at, checksum)
                    VALUES (?, ?, ?, ?, ?)
                ''', (
                    dataset_id,
                    str(backup_dir),
                    backup_size_mb,
                    datetime.now().isoformat(),
                    checksum
                ))
                
                conn.commit()
            
            logger.info(f"데이터셋 백업 완료: {dataset_info.dataset_name}")
            return True
            
        except Exception as e:
            logger.error(f"데이터셋 백업 오류: {e}")
            return False
    
    def restore_dataset(self, backup_id: int) -> bool:
        """데이터셋 복원"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 백업 정보 조회
                cursor.execute('''
                    SELECT dataset_id, backup_path, backup_size_mb, created_at, checksum
                    FROM dataset_backups
                    WHERE backup_id = ?
                ''', (backup_id,))
                
                row = cursor.fetchone()
                if not row:
                    return False
                
                dataset_id, backup_path, backup_size_mb, created_at, checksum = row
                
                # 데이터셋 정보 조회
                dataset_info = self.get_dataset_info(dataset_id)
                if not dataset_info:
                    return False
                
                # 복원 디렉토리 생성
                restore_dir = self.base_dir / "restored" / dataset_id
                restore_dir.mkdir(parents=True, exist_ok=True)
                
                # 파일 복원
                restored_files = []
                for file_path in dataset_info.file_list:
                    file_name = os.path.basename(file_path)
                    restore_path = restore_dir / file_name
                    
                    shutil.copy2(os.path.join(backup_path, file_name), restore_path)
                    restored_files.append(str(restore_path))
                
                # 새로운 데이터셋 정보 생성
                new_dataset_info = TestDataInfo(
                    dataset_id=str(uuid.uuid4()),
                    dataset_name=f"{dataset_info.dataset_name}_restored",
                    data_size=dataset_info.data_size,
                    data_type=dataset_info.data_type,
                    data_format=dataset_info.data_format,
                    file_count=dataset_info.file_count,
                    total_size_mb=backup_size_mb,
                    created_at=datetime.now(),
                    version=dataset_info.version,
                    checksum=checksum,
                    file_list=restored_files,
                    metadata=dataset_info.metadata
                )
                
                # 새로운 데이터셋 정보 저장
                self._save_dataset_info(new_dataset_info)
                
                logger.info(f"데이터셋 복원 완료: {new_dataset_info.dataset_name}")
                return True
                
        except Exception as e:
            logger.error(f"데이터셋 복원 오류: {e}")
            return False
    
    def verify_dataset_integrity(self, dataset_id: str) -> bool:
        """데이터셋 무결성 검증"""
        try:
            dataset_info = self.get_dataset_info(dataset_id)
            if not dataset_info:
                return False
            
            # 파일 존재 여부 확인
            for file_path in dataset_info.file_list:
                if not os.path.exists(file_path):
                    logger.error(f"파일이 존재하지 않음: {file_path}")
                    return False
            
            # 체크섬 검증
            current_checksum = self._calculate_dataset_checksum(dataset_info.file_list)
            if current_checksum != dataset_info.checksum:
                logger.error(f"체크섬 불일치: {dataset_info.dataset_name}")
                return False
            
            logger.info(f"데이터셋 무결성 검증 성공: {dataset_info.dataset_name}")
            return True
            
        except Exception as e:
            logger.error(f"데이터셋 무결성 검증 오류: {e}")
            return False
    
    def cleanup_old_data(self):
        """오래된 데이터 정리"""
        try:
            cutoff_date = datetime.now() - timedelta(days=self.config['cleanup_old_days'])
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 오래된 데이터셋 조회
                cursor.execute('''
                    SELECT dataset_id, dataset_name
                    FROM datasets
                    WHERE created_at < ?
                ''', (cutoff_date.isoformat(),))
                
                old_datasets = cursor.fetchall()
                
                for dataset_id, dataset_name in old_datasets:
                    # 데이터셋 삭제
                    if self.delete_dataset(dataset_id):
                        logger.info(f"오래된 데이터셋 삭제: {dataset_name}")
                
                conn.commit()
                logger.info(f"오래된 데이터 정리 완료: {len(old_datasets)}개 데이터셋")
                
        except Exception as e:
            logger.error(f"오래된 데이터 정리 오류: {e}")
    
    def get_storage_stats(self) -> Dict[str, Any]:
        """저장 공간 통계"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 데이터셋 통계
                cursor.execute('''
                    SELECT 
                        COUNT(*) as total_datasets,
                        SUM(file_count) as total_files,
                        SUM(total_size_mb) as total_size_mb,
                        AVG(total_size_mb) as avg_size_mb
                    FROM datasets
                ''')
                
                dataset_stats = cursor.fetchone()
                
                # 데이터 크기별 통계
                cursor.execute('''
                    SELECT data_size, COUNT(*) as count, SUM(total_size_mb) as total_size
                    FROM datasets
                    GROUP BY data_size
                    ORDER BY data_size
                ''')
                
                size_stats = []
                for row in cursor.fetchall():
                    size_stats.append({
                        'data_size': row[0],
                        'count': row[1],
                        'total_size_mb': row[2]
                    })
                
                # 데이터 타입별 통계
                cursor.execute('''
                    SELECT data_type, COUNT(*) as count, SUM(total_size_mb) as total_size
                    FROM datasets
                    GROUP BY data_type
                    ORDER BY data_type
                ''')
                
                type_stats = []
                for row in cursor.fetchall():
                    type_stats.append({
                        'data_type': row[0],
                        'count': row[1],
                        'total_size_mb': row[2]
                    })
                
                return {
                    'total_datasets': dataset_stats[0],
                    'total_files': dataset_stats[1],
                    'total_size_mb': dataset_stats[2],
                    'avg_size_mb': dataset_stats[3],
                    'size_breakdown': size_stats,
                    'type_breakdown': type_stats,
                    'generated_at': datetime.now().isoformat()
                }
                
        except Exception as e:
            logger.error(f"저장 공간 통계 조회 오류: {e}")
            return {}
    
    def export_dataset_metadata(self, dataset_id: str, output_path: str) -> bool:
        """데이터셋 메타데이터 내보내기"""
        try:
            dataset_info = self.get_dataset_info(dataset_id)
            if not dataset_info:
                return False
            
            # 메타데이터 생성
            metadata = {
                'dataset_info': asdict(dataset_info),
                'file_list': dataset_info.file_list,
                'storage_stats': self.get_storage_stats(),
                'exported_at': datetime.now().isoformat()
            }
            
            # 파일 저장
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)
            
            logger.info(f"데이터셋 메타데이터 내보내기 완료: {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"데이터셋 메타데이터 내보내기 오류: {e}")
            return False

# 유틸리티 함수
def create_test_data_manager(db_path: str = "performance_results/test_data.db", 
                           base_dir: str = "test_data") -> TestDataManager:
    """테스트 데이터 관리 시스템 인스턴스 생성"""
    return TestDataManager(db_path, base_dir)

def create_sample_datasets():
    """샘플 데이터셋 생성"""
    data_manager = create_test_data_manager()
    
    # 소규모 데이터셋
    small_config = TestDataConfig(
        dataset_name="small_dataset",
        data_size=DataSize.SMALL,
        data_type=DataType.DOCUMENT,
        data_format=DataFormat.JSON,
        file_count=10,
        file_size_mb=0.1,
        language="ko"
    )
    
    # 중규모 데이터셋
    medium_config = TestDataConfig(
        dataset_name="medium_dataset",
        data_size=DataSize.MEDIUM,
        data_type=DataType.DOCUMENT,
        data_format=DataFormat.CSV,
        file_count=50,
        file_size_mb=2.0,
        language="en"
    )
    
    # 대규모 데이터셋
    large_config = TestDataConfig(
        dataset_name="large_dataset",
        data_size=DataSize.LARGE,
        data_type=DataType.DOCUMENT,
        data_format=DataFormat.TXT,
        file_count=100,
        file_size_mb=10.0,
        language="ko",
        include_duplicates=True
    )
    
    # 엣지 케이스 데이터셋
    edge_config = TestDataConfig(
        dataset_name="edge_case_dataset",
        data_size=DataSize.SMALL,
        data_type=DataType.DOCUMENT,
        data_format=DataFormat.TXT,
        file_count=5,
        file_size_mb=0.5,
        include_corrupted=True,
        include_special_chars=True
    )
    
    # 데이터셋 생성
    datasets = [
        data_manager.generate_test_dataset(small_config),
        data_manager.generate_test_dataset(medium_config),
        data_manager.generate_test_dataset(large_config),
        data_manager.generate_test_dataset(edge_config)
    ]
    
    # 결과 출력
    for result in datasets:
        if result.success:
            print(f"데이터셋 생성 성공: {result.dataset_info.dataset_name}")
            print(f"  - 파일 수: {result.dataset_info.file_count}")
            print(f"  - 총 크기: {result.dataset_info.total_size_mb:.2f}MB")
            print(f"  - 생성 시간: {result.generation_time:.2f}초")
        else:
            print(f"데이터셋 생성 실패: {result.error_message}")
    
    return datasets

if __name__ == "__main__":
    print("WinForms_Docs 테스트 데이터 생성 및 관리 시스템")
    print("=" * 50)
    
    # 샘플 데이터셋 생성
    datasets = create_sample_datasets()
    
    # 데이터 관리 시스템 생성
    data_manager = create_test_data_manager()
    
    # 저장 공간 통계 출력
    stats = data_manager.get_storage_stats()
    print(f"\n저장 공간 통계:")
    print(f"  - 총 데이터셋 수: {stats['total_datasets']}")
    print(f"  - 총 파일 수: {stats['total_files']}")
    print(f"  - 총 크기: {stats['total_size_mb']:.2f}MB")
    print(f"  - 평균 크기: {stats['avg_size_mb']:.2f}MB")
    
    # 데이터셋 목록 출력
    print(f"\n데이터셋 목록:")
    for dataset in data_manager.list_datasets():
        print(f"  - {dataset.dataset_name}: {dataset.file_count}개 파일, {dataset.total_size_mb:.2f}MB")