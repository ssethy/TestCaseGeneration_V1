import logging
from uuid import UUID
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.testcase import TestCase

logger = logging.getLogger(__name__)

# Create test case
async def create_testcase(session: AsyncSession, testcase: TestCase) -> TestCase:
    logger.info(f"[CRUD] Creating testcase for requirement_id={testcase.requirement_id}")
    session.add(testcase)
    await session.flush()
    return testcase

# Get test cases for a requirement_id
async def get_testcases_by_requirement(session: AsyncSession, requirement_id: UUID):
    logger.info(f"[CRUD] Fetching testcases for requirement_id={requirement_id}")
    result = await session.execute(
        select(TestCase).where(TestCase.requirement_id == requirement_id)
    )
    return result.scalars().all()

# Get a specific test case version
async def get_testcase_by_version(session: AsyncSession, requirement_id: UUID, version: str):
    logger.info(f"[CRUD] Fetching testcase for requirement_id={requirement_id}, version={version}")
    result = await session.execute(
        select(TestCase).where(
            TestCase.requirement_id == requirement_id,
            TestCase.version == version
        )
    )
    return result.scalars().first()
