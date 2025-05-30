from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from uuid import UUID
from enum import Enum


class TestcaseGenerationStatus(str, Enum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class RequirementLabelBase(BaseModel):
    requirement_label: str = Field(..., example="LoginPage")


class RequirementLabelCreate(RequirementLabelBase):
    pass


class RequirementLabelOut(RequirementLabelBase):
    label_id: int

    class Config:
        orm_mode = True


class RequirementBase(BaseModel):
    title: str = Field(..., example="Login page must allow email/password login")
    version: str = Field(..., example="v1")
    raw_text: Optional[str] = Field(
        None, example="The login page allows users to authenticate using email and password."
    )
    requirement_detail: List[str] = Field(
        ..., example=[
            "User must enter email and password.",
            "System should validate credentials before login."
        ]
    )
    testcase_generation_status: TestcaseGenerationStatus = Field(..., example="NOT_STARTED")
    meta_info: Optional[Dict] = Field(None, example={"source": "unit-test"})


class RequirementCreate(RequirementBase):
    requirement_label: str = Field(..., example="LoginPage")


class RequirementCreateOut(RequirementBase):
    requirement_id: UUID = Field(..., example="3fa85f64-5717-4562-b3fc-2c963f66afa6")
    label_id: int = Field(..., example=5)

    class Config:
        orm_mode = True


class RequirementOut(RequirementCreateOut):
    requirement_label: str = Field(..., example="LoginPage")
