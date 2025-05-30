import logging
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# ✅ Initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# ✅ Use environment variable or default to local sqlite for development
DATABASE_URL = os.getenv("DB_URL", "sqlite+aiosqlite:///./test.db")

engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)

Base = declarative_base()

async def init_db():
    async with engine.begin() as conn:
        logger.info("Creating all tables")
        await conn.run_sync(Base.metadata.create_all)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
