# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
import fitz

doc = fitz.open('ssp_7to12.pdf')
toc = doc.getToC()
print (toc)  

page = doc[211]
text = page.getText('text')
print(text)
text_strippped = ''.join(text.split())
print (text_strippped)

g = open("kalyani sancari.txt", "a", encoding = "utf-8")

g.seek(0)                                   #  deletes existing contents
g.truncate()

g.write(text_strippped)
g.close()




