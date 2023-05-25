from markdown import markdown
from pygments import highlight
from pygments. lexers import get_lexer_by_name
from pygments. formatters import HtmlFormatter

# Read text from Markdown file
with open ('example.md', 'r') as f:
    text = f.read ()

# Use the Markdown library to convert text to HTML
html = markdown (text)

# Use the Pygments library to obtain the highlighted lexer and formatter in Python syntax
lexer = get_lexer_by_name ("python", stripall = True)
formatter = HtmlFormatter ()

# Find all the code blocks in HTML and highlight them using the Pygments Library.
# Assume that the code block starts with 'Python and ends '''.
code_blocks = re.findall(r'```python(.*?)```', html, re.DOTALL)
for code in code_blocks:
    highlighted_code = highlight (code, lexer, formatter)
html = html. replace (f '``` python {code} ```', highlighted_code)

# Write HTML to a new file
with open('your_file.html ',' w ') as f:
    f. write (html)