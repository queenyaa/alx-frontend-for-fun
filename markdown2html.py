#!/usr/bin/python3

"""
This file converts a readme to html
"""

import sys
import os.path
import markdown


def convert_markdown_to_html(markdown_file, output_file):
    """
    function to convert markdown file to HTML file
    """
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    with open(markdown_file, 'r') as md_file:
        markdown_text = md_file.read()

    html_text = markdown.markdown(markdown_text)

    with open(output_file, 'w') as html_file:
        html_file.write(html_text)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        var1 = "Usage: ./markdown2html.py README.md README.html"
        print(var1, file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(markdown_file, output_file)
    sys.exit(0)
