import logging
import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import JSON
from sqlalchemy.sql import func

from app.database import Base

logger = logging.getLogger(__name__)


class TestCase(Base):
    __tablename__ = "testcases"

    testcase_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    requirement_id = Column(UUID(as_uuid=True), ForeignKey("requirements.requirement_id"), nullable=False)
    version = Column(String, nullable=False)
    content = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        logger.debug(f"[DB Model] Created TestCase for requirement_id={self.requirement_id}, version={self.version}")
