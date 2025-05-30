import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.crud import testcase as crud_testcase
from app.schemas.testcase import TestCaseCreate, TestCaseOut
from app.database import get_db
from uuid import UUID
from typing import List, Dict

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

router = APIRouter()

@router.post("/testcase", response_model=TestCaseOut)
async def create_testcase(payload: TestCaseCreate, db: AsyncSession = Depends(get_db)):
    logger.info(f"API Call: Create testcase for requirement_id {payload.requirement_id}")
    try:
        testcase = await crud_testcase.create_testcase(db, payload)
        await db.commit()
        logger.info(f"Testcase created with id {testcase.testcase_id}")
        return testcase
    except Exception as e:
        logger.error(f"Failed to create testcase: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Failed to create testcase")

@router.get("/testcase/{requirement_id}", response_model=Dict[str, List[TestCaseOut]])
async def list_testcases_for_requirement(
    requirement_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    testcases = await crud_testcase.get_testcases_by_requirement(db, requirement_id)
    if not testcases:
        # Return empty list inside dict instead of None
        return {"testcases": []}

    return {"testcases": testcases}

@router.get("/testcase/{requirement_id}/version/{version}", response_model=TestCaseOut)
async def get_testcase_version(requirement_id: UUID, version: str, db: AsyncSession = Depends(get_db)):
    logger.info(f"API Call: Get testcase for requirement_id {requirement_id} version {version}")
    testcase = await crud_testcase.get_testcase_by_version(db, requirement_id, version)
    if not testcase:
        logger.warning(f"Testcase not found for requirement_id {requirement_id} version {version}")
        raise HTTPException(status_code=404, detail="Testcase not found")
    return testcase
