# app/service/parsers/pdf_parser.py

import pdfplumber
import os

def parse_pdf(file_path: str) -> str:
    """
    Parses a PDF file and extracts text from all pages.

    :param file_path: Path to the PDF file
    :return: Combined text from all pages
    :raises ValueError: If file not found or parsing fails
    """
    if not os.path.exists(file_path):
        raise ValueError(f"File not found: {file_path}")

    try:
        full_text = []

        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text.append(text.strip())

        return "\n".join(full_text).strip()
    except Exception as e:
        raise ValueError(f"Failed to parse PDF file: {str(e)}")
