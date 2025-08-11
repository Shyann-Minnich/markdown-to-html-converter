import re

def parse_markdown(md_text):
    """Parse Markdown text and return a tuple."""
    parsed_text = []
    lines = md_text.splitlines()
    in_ul = False
    in_ol = False
    in_code_block = False
    code_block_lines = []
    table_lines = []
    in_table = False

    for line in lines:
        # Code Blocks
        if line.strip().startswith("```"):
            if not in_code_block:
                in_code_block = True
                code_block_lines = []
            else:
                in_code_block = False
                parsed_text.append(('codeblock', '\n'.join(code_block_lines)))
            continue
        if in_code_block:
            code_block_lines.append(line)
            continue

        # Table
        if "|" in line:
            # Skip separator lines like |----|----|
            if re.match(r'^\s*\|?[- ]+\|?[- |]*$', line):
                continue
            if not in_table:
                table_lines = []
                in_table = True
            table_lines.append(line)
            continue
        elif in_table:
            parsed_text.append(('table', table_lines))
            table_lines = []
            in_table = False

        # Headings
        if line.startswith('######'):
            parsed_text.append(('h6', line[6:].strip()))
        elif line.startswith('#####'):
            parsed_text.append(('h5', line[5:].strip()))
        elif line.startswith('####'):
            parsed_text.append(('h4', line[4:].strip()))
        elif line.startswith('###'):
            parsed_text.append(('h3', line[3:].strip()))
        elif line.startswith('##'):
            parsed_text.append(('h2', line[2:].strip()))
        elif line.startswith('#'):
            parsed_text.append(('h1', line[1:].strip()))

        # Blockquotes
        elif line.startswith('>'):
            parsed_text.append(('blockquote', line[1:].strip()))

        # Unordered list
        elif re.match(r'[*+-] ', line):
            if not in_ul:
                parsed_text.append(('ul_start', None))
                in_ul = True
            parsed_text.append(('li', line[2:].strip()))
            continue
        elif in_ul and not re.match(r'[*+-] ', line):
            parsed_text.append(('ul_end', None))
            in_ul = False

        # Ordered list
        elif re.match(r'\d+\.\s', line):
            if not in_ol:
                parsed_text.append(('ol_start', None))
                in_ol = True
            parsed_text.append(('li', re.sub(r'^\d+\.\s', '', line).strip()))
            continue
        elif in_ol and not re.match(r'\d+\.\s', line):
            parsed_text.append(('ol_end', None))
            in_ol = False

        # Horizontal Rule
        elif re.match(r'^(-{3,}|_{3,}|\*{3,})$', line.strip()):
            parsed_text.append(('hr', None))

        # Paragraphs and inline
        elif line.strip():
            parsed_text.append(('p', line.strip()))

    # Close any open lists or tables at the end
    if in_ul:
        parsed_text.append(('ul_end', None))
    if in_ol:
        parsed_text.append(('ol_end', None))
    if in_table and table_lines:
        parsed_text.append(('table', table_lines))

    return parsed_text