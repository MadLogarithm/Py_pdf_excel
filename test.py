import pdfplumber
import pandas as pd
import PyPDF2

def tail_not_space_char(page_chars):
    i = -1
    while page_chars[i].get('text').isspace():
        i -= 1
    return page_chars[i]

def head_not_space_char(page_chars):
    i = 0
    while page_chars[i].get('text').isspace():
        i += 1
    return page_chars[i]

with pdfplumber.open('gg.pdf') as pdf:
    for page in pdf.pages:
        print(page)
        print(head_not_space_char(page.chars).get('text'))
        print(head_not_space_char(page.chars).get('x0'))
        print(head_not_space_char(page.chars).get('y0'))
        print(head_not_space_char(page.chars).get('x1'))
        print(head_not_space_char(page.chars).get('y1'))
        print(tail_not_space_char(page.chars).get('text'))
        print(tail_not_space_char(page.chars).get('x0'))
        print(tail_not_space_char(page.chars).get('y0'))
        print(tail_not_space_char(page.chars).get('x1'))
        print(tail_not_space_char(page.chars).get('y1'))

        for page_char in page.chars:
            print(page_char.get('text'))