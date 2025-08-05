#!/usr/bin/env python3
"""
데이터셋 검증 및 품질 평가 스크립트
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import logging
from datetime import datetime
import statistics
import re

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/dataset_validation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DatasetValidator:
    """데이터셋 검증기"""
    
    def __init__(self, dataset_dir: str = "unsloth_alpaca_datasets"):
        self.dataset_dir = Path(dataset_dir)
        self.validation_results = {}
        
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
            "sample_items": []
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
                    "output_preview": item.get("output", "")[:100] + "..." if item.get("output") else ""
                })
        
        # 품질 메트릭 계산
        validation_result["quality_metrics"] = self._calculate_quality_metrics(data, dataset_name)
        
        logger.info(f"데이터셋 구조 검증 완료: {dataset_name}")
        return validation_result
    
    def _get_required_fields(self, dataset_name: str) -> List[str]:
        """데이터셋별 필수 필드 정의"""
        if dataset_name == "unsloth_format":
            return ["instruction", "input", "output", "category", "metadata"]
        elif dataset_name == "alpaca_format":
            return ["instruction", "input", "output"]
        elif dataset_name == "unified_format":
            return ["instruction", "input", "output", "text", "category", "subcategory", "difficulty", "language", "metadata"]
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
                "min_length": min(len(inst) for inst in instructions)
            }
        
        # output 분석
        outputs = [item.get("output", "") for item in data if item.get("output")]
        if outputs:
            metrics["output_stats"] = {
                "total": len(outputs),
                "empty_count": sum(1 for out in outputs if not out.strip()),
                "avg_length": statistics.mean(len(out) for out in outputs),
                "max_length": max(len(out) for out in outputs),
                "min_length": min(len(out) for out in outputs)
            }
        
        # 카테고리 분포
        categories = [item.get("category", "unknown") for item in data if item.get("category")]
        if categories:
            category_counts = {}
            for cat in categories:
                category_counts[cat] = category_counts.get(cat, 0) + 1
            metrics["category_distribution"] = category_counts
        
        # 난이도 분포 (unified_format인 경우)
        if dataset_name == "unified_format":
            difficulties = [item.get("difficulty", "unknown") for item in data if item.get("difficulty")]
            if difficulties:
                difficulty_counts = {}
                for diff in difficulties:
                    difficulty_counts[diff] = difficulty_counts.get(diff, 0) + 1
                metrics["difficulty_distribution"] = difficulty_counts
        
        return metrics
    
    def validate_all_datasets(self) -> Dict[str, Any]:
        """모든 데이터셋 검증"""
        logger.info("모든 데이터셋 검증 시작")
        
        dataset_files = ["unsloth_format", "alpaca_format", "unified_format"]
        all_results = {}
        
        for dataset_name in dataset_files:
            result = self.validate_dataset_structure(dataset_name)
            all_results[dataset_name] = result
        
        # 종합 검증 결과 생성
        summary = self._generate_validation_summary(all_results)
        all_results["summary"] = summary
        
        logger.info("모든 데이터셋 검증 완료")
        return all_results
    
    def _generate_validation_summary(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """검증 요약 생성"""
        summary = {
            "validation_timestamp": datetime.now().isoformat(),
            "total_datasets": len(results) - 1,  # summary 제외
            "valid_datasets": 0,
            "invalid_datasets": 0,
            "total_items": 0,
            "common_issues": [],
            "recommendations": []
        }
        
        for dataset_name, result in results.items():
            if dataset_name == "summary":
                continue
            
            if "error" in result:
                summary["invalid_datasets"] += 1
                summary["common_issues"].append(f"{dataset_name}: {result['error']}")
            else:
                summary["valid_datasets"] += 1
                summary["total_items"] += result.get("total_items", 0)
                
                # 공통 이슈 분석
                if result.get("structure_issues"):
                    summary["common_issues"].extend(result["structure_issues"][:3])  # 상위 3개만
        
        # 추천 사항 생성
        if summary["invalid_datasets"] > 0:
            summary["recommendations"].append("데이터셋 구조를 수정해야 합니다")
        
        if summary["total_items"] == 0:
            summary["recommendations"].append("데이터셋이 비어있거나 유효하지 않습니다")
        
        return summary
    
    def save_validation_report(self, results: Dict[str, Any], filename: str = "validation_report.json"):
        """검증 보고서 저장"""
        report_path = self.dataset_dir / filename
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        logger.info(f"검증 보고서 저장 완료: {report_path}")

def main():
    """메인 함수"""
    validator = DatasetValidator()
    
    try:
        # 모든 데이터셋 검증
        validation_results = validator.validate_all_datasets()
        
        # 검증 보고서 저장
        validator.save_validation_report(validation_results)
        
        # 결과 출력
        print("\n" + "="*60)
        print("데이터셋 검증 결과")
        print("="*60)
        
        summary = validation_results.get("summary", {})
        print(f"검증 시간: {summary.get('validation_timestamp', 'N/A')}")
        print(f"총 데이터셋 수: {summary.get('total_datasets', 0)}")
        print(f"유효한 데이터셋: {summary.get('valid_datasets', 0)}")
        print(f"유효하지 않은 데이터셋: {summary.get('invalid_datasets', 0)}")
        print(f"총 데이터 항목 수: {summary.get('total_items', 0)}")
        
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
                print(f"  구조 이슈: {len(result.get('structure_issues', []))}")
                
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
        print("검증 완료!")
        print("="*60)
        
    except Exception as e:
        logger.error(f"데이터셋 검증 실패: {e}")
        raise

if __name__ == "__main__":
    main()