from fastapi import APIRouter, HTTPException
from app.schemas.requirement_schema import (
    RequirementCreateRequest,
    RequirementCreateResponse,
    RequirementMetadataResponse,
    RequirementDetailResponse,
    StatusUpdateRequest,
    StatusUpdateResponse
)
from app.services.requirement_logic import (
    create_requirement,
    list_requirements,
    get_requirement_by_id,
    update_testcase_generation_status
)
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/internal/requirements", response_model=RequirementCreateResponse)
async def post_requirement(payload: RequirementCreateRequest):
    logger.info("Received POST /internal/requirements")
    try:
        return await create_requirement(payload)
    except Exception as e:
        logger.exception("Error while creating requirement")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/internal/requirements", response_model=list[RequirementMetadataResponse])
async def get_all_requirements():
    logger.info("Received GET /internal/requirements")
    try:
        return await list_requirements()
    except Exception as e:
        logger.exception("Error while listing requirements")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/internal/requirements/{requirement_id}", response_model=RequirementDetailResponse)
async def get_requirement(requirement_id: str):
    logger.info(f"Received GET /internal/requirements/{requirement_id}")
    try:
        return await get_requirement_by_id(requirement_id)
    except Exception as e:
        logger.exception("Error while retrieving requirement")
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/internal/requirements/{requirement_id}/status", response_model=StatusUpdateResponse)
async def patch_status(requirement_id: str, payload: StatusUpdateRequest):
    logger.info(f"Received PATCH /internal/requirements/{requirement_id}/status")
    try:
        return await update_testcase_generation_status(requirement_id, payload.testcase_generation_status)
    except Exception as e:
        logger.exception("Error while updating status")
        raise HTTPException(status_code=500, detail=str(e))
