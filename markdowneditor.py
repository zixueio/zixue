import tkinter as tk
import os
import index
import re

def clean_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)

def save_text():
    filename = clean_filename(filename_entry.get("1.0", "end-1c").strip())
    text = text_entry.get("1.0", "end-1c")  # 获取文本框中的内容
    directory = "log"
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(os.path.join(directory, filename + ".md"), 'w', encoding='utf-8') as f:
        f.write(text)
    index.job()

    text_entry.delete("1.0", "end")  # 清空文本编辑器
    filename_entry.delete("1.0", "end")  # 清空文件名输入框



root = tk.Tk()
root.title("Markdown Editor")

tk.Label(root, text="File Name").grid(row=0)
tk.Label(root, text="Text").grid(row=1)

filename_entry = tk.Text(root, height=1)
text_entry = tk.Text(root)

filename_entry.grid(row=0, column=1)
text_entry.grid(row=1, column=1)

tk.Button(root, text='Save', command=save_text).grid(row=2, column=1, sticky=tk.W, pady=4)


root.mainloop()
