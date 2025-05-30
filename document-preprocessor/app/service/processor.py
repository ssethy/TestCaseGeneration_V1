import os
import tempfile
from fastapi import UploadFile
from app.service.parsers.docx_parser import parse_docx
from app.service.parsers.pdf_parser import parse_pdf
from app.service.parsers.image_parser import parse_image
from app.utils.text_segmenter import segment_text


def process_uploaded_document(file: UploadFile, file_type: str) -> dict:
    """
    Handles uploaded file, saves it temporarily, and processes it.
    """
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_type}") as tmp:
            tmp.write(file.file.read())
            tmp_path = tmp.name

        if file_type == "docx":
            raw_text = parse_docx(tmp_path)
        elif file_type == "pdf":
            raw_text = parse_pdf(tmp_path)
        elif file_type in ("jpg", "png"):
            raw_text = parse_image(tmp_path)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")

        if not raw_text.strip():
            raise ValueError("Parsed document is empty or unreadable.")

        structured_sections = segment_text(raw_text)

        return {
            "raw_text": raw_text,
            "sections": structured_sections
        }

    finally:
        if 'tmp_path' in locals() and os.path.exists(tmp_path):
            os.remove(tmp_path)
