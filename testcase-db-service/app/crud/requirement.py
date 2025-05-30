import logging
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.requirement import RequirementLabel, Requirement
from typing import Optional, List
import uuid
from sqlalchemy.orm import selectinload
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

async def get_or_create_label(session: AsyncSession, label_name: str) -> RequirementLabel:
    logger.info(f"Searching for label: {label_name}")
    result = await session.execute(select(RequirementLabel).where(RequirementLabel.requirement_label == label_name))
    label = result.scalar_one_or_none()
    if label:
        logger.info(f"Found existing label: {label_name} (ID: {label.label_id})")
        return label
    new_label = RequirementLabel(requirement_label=label_name)
    session.add(new_label)
    await session.flush()
    logger.info(f"Created new label: {label_name} (ID: {new_label.label_id})")
    return new_label

async def create_requirement(session: AsyncSession, requirement_data) -> Requirement:
    label = await get_or_create_label(session, requirement_data.requirement_label)
    requirement = Requirement(
        requirement_id = uuid.uuid4(),
        label_id=label.label_id,
        title=requirement_data.title,
        version=requirement_data.version,
        raw_text=getattr(requirement_data, "raw_text", None),
        requirement_detail=requirement_data.requirement_detail,
        testcase_generation_status=requirement_data.testcase_generation_status,
        meta_info=requirement_data.meta_info,
    )
    session.add(requirement)
    await session.flush()
    logger.info(f"Created requirement: {requirement.title} (ID: {requirement.requirement_id})")
    return requirement

async def get_latest_requirements(session: AsyncSession) -> List[Requirement]:
    logger.info("Fetching latest requirements per label")
    query = text("""
        SELECT DISTINCT ON (rl.requirement_label) r.requirement_id, rl.requirement_label, r.title, r.version,
        r.testcase_generation_status, r.created_at
        FROM requirements r
        JOIN requirement_labels rl ON r.label_id = rl.label_id
        ORDER BY rl.requirement_label, r.created_at DESC
    """)
    result = await session.execute(query)
    rows = result.mappings().all()
    logger.info(f"Fetched {len(rows)} latest requirements")
    return rows

async def get_requirement_by_id(session: AsyncSession, requirement_id: int) -> Optional[Requirement]:
    logger.info(f"Fetching requirement by ID: {requirement_id}")
    query = (
        select(Requirement)
        .options(selectinload(Requirement.label))  # eager load related label
        .where(Requirement.requirement_id == requirement_id)
    )
    result = await session.execute(query)
    requirement = result.scalar_one_or_none()
    if requirement:
        logger.info(f"Found requirement: {requirement.title} (ID: {result})")
    else:
        logger.warning(f"Requirement not found with ID: {requirement_id}")
    return requirement
