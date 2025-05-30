import logging
from uuid import UUID
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

logger = logging.getLogger(__name__)


class TestCaseGenerationStatus(str, Enum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class RequirementBase(BaseModel):
    title: str
    version: str
    requirement_detail: List[str]
    testcase_generation_status: TestCaseGenerationStatus
    meta_info: Optional[dict] = None


class RequirementCreate(RequirementBase):
    requirement_label: str


class RequirementInDB(RequirementBase):
    requirement_id: UUID
    label_id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class RequirementLabelOut(BaseModel):
    requirement_id: UUID
    requirement_label: str
    title: str
    version: str
    testcase_generation_status: TestCaseGenerationStatus
    created_at: datetime

    class Config:
        orm_mode = True
