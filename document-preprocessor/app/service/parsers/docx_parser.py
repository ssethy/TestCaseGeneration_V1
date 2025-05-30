# app/service/parsers/docx_parser.py

from docx import Document
import os

def parse_docx(file_path: str) -> str:
    """
    Parses a .docx file and returns the extracted raw text.

    :param file_path: Path to the DOCX file
    :return: Concatenated text from paragraphs
    :raises ValueError: If file not found or parsing fails
    """
    if not os.path.exists(file_path):
        raise ValueError(f"File not found: {file_path}")

    try:
        doc = Document(file_path)
        paragraphs = [para.text.strip() for para in doc.paragraphs if para.text.strip()]
        return "\n".join(paragraphs)
    except Exception as e:
        raise ValueError(f"Failed to parse DOCX file: {str(e)}")
