import logging
from pydantic import BaseModel, Field
from typing import Dict
from datetime import datetime
from uuid import UUID

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class TestCaseBase(BaseModel):
    requirement_id: UUID = Field(..., example="3fa85f64-5717-4562-b3fc-2c963f66afa6")
    version: str = Field(..., example="v1")
    content: Dict = Field(..., example={"steps": ["step1", "step2"]})

class TestCaseCreate(TestCaseBase):
    pass

class TestCaseOut(TestCaseBase):
    testcase_id: UUID = Field(..., example="3fa85f64-5717-4562-b3fc-2c963f66afa6")

    class Config:
        orm_mode = True
