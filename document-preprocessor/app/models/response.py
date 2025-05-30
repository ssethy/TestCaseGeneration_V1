# app/models/response.py

from pydantic import BaseModel
from typing import List

class Section(BaseModel):
    title: str
    content: str

class PreprocessResponse(BaseModel):
    raw_text: str
    sections: List[Section]
