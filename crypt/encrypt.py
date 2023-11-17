import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def encrypt_pdf(filepath, save_filepath, passwd):
    """
    PDF文档加密
    @param filepath:PDF文件路径
    @param save_filepath:加密后的文件保存路径
    @param passwd:密码
    @return:
    """
    pdf_reader = PdfFileReader(filepath)
    pdf_writer = PdfFileWriter()

    for page_index in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page_index))

    # 添加密码
    pdf_writer.encrypt(passwd)
    with open(save_filepath, "wb") as out:
        pdf_writer.write(out)
        
# 文档加密
if __name__ == '__main__':
    filepath = ""
    save_filepath = ""
    encrypt_pdf(filepath, save_filepath, passwd='*')