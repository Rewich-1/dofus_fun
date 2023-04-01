import os
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\jb\AppData\Local\Programs\Tesseract-OCR\tesseract'
from PIL import Image

print('TEST')
print(os.getcwd())
img = Image.open('../Screen/ligne_0.png')

print(tess.image_to_string(img))