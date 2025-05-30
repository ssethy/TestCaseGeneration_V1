# app/api/internal_routes.py

from fastapi import APIRouter, HTTPException, Path
from app.schemas.requirement_schema import (
    CreateRequirementRequest,
    RequirementResponse,
    RequirementListResponse,
    UpdateStatusRequest,
    UpdateStatusResponse,
)
from app.services import requirement_logic
from app.utils.logger import logger

router = APIRouter(prefix="/internal/requirements", tags=["Requirements"])


@router.post("/", response_model=RequirementResponse)
async def create_requirement(req: CreateRequirementRequest):
    logger.info("API called: POST /internal/requirements")
    try:
        response = await requirement_logic.create_requirement_service(req.dict())
        return response
    except HTTPException as e:
        logger.error(f"Error in create_requirement: {e.detail}")
        raise


@router.get("/", response_model=RequirementListResponse)
async def list_requirements():
    logger.info("API called: GET /internal/requirements")
    try:
        response = await requirement_logic.list_requirements_service()
        return response
    except HTTPException as e:
        logger.error(f"Error in list_requirements: {e.detail}")
        raise


@router.get("/{requirement_id}", response_model=RequirementResponse)
async def get_requirement(requirement_id: str = Path(..., description="Requirement UUID")):
    logger.info(f"API called: GET /internal/requirements/{requirement_id}")
    try:
        response = await requirement_logic.get_requirement_by_id_service(requirement_id)
        return response
    except HTTPException as e:
        logger.error(f"Error in get_requirement: {e.detail}")
        raise


@router.patch("/{requirement_id}/status", response_model=UpdateStatusResponse)
async def update_testcase_status(
    requirement_id: str = Path(..., description="Requirement UUID"),
    status_update: UpdateStatusRequest = ...,
):
    logger.info(f"API called: PATCH /internal/requirements/{requirement_id}/status")
    try:
        response = await requirement_logic.update_requirement_status_service(requirement_id, status_update.dict())
        return response
    except HTTPException as e:
        logger.error(f"Error in update_testcase_status: {e.detail}")
        raise
