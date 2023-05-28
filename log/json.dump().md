`json.dump()`是Python标准库中`json`模块的一个函数，用于将Python对象序列化为JSON格式，并将其写入一个可写的文件对象中。

具体而言，`json.dump()`函数接受两个参数：

1. `obj`：要序列化为JSON并写入文件的Python对象。
2. `fp`：一个可写的文件对象，表示目标文件。

以下是函数的基本用法示例：

```python
import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# 打开文件对象并将数据写入JSON格式
with open("data.json", "w") as fp:
    json.dump(data, fp)
```

在上述示例中，我们创建了一个字典对象`data`，表示某些数据。然后，我们使用`json.dump()`将该字典对象写入名为`data.json`的文件中。`with`语句用于自动管理文件的打开和关闭。

执行以上代码后，`data.json`文件将包含序列化后的JSON数据，类似于以下内容：

```json
{"name": "John", "age": 30, "city": "New York"}
```

`json.dump()`函数将Python对象转换为JSON格式，并将其写入文件中。确保文件对象以可写模式打开，否则会引发IOError。

该函数的作用与`json.dumps()`函数类似，但是`json.dump()`直接将JSON数据写入文件，而`json.dumps()`将数据序列化为字符串。
