# app/crud/testcase.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.testcase import TestCase
from app.schemas.testcase import TestCaseCreate
from uuid import uuid4


async def create_testcase(session: AsyncSession, data: TestCaseCreate) -> TestCase:
    tc = TestCase(
        test_case_id=uuid4(),
        requirement_id=data.requirement_id,
        version=data.version,
        content=data.content,
        author=data.author,
        change_reason=data.change_reason
    )
    session.add(tc)
    await session.commit()
    await session.refresh(tc)
    return tc


async def get_testcases_by_requirement(session: AsyncSession, requirement_id):
    stmt = select(TestCase).where(TestCase.requirement_id == requirement_id)
    result = await session.execute(stmt)
    return result.scalars().all()
