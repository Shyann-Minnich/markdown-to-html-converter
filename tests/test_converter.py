import unittest
from markdown_converter.parser import parse_markdown
from markdown_converter.render import render_html

class TestMarkdownConverter(unittest.TestCase):
    def test_heading(self):
        md = "# Heading"
        parsed = parse_markdown(md)
        html = render_html(parsed)
        self.assertIn("<h1>Heading</h1>", html)

    def test_bold(self):
        md = "**bold**"
        parsed = parse_markdown(md)
        html = render_html(parsed)
        self.assertIn("<strong>bold</strong>", html)

    def test_list(self):
        md = "- item1\n- item2"
        parsed = parse_markdown(md)
        html = render_html(parsed)
        self.assertIn("<ul>", html)
        self.assertIn("<li>item1</li>", html)
        self.assertIn("<li>item2</li>", html)
        self.assertIn("</ul>", html)

    def test_codeblock(self):
        md = "```\ncode\n```"
        parsed = parse_markdown(md)
        html = render_html(parsed)
        self.assertIn("<pre><code>code</code></pre>", html)

    def test_table(self):
        md = "| h1 | h2 |\n|----|----|\n| a  | b  |"
        parsed = parse_markdown(md)
        html = render_html(parsed)
        self.assertIn("<table>", html)
        self.assertIn("<th>h1</th>", html)
        self.assertIn("<td>a</td>", html)
        self.assertIn("</table>", html)

if __name__ == '__main__':
    unittest.main()