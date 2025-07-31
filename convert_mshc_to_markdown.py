#!/usr/bin/env python3
"""
Microsoft Help Container (.mshc) to Markdown Converter using MarkItDown

This script converts all .mshc files in the wf directory to markdown format
using Microsoft's MarkItDown tool.
"""

import os
import glob
from pathlib import Path
from markitdown import MarkItDown

def convert_mshc_files():
    """Convert all .mshc files in the wf directory to markdown"""
    
    # Set up paths
    wf_dir = Path("wf")
    output_dir = Path("wf_converted_markitdown")
    
    # Ensure output directory exists
    output_dir.mkdir(exist_ok=True)
    
    # Initialize MarkItDown
    md_converter = MarkItDown()
    
    # Find all .mshc files
    mshc_files = list(wf_dir.glob("*.mshc"))
    
    if not mshc_files:
        print("No .mshc files found in the wf directory")
        return
    
    print(f"Found {len(mshc_files)} .mshc files to convert")
    
    # Convert each file
    for mshc_file in mshc_files:
        try:
            print(f"Converting: {mshc_file.name}")
            
            # Create output filename
            output_filename = mshc_file.stem + ".md"
            output_path = output_dir / output_filename
            
            # Convert the file
            result = md_converter.convert(str(mshc_file))
            
            # Write the markdown content
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result.text_content)
            
            print(f"  [OK] Converted to: {output_path}")
            
        except Exception as e:
            print(f"  [ERROR] Error converting {mshc_file.name}: {str(e)}")
            continue
    
    print(f"\nConversion complete! Check the '{output_dir}' directory for results.")

if __name__ == "__main__":
    # Change to the script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    print("Microsoft Help Container (.mshc) to Markdown Converter")
    print("=" * 60)
    
    convert_mshc_files()