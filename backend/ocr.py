import os
import pytesseract
from pdf2image import convert_from_path

if os.name == "nt":  
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
    POPPLER_PATH = r"F:\Programs\poppler-25.12.0\Library\bin"
else:
    POPPLER_PATH = None

def extract_text_from_pdf(pdf_path):
    if POPPLER_PATH:
        images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
    else:
        images = convert_from_path(pdf_path)

    text_content = ""
    for image in images:
        text_content += pytesseract.image_to_string(image) + "\n"

    return text_content