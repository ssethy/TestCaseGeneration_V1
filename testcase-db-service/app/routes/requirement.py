from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.requirement import RequirementCreate, RequirementInDB
from app.database import get_db
from app.crud.requirement import create_requirement, get_latest_requirements, get_requirement_by_id
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/requirement", response_model=RequirementInDB)
async def create_new_requirement(payload: RequirementCreate, db: AsyncSession = Depends(get_db)):
    try:
        requirement = await create_requirement(db, payload)
        await db.commit()
        await db.refresh(requirement)
        return requirement
    except Exception as e:
        logger.error(f"Failed to create requirement: {e}")
        raise HTTPException(status_code=500, detail="Failed to create requirement")

@router.get("/requirements/latest")
async def get_latest(db: AsyncSession = Depends(get_db)):
    return await get_latest_requirements(db)

@router.get("/requirement/{req_id}", response_model=RequirementInDB)
async def get_requirement(req_id: str, db: AsyncSession = Depends(get_db)):
    requirement = await get_requirement_by_id(db, req_id)
    if not requirement:
        raise HTTPException(status_code=404, detail="Requirement not found")
    return requirement
