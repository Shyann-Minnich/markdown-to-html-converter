import re

def parse_markdown(md_text):
    """Parse Markdown text and return a tuple."""
    parsed_text = ()

    for line in md_text:
        # Check for headings 
        if line.startswith('######'):
            parsed_text.append(('h6', line.strip('###### ')))
        elif line.startswith('#####'):
            parsed_text.append(('h5', line.strip('##### ')))
        elif line.startswith('####'):
            parsed_text.append(('h4', line.strip('#### ')))
        elif line.startswith('####'):
            parsed_text.append(('h4', line.strip('#### ')))
        elif line.startswith('###'):
            parsed_text.append(('h3', line.strip('### ')))
        elif line.startswith('##'):
            parsed_text.append(('h2', line.strip('## ')))
        elif line.startswith('#'):
            parsed_text.append(('h1', line.strip('# ')))

        # Bold
        if '**' in line or '__' in line:
            parsed_text.append(('bold', line.strip('**').strip('__')))
        # Italic
        if '*' in line or '_' in line:
            parsed_text.append(('italic', line.strip('*').strip('_')))

        #Bold + Italic
        if '***' in line or '___' in line:
            parsed_text.append(('bold_italic', line.strip('***').strip('___')))

        # Inline
        if '`' in line:
            parsed_text.append(('inline', line.strip('`')))

        # Code Blocks
        if '```' in line:
            parsed_text.append(('code_block', line.strip('```')))

        # Blockquotes
        if '>' in line:
            parsed_text.append(('blockquote', line.strip('>')))

        # Unordered Lists
        if '*' in line or '-' in line or '+' in line:
            parsed_text.append(('unordered_list', line.strip('*').strip('-').strip('+')))

        # Ordered LIsts
        if re.match(r'^\d.', line):
            parsed_text.append(('ordered_list', line.strip('\d.')))

        # Links
        if re.match(r'^[a-zA-Z0-9]', line):
            parsed_text.append(('link', line))

        # Images
        if re.match(r'!^[a-zA-Z0-9]', line):
            parsed_text.append(('image', line))

        # Horizontal Rule
        if re.match(r'^---', line) or re.match(r'^___', line) or re.match(r'^***', line):
            parsed_text.append(('horizontal_rule', line))

        # Strikethrough
        if '~~' in line:
            parsed_text.append(('strikethrough', line.strip('~~')))

        # Table
        if '|' in line:
            parsed_text.append(('table', line))

        # Escaping Characters
        if re.match(r'\'', line):
            parsed_text.append(('escape', line.strip('\'')))