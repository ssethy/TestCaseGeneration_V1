# ✅ tests/conftest.py

import pytest_asyncio
from httpx import AsyncClient, ASGITransport  # ✅ Import ASGITransport
from app.main import app
from app.database import Base, get_db
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import logging

# ✅ Setup logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# ✅ Setup test database (SQLite in-memory)
DATABASE_URL = "sqlite+aiosqlite:///:memory:"
engine = create_async_engine(DATABASE_URL, echo=False)
TestingSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# ✅ Setup DB schema before test session
@pytest_asyncio.fixture(scope="session")
async def db_setup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("✅ Test DB schema created.")
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    logger.info("🧹 Test DB schema dropped.")

# ✅ Create DB session per test
@pytest_asyncio.fixture
async def db_session(db_setup):
    async with TestingSessionLocal() as session:
        yield session

# ✅ Inject test DB session and test client using ASGITransport
@pytest_asyncio.fixture
async def client(db_session):
    async def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    # ✅ Use ASGITransport to wrap FastAPI app for test client
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as test_client:
        yield test_client
