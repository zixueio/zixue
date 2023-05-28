在Linux中，你可以使用`mv`命令来修改文件名。`mv`命令既可以用于移动文件，也可以用于重命名文件。

以下是一些常见的用法示例：

1. **重命名文件**：
   ```bash
   mv old_filename new_filename
   ```
   将`old_filename`更改为`new_filename`，两者可以是相对路径或绝对路径。

2. **移动文件并重命名**：
   ```bash
   mv old_location/new_filename new_location/
   ```
   将位于`old_location`的文件移动到`new_location`目录，并将其重命名为`new_filename`。

3. **批量重命名文件**：
   ```bash
   rename 's/old_pattern/new_pattern/' file_pattern
   ```
   使用`rename`命令批量重命名符合`file_pattern`的文件。`old_pattern`是要被替换的模式，`new_pattern`是替换后的模式。可以使用正则表达式进行模式匹配和替换。

请注意，在执行文件重命名操作之前，请谨慎确认文件名和目录路径。误操作可能导致文件丢失或被覆盖。

此外，还有其他更高级的文件批量重命名工具和脚本，例如`mmv`、`renameutils`、`pyRenamer`等，它们提供更多灵活的选项和规则来处理文件重命名任务。

总之，通过使用`mv`命令或其他文件批量重命名工具，你可以在Linux中方便地修改文件名和文件位置。
