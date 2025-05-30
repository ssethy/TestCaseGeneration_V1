# app/service/parsers/image_parser.py

import pytesseract
from PIL import Image
import os

def parse_image(file_path: str) -> str:
    """
    Uses Tesseract OCR to extract text from an image file (PNG or JPG).

    :param file_path: Path to the image file
    :return: Extracted text
    :raises ValueError: If file not found or OCR fails
    """
    if not os.path.exists(file_path):
        raise ValueError(f"File not found: {file_path}")

    try:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        raise ValueError(f"Failed to parse image file: {str(e)}")
