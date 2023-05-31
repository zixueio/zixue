当需要对包含时间信息的对象进行排序时，可以使用`sorted()`函数并结合`key`参数来指定排序的依据。下面是一个示例，演示如何按照时间从早到晚对包含时间字符串的列表进行排序：

```python
from datetime import datetime

timestamps = [
    "2023-05-28 09:30:00",
    "2023-05-29 14:45:00",
    "2023-05-27 12:00:00",
    "2023-05-30 08:15:00"
]

sorted_timestamps = sorted(timestamps, key=lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))

for timestamp in sorted_timestamps:
    print(timestamp)
```

输出结果：
```
2023-05-27 12:00:00
2023-05-28 09:30:00
2023-05-29 14:45:00
2023-05-30 08:15:00
```

在这个例子中，我们有一个包含时间字符串的列表 `timestamps`。通过使用`sorted()`函数和`key`参数，我们将时间字符串转换为`datetime`对象，并以此作为排序的依据。lambda函数`lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S")`将每个时间字符串`x`转换为对应的`datetime`对象。

最后，我们按照从早到晚的顺序打印输出了排序后的时间字符串列表`sorted_timestamps`。

需要注意的是，上述代码假设时间字符串的格式为`"%Y-%m-%d %H:%M:%S"`，如果实际情况中的时间格式不同，需要根据实际情况进行相应的调整。