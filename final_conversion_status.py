#!/usr/bin/env python3
"""
Check conversion status and convert remaining large files
"""

from pathlib import Path

def check_conversion_status():
    """Check which files have been converted and which remain"""
    
    wf_dir = Path('wf')
    output_dir = Path('wf_converted_markitdown')
    
    # All .mshc files
    all_files = [
        "WF_CALCULATE.1.mshc",
        "WF_DICOM.1.mshc",
        "WF_SCRIPTING.1.mshc", 
        "WF_PDF VIEWER.1.mshc",
        "WF_SCHEDULE.1.mshc",
        "WF_PIVOT ANALYSIS.1.mshc",
        "WF_HTML UI.1.mshc",
        "WF_DOCIO.1.mshc",
        "WF_GROUPING.1.mshc",
        "WF_PDF.1.mshc",
        "WF_EDIT.1.mshc",
        "WF_CHART.1.mshc",
        "WF_DIAGRAM.1.mshc",
        "WF_GRID.1.mshc",
        "WF_TOOLS.1.mshc",
        "WF_XLSIO.1.mshc"
    ]
    
    print("Conversion Status Report")
    print("=" * 60)
    
    converted = []
    remaining = []
    
    for filename in all_files:
        mshc_file = wf_dir / filename
        output_path = output_dir / (mshc_file.stem + '.md')
        file_size_mb = mshc_file.stat().st_size / (1024 * 1024)
        
        if output_path.exists():
            output_size_mb = output_path.stat().st_size / (1024 * 1024)
            converted.append((filename, file_size_mb, output_size_mb))
            print(f"[DONE] {filename:<30} ({file_size_mb:6.1f} MB -> {output_size_mb:6.1f} MB)")
        else:
            remaining.append((filename, file_size_mb))
            print(f"[TODO] {filename:<30} ({file_size_mb:6.1f} MB)")
    
    print("-" * 60)
    print(f"Converted: {len(converted)}/{len(all_files)} files")
    print(f"Remaining: {len(remaining)} files")
    
    if remaining:
        total_remaining_mb = sum(size for _, size in remaining)
        print(f"Total remaining size: {total_remaining_mb:.1f} MB")
        print("\nRemaining files (largest first):")
        remaining.sort(key=lambda x: x[1], reverse=True)
        for filename, size_mb in remaining:
            print(f"  - {filename} ({size_mb:.1f} MB)")

if __name__ == "__main__":
    check_conversion_status()