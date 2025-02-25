# Markdown to HTML Converter

This Python script converts **Markdown (.md)** files to **HTML**. It parses the text and applies the correct HTML tags for headers, lists, bold/italic text, and other Markdown elements.

## Features
- Converts basic Markdown elements (headers, lists, bold, italic, etc.) into HTML.
- Supports both single-line and multi-line Markdown elements.
- Saves the converted HTML output to a file.

## Technologies Used
- Python
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

3. Install any dependencies (if needed):
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the converter, simply run the script with the path to a Markdown file:

```bash
python convert.py path_to_markdown_file.md
