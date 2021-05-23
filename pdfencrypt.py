#install PyPDF2 (pip install PyPDF2)
from PyPDF2 import PdfFileReader,PdfFileWriter
out = PdfFileWriter()
file = PdfFileReader('assignment-1.pdf')#input the pdf you want to encrypt
num = file.numPages
for i in range(num):
    page = file.getPage(i)
    out.addPage(page)
password ='1234' #create password
out.encrypt(password)
with open("encrypted.pdf","wb") as file2:#enter name the file you want to save  as
    out.write(file2)
