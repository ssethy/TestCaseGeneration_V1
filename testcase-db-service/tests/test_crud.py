import pytest
from app.crud import requirement, testcase
from app.schemas.requirement import RequirementCreate
from app.schemas.testcase import TestCaseCreate

@pytest.mark.asyncio
async def test_requirement_crud(db_session):
    # Create requirement data (simulate Pydantic schema instance)
    requirement_data = RequirementCreate(
        requirement_label="LoginPage",
        title="Login page must allow email/password login",
        version="v1",
        requirement_detail=["Enter email", "Enter password"],
        testcase_generation_status="NOT_STARTED",
        meta_info={"source": "unit-test"},
        raw_text="Raw requirement text",
    )

    # Create requirement
    requirement_obj = await requirement.create_requirement(db_session, requirement_data)
    await db_session.commit()

    assert requirement_obj.requirement_id is not None
    assert requirement_obj.title == requirement_data.title

    # Fetch requirement by ID
    fetched_req = await requirement.get_requirement_by_id(db_session, requirement_obj.requirement_id)
    assert fetched_req is not None
    assert fetched_req.requirement_id == requirement_obj.requirement_id

@pytest.mark.asyncio
async def test_testcase_crud(db_session):
    # First create a requirement for FK
    requirement_data = RequirementCreate(
        requirement_label="SignupPage",
        title="Signup page",
        version="v1",
        requirement_detail=["Enter username", "Enter password"],
        testcase_generation_status="NOT_STARTED",
        meta_info={"source": "unit-test"},
        raw_text="Raw text"
    )
    requirement_obj = await requirement.create_requirement(db_session, requirement_data)
    await db_session.commit()

    # Create testcase data
    testcase_data = TestCaseCreate(
        requirement_id=requirement_obj.requirement_id,
        version="v1",
        content={"steps": ["Open page", "Enter data", "Submit"]}
    )

    # Create testcase
    testcase_obj = await testcase.create_testcase(db_session, testcase_data)
    await db_session.commit()

    assert testcase_obj.testcase_id is not None
    assert testcase_obj.requirement_id == requirement_obj.requirement_id

    # Fetch testcases by requirement_id
    testcases = await testcase.get_testcases_by_requirement(db_session, requirement_obj.requirement_id)
    assert len(testcases) >= 1

    # Fetch specific testcase by version
    fetched_tc = await testcase.get_testcase_by_version(db_session, requirement_obj.requirement_id, "v1")
    assert fetched_tc is not None
    assert fetched_tc.version == "v1"
