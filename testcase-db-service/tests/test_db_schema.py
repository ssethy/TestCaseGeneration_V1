import pytest
from sqlalchemy import create_engine, inspect, Table, MetaData
from app.database import Base, DATABASE_URL

@pytest.mark.asyncio
async def test_verify_table_schema():
    # Use sync engine for schema inspection
    sync_url = DATABASE_URL.replace("sqlite+aiosqlite", "sqlite")
    sync_engine = create_engine(sync_url)

    # Ensure schema is created for test inspection
    Base.metadata.create_all(bind=sync_engine)

    inspector = inspect(sync_engine)

    # === requirement_labels ===
    labels_columns = {col["name"]: col for col in inspector.get_columns("requirement_labels")}
    assert "label_id" in labels_columns
    assert labels_columns["label_id"]["nullable"] is False
    assert labels_columns["label_id"]["primary_key"] == 1

    assert "requirement_label" in labels_columns
    assert labels_columns["requirement_label"]["nullable"] is False

    assert "created_at" in labels_columns

    # === requirements ===
    req_columns = {col["name"]: col for col in inspector.get_columns("requirements")}
    assert set(req_columns.keys()) >= {
        "requirement_id", "label_id", "title", "version",
        "requirement_detail", "testcase_generation_status",
        "meta_info", "created_at", "updated_at"
    }
    assert req_columns["requirement_id"]["nullable"] is False
    assert req_columns["label_id"]["nullable"] is False
    assert req_columns["title"]["nullable"] is False
    assert req_columns["requirement_detail"]["nullable"] is False
    assert req_columns["testcase_generation_status"]["nullable"] is False

    # === testcases ===
    tc_columns = {col["name"]: col for col in inspector.get_columns("testcases")}
    assert set(tc_columns.keys()) >= {
        "testcase_id", "requirement_id", "version", "content", "created_at", "updated_at"
    }
    assert tc_columns["testcase_id"]["nullable"] is False
    assert tc_columns["requirement_id"]["nullable"] is False
    assert tc_columns["version"]["nullable"] is False
    assert tc_columns["content"]["nullable"] is False

    # === Foreign Key check: requirements.label_id -> requirement_labels.label_id
    fks = inspector.get_foreign_keys("requirements")
    assert any(
        fk["referred_table"] == "requirement_labels" and "label_id" in fk["constrained_columns"]
        for fk in fks
    )

    # === Foreign Key check: testcases.requirement_id -> requirements.requirement_id
    fks = inspector.get_foreign_keys("testcases")
    assert any(
        fk["referred_table"] == "requirements" and "requirement_id" in fk["constrained_columns"]
        for fk in fks
    )
