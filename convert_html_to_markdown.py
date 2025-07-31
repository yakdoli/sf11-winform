import os
import glob
import re
from html2text import HTML2Text
from datetime import datetime

def convert_html_to_markdown(input_dir, output_dir):
    # HTML2Text 객체 생성 및 설정
    h = HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    
    # 입력 디렉토리의 모든 HTML 파일 찾기
    html_files = glob.glob(os.path.join(input_dir, "*.htm*"), recursive=False)
    
    # ASP, MVC 관련 파일 필터링
    filtered_html_files = [f for f in html_files if not any(term in os.path.basename(f).lower() for term in ['asp', 'mvc', 'aspx', 'razor', 'controller'])]
    
    for html_file in filtered_html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # 파일 내용에 '.Mvc'가 포함된 경우 제외
            if '.Mvc' in html_content:
                print(f"Skipped: {html_file} (contains .Mvc namespace)")
                continue
            
            # HTML을 마크다운으로 변환
            markdown_content = h.handle(html_content)
            
            # VB.NET 내용 삭제 처리
            markdown_content = re.sub(r'\*\*\[VB\.NET\]\*\*.*?(\n\n|$)', '', markdown_content, flags=re.DOTALL)
            
            # ms-xhelp 마크업 삭제 처리
            markdown_content = re.sub(r'\[\]\(ms-xhelp:///\?Id=[^\)]*\)', '', markdown_content)
            
            # ![](!package_url!) 패턴 삭제 처리
            markdown_content = re.sub(r'!\[\]\(!package_url!\)', '', markdown_content)
            
            # See [Zoom with Navigation Control](ms-xhelp:///?Id=...) 패턴 삭제 처리
            markdown_content = re.sub(r'See \[[^\]]*\]\(ms-xhelp:///\?Id=[^\)]*\)', '', markdown_content)
            
            # [Essential Studio User Guide Documentation](ms-xhelp:///?Id=...) > [Reporting Edition](ms-xhelp:///?Id=...) > ... 패턴 삭제 처리
            markdown_content = re.sub(r'\[[^\]]*\]\(ms-xhelp:///\?Id=[^\)]*\)(?: > \[[^\]]*\]\(ms-xhelp:///\?Id=[^\)]*\))*', '', markdown_content)
            
            # [](ms-xhelp:///?Id=...) > > "" > [](ms-xhelp:///?Id=...) > [](ms-xhelp:///?Id=...) 패턴 삭제 처리
            markdown_content = re.sub(r'\[\]\(ms-xhelp:///\?Id=[^\)]*\)(?: >(?: > "")?(?: > \[\]\(ms-xhelp:///\?Id=[^\)]*\))*)?', '', markdown_content)
            
            # C# 이외의 플랫폼 소스 삭제 처리
            markdown_content = re.sub(r'\*\*View\[aspx\]\*\*.*?(?:\n\n|$)', '', markdown_content, flags=re.DOTALL)
            markdown_content = re.sub(r'\*\*View\[cshtml\]\*\*.*?(?:\n\n|$)', '', markdown_content, flags=re.DOTALL)
            markdown_content = re.sub(r'\*\*\[Controller\]\*\*.*?(?:\n\n|$)', '', markdown_content, flags=re.DOTALL)
            markdown_content = re.sub(r'\*\*\[controller\]\*\*.*?(?:\n\n|$)', '', markdown_content, flags=re.DOTALL)
            markdown_content = re.sub(r'\*\*\[Controller\] \*\*.*?(?:\n\n|$)', '', markdown_content, flags=re.DOTALL)
            markdown_content = re.sub(r'\*\*\[ASPX\] \*\*.*?(?:\n\n|$)', '', markdown_content, flags=re.DOTALL)
            markdown_content = re.sub(r'\*\* \[Razor\] \*\*.*?(?:\n\n|$)', '', markdown_content, flags=re.DOTALL)
            markdown_content = re.sub(r'\*\* \[Controller\] \*\*.*?(?:\n\n|$)', '', markdown_content, flags=re.DOTALL)
            markdown_content = re.sub(r'\*\* \[ASPX\] \*\*.*?(?:\n\n|$)', '', markdown_content, flags=re.DOTALL)
            markdown_content = re.sub(r'\*\* \*\* \*\*\[Controller\] \*\* \*\*.*?(?:\n\n|$)', '', markdown_content, flags=re.DOTALL)
            markdown_content = re.sub(r'\*\*\[ASPX\]\*\*.*?(?:\n\n|$)', '', markdown_content, flags=re.DOTALL)
            markdown_content = re.sub(r'\*\*\[Javascirpt\]\*\*.*?(?:\n\n|$)', '', markdown_content, flags=re.DOTALL)
            markdown_content = re.sub(r'\*\*\[XAML\]\*\*.*?(?:\n\n|$)', '', markdown_content, flags=re.DOTALL)
            markdown_content = re.sub(r'\*\*XAML\*\*.*?(?:\n\n|$)', '', markdown_content, flags=re.DOTALL)
            markdown_content = re.sub(r'\*\*\[VB\]\*\*.*?(?:\n\n|$)', '', markdown_content, flags=re.DOTALL)
            
            # 인덱스 바로가기 마크업 삭제 처리
            markdown_content = re.sub(r'\[[^\]]*\]\(ms-xhelp:///\?Id=[^\)]*\)(?: > > [^\n]* > > \[[^\]]*\]\(ms-xhelp:///\?Id=[^\)]*\))', '', markdown_content)
            markdown_content = re.sub(r'\[[^\]]*\]\(ms-xhelp:///\?Id=[^\)]*\)(?: > > [^\n]* > \[[^\]]*\]\(ms-xhelp:///\?Id=[^\)]*\))', '', markdown_content)
            
            # 버튼 바로가기 마크업 삭제 처리
            markdown_content = re.sub(r'\[![\w\s]*\(button\.gif\)[^\]]*\]\(ms-xhelp:///\?Id=[^\)]*\)', '', markdown_content)
            
            # 이미지 마크업 삭제 처리
            markdown_content = re.sub(r'!\[\]\(ImagesExt/image\d+_\d+\.jpg\)', '', markdown_content)
            markdown_content = re.sub(r'!\[Description:[^\]]*\]\(ImagesExt/image\d+_\d+\.jpg\)', '', markdown_content)
            markdown_content = re.sub(r'Figure \d+:[^\n]*', '', markdown_content)
            
            # 파일 제목 추출 (파일명에서)
            title = os.path.basename(html_file).rsplit('.', 1)[0]
            
            # 생성 날짜 설정
            try:
                created_at = datetime.fromtimestamp(os.path.getctime(html_file)).strftime('%Y-%m-%d')
            except:
                created_at = '2025-07-04'
            
            # YAML 메타데이터 생성
            yaml_metadata = f"""---
title: {title}
original_path: {html_file}
created_at: {created_at}
---

"""
            final_content = yaml_metadata + markdown_content
            
            # 출력 파일 경로 생성
            relative_path = os.path.relpath(html_file, input_dir)
            markdown_file = os.path.join(output_dir, relative_path.rsplit('.', 1)[0] + '.md')
            
            # 출력 디렉토리 생성
            os.makedirs(os.path.dirname(markdown_file), exist_ok=True)
            
            # 마크다운 파일로 저장
            with open(markdown_file, 'w', encoding='utf-8') as f:
                f.write(final_content)
                
            print(f"Converted: {html_file} -> {markdown_file}")
            
        except Exception as e:
            print(f"Error converting file {html_file}: {e}")

if __name__ == "__main__":
    input_directory = 'wf/extracted'
    output_directory = 'WinForms_Docs_converted_wf'
    convert_html_to_markdown(input_directory, output_directory)
    print("Conversion complete.")
