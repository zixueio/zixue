import tkinter as tk
import os

def save_text():
    filename = filename_entry.get()
    text = text_entry.get("1.0", "end-1c")  # 获取文本框中的内容
    with open(os.path.join("log", filename + ".md"), 'w', encoding='utf-8') as f:
        f.write(text)

root = tk.Tk()
root.title("Markdown Editor")

tk.Label(root, text="File Name").grid(row=0)
tk.Label(root, text="Text").grid(row=1)

filename_entry = tk.Entry(root)
text_entry = tk.Text(root)

filename_entry.grid(row=0, column=1)
text_entry.grid(row=1, column=1)

tk.Button(root, text='Save', command=save_text).grid(row=2, column=1, sticky=tk.W, pady=4)

root.mainloop()
