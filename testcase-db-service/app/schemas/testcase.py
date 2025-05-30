import logging
from uuid import UUID
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

logger = logging.getLogger(__name__)


class TestCaseBase(BaseModel):
    version: str
    content: dict


class TestCaseCreate(TestCaseBase):
    requirement_id: UUID


class TestCaseInDB(TestCaseBase):
    testcase_id: UUID
    requirement_id: UUID
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class TestCaseList(BaseModel):
    testcases: List[TestCaseInDB]
