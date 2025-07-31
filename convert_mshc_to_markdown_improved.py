#!/usr/bin/env python3
"""
Microsoft Help Container (.mshc) to Markdown Converter using MarkItDown - Improved Version

This script converts all .mshc files in the wf directory to markdown format
using Microsoft's MarkItDown tool with better progress tracking and resume capability.
"""

import os
import time
from pathlib import Path
from markitdown import MarkItDown

def get_file_size_mb(file_path):
    """Get file size in MB"""
    return file_path.stat().st_size / (1024 * 1024)

def convert_mshc_files():
    """Convert all .mshc files in the wf directory to markdown"""
    
    # Set up paths
    wf_dir = Path("wf")
    output_dir = Path("wf_converted_markitdown")
    
    # Ensure output directory exists
    output_dir.mkdir(exist_ok=True)
    
    # Initialize MarkItDown
    md_converter = MarkItDown()
    
    # Find all .mshc files and sort by size (smallest first)
    mshc_files = list(wf_dir.glob("*.mshc"))
    mshc_files.sort(key=lambda x: x.stat().st_size)
    
    if not mshc_files:
        print("No .mshc files found in the wf directory")
        return
    
    print(f"Found {len(mshc_files)} .mshc files to convert")
    print("Processing files from smallest to largest...")
    print("-" * 60)
    
    # Convert each file
    converted_count = 0
    skipped_count = 0
    error_count = 0
    
    for i, mshc_file in enumerate(mshc_files, 1):
        file_size_mb = get_file_size_mb(mshc_file)
        output_filename = mshc_file.stem + ".md"
        output_path = output_dir / output_filename
        
        print(f"[{i}/{len(mshc_files)}] {mshc_file.name} ({file_size_mb:.1f} MB)")
        
        # Skip if already converted
        if output_path.exists():
            print(f"  [SKIP] Already converted")
            skipped_count += 1
            continue
        
        try:
            start_time = time.time()
            
            # Convert the file
            result = md_converter.convert(str(mshc_file))
            
            # Write the markdown content
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result.text_content)
            
            elapsed_time = time.time() - start_time
            output_size_mb = get_file_size_mb(output_path)
            
            print(f"  [OK] Converted in {elapsed_time:.1f}s -> {output_filename} ({output_size_mb:.1f} MB)")
            converted_count += 1
            
        except Exception as e:
            print(f"  [ERROR] {str(e)}")
            error_count += 1
            continue
    
    print("-" * 60)
    print(f"Conversion Summary:")
    print(f"  Converted: {converted_count}")
    print(f"  Skipped: {skipped_count}")
    print(f"  Errors: {error_count}")
    print(f"  Total: {len(mshc_files)}")
    print(f"\nResults saved in: {output_dir}")

def list_files_by_size():
    """List all .mshc files by size for reference"""
    wf_dir = Path("wf")
    mshc_files = list(wf_dir.glob("*.mshc"))
    mshc_files.sort(key=lambda x: x.stat().st_size)
    
    print("Available .mshc files (sorted by size):")
    print("-" * 60)
    for i, mshc_file in enumerate(mshc_files, 1):
        file_size_mb = get_file_size_mb(mshc_file)
        print(f"{i:2d}. {mshc_file.name:<30} ({file_size_mb:6.1f} MB)")

if __name__ == "__main__":
    # Change to the script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    print("Microsoft Help Container (.mshc) to Markdown Converter - Improved")
    print("=" * 70)
    
    # Show file list first
    list_files_by_size()
    print()
    
    # Ask for confirmation
    response = input("Proceed with conversion? (y/n): ").lower().strip()
    if response != 'y':
        print("Conversion cancelled.")
        exit(0)
    
    print()
    convert_mshc_files()