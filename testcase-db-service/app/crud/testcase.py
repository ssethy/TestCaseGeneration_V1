import logging
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.testcase import TestCase
from typing import List, Optional

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

async def create_testcase(session: AsyncSession, testcase_data) -> TestCase:
    testcase = TestCase(
        requirement_id=testcase_data.requirement_id,
        version=testcase_data.version,
        content=testcase_data.content,
    )
    session.add(testcase)
    await session.flush()
    logger.info(f"Created testcase for requirement_id={testcase.requirement_id} version={testcase.version}")
    return testcase

async def get_testcases_by_requirement(session: AsyncSession, requirement_id: int) -> List[TestCase]:
    logger.info(f"Fetching testcases for requirement_id={requirement_id}")
    result = await session.execute(select(TestCase).where(TestCase.requirement_id == requirement_id))
    testcases = result.scalars().all()
    logger.info(f"Found {len(testcases)} testcases for requirement_id={requirement_id}")
    return testcases

async def get_testcase_by_version(session: AsyncSession, requirement_id: int, version: str) -> Optional[TestCase]:
    logger.info(f"Fetching testcase for requirement_id={requirement_id} version={version}")
    result = await session.execute(
        select(TestCase).where(
            TestCase.requirement_id == requirement_id,
            TestCase.version == version
        )
    )
    testcase = result.scalar_one_or_none()
    if testcase:
        logger.info(f"Found testcase id={testcase.testcase_id} for requirement_id={requirement_id} version={version}")
    else:
        logger.warning(f"No testcase found for requirement_id={requirement_id} version={version}")
    return testcase
