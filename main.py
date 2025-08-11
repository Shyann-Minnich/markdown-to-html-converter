import sys
from markdown_converter.parser import parse_markdown
from markdown_converter.render import render_html

def convert_markdown_to_html(file_path):
    """Reads a markdown file and returns its as an HTML file."""
    
    # Reads a markdown file and returns its content as a string. 
    with open(file_path, 'r') as file:
        md_text =  file.read()
    
    # Parse the markdown text
    parsed_text = parse_markdown(md_text)
    # Render the parsed text as HTML
    html_body = render_html(parsed_text)
    full_html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Converted Markdown</title>
</head>
<body>
{html_body}
</body>
</html>
"""

    # Write the HTML output to a file
    with open('output.html', 'w') as file:
        file.write(full_html)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        convert_markdown_to_html(sys.argv[1])
    else:
        print("Usage: python main.py <path_to_markdown_file>")
        sys.exit(1)