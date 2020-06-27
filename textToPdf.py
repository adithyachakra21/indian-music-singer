# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
import PyPDF2

pdfFileObj = open('ssp_7to12.pdf','rb')     #'rb' for read binary mode
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)


pageObj = pdfReader.getPage(197)          #'9' is the page number
result = pageObj.extractText()

print(result)

f = open("demofile.txt", "a", encoding = "utf-8")
f.write(result)
f.close()



