import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def decrypt_pdf(filepath, save_filepath, passwd):
    """
    解密 PDF 文档并且保存为未加密的 PDF
    @param filepath:PDF文件路径
    @param save_filepath:解密后的文件保存路径
    @param passwd:密码
    @return:
    """
    pdf_reader = PdfFileReader(filepath)
    # PDF文档解密
    pdf_reader.decrypt('xiaoyi')

    pdf_writer = PdfFileWriter()
    for page_index in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page_index))

    with open(save_filepath, "wb") as out:
        pdf_writer.write(out)
        
# 文档解密
if __name__ == '__main__':
    filepath = ""
    save_filepath = ""
    decrypt_pdf(filepath, save_filepath, passwd='*')