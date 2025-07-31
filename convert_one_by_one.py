#!/usr/bin/env python3
"""
Convert .mshc files one by one with progress tracking
"""

import time
from pathlib import Path
from markitdown import MarkItDown

def convert_next_file():
    """Convert the next unconverted file"""
    
    wf_dir = Path('wf')
    output_dir = Path('wf_converted_markitdown')
    output_dir.mkdir(exist_ok=True)
    
    md_converter = MarkItDown()
    
    # All files in order of size
    all_files = [   
        "WF_TOOLS.1.mshc",
        "WF_XLSIO.1.mshc"
    ]
    
    # Find the next file to convert
    for filename in all_files:
        mshc_file = wf_dir / filename
        output_path = output_dir / (mshc_file.stem + '.md')
        
        if not output_path.exists():
            file_size_mb = mshc_file.stat().st_size / (1024 * 1024)
            print(f"Converting {filename} ({file_size_mb:.1f} MB)...")
            
            start_time = time.time()
            
            try:
                result = md_converter.convert(str(mshc_file))
                
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(result.text_content)
                
                elapsed_time = time.time() - start_time
                output_size_mb = output_path.stat().st_size / (1024 * 1024)
                print(f"[OK] Converted in {elapsed_time:.1f}s -> {output_path.name} ({output_size_mb:.1f} MB)")
                return
                
            except Exception as e:
                print(f"[ERROR] {str(e)}")
                return
    
    print("All files have been converted!")

if __name__ == "__main__":
    convert_next_file()