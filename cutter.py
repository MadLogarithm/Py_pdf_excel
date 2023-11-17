from PyPDF2 import PdfFileReader, PdfFileWriter
import fitz
import glob

def cut_header_and_footer(filename):
    # how? try PyPDF2 cropBox
    # It has been proven that cropBox is changing the visible part of the PDF. The other parts are all there, but they just can't be seen.
    input_pdf = PdfFileReader(open(filename,"rb"))
    output_pdf = PdfFileWriter()

    for page in input_pdf.pages:
        page.cropBox.setLowerLeft((0, 73))
        page.cropBox.setUpperRight((1000, 788))

        output_pdf.addPage(page)
    
    output_pdf_stream = open('./cut_pdf/' + str(filename)[6:-4] + '.pdf', "wb")
    output_pdf.write(output_pdf_stream)
    output_pdf_stream.close()

# def cut_header_and_footer(filename):
#     # how? try fitz crop
#     input_pdf = fitz.open(filename)
#     output_pdf = fitz.open

#     for i in range(0, input_pdf.pageCount):
#         page = input_pdf.loadPage(i)
#         rect = fitz.Rect(0, 73, 1000, 788)
#         cropped_page = page.crop(rect)
#         output_pdf.insertPDF(cropped_page)
    
#     output_pdf.save('./cut_pdf/' + str(filename)[6:-4] + '.pdf')


if __name__ == '__main__':
    
    path = "./pdf/*.pdf"
    file_list = glob.glob(path)
    for filename in file_list:
        cut_header_and_footer(filename)