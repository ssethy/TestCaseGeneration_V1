import os
import requests
from fastapi import UploadFile


DOCUMENT_PREPROCESSOR_URL = os.getenv(
    "DOCUMENT_PREPROCESSOR_URL",
    "http://document-preprocessor-service:8020"
)


def preprocess_document(file: UploadFile, file_type: str) -> dict:
    """
    Send a single uploaded document to the document-preprocessor-service
    and return the parsed JSON content.
    """
    try:
        # Prepare multipart form data with one file and one form field
        files = {
            "file": (file.filename, file.file, file.content_type)
        }
        data = {
            "file_type": file_type
        }

        response = requests.post(
            f"{DOCUMENT_PREPROCESSOR_URL}/preprocess/",
            files=files,
            data=data,
            timeout=15
        )
        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        raise Exception(f"Failed to preprocess document: {str(e)}")
