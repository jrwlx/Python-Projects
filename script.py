# mysolution
# given a pdf, merges pdf with wtr.pdf

import PyPDF2
import sys

# PDF_to_wtr = sys.argv[1]
#
# def watermark(PDF_to_wtr):
#
#     output = PyPDF2.PdfFileWriter()
#
#     to_wtrmark = PyPDF2.PdfFileReader(PDF_to_wtr)  # read PDF given
#     wtrmark = PyPDF2.PdfFileReader('wtr.pdf')  # read PDF to merge
#
#     num_pages = to_wtrmark.getNumPages()  # to loop through PDF
#
#     for i in range(0, num_pages):
#         x = to_wtrmark.getPage(i)
#         y = wtrmark.getPage(0)
#         x.mergePage(y)  # merges each page of pdf with wtr.pdf
#         output.addPage(x)  # merged pdf is written to output object
#
#     with open('wtrsuper.pdf', 'wb') as file:
#         output.write(file)  # output object written on new pdf
#
#
# watermark(PDF_to_wtr)

# SOLUTION from Andrei

template = PyPDF2.PdfFileReader(open('../super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('../wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open('../watermarked_output.pdf', 'wb') as file:
    output.write(file)



