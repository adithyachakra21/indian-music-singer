# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 08:04:52 2020

@author: mythkc
"""
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open('telugu1.png')
text = tess.image_to_string (img, lang="tel")

print(text)
#Hello 
