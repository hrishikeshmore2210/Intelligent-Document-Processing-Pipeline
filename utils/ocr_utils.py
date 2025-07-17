import pytesseract
from pdf2image import convert_from_path
import os

def pdf_to_text(pdf_path):
    images = convert_from_path(pdf_path)
    text = ''
    for i, img in enumerate(images):
        text += pytesseract.image_to_string(img)
    return text
