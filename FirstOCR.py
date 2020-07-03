# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 08:04:52 2020

@author: mythkc
"""
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

# Next four lines convert the image into black and white
column = Image.open('begada.PNG')
gray = column.convert('L')    # convert to gray scale vs. RGB or CMYK.
blackwhite = gray.point(lambda x: 0 if x < 200 else 255, '1')

# Below line saves black and white picture as different file 
# blackwhite.save("code_bw.jpg")

custom_config = r' --psm 6 -c load_system_dawg=False -c load_freq_dawg=False'

text = tess.image_to_string (column, lang='tel', config = custom_config)

print (text)


"""
Make a list of parameters to set:
    - psm = 8                 (single word)
    - load_system_dawg=False  (don't look at dictionary) -- not working
    - load_freq_dawg=False    (don't look at dictionary) -- not working
    
    
Use this link to add new characters:
    https://wilsonmar.github.io/tesseract/    
   
Use this link to remove lines:
    https://docs.opencv.org/3.1.0/d1/dee/tutorial_moprh_lines_detection.html

"""
