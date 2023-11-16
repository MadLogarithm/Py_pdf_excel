from PyPDF2 import PdfFileReader, PdfFileWriter
import glob

# It has been proven that cropBox is changing the visible part of the PDF. The other parts are all there, but they just can't be seen.

def cut_header_and_footer(filename):
    # how?
    input_pdf = PdfFileReader(open(filename,"rb"))
    output_pdf = PdfFileWriter()

    for page in input_pdf.pages:
        page.cropBox.setLowerLeft((0, 73))
        page.cropBox.setUpperRight((1000, 788))

        output_pdf.addPage(page)
    
    output_pdf_stream = open('./cut_pdf/' + str(filename)[6:-4] + '.pdf', "wb")
    output_pdf.write(output_pdf_stream)
    output_pdf_stream.close()

if __name__ == '__main__':
    
    path = "./pdf/*.pdf"
    file_list = glob.glob(path)
    for filename in file_list:
        cut_header_and_footer(filename)