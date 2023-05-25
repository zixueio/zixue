import markdown

# 打开Markdown文件并读取内容
with open('example.md', 'r', encoding='utf-8') as f:
    text = f.read()


# 使用markdown库将Markdown转换为HTML
html = markdown.markdown(text)

# 将HTML写入新的文件
with open('example.html', 'w',encoding='utf-8') as f:
    f.write(html)
