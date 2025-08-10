# Additional Considerations:
# 1. Multiple Paragraphs
# 2. Tables
# 3. Multiple Tags

def render_html(parsed_text):
    """Render the parsed text as HTML."""
    html_output = ""

    for tag, content in parsed_text:
        if(tag == "link"):
            # Error handling for malformed links
            if "(" in content and "]" in content:
                text = content.split("]")[0].strip("[")
                link = content.split("(", 1)[1].strip(")")
                html_output += f"<a href='{link}'>{text}</a>"
            else:
                html_output += content  # fallback for malformed links
        elif(tag == "img"):
            text = content.split("]")[0].strip("[")
            image = content.split("(")[1].strip(")")
            html_output += f"<img src='{image}' alt='{text}'>"
        elif(tag == "hr"):
            html_output += "<hr>"
        elif(tag == "escape"):
            html_output += f"{content}"
        elif(tag == "table"):
            continue
        else:
            html_output += f"<{tag}>{content}</{tag}>"

    return html_output