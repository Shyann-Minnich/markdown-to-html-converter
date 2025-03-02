from markdown_converter import parser_markdown
from markdown_converter import render_html

def convert_markdown_to_html(file_path):
    """Reads a markdown file and returns its as an HTML file."""
    
    # Reads a markdown file and returns its content as a string. 
    with open(file_path, 'r') as file:
        return file.read()
    
    # Parse the markdown text
    parsed_text = parse_markdown(md_text)
    # Render the parsed text as HTML
    html_output = render_html(parsed_text)

    # Write the HTML output to a file
    with open('output.html', 'w') as file:
        file.write(html_output)

    if __name__ == '__main__':
        convert_markdown_to_html('examples/test_file_1.md')