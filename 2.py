import pytesseract as tess
tess.pytesseract.tesseract_cmd= r'C:\Program Files\Tesseract-OCR\tesseract'
from PIL import Image

img = Image.open('textquote.png')
text = tess.image_to_string(img)

print(text)
