from markdown import markdown
from pygments import highlight
from pygments. lexers import get_lexer_by_name
from pygments. formatters import HtmlFormatter
import re

def convert_md_to_html (md_text):
# Convert Markdown to HTML
html = markdown (md_text)

# Find code blocks
code_blocks = re. findall (r '<pre> <code class = "([^"] *) "> (. *?) </code> </pre> ', html, flags = re. DOTALL)

for lang, code in code_blocks:
# Remove 'language-' prefix from language name
lang = lang [9:]

# Highlight code
lexer = get_lexer_by_name (lang, stripall = True)
formatter = HtmlFormatter ()
code_highlighted = highlight (code, lexer, formatter)

# Replace original code block with highlighted code
html = html. replace ('<pre> <code class = "language-{}"> {} </code> </pre>'. format (lang, code), code_highlighted)

return html