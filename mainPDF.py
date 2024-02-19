import PyPDF2
from PyPDF2 import PdfReader

pdf = open("file.pdf", "rb")
pdf_reader = PdfReader(pdf)
print("NumPages: ", len(pdf_reader.pages))
print("Info: ", pdf_reader.metadata)

page = pdf_reader.pages[10]
print(page.extract_text())
pdf.close()
