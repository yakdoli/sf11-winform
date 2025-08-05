#!/usr/bin/env python3
"""
개선된 데이터셋 검증 및 품질 평가 스크립트
- 코드 스니펫/자연어 지침 구분 검증
- 데이터셋 품질 강화 검증
- 데이터 구조 최적화 검증
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import logging
from datetime import datetime
import statistics
import re
import difflib
import string
from collections import Counter
import unicodedata

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/improved_dataset_validation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ImprovedDatasetValidator:
    """개선된 데이터셋 검증기"""
    
    def __init__(self, dataset_dir: str = "unsloth_alpaca_datasets"):
        self.dataset_dir = Path(dataset_dir)
        self.validation_results = {}
        
        # 코드 블록 패턴
        self.code_block_pattern = r'```(\w+)?\s*\n(.*?)```'
        
        # 품질 검사 기준
        self.quality_thresholds = {
            'min_instruction_length': 10,
            'max_instruction_length': 500,
            'min_output_length': 50,
            'max_output_length': 10000,
            'min_code_blocks': 0,
            'max_code_blocks': 10,
            'min_code_lines': 1,
            'max_code_lines': 1000,
            'similarity_threshold': 0.8
        }
    
    def validate_dataset_structure(self, dataset_name: str) -> Dict[str, Any]:
        """데이터셋 구조 검증"""
        logger.info(f"데이터셋 구조 검증 시작: {dataset_name}")
        
        dataset_path = self.dataset_dir / f"{dataset_name}.json"
        if not dataset_path.exists():
            return {"error": f"데이터셋 파일不存在: {dataset_path}"}
        
        try:
            with open(dataset_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            return {"error": f"JSON 파싱 오류: {e}"}
        except Exception as e:
            return {"error": f"파일 읽기 오류: {e}"}
        
        # 기본 구조 검증
        if not isinstance(data, list):
            return {"error": "데이터셋은 리스트 형태여야 합니다"}
        
        validation_result = {
            "dataset_name": dataset_name,
            "total_items": len(data),
            "structure_issues": [],
            "quality_metrics": {},
            "code_block_analysis": {},
            "sample_items": [],
            "quality_score": 0.0
        }
        
        # 데이터 구조 검증
        required_fields = self._get_required_fields(dataset_name)
        
        for i, item in enumerate(data[:100]):  # 첫 100개 항목만 검증
            if not isinstance(item, dict):
                validation_result["structure_issues"].append(f"항목 {i}: 딕셔너리 형태가 아님")
                continue
            
            # 필수 필드 검증
            missing_fields = [field for field in required_fields if field not in item]
            if missing_fields:
                validation_result["structure_issues"].append(f"항목 {i}: 필수 필드 누락 - {missing_fields}")
            
            # 샘플 아이템 저장
            if i < 3:
                validation_result["sample_items"].append({
                    "index": i,
                    "keys": list(item.keys()),
                    "instruction_preview": item.get("instruction", "")[:100] + "..." if item.get("instruction") else "",
                    "output_preview": item.get("output", "")[:100] + "..." if item.get("output") else "",
                    "has_code_blocks": "code_blocks" in item and len(item["code_blocks"]) > 0,
                    "code_block_count": len(item.get("code_blocks", []))
                })
        
        # 품질 메트릭 계산
        validation_result["quality_metrics"] = self._calculate_quality_metrics(data, dataset_name)
        
        # 코드 블록 분석
        validation_result["code_block_analysis"] = self._analyze_code_blocks(data)
        
        # 품질 점수 계산
        validation_result["quality_score"] = self._calculate_quality_score(validation_result)
        
        logger.info(f"데이터셋 구조 검증 완료: {dataset_name}")
        return validation_result
    
    def _get_required_fields(self, dataset_name: str) -> List[str]:
        """데이터셋별 필수 필드 정의"""
        if dataset_name == "improved_unsloth_format":
            return ["instruction", "input", "output", "category", "metadata"]
        elif dataset_name == "improved_alpaca_format":
            return ["instruction", "input", "output"]
        elif dataset_name == "improved_unified_format":
            return ["instruction", "input", "output", "text", "category", "subcategory", "difficulty", "language", "metadata", "code_blocks", "description"]
        else:
            return ["instruction", "input", "output"]
    
    def _calculate_quality_metrics(self, data: List[Dict[str, Any]], dataset_name: str) -> Dict[str, Any]:
        """품질 메트릭 계산"""
        if not data:
            return {}
        
        metrics = {}
        
        # instruction 분석
        instructions = [item.get("instruction", "") for item in data if item.get("instruction")]
        if instructions:
            metrics["instruction_stats"] = {
                "total": len(instructions),
                "empty_count": sum(1 for inst in instructions if not inst.strip()),
                "avg_length": statistics.mean(len(inst) for inst in instructions),
                "max_length": max(len(inst) for inst in instructions),
                "min_length": min(len(inst) for inst in instructions),
                "length_distribution": self._get_length_distribution(instructions)
            }
        
        # output 분석
        outputs = [item.get("output", "") for item in data if item.get("output")]
        if outputs:
            metrics["output_stats"] = {
                "total": len(outputs),
                "empty_count": sum(1 for out in outputs if not out.strip()),
                "avg_length": statistics.mean(len(out) for out in outputs),
                "max_length": max(len(out) for out in outputs),
                "min_length": min(len(out) for out in outputs),
                "length_distribution": self._get_length_distribution(outputs)
            }
        
        # 카테고리 분포
        categories = [item.get("category", "unknown") for item in data if item.get("category")]
        if categories:
            category_counts = Counter(categories)
            metrics["category_distribution"] = dict(category_counts)
            metrics["category_balance"] = self._calculate_balance_score(category_counts)
        
        # 난이도 분포 (improved_unified_format인 경우)
        if dataset_name == "improved_unified_format":
            difficulties = [item.get("difficulty", "unknown") for item in data if item.get("difficulty")]
            if difficulties:
                difficulty_counts = Counter(difficulties)
                metrics["difficulty_distribution"] = dict(difficulty_counts)
                metrics["difficulty_balance"] = self._calculate_balance_score(difficulty_counts)
        
        # 언어 분포
        languages = [item.get("language", "unknown") for item in data if item.get("language")]
        if languages:
            language_counts = Counter(languages)
            metrics["language_distribution"] = dict(language_counts)
        
        return metrics
    
    def _get_length_distribution(self, texts: List[str]) -> Dict[str, int]:
        """길이 분포 계산"""
        distribution = {
            "very_short": sum(1 for text in texts if len(text) < 50),
            "short": sum(1 for text in texts if 50 <= len(text) < 200),
            "medium": sum(1 for text in texts if 200 <= len(text) < 800),
            "long": sum(1 for text in texts if 800 <= len(text) < 2000),
            "very_long": sum(1 for text in texts if len(text) >= 2000)
        }
        return distribution
    
    def _calculate_balance_score(self, counts: Counter) -> float:
        """분포 균형 점수 계산 (0-1 사이, 1에 가까울수록 균형)"""
        if len(counts) <= 1:
            return 1.0
        
        values = list(counts.values())
        max_count = max(values)
        min_count = min(values)
        
        # 변동 계수 기반 균형 점수
        mean = statistics.mean(values)
        std = statistics.stdev(values) if len(values) > 1 else 0
        
        if mean == 0:
            return 1.0
        
        cv = std / mean
        balance_score = max(0, 1 - cv)
        return round(balance_score, 3)
    
    def _analyze_code_blocks(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """코드 블록 분석"""
        code_analysis = {
            "total_items": len(data),
            "items_with_code_blocks": 0,
            "items_without_code_blocks": 0,
            "code_block_stats": {
                "total_code_blocks": 0,
                "avg_code_blocks_per_item": 0,
                "max_code_blocks_per_item": 0,
                "min_code_blocks_per_item": 0
            },
            "language_distribution": {},
            "code_length_distribution": {
                "very_short": 0,
                "short": 0,
                "medium": 0,
                "long": 0,
                "very_long": 0
            },
            "quality_issues": []
        }
        
        code_block_counts = []
        
        for item in data:
            code_blocks = item.get("code_blocks", [])
            code_block_count = len(code_blocks)
            code_block_counts.append(code_block_count)
            
            if code_block_count > 0:
                code_analysis["items_with_code_blocks"] += 1
            else:
                code_analysis["items_without_code_blocks"] += 1
            
            code_analysis["code_block_stats"]["total_code_blocks"] += code_block_count
            
            # 코드 블록 언어 분석
            for code_block in code_blocks:
                language = code_block.get("language", "unknown")
                code_analysis["language_distribution"][language] = code_analysis["language_distribution"].get(language, 0) + 1
                
                # 코드 길이 분석
                code_length = len(code_block.get("code", ""))
                if code_length < 10:
                    code_analysis["code_length_distribution"]["very_short"] += 1
                elif code_length < 50:
                    code_analysis["code_length_distribution"]["short"] += 1
                elif code_length < 200:
                    code_analysis["code_length_distribution"]["medium"] += 1
                elif code_length < 1000:
                    code_analysis["code_length_distribution"]["long"] += 1
                else:
                    code_analysis["code_length_distribution"]["very_long"] += 1
        
        # 통계 계산
        if code_block_counts:
            code_analysis["code_block_stats"]["avg_code_blocks_per_item"] = round(statistics.mean(code_block_counts), 2)
            code_analysis["code_block_stats"]["max_code_blocks_per_item"] = max(code_block_counts)
            code_analysis["code_block_stats"]["min_code_blocks_per_item"] = min(code_block_counts)
        
        return code_analysis
    
    def _calculate_quality_score(self, validation_result: Dict[str, Any]) -> float:
        """품질 점수 계산 (0-100 사이)"""
        score = 100.0
        
        # 구조 문제 점수 감소
        structure_issues = len(validation_result.get("structure_issues", []))
        score -= structure_issues * 2
        
        # 코드 블록 품질 점수
        code_analysis = validation_result.get("code_block_analysis", {})
        if code_analysis:
            code_coverage = code_analysis.get("items_with_code_blocks", 0) / code_analysis.get("total_items", 1)
            score += code_coverage * 10  # 코드 블록이 있으면 점수 추가
        
        # 카테고리 균형 점수
        quality_metrics = validation_result.get("quality_metrics", {})
        if "category_balance" in quality_metrics:
            score += quality_metrics["category_balance"] * 20
        
        # 난이도 균형 점수
        if "difficulty_balance" in quality_metrics:
            score += quality_metrics["difficulty_balance"] * 20
        
        # 길이 분포 점수
        if "instruction_stats" in quality_metrics:
            inst_dist = quality_metrics["instruction_stats"].get("length_distribution", {})
            if inst_dist.get("medium", 0) > 0:
                score += 10
        
        if "output_stats" in quality_metrics:
            out_dist = quality_metrics["output_stats"].get("length_distribution", {})
            if out_dist.get("medium", 0) > 0 or out_dist.get("long", 0) > 0:
                score += 10
        
        # 최소 점수 보장
        return max(0, min(100, round(score, 2)))
    
    def validate_all_datasets(self) -> Dict[str, Any]:
        """모든 데이터셋 검증"""
        logger.info("모든 개선된 데이터셋 검증 시작")
        
        dataset_files = ["improved_unsloth_format", "improved_alpaca_format", "improved_unified_format"]
        all_results = {}
        
        for dataset_name in dataset_files:
            result = self.validate_dataset_structure(dataset_name)
            all_results[dataset_name] = result
        
        # 종합 검증 결과 생성
        summary = self._generate_validation_summary(all_results)
        all_results["summary"] = summary
        
        logger.info("모든 개선된 데이터셋 검증 완료")
        return all_results
    
    def _generate_validation_summary(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """검증 요약 생성"""
        summary = {
            "validation_timestamp": datetime.now().isoformat(),
            "total_datasets": len(results) - 1,  # summary 제외
            "valid_datasets": 0,
            "invalid_datasets": 0,
            "total_items": 0,
            "average_quality_score": 0.0,
            "common_issues": [],
            "recommendations": []
        }
        
        quality_scores = []
        
        for dataset_name, result in results.items():
            if dataset_name == "summary":
                continue
            
            if "error" in result:
                summary["invalid_datasets"] += 1
                summary["common_issues"].append(f"{dataset_name}: {result['error']}")
            else:
                summary["valid_datasets"] += 1
                summary["total_items"] += result.get("total_items", 0)
                
                # 품질 점수 계산
                quality_score = result.get("quality_score", 0)
                quality_scores.append(quality_score)
                
                # 공통 이슈 분석
                if result.get("structure_issues"):
                    summary["common_issues"].extend(result["structure_issues"][:3])  # 상위 3개만
        
        # 평균 품질 점수 계산
        if quality_scores:
            summary["average_quality_score"] = round(statistics.mean(quality_scores), 2)
        
        # 추천 사항 생성
        if summary["invalid_datasets"] > 0:
            summary["recommendations"].append("데이터셋 구조를 수정해야 합니다")
        
        if summary["total_items"] == 0:
            summary["recommendations"].append("데이터셋이 비어있거나 유효하지 않습니다")
        
        if summary["average_quality_score"] < 70:
            summary["recommendations"].append("데이터 품질 개선이 필요합니다")
        
        return summary
    
    def save_validation_report(self, results: Dict[str, Any], filename: str = "improved_validation_report.json"):
        """검증 보고서 저장"""
        report_path = self.dataset_dir / filename
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        logger.info(f"개선된 검증 보고서 저장 완료: {report_path}")
    
    def generate_html_report(self, results: Dict[str, Any], filename: str = "improved_validation_report.html"):
        """HTML 보고서 생성"""
        html_content = self._generate_html_content(results)
        
        report_path = self.dataset_dir / filename
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        logger.info(f"개선된 HTML 보고서 저장 완료: {report_path}")
    
    def _generate_html_content(self, results: Dict[str, Any]) -> str:
        """HTML 보고서 내용 생성"""
        summary = results.get("summary", {})
        
        html = f"""
        <!DOCTYPE html>
        <html lang="ko">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>개선된 데이터셋 검증 보고서</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .header {{ background-color: #f0f0f0; padding: 20px; border-radius: 5px; }}
                .summary {{ background-color: #e8f5e8; padding: 15px; margin: 20px 0; border-radius: 5px; }}
                .dataset {{ border: 1px solid #ddd; margin: 20px 0; padding: 15px; border-radius: 5px; }}
                .quality-high {{ background-color: #d4edda; }}
                .quality-medium {{ background-color: #fff3cd; }}
                .quality-low {{ background-color: #f8d7da; }}
                .metrics {{ display: flex; flex-wrap: wrap; gap: 20px; margin: 10px 0; }}
                .metric {{ background-color: #f8f9fa; padding: 10px; border-radius: 3px; min-width: 150px; }}
                .code-analysis {{ background-color: #e3f2fd; padding: 15px; margin: 10px 0; border-radius: 5px; }}
                .issues {{ background-color: #ffebee; padding: 15px; margin: 10px 0; border-radius: 5px; }}
                .recommendations {{ background-color: #e8f5e8; padding: 15px; margin: 10px 0; border-radius: 5px; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>개선된 데이터셋 검증 보고서</h1>
                <p>검증 시간: {summary.get('validation_timestamp', 'N/A')}</p>
            </div>
            
            <div class="summary">
                <h2>종합 요약</h2>
                <div class="metrics">
                    <div class="metric">
                        <strong>총 데이터셋 수:</strong> {summary.get('total_datasets', 0)}
                    </div>
                    <div class="metric">
                        <strong>유효한 데이터셋:</strong> {summary.get('valid_datasets', 0)}
                    </div>
                    <div class="metric">
                        <strong>유효하지 않은 데이터셋:</strong> {summary.get('invalid_datasets', 0)}
                    </div>
                    <div class="metric">
                        <strong>총 데이터 항목 수:</strong> {summary.get('total_items', 0)}
                    </div>
                    <div class="metric">
                        <strong>평균 품질 점수:</strong> {summary.get('average_quality_score', 0)}
                    </div>
                </div>
            </div>
        """
        
        # 개별 데이터셋 정보
        for dataset_name, result in results.items():
            if dataset_name == "summary":
                continue
            
            quality_score = result.get("quality_score", 0)
            quality_class = "quality-high" if quality_score >= 80 else "quality-medium" if quality_score >= 60 else "quality-low"
            
            html += f"""
            <div class="dataset {quality_class}">
                <h2>{dataset_name.upper()}</h2>
                <div class="metrics">
                    <div class="metric">
                        <strong>품질 점수:</strong> {quality_score}
                    </div>
                    <div class="metric">
                        <strong>항목 수:</strong> {result.get('total_items', 0)}
                    </div>
                    <div class="metric">
                        <strong>구조 이슈:</strong> {len(result.get('structure_issues', []))}
                    </div>
                </div>
            """
            
            # 코드 블록 분석
            code_analysis = result.get('code_block_analysis', {})
            if code_analysis:
                html += f"""
                <div class="code-analysis">
                    <h3>코드 블록 분석</h3>
                    <div class="metrics">
                        <div class="metric">
                            <strong>코드 블록 포함 항목:</strong> {code_analysis.get('items_with_code_blocks', 0)}
                        </div>
                        <div class="metric">
                            <strong>평균 코드 블록 수:</strong> {code_analysis.get('code_block_stats', {}).get('avg_code_blocks_per_item', 0)}
                        </div>
                        <div class="metric">
                            <strong>코드 블언어 수:</strong> {len(code_analysis.get('language_distribution', {}))}
                        </div>
                    </div>
                </div>
                """
            
            # 이슈
            if result.get('structure_issues'):
                html += """
                <div class="issues">
                    <h3>구조 이슈</h3>
                    <ul>
                """
                for issue in result['structure_issues'][:5]:  # 상위 5개만
                    html += f"<li>{issue}</li>"
                html += "</ul></div>"
            
            html += "</div>"
        
        # 추천 사항
        if summary.get('recommendations'):
            html += """
            <div class="recommendations">
                <h2>추천 사항</h2>
                <ul>
            """
            for rec in summary['recommendations']:
                html += f"<li>{rec}</li>"
            html += "</ul></div>"
        
        html += """
        </body>
        </html>
        """
        
        return html

def main():
    """메인 함수"""
    validator = ImprovedDatasetValidator()
    
    try:
        # 모든 개선된 데이터셋 검증
        validation_results = validator.validate_all_datasets()
        
        # 검증 보고서 저장
        validator.save_validation_report(validation_results)
        validator.generate_html_report(validation_results)
        
        # 결과 출력
        print("\n" + "="*60)
        print("개선된 데이터셋 검증 결과")
        print("="*60)
        
        summary = validation_results.get("summary", {})
        print(f"검증 시간: {summary.get('validation_timestamp', 'N/A')}")
        print(f"총 데이터셋 수: {summary.get('total_datasets', 0)}")
        print(f"유효한 데이터셋: {summary.get('valid_datasets', 0)}")
        print(f"유효하지 않은 데이터셋: {summary.get('invalid_datasets', 0)}")
        print(f"총 데이터 항목 수: {summary.get('total_items', 0)}")
        print(f"평균 품질 점수: {summary.get('average_quality_score', 0)}")
        
        if summary.get("common_issues"):
            print("\n주요 이슈:")
            for issue in summary["common_issues"][:5]:  # 상위 5개만
                print(f"  - {issue}")
        
        if summary.get("recommendations"):
            print("\n추천 사항:")
            for rec in summary["recommendations"]:
                print(f"  - {rec}")
        
        # 개별 데이터셋 상세 정보
        print("\n" + "="*60)
        print("개별 데이터셋 상세 정보")
        print("="*60)
        
        for dataset_name, result in validation_results.items():
            if dataset_name == "summary":
                continue
            
            print(f"\n{dataset_name.upper()}:")
            if "error" in result:
                print(f"  상태: 오류 - {result['error']}")
            else:
                print(f"  상태: 유효")
                print(f"  항목 수: {result.get('total_items', 0)}")
                print(f"  품질 점수: {result.get('quality_score', 0)}")
                print(f"  구조 이슈: {len(result.get('structure_issues', []))}")
                
                # 코드 블록 분석
                code_analysis = result.get('code_block_analysis', {})
                if code_analysis:
                    print(f"  코드 블록 포함 항목: {code_analysis.get('items_with_code_blocks', 0)}")
                    print(f"  평균 코드 블록 수: {code_analysis.get('code_block_stats', {}).get('avg_code_blocks_per_item', 0)}")
                
                # 품질 메트릭
                quality = result.get('quality_metrics', {})
                if quality:
                    print(f"  품질 메트릭:")
                    if 'instruction_stats' in quality:
                        inst_stats = quality['instruction_stats']
                        print(f"    - Instruction 평균 길이: {inst_stats.get('avg_length', 0):.1f}")
                        print(f"    - Instruction 최대 길이: {inst_stats.get('max_length', 0)}")
                    
                    if 'output_stats' in quality:
                        out_stats = quality['output_stats']
                        print(f"    - Output 평균 길이: {out_stats.get('avg_length', 0):.1f}")
                        print(f"    - Output 최대 길이: {out_stats.get('max_length', 0)}")
                    
                    if 'category_distribution' in quality:
                        cat_dist = quality['category_distribution']
                        print(f"    - 카테고리 분포: {dict(list(cat_dist.items())[:3])}...")  # 상위 3개만
        
        print("\n" + "="*60)
        print("개선된 검증 완료!")
        print("="*60)
        
    except Exception as e:
        logger.error(f"개선된 데이터셋 검증 실패: {e}")
        raise

if __name__ == "__main__":
    main()