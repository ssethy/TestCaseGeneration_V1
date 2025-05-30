from fastapi import APIRouter, HTTPException
from typing import List
from app.clients.test_case_client import (
    generate_test_cases,
    get_test_cases_by_requirement_id,
    get_test_case_metadata,
    compare_test_cases
)
from app.schemas.request_models import GenerateTestCaseRequest, TestCaseCompareRequest
from app.schemas.response_models import (
    TestCase,
    TestCaseMetadata,
    TestCaseCompareResponse
)

router = APIRouter()


@router.post("/generate-test-cases")
def generate(request: GenerateTestCaseRequest):
    """
    Trigger test case generation for a given requirement ID.
    """
    try:
        return generate_test_cases(request.requirement_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/requirements/{requirement_id}/test-cases", response_model=List[TestCase])
def get_test_cases(requirement_id: str):
    """
    Get all generated test cases for a requirement.
    """
    try:
        return get_test_cases_by_requirement_id(requirement_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/requirements/{requirement_id}/test-cases/metadata", response_model=TestCaseMetadata)
def get_test_case_generation_metadata(requirement_id: str):
    """
    Get generation status and available versions for test cases.
    """
    try:
        return get_test_case_metadata(requirement_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/test-cases/compare", response_model=TestCaseCompareResponse)
def compare_versions(request: TestCaseCompareRequest):
    """
    Compare two versions of test cases.
    """
    try:
        return compare_test_cases(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
