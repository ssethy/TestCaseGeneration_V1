import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.crud import requirement as crud_requirement
from app.schemas.requirement import RequirementCreate, RequirementOut, RequirementCreateOut
from app.database import get_db

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

router = APIRouter()

@router.post("/requirement", response_model=RequirementCreateOut)
async def create_requirement(payload: RequirementCreate, db: AsyncSession = Depends(get_db)):
    logger.info(f"API Call: Create requirement with label '{payload.requirement_label}'")
    try:
        requirement = await crud_requirement.create_requirement(db, payload)
        await db.commit()
        logger.info(f"Requirement created with id {requirement.requirement_id}")
        logger.info(f"Requirement created with id {requirement} ")
        return requirement
    except Exception as e:
        logger.error(f"Failed to create requirement: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Failed to create requirement")

@router.get("/requirements/latest", response_model=List[RequirementOut])
async def get_latest_requirements(db: AsyncSession = Depends(get_db)):
    logger.info("API Call: Get latest requirements")
    try:
        requirements = await crud_requirement.get_latest_requirements(db)
        return requirements
    except Exception as e:
        logger.error(f"Failed to fetch latest requirements: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Failed to fetch requirements")

@router.get("/requirement/{requirement_id}", response_model=RequirementOut)
async def get_requirement(requirement_id: int, db: AsyncSession = Depends(get_db)):
    logger.info(f"API Call: Get requirement by id {requirement_id}")
    requirement = await crud_requirement.get_requirement_by_id(db, requirement_id)
    if not requirement:
        logger.warning(f"Requirement not found: id {requirement_id}")
        raise HTTPException(status_code=404, detail="Requirement not found")
    return requirement
