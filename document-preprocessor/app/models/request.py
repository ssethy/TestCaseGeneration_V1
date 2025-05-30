# app/models/request.py

from pydantic import BaseModel, Field
from enum import Enum

class FileType(str, Enum):
    docx = "docx"
    pdf = "pdf"
    png = "png"
    jpg = "jpg"

class PreprocessRequest(BaseModel):
    file_path: str = Field(..., example="./requirements/login.docx")
    file_type: FileType = Field(..., example="docx")
