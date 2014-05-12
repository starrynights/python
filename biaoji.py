import re
import fileinput
import sys

input_file = sys.argv[1]
#output_file = sys.argv[2]

blocks = []
def get_block(file):
    p = ''
    for line in fileinput.input(file):
        line = line.strip('\n')
        if line:
            p = p + line
        else:
            blocks.append(p)
            p = ''
    blocks.append(p)

def deal_paragraph(block):
    block = '<p>' + block + '</p>'
    return block

def deal_emphasize(block):
    block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
    return block

def deal_hyperlink(block):
    block = re.sub(r'(https?://[/\.a-zA-Z_-]+)',r'<a href=\1>',block)
    return block

def convert(file):
    get_block(file)
    i = 0
    while i < len(blocks):
        blocks[i] = deal_paragraph(blocks[i])
        blocks[i] = deal_emphasize(blocks[i])
        blocks[i] = deal_hyperlink(blocks[i])
        print blocks[i]
        i += 1

if __name__ == '__main__':
    convert(input_file)

