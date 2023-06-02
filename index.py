import os
from convert_md_to_html import convert_md_to_html

unlist= ['venv','.idea','.git']
unfile = ['index.py','GitAutoPush.bat','Markdown Editor.html']

def job():
    current_folder_path = os.getcwd()
    index_file_path= os.path.join(current_folder_path,'index.html')

    with open(index_file_path,'w', encoding='utf-8') as f:
        f.write("<!DOCTYPE html>\n")
        f.write("<html>\n")
        f.write("<head>\n")
        f.write("<meta charset='UTF-8'>\n")
        f.write("</head>\n")
        f.write("<body>\n\n")

    traverse_folder(current_folder_path, index_file_path)

    with open(index_file_path, 'a', encoding='utf-8') as f:
        f.write("</body>\n")
        f.write("</html>\n")

def traverse_folder(path, d=None, index_file='index.html'):

    for root,dirs,files in os.walk(path):
        dirs[:] = [dir for dir in dirs if dir not in unlist]
        files[:] = [file_name for file_name in files if file_name not in unfile]
        if d not in unlist:
            for file_name in files:
                if file_name.endswith('.md'):
                    md_path = os.path.join(root,file_name)
                    convert_md_to_html(md_path,file_name)

    for root, dirs, files in os.walk(path):
        dirs[:] = [dir for dir in dirs if dir not in unlist]
        files[:] = [file_name for file_name in files if file_name not in unfile]
        if d not in unlist:
            for file_name in files:
                if file_name.endswith('.html'):
                    relative_path = os.path.relpath(os.path.join(root, file_name), os.path.dirname(index_file))
                    with open(index_file, 'a', encoding='utf-8') as f:
                        f.write(f"<p><a href='{relative_path}'>{relative_path}</a></p>\n")
