import pdfplumber
import pdfminer
import pandas as pd
import glob

def cut_header_and_footer(filename):
    # how?

if __name__ == '__main__':
    
    path = "./pdf/*.pdf"
    file_list = glob.glob(path)
    for filename in file_list:
        cut_header_and_footer(filename)