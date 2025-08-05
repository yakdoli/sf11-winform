import os
import re
from datetime import datetime
import glob

def process_markdown_file(file_path, output_dir):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove ms-xhelp links and other unnecessary markup
        content = re.sub(r'\[(.*?)\]\(ms-xhelp:\/\/.*?\)', r'\\1', content)
        content = re.sub(r'::::?.*\\n', '', content)
        content = re.sub(r'::::?.*', '', content)
        content = re.sub(r'{style=.*?}', '', content)
        content = re.sub(r'!\[.*?\]\(.*?\)', '', content)
        
        # Additional markup removal as specified by user
        content = re.sub(r'\\1\{.d2h_breadcrumbsNormal\}', '', content)
        content = re.sub(r'\\1\{#d2h_url_template\}\{#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"\}', '', content)
        content = re.sub(r'\\1\{#D2HPrevious .D2HPreviousEnabled\}', '', content)
        content = re.sub(r'\\1\{#D2HNext .D2HNextEnabled\}', '', content)
        content = re.sub(r'\[ \]\{#related-topics\}', '', content)
        content = re.sub(r'\\1', '', content)

        # Extract title from the first ## heading
        title_match = re.search(r'##\\s*(.*)', content)
        title = title_match.group(1).strip() if title_match else os.path.basename(file_path)

        # Clean up extra newlines
        content = re.sub(r'\\n{2,}', '\\n\\n', content)
        
        try:
            created_at = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d')
        except:
            created_at = '2025-07-04'

        # Create YAML metadata
        yaml_metadata = f"""---
title: {title}
original_path: {file_path}
created_at: {created_at}
---

"""
        new_content = yaml_metadata + content

        # Create new file path
        relative_path = os.path.relpath(file_path, 'WinForms_Docs')
        new_file_path = os.path.join(output_dir, relative_path)
        
        os.makedirs(os.path.dirname(new_file_path), exist_ok=True)

        with open(new_file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Processed: {file_path} -> {new_file_path}")

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

all_files = glob.glob("WinForms_Docs/**/*.md", recursive=True)
output_directory = 'WinForms_Docs_structured'

for file in all_files:
    process_markdown_file(file, output_directory)

print("Processing complete.")
