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
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f'Missing {input_file}', file=sys.stderr)
        sys.exit(1)

    with open(input_file, 'r', encoding='utf-8') as md_file:
        markdown_lines = md_file.readlines()

    html_content = []
    in_list = False

    for line in markdown_lines:
        if line.startswith('- '):
            if not in_list:
                html_content.append('<ul>\n')
                in_list = True
            html_content.append(f'<li>{line.strip()[2:]}</li>\n')
        else:
            if in_list:
                html_content.append('</ul>\n')
                in_list = False
            html_content.append(line)

    if in_list:
        html_content.append('</ul>\n')

    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.writelines(html_content)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)
