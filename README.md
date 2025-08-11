# Markdown to HTML Converter

This Python script converts **Markdown (.md)** files to **HTML**. It parses the text and applies the correct HTML tags for headers, lists, bold/italic text, and other Markdown elements.

## Features
- Converts basic Markdown elements (headers, lists, bold, italic, etc.) into HTML.
- Supports both single-line and multi-line Markdown elements.
- Handles tables, code blocks, blockquotes, and links.
- Saves the converted HTML output to a file.

## Technologies Used
- Python 3.7+
- Regular Expressions (for parsing Markdown)

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/markdown-to-html-converter.git
    ```

2. Navigate to the project directory:
    ```bash
    cd markdown-to-html-converter
    ```

3. (Optional) Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the converter, run:

```bash
python main.py path/to/yourfile.md
```

The converted HTML will be saved as `output.html` in the current directory.

