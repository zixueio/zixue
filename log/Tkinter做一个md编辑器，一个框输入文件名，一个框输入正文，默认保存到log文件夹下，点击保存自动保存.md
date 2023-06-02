下面是一个简单的Markdown编辑器，用Python的Tkinter库创建。这个程序允许你输入文件名和文本内容，然后点击“保存”按钮将文本内容保存到指定的文件中。注意，该程序不会处理Markdown格式，只是简单地保存你输入的文本。

```python
import tkinter as tk
import os

def save_text():
    filename = filename_entry.get()
    text = text_entry.get("1.0", "end-1c")  # 获取文本框中的内容
    with open(os.path.join("log", filename), 'w') as f:
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

在这个程序中，我们首先创建了一个Tkinter窗口和两个标签、两个输入框以及一个按钮。一个输入框用于输入文件名，另一个用于输入文本。按钮关联了一个函数，该函数获取这两个输入框的内容，然后将文本写入指定的文件。

注意，你需要确保运行程序的当前目录下存在一个名为"log"的文件夹，如果不存在，需要手动创建，或者在代码中添加创建文件夹的逻辑。

还要注意，这个程序不会检查你输入的文件名是否有效或者该文件是否已经存在并可能被覆盖，如果你需要这些功能，你可能需要对代码进行一些修改。