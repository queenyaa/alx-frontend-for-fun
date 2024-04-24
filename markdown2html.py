#!/usr/bin/python3
"""
This file converts a readme to html
"""
import sys
import os.path

def convert_markdown_to_html(markdown_file, output_file):
    """
    function to convert markdown file to HTML file
    """
    if len(sys.argv[1:]) != 2:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        sys.exit(1)

    if not (os.path.exists(markdown_file) and os.path.isfile(markdown_file)):
        print(f'Missing {markdown_file}', file=sys.stderr)
        sys.exit(1)

    with open(markdown_file, encoding='utf-8') as md_file:
        html_content = md_file.read()

    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

if __name__ == '__main__':
    if len(sys.argv[1:]) != 2:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(markdown_file, output_file)
