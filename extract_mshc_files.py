import os
import zipfile
import glob
import shutil

def extract_mshc_files(input_dir, output_dir):
    # MSHC 파일 찾기
    mshc_files = glob.glob(os.path.join(input_dir, "*.mshc"))
    
    for mshc_file in mshc_files:
        print(f"Extracting: {mshc_file}")
        with zipfile.ZipFile(mshc_file, 'r') as zip_ref:
            # MSHC 파일 내의 HTML 파일을 추출
            for file in zip_ref.namelist():
                if file.endswith('.htm') or file.endswith('.html'):
                    zip_ref.extract(file, output_dir)
                    print(f"Extracted: {file}")
    
    print("Extraction complete.")

if __name__ == "__main__":
    input_directory = 'wf'
    output_directory = 'wf/extracted'
    os.makedirs(output_directory, exist_ok=True)
    extract_mshc_files(input_directory, output_directory)
