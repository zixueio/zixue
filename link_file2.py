import os

def link_files(file1_path, file2_path):
    # 提取甲md文件的文件名
    file1_name = os.path.splitext(os.path.basename(file1_path))[0]

    # 读取乙md文件的内容
    with open(file2_path, 'r', encoding='utf-8') as file2:
        content = file2.read()

    # 查找甲md文件名在乙md文件中的位置
    start_index = content.find(file1_name)

    if start_index != -1:
        # 构建超链接
        link = f"[{file1_name}]({os.path.relpath(file1_path, os.path.dirname(file2_path))})"

        # 在乙md文件中插入超链接
        end_index = start_index + len(file1_name)
        content = content[:start_index] + link + content[end_index:]

        # 将修改后的内容写回乙md文件
        with open(file2_path, 'w', encoding='utf-8') as file2:
            file2.write(content)

link_files('b1.md','a.md')

