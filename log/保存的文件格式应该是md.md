如果你想要保存的文件具有`.md`扩展名，你可以在保存文件时添加扩展名。以下是修改后的代码：

```python
import tkinter as tk
import os

def save_text():
    filename = filename_entry.get()
    text = text_entry.get("1.0", "end-1c")  # 获取文本框中的内容
    with open(os.path.join("log", filename + ".md"), 'w') as f:
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

在这个版本的代码中，`save_text`函数将`.md`扩展名添加到了文件名后面，所以保存的文件将是Markdown文件。

记住，你仍然需要确保运行程序的当前目录下存在一个名为"log"的文件夹。如果不存在，需要手动创建，或者在代码中添加创建文件夹的逻辑。