import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app.database import get_db
from app.schemas.testcase import (
    TestCaseCreate,
    TestCaseInDB,
    TestCaseList
)
from app.models.testcase import TestCase
from app.crud.testcase import (
    create_testcase,
    get_testcases_by_requirement,
    get_testcase_by_version
)

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/internal/testcase", response_model=TestCaseInDB)
async def create_test_case(payload: TestCaseCreate, db: AsyncSession = Depends(get_db)):
    logger.info(f"[ROUTE] POST /internal/testcase for requirement_id={payload.requirement_id}")
    try:
        testcase = TestCase(
            requirement_id=payload.requirement_id,
            version=payload.version,
            content=payload.content
        )
        await create_testcase(db, testcase)
        return testcase
    except Exception as e:
        logger.exception("[ROUTE] Failed to create test case")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/internal/testcase/{requirement_id}", response_model=TestCaseList)
async def list_testcases(requirement_id: UUID, db: AsyncSession = Depends(get_db)):
    logger.info(f"[ROUTE] GET /internal/testcase/{requirement_id}")
    try:
        testcases = await get_testcases_by_requirement(db, requirement_id)
        return TestCaseList(testcases=testcases)
    except Exception as e:
        logger.exception("[ROUTE] Failed to fetch test cases")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/internal/testcase/{requirement_id}/version/{version}", response_model=TestCaseInDB)
async def get_testcase_version(requirement_id: UUID, version: str, db: AsyncSession = Depends(get_db)):
    logger.info(f"[ROUTE] GET /internal/testcase/{requirement_id}/version/{version}")
    try:
        result = await get_testcase_by_version(db, requirement_id, version)
        if result is None:
            raise HTTPException(status_code=404, detail="Test case not found")
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.exception("[ROUTE] Failed to fetch specific test case version")
        raise HTTPException(status_code=500, detail="Internal Server Error")
