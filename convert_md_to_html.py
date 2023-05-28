import os
import time
import markdown
import json

def convert_md_to_html(base_path,md_filename):
    try:
        with open('conversion_times.json', 'r') as f:
            conversion_times = json.load(f)
    except FileNotFoundError:
        conversion_times = {}

    # 获取文件的最后修改时间
    last_modified = os.path.getmtime(base_path)

    # 如果文件未被转换过，或者最后修改时间晚于最后转换时间，那么重新转换文件
    if md_filename not in conversion_times or last_modified > conversion_times[md_filename]:
        with open(base_path, 'r', encoding='utf-8') as f:
            md_text = f.read()
            html_text = markdown.markdown(md_text, extensions=['fenced_code'])
            html_filename = md_filename.replace('.md', '.html')
        html_path = os.path.join(os.path.dirname(base_path), html_filename)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write("<!DOCTYPE html>\n")
            f.write("<html>\n")
            f.write("<head>\n")
            f.write("<meta charset='UTF-8'>\n")
            f.write("</head>\n")
            f.write("<body>\n\n")

            f.write(html_text)

            f.write("</body>\n")
            f.write("</html>\n")

        # 更新文件的最后转换时间
        conversion_times[md_filename] = time.time()

    # 存储文件最后转换时间字典
    with open('conversion_times.json', 'w') as f:
        json.dump(conversion_times, f)