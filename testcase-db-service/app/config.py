# app/config.py

import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@postgres:5432/testcase_db"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Singleton settings instance to be imported
settings = Settings()
