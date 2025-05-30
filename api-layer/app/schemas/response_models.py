from pydantic import BaseModel
from typing import List


class ParsedSection(BaseModel):
    heading: str
    content: str


class UploadResponse(BaseModel):
    requirement_id: str
    title: str
    version: str
    testcase_generation_status: str
    sections: List[ParsedSection]


class RequirementSummary(BaseModel):
    requirement_id: str
    title: str
    version: str
    testcase_generation_status: str


class RequirementDetails(BaseModel):
    requirement_id: str
    title: str
    version: str
    testcase_generation_status: str
    sections: List[ParsedSection]


class TestCase(BaseModel):
    test_case_id: str
    requirement_id: str
    version: str
    title: str
    steps: List[str]
    expected_result: str
    priority: str


class TestCaseMetadata(BaseModel):
    requirement_id: str
    testcase_generation_status: str
    current_version: str
    available_versions: List[str]


class TestCaseCompareResponse(BaseModel):
    requirement_id: str
    version_a: str
    version_b: str
    differences: List[str]
