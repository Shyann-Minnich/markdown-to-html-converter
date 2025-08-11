import re
import html 

def render_inline(text):
    """Converts Markdown inline elements in a string to their HTML equivalents."""
    # Images
    text = re.sub(r'!\[([^\]]+)\]\(([^\)]+)\)', r'<img src="\2" alt="\1">', text)
    # Links
    text = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', text)
    # Bold + Italic
    text = re.sub(r'\*\*\*([^\*]+)\*\*\*', r'<strong><em>\1</em></strong>', text)
    # Bold
    text = re.sub(r'\*\*([^\*]+)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*([^\*]+)\*', r'<em>\1</em>', text)
    # Strikethrough
    text = re.sub(r'~~([^~]+)~~', r'<del>\1</del>', text)
    # Inline code
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # Handle escaping: replace \* with *, \_ with _, etc.
    text = re.sub(r'\\([\\`*_{}\[\]()#+\-.!|])', r'\1', text)
    return text

def render_html(parsed_text):
    """Render the parsed text as HTML."""
    html_output = ""
    in_ul = False
    in_ol = False

    for tag, content in parsed_text:
        if tag == "h1":
            html_output += f"<h1>{render_inline(content)}</h1>"
        elif tag == "h2":
            html_output += f"<h2>{render_inline(content)}</h2>"
        elif tag == "h3":
            html_output += f"<h3>{render_inline(content)}</h3>"
        elif tag == "h4":
            html_output += f"<h4>{render_inline(content)}</h4>"
        elif tag == "h5":
            html_output += f"<h5>{render_inline(content)}</h5>"
        elif tag == "h6":
            html_output += f"<h6>{render_inline(content)}</h6>"
        elif tag == "ul_start":
            html_output += "<ul>"
            in_ul = True
        elif tag == "ul_end":
            html_output += "</ul>"
            in_ul = False
        elif tag == "ol_start":
            html_output += "<ol>"
            in_ol = True
        elif tag == "ol_end":
            html_output += "</ol>"
            in_ol = False
        elif tag == "li":
            html_output += f"<li>{render_inline(content)}</li>"
        elif tag == "blockquote":
            html_output += f"<blockquote>{render_inline(content)}</blockquote>"
        elif tag == "hr":
            html_output += "<hr>"
        elif tag == "codeblock":
            html_output += f"<pre><code>{html.escape(content)}</code></pre>"
        elif tag == "p":
            html_output += f"<p>{render_inline(content)}</p>"
        elif tag == "table":
            # Simple table rendering
            html_output += "<table>\n"
            for i, row in enumerate(content):
                cols = [c.strip() for c in row.strip().split('|')]
                cols = [c for c in cols if c]  # Remove empty columns
                if i == 0:
                    html_output += "<tr>" + "".join(f"<th>{render_inline(col)}</th>" for col in cols) + "</tr>\n"
                else:
                    html_output += "<tr>" + "".join(f"<td>{render_inline(col)}</td>" for col in cols) + "</tr>\n"
            html_output += "</table>\n"

    return html_output