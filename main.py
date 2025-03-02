def read_markdown(file_path):
    """Reads a markdown file and returns its content as a string."""
    with open(file_path, 'r') as file:
        return file.read()