#!/usr/bin/python3
"""
This file converts a readme to html
"""
import sys
import os.path

def convert_markdown_to_html(input_file, output_file):
    """
    function to convert markdown file to HTML file
    """
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f'Missing {input_file}', file=sys.stderr)
        sys.exit(1)

    with open(input_file, 'r', encoding='utf-8') as md_file:
        markdown_lines = md_file.readlines()

    html_content = []
    in_ul = False
    in_ol = False

    for line in markdown_lines:
        if line.startswith('#'):
            level = line.count('#')
            html_content.append(f'<h{level}>{line.strip()[level+1:]}</h{level}>\n')
        
        elif line.startswith('- '):
            if not in_ol:
                if not in_ul:
                    html_content.append('<ul>\n')
                    in_ul = True
                elif in_ol:
                    html_content.append('</ol>\n')
                    in_ol = False
                html_content.append('<li>' + line.strip()[2:] + '</li>\n')
            elif in_ol:
                html_content.append('</ol>\n')
                in_ol = False
                html_content.append('<ul>\n')
                in_ul = True
            else:
                html_content.append('<li>' + line.strip()[2:] + '</li>\n')
        
        elif line.startswith('* '):
            if not in_ol:
                if not in_ul:
                    html_content.append('<ol>\n')
                    in_ol = True
                elif in_ul:
                    html_content.append('</ul>\n')
                    in_ul = False
                if not in_ol:
                    html_content.append('<ol>\n')
                    in_ol = True
                html_content.append('<li>' + line.strip()[2:] + '</li>\n')
            elif in_ol:
                html_content.append('<li>' + line.strip()[2:] + '</li>\n')
            else:
                html_content.append('<li>' + line.strip()[2:] + '</li>\n')
        
        else:
            if in_ul:
                html_content.append('</ul>\n')
                in_ul = False
            elif in_ol:
                html_content.append('</ol>\n')
                in_ol = False
            html_content.append(line)

    if in_ul:
        html_content.append('</ul>\n')
    elif in_ol:
        html_content.append('</ol>\n')

    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.writelines(html_content)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)

