#!/usr/bin/env python3
"""
Batch convert remaining .mshc files to markdown
"""

import time
from pathlib import Path
from markitdown import MarkItDown

def batch_convert_remaining():
    """Convert remaining .mshc files"""
    
    wf_dir = Path('wf')
    output_dir = Path('wf_converted_markitdown')
    output_dir.mkdir(exist_ok=True)
    
    md_converter = MarkItDown()
    
    # Get all .mshc files sorted by size
    mshc_files = list(wf_dir.glob("*.mshc"))
    mshc_files.sort(key=lambda x: x.stat().st_size)
    
    # Files to convert (remaining ones)
    remaining_files = [
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
    
    print(f"Converting {len(remaining_files)} remaining files...")
    print("-" * 60)
    
    for i, filename in enumerate(remaining_files, 1):
        mshc_file = wf_dir / filename
        output_path = output_dir / (mshc_file.stem + '.md')
        
        if not mshc_file.exists():
            print(f"[{i}/{len(remaining_files)}] File not found: {filename}")
            continue
            
        if output_path.exists():
            print(f"[{i}/{len(remaining_files)}] Already converted: {filename}")
            continue
        
        file_size_mb = mshc_file.stat().st_size / (1024 * 1024)
        print(f"[{i}/{len(remaining_files)}] Converting {filename} ({file_size_mb:.1f} MB)...")
        
        start_time = time.time()
        
        try:
            result = md_converter.convert(str(mshc_file))
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result.text_content)
            
            elapsed_time = time.time() - start_time
            output_size_mb = output_path.stat().st_size / (1024 * 1024)
            print(f"  [OK] Converted in {elapsed_time:.1f}s -> {output_path.name} ({output_size_mb:.1f} MB)")
            
        except Exception as e:
            print(f"  [ERROR] {str(e)}")
            continue
    
    print("-" * 60)
    print("Batch conversion complete!")

if __name__ == "__main__":
    batch_convert_remaining()