import logging
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.requirement import Requirement, RequirementLabel

logger = logging.getLogger(__name__)

async def get_or_create_label(session: AsyncSession, label_name: str) -> int:
    logger.info(f"Looking for label: {label_name}")
    result = await session.execute(select(RequirementLabel).where(RequirementLabel.requirement_label == label_name))
    label = result.scalar_one_or_none()
    if label:
        return label.label_id

    new_label = RequirementLabel(requirement_label=label_name)
    session.add(new_label)
    await session.flush()
    return new_label.label_id

async def create_requirement(session: AsyncSession, payload):
    label_id = await get_or_create_label(session, payload.requirement_label)
    requirement = Requirement(
        label_id=label_id,
        title=payload.title,
        version=payload.version,
        raw_text=getattr(payload, 'raw_text', ''),
        requirement_detail=payload.requirement_detail,
        testcase_generation_status=payload.testcase_generation_status,
        meta_info=getattr(payload, 'meta_info', None)
    )
    session.add(requirement)
    await session.flush()
    return requirement

async def get_latest_requirements(session: AsyncSession):
    query = text("""
        SELECT DISTINCT ON (rl.requirement_label) r.*
        FROM requirements r
        JOIN requirement_labels rl ON r.label_id = rl.label_id
        ORDER BY rl.requirement_label, r.created_at DESC
    """)
    result = await session.execute(query)
    return [dict(row._mapping) for row in result]

async def get_requirement_by_id(session: AsyncSession, req_id):
    result = await session.execute(select(Requirement).where(Requirement.requirement_id == req_id))
    return result.scalar_one_or_none()
