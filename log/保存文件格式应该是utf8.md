看起来你可能在输入文件名时误输入了换行符 `\n`，这可能是因为你在文件名输入框中按了"Enter"键。此外，你可能需要确保 "log" 文件夹存在于你的当前工作目录下。以下是更新后的代码，它将删除文件名中可能存在的换行符，并确保 "log" 文件夹存在：

```python
import tkinter as tk
import os

def save_text():
    filename = filename_entry.get().strip()  # 去掉可能的换行符或空格
    text = text_entry.get("1.0", "end-1c")  # 获取文本框中的内容
    directory = "log"
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(os.path.join(directory, filename + ".md"), 'w', encoding='utf-8') as f:
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
```

在上述代码中，我添加了 `.strip()` 方法来移除文件名两侧可能存在的空白字符（包括换行符）。另外，我添加了检查 "log" 文件夹是否存在的代码，如果不存在则会创建该文件夹。