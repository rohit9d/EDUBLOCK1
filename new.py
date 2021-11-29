import pytesseract
def ocr_core(filename):
    print(filename)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    text= pytesseract.image_to_string(str(filename))
    return text
