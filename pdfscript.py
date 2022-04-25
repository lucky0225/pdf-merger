from PyPDF2 import PdfFileMerger

#pdf files
pdfs = ['Adamski.pdf', 'Busch.pdf', 'Kudra.pdf', 'Menzer.pdf']

merger = PdfFileMerger()

#merge pdfs
for pdf in pdfs:
    merger.append(pdf)

#create merged pdf
merger.write("result.pdf")
merger.close()


"""
import os
from PyPDF2 import PdfFileMerger

x = [a for a in os.listdir() if a.endswith(".pdf")]

merger = PdfFileMerger()

for pdf in x:
    merger.append(open(pdf, 'rb'))

with open("result.pdf", "wb") as fout:
    merger.write(fout)
"""