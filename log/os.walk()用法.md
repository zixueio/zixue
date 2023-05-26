在Python中，`os.walk()`函数用于遍历目录树，并返回每个目录中的文件和子目录。它是一个非常有用的函数，常用于遍历目录结构，查找特定类型的文件，或执行对目录中的所有文件的批处理操作。

下面是`os.walk()`函数的用法示例：

```python
import os

# 遍历目录树
for root, dirs, files in os.walk('/path/to/directory'):
    # root表示当前目录的路径
    # dirs表示当前目录中的子目录列表
    # files表示当前目录中的文件列表
    
    # 遍历子目录
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        print("子目录:", dir_path)
    
    # 遍历文件
    for file in files:
        file_path = os.path.join(root, file)
        print("文件:", file_path)
```

在上面的示例中，我们使用`os.walk()`函数来遍历`/path/to/directory`目录及其子目录。在每次迭代中，我们获取当前目录的路径（`root`）、子目录列表（`dirs`）和文件列表（`files`）。然后，我们可以根据需要对这些目录和文件进行处理。

请注意，`os.walk()`函数是一个生成器（generator），因此它会动态地返回目录结构中的每个目录和文件。这使得它非常适合处理大型目录树，因为它一次只返回一个目录，而不是一次性将整个目录树加载到内存中。

希望这个示例可以帮助你理解`os.walk()`函数的用法！
