使用`Text`部件来替代`Entry`部件的确可以解决你的问题。`Text`部件支持多行文本输入，并且可以根据内容的多少自动调整大小。以下是如何修改你的代码来实现这个效果的例子：

```python
import tkinter as tk
import os
import index  # 引入index库

def save_text():
    filename = filename_entry.get("1.0", "end-1c").strip()  # 修改这里，从Text部件获取文本
    text = text_entry.get("1.0", "end-1c")
    directory = "log"
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(os.path.join(directory, filename + ".md"), 'w', encoding='utf-8') as f:
        f.write(text)
    
    index.job()  # 调用index库中的job函数

    text_entry.delete("1.0", "end")  # 清空文本编辑器
    filename_entry.delete("1.0", "end")  # 清空文件名输入框

root = tk.Tk()
root.title("Markdown Editor")

tk.Label(root, text="File Name").grid(row=0)
tk.Label(root, text="Text").grid(row=1)

filename_entry = tk.Text(root, height=1)  # 修改这里，使用Text部件代替Entry部件
text_entry = tk.Text(root)

filename_entry.grid(row=0, column=1)
text_entry.grid(row=1, column=1)

tk.Button(root, text='Save', command=save_text).grid(row=2, column=1, sticky=tk.W, pady=4)

root.mainloop()
```

在这个代码中，我将`filename_entry`部件从`Entry`部件改为`Text`部件，并且设置`height=1`以使它在没有文本时的高度和`Entry`部件相似。另外，我还修改了`save_text`函数，以使它可以从`Text`部件获取文件名。

然而，请注意，由于`Text`部件支持多行文本输入，用户可能会输入包含换行符的文件名，这可能会导致问题。你可能需要添加一些代码来处理这个问题，例如，通过使用`filename.replace('\n', '')`来删除文件名中的所有换行符。