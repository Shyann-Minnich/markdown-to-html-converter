import re

# Advanced Considerations
# 1. Inline vs Block Processing
# 2. Nested Lists
# 3. Raw HTML Blocks
# 4. Error Handling 

def parse_markdown(md_text):
    """Parse Markdown text and return a tuple."""
    parsed_text = []
    lines = md_text.splitlines()

    for line in lines:
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

        # Unordered Lists
        elif line.startswith('* '):
            parsed_text.append(('ul', line[2:].strip()))
        elif line.startswith('- '):
            parsed_text.append(('ul', line[2:].strip()))
        elif line.startswith('+ '):
            parsed_text.append(('ul', line[2:].strip()))
        
        # Ordered Lists
        elif re.match(r'^\d+\.\s', line):
            parsed_text.append(('ol', re.sub(r'^\d+\.\s', '', line).strip()))

        # Bold
        if '**' in line or '__' in line:
            parsed_text.append(('strong', line.strip('**').strip('__')))
        # Italic
        if '*' in line or '_' in line:
            parsed_text.append(('em', line.strip('*').strip('_')))

        #Bold + Italic
        if '***' in line or '___' in line:
            parsed_text.append(('strong><em', line.strip('***').strip('___')))

        # Inline
        if '`' in line:
            parsed_text.append(('code', line.strip('`')))

        # Code Blocks
        if '```' in line:
            parsed_text.append(('pre><code', line.strip('```')))

        # Links
        if re.match(r'^\[.*\]\(.*\)$', line):
            parsed_text.append(('link', line))

        # Images
        if re.match(r'!^[a-zA-Z0-9]', line):
            parsed_text.append(('img', line.strip('!')))

        # Horizontal Rule
        if re.match(r'^---', line) or re.match(r'^___', line) or re.match(r'^\*\*\*', line):
            parsed_text.append(('hr', line))

        # Strikethrough
        if '~~' in line:
            parsed_text.append(('del', line.strip('~~')))

        # Table
        if '|' in line:
            parsed_text.append(('table', line))

        # Escaping Characters
        if re.match(r'\'', line):
            parsed_text.append(('escape', line.strip('\'')))

    return parsed_text