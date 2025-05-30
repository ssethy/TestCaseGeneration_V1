import os
import requests
from typing import List
from app.schemas.request_models import TestCaseCompareRequest
from app.schemas.response_models import (
    TestCase,
    TestCaseMetadata,
    TestCaseCompareResponse
)

TEST_CASE_SERVICE_URL = os.getenv("TEST_CASE_SERVICE_URL", "http://test-case-manager:8050")


def generate_test_cases(requirement_id: str) -> dict:
    """
    Trigger test case generation for a requirement ID.
    """
    try:
        payload = {"requirement_id": requirement_id}
        response = requests.post(f"{TEST_CASE_SERVICE_URL}/internal/test-cases/generate", json=payload, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"Failed to trigger generation: {str(e)}")


def get_test_cases_by_requirement_id(requirement_id: str) -> List[TestCase]:
    """
    Fetch all test cases for a requirement.
    """
    try:
        response = requests.get(f"{TEST_CASE_SERVICE_URL}/internal/test-cases/{requirement_id}", timeout=10)
        response.raise_for_status()
        return [TestCase(**tc) for tc in response.json()]
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch test cases: {str(e)}")


def get_test_case_metadata(requirement_id: str) -> TestCaseMetadata:
    """
    Fetch test case generation status and available versions.
    """
    try:
        response = requests.get(
            f"{TEST_CASE_SERVICE_URL}/internal/test-cases/{requirement_id}/metadata", timeout=10
        )
        response.raise_for_status()
        return TestCaseMetadata(**response.json())
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch metadata: {str(e)}")


def compare_test_cases(request: TestCaseCompareRequest) -> TestCaseCompareResponse:
    """
    Compare two versions of test cases.
    """
    try:
        response = requests.post(
            f"{TEST_CASE_SERVICE_URL}/internal/test-cases/compare", json=request.dict(), timeout=10
        )
        response.raise_for_status()
        return TestCaseCompareResponse(**response.json())
    except requests.RequestException as e:
        raise Exception(f"Failed to compare test cases: {str(e)}")
