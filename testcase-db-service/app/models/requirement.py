import enum
import uuid
import logging
from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Text, DateTime,
    ForeignKey, JSON, Enum
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.models.base import Base

logger = logging.getLogger(__name__)

class TestcaseGenerationStatusEnum(str, enum.Enum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class RequirementLabel(Base):
    __tablename__ = "requirement_labels"

    label_id = Column(Integer, primary_key=True, index=True)
    requirement_label = Column(String, unique=True, nullable=False)
    requirements = relationship(
        "Requirement",
        back_populates="label",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<RequirementLabel(id={self.label_id}, label='{self.requirement_label}')>"

class Requirement(Base):
    __tablename__ = "requirements"

    requirement_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
        index=True
    )
    label_id = Column(Integer, ForeignKey("requirement_labels.label_id", ondelete="CASCADE"), nullable=False)
    title = Column(String, nullable=False)
    version = Column(String, nullable=False)
    raw_text = Column(Text)
    requirement_detail = Column(JSON, nullable=False)
    testcase_generation_status = Column(
        Enum(TestcaseGenerationStatusEnum),
        default=TestcaseGenerationStatusEnum.NOT_STARTED
    )
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    meta_info = Column(JSON, nullable=True)

    label = relationship("RequirementLabel", back_populates="requirements")

    def __repr__(self):
        return (
            f"<Requirement(id={self.requirement_id}, label_id={self.label_id}, "
            f"title='{self.title}', version='{self.version}')>"
        )

    def log_creation(self):
        logger.info(f"Requirement created: {self}")

    def log_update(self):
        logger.info(f"Requirement updated: {self}")
