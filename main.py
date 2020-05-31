# version 0.0.1
import pytesseract as tess
from PIL import Image

tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = Image.open("img1.png")
txt = tess.image_to_string(img)

print(txt)
