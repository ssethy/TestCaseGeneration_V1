from fastapi import APIRouter, HTTPException
from typing import List

from app.schemas.response_models import RequirementSummary, RequirementDetails
from app.clients.requirement_client import fetch_all_requirements, fetch_requirement_by_id

router = APIRouter()


@router.get("", response_model=List[RequirementSummary])
def get_all_requirements():
    """
    Get list of all uploaded requirements with summary.
    """
    try:
        return fetch_all_requirements()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch requirements: {str(e)}")


@router.get("/{requirement_id}", response_model=RequirementDetails)
def get_requirement_by_id(requirement_id: str):
    """
    Get full structured content for a specific requirement ID.
    """
    try:
        return fetch_requirement_by_id(requirement_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Requirement not found: {str(e)}")
