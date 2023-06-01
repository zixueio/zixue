Python自带的GUI（图形用户界面）库是Tkinter。它提供了Python程序员创建GUI应用程序的简单方法。

以下是一个简单的Tkinter程序的示例：

```python
import tkinter as tk

root = tk.Tk()  # 创建窗口对象的背景色
# 创建两个标签
w = tk.Label(root, text="Hello, world!")
w.pack()

# 运行事件循环
root.mainloop()
```

在这个例子中，我们首先导入Tkinter库，然后创建一个新的Tk窗口。然后我们创建一个Label，其文本是"Hello, world!"，并将其添加到窗口中。最后，我们启动Tkinter的事件循环。

Tkinter功能丰富，可以用来创建各种复杂的GUI应用程序，包括文本框、按钮、菜单、滚动条和其他许多组件。虽然它可能不如一些更现代的Python GUI库那样具有吸引力（如PyQt或wxPython），但它的优势在于其简单性和易用性，以及它作为Python标准库的一部分而不需要额外安装。