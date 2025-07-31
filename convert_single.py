#!/usr/bin/env python3
"""
Convert a single .mshc file to test the process
"""

import time
from pathlib import Path
from markitdown import MarkItDown

def convert_single_file(filename):
    """Convert a single .mshc file"""
    
    wf_dir = Path('wf')
    output_dir = Path('wf_converted_markitdown')
    output_dir.mkdir(exist_ok=True)
    
    md_converter = MarkItDown()
    mshc_file = wf_dir / filename
    output_path = output_dir / (mshc_file.stem + '.md')
    
    if not mshc_file.exists():
        print(f"File not found: {mshc_file}")
        return
    
    if output_path.exists():
        print(f"Already converted: {output_path}")
        return
    
    print(f"Converting {mshc_file.name}...")
    start_time = time.time()
    
    try:
        result = md_converter.convert(str(mshc_file))
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result.text_content)
        
        elapsed_time = time.time() - start_time
        file_size = output_path.stat().st_size / (1024 * 1024)
        print(f"Converted in {elapsed_time:.1f}s -> {output_path.name} ({file_size:.1f} MB)")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Convert the next file in the list
    convert_single_file("WF_PIVOT ANALYSIS.1.mshc")