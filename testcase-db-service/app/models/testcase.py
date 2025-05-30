import logging
from sqlalchemy import (
    Column, Integer, String, ForeignKey, DateTime, JSON
)
from sqlalchemy.orm import declarative_base
import datetime
from app.models.base import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class TestCase(Base):
    __tablename__ = "testcases"

    testcase_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    requirement_id = Column(UUID(as_uuid=True), ForeignKey("requirements.requirement_id"), nullable=False)
    version = Column(String, nullable=False)
    content = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logger.info(f"TestCase created for requirement_id={self.requirement_id}, version={self.version}")
