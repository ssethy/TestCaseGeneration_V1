from pydantic import BaseModel
from typing import List


class ParsedSection(BaseModel):
    heading: str
    content: str


class GenerateTestCaseRequest(BaseModel):
    requirement_id: str


class TestCaseCompareRequest(BaseModel):
    requirement_id: str
    version_a: str
    version_b: str
