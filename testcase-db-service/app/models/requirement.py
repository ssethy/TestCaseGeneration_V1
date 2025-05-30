import logging
import uuid
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import JSON
from sqlalchemy.sql import func

from app.database import Base

logger = logging.getLogger(__name__)


class RequirementLabel(Base):
    __tablename__ = "requirement_labels"

    label_id = Column(Integer, primary_key=True, index=True)
    requirement_label = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        logger.debug(f"[DB Model] Created RequirementLabel: {self.requirement_label}")


class Requirement(Base):
    __tablename__ = "requirements"

    requirement_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    label_id = Column(Integer, ForeignKey("requirement_labels.label_id"), nullable=False)
    title = Column(Text, nullable=False)
    version = Column(String, nullable=False)
    requirement_detail = Column(JSON, nullable=False)
    testcase_generation_status = Column(String, nullable=False)
    meta_info = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        logger.debug(f"[DB Model] Created Requirement: {self.title} (v{self.version})")
