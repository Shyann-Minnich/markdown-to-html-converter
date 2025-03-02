def render_html(parsed_text):
    """Render the parsed text as HTML."""
    html_output = ""

    for tag, content in parsed_text:
        html_output += f"<{tag}>{content}</{tag}>"

    return html_output