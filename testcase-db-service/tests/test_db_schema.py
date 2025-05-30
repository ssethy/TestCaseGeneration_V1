import pytest
from sqlalchemy import create_engine , inspect
from app.models.requirement import RequirementLabel, Requirement
from app.models.testcase import TestCase
from app.database import Base

DATABASE_URL = "sqlite+aiosqlite:///:memory:"

@pytest.mark.asyncio
async def test_verify_table_schema():
    # Create synchronous engine for inspection
    sync_url = DATABASE_URL.replace("sqlite+aiosqlite", "sqlite")
    sync_engine = create_engine(sync_url, echo=False)

    # Create all tables synchronously
    Base.metadata.create_all(bind=sync_engine)

    inspector = inspect(sync_engine)

    # Verify tables exist
    tables = inspector.get_table_names()
    assert "requirement_labels" in tables
    assert "requirements" in tables
    assert "testcases" in tables

    # Verify columns in requirements table
    req_cols = {col["name"]: col for col in inspector.get_columns("requirements")}
    for col_name in [
        "requirement_id",
        "label_id",
        "title",
        "version",
        "raw_text",
        "requirement_detail",
        "testcase_generation_status",
        "meta_info",
        "created_at",
        "updated_at",
    ]:
        assert col_name in req_cols

    # Verify columns in testcases table
    tc_cols = {col["name"]: col for col in inspector.get_columns("testcases")}
    for col_name in [
        "testcase_id",
        "requirement_id",
        "version",
        "content",
        "created_at",
        "updated_at",
    ]:
        assert col_name in tc_cols

    # Verify columns in requirement_labels table
    label_cols = {col["name"]: col for col in inspector.get_columns("requirement_labels")}
    for col_name in ["label_id", "requirement_label"]:
        assert col_name in label_cols
