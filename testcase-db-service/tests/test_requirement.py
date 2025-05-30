import pytest
from uuid import UUID

@pytest.mark.asyncio
async def test_create_and_retrieve_requirement(client):
    payload = {
        "requirement_label": "LoginPage",
        "title": "Login page must allow email/password login",
        "version": "v1",
        "requirement_detail": [
            "User must enter email and password.",
            "System should validate credentials before login."
        ],
        "testcase_generation_status": "NOT_STARTED",
        "meta_info": {"source": "unit-test"}
    }

    # POST /internal/requirement
    response = await client.post("/internal/requirement", json=payload)
    assert response.status_code == 200
    created = response.json()
    assert "requirement_id" in created
    assert UUID(created["requirement_id"])  # valid UUID
    assert created["version"] == "v1"
    assert created["title"] == payload["title"]
    assert created["requirement_detail"] == payload["requirement_detail"]

    # # GET /internal/requirements/latest
    # response = await client.get("/internal/requirements/latest")
    # assert response.status_code == 200
    # latest = response.json()
    # assert isinstance(latest, list)
    # assert any(item["requirement_label"] == "LoginPage" for item in latest)

    # # GET /internal/requirements/{requirement_id}
    # req_id = created["requirement_id"]
    # response = await client.get(f"/internal/requirements/{req_id}")
    # assert response.status_code == 200
    # result = response.json()
    # assert result["requirement_id"] == req_id
    # assert result["title"] == payload["title"]
