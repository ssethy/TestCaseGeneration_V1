from fastapi.testclient import TestClient
from app.main import app
import tempfile
from unittest.mock import patch
from app.schemas.request_models import ParsedSection
from app.clients.requirement_client import RequirementCreateResponse

client = TestClient(app)


@patch("app.clients.document_client.preprocess_document")
@patch("app.clients.requirement_client.create_requirement")
def test_upload_document_success(mock_create_req, mock_preprocess_doc):
    # Mock parsed output from Document Preprocessor
    mock_preprocess_doc.return_value = type("Parsed", (), {
        "title": "Login Feature",
        "sections": [
            ParsedSection(heading="Functional", content="User must login."),
            ParsedSection(heading="Non-functional", content="Fast response.")
        ]
    })

    # Mock Requirement Service response
    mock_create_req.return_value = RequirementCreateResponse(
        requirement_id="req-001",
        version="v1",
        testcase_generation_status="NOT_STARTED"
    )

    # Create temp DOCX file to upload
    with tempfile.NamedTemporaryFile(suffix=".docx") as tmp:
        tmp.write(b"Fake DOCX content")
        tmp.seek(0)
        files = {"file": ("sample.docx", tmp, "application/vnd.openxmlformats-officedocument.wordprocessingml.document")}

        response = client.post("/api/upload", files=files)

    assert response.status_code == 200
    data = response.json()
    assert data["requirement_id"] == "req-001"
    assert data["title"] == "Login Feature"
    assert data["version"] == "v1"
    assert data["testcase_generation_status"] == "NOT_STARTED"
    assert len(data["sections"]) == 2
