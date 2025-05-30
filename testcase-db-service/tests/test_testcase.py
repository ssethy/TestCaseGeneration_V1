import pytest
from uuid import UUID

requirement_payload = {
    "requirement_label": "LoginPage",
    "title": "Login flow should support email login",
    "version": "v2",
    "requirement_detail": [
        "User can input email and password",
        "System will authenticate and redirect to dashboard"
    ],
    "testcase_generation_status": "COMPLETED",
    "meta_info": {"source": "test-testcase"}
}

testcase_payload_template = {
    "version": "v2",
    "content": {
        "title": "Valid email/password login",
        "steps": [
            "Navigate to /login",
            "Enter valid email and password",
            "Click login button",
            "Expect redirect to /dashboard"
        ]
    }
}

@pytest.mark.asyncio
async def test_create_and_fetch_testcases(client):
    # Step 1: Create requirement
    r_response = await client.post("/internal/requirement", json=requirement_payload)
    assert r_response.status_code == 200
    requirement = r_response.json()
    requirement_id = requirement["requirement_id"]
    assert UUID(requirement_id)

    # Step 2: Create testcase for that requirement
    testcase_payload = dict(testcase_payload_template)
    testcase_payload["requirement_id"] = requirement_id

    tc_response = await client.post("/internal/testcase", json=testcase_payload)
    assert tc_response.status_code == 200
    testcase = tc_response.json()
    assert UUID(testcase["testcase_id"])
    assert testcase["version"] == "v2"

    # Step 3: GET /internal/testcase/{requirement_id}
    list_response = await client.get(f"/internal/testcase/{requirement_id}")
    assert list_response.status_code == 200
    all_testcases = list_response.json()["testcases"]
    assert isinstance(all_testcases, list)
    assert len(all_testcases) >= 1

    # Step 4: GET /internal/testcase/{requirement_id}/version/v2
    version_response = await client.get(f"/internal/testcase/{requirement_id}/version/v2")
    assert version_response.status_code == 200
    versioned = version_response.json()
    assert versioned["version"] == "v2"
    assert versioned["requirement_id"] == requirement_id
