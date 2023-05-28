在Python中，with语句可以用来自动管理资源，例如文件、网络连接、数据库连接等。使用with语句可以避免手动关闭资源的繁琐，同时也可以确保资源在使用完毕后被正确地关闭，从而防止资源泄漏和错误。

with语句的一般语法如下：

```
with expression [as variable]:
    with-block
```

其中，expression表示要使用的资源，如文件对象或网络连接对象等；with-block表示使用资源的代码块。在with语句执行完毕后，Python会自动调用资源的`__exit__`方法来释放资源。

例如，使用with语句来读取一个文件：

```python
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)
```

在这个例子中，`open('file.txt', 'r')`返回一个文件对象，with语句将该文件对象赋值给变量f。在with-block中，我们使用f来读取文件内容，并将其打印到控制台上。当with语句执行完毕后，Python会自动关闭文件对象并释放资源。

除了文件对象，with语句还可以用于其它类型的资源，例如网络连接对象、数据库连接对象等。例如，使用with语句来连接MySQL数据库：

```python
import mysql.connector

config = {
  'user': 'username',
  'password': 'password',
  'host': 'localhost',
  'database': 'mydatabase'
}

with mysql.connector.connect(**config) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
```

在这个例子中，`mysql.connector.connect(**config)`返回一个MySQL连接对象，with语句将该连接对象赋值给变量conn。在with-block中，我们使用conn创建一个游标对象，并使用该游标对象执行SQL查询，并将结果打印到控制台上。当with语句执行完毕后，Python会自动关闭连接对象并释放资源。

总之，使用with语句可以方便地管理资源，避免手动关闭资源的繁琐，同时也可以确保资源在使用完毕后被正确地关闭，从而防止资源泄漏和错误。在Python中，with语句广泛应用于文件、网络连接、数据库连接等资源的管理。