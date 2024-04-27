#!/usr/bin/python3
"""
A script to convert Markdown to HTML
"""
import sys
import os.path
import re

def convert_markdown_to_html(input_file, output_file):
    """
    Converts Markdown file to HTML file
    """
    # Check if the number of arguments passed is 2
    if len(sys.argv[1:]) != 2:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        sys.exit(1)

    # Check if the input Markdown file exists and is a file
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f'Missing {input_file}', file=sys.stderr)
        sys.exit(1)

    # Read the input Markdown file and convert it to HTML
    with open(input_file, encoding='utf-8') as md_file:
        html_content = []
        for line in md_file:
            heading = re.split(r'#{1,6} ', line)
            if len(heading) > 1:
                # Compute the number of '#' present to determine heading level
                h_level = len(line[:line.find(heading[1])-1])
                # Append the HTML equivalent of the heading
                html_content.append(f'<h{h_level}>{heading[1]}</h{h_level}>\n')
            else:
                html_content.append(line)

    # Write the HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.writelines(html_content)

if __name__ == '__main__':
    # Store the arguments into variables
    if len(sys.argv[1:]) != 2:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)
