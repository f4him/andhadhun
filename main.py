import pytesseract

from PIL import Image



text = pytesseract.image_to_string(Image.open('image.jpg'), lang='ben')

print(text)