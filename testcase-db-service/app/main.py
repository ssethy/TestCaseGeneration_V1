# app/main.py (updated)

from fastapi import FastAPI
from app.routes.requirement import router as requirement_router
from app.routes.testcase import router as testcase_router
from app.database import init_db
import logging

app = FastAPI(
    title="Testcase DB Service",
    version="1.0.0"
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app.include_router(requirement_router, prefix="/internal")
app.include_router(testcase_router, prefix="/internal")

@app.on_event("startup")
async def startup_event():
    logger.info("Starting Testcase DB Service...")
    await init_db()


# ✅ Health check endpoint
@app.get("/healthz")
async def health_check():
    logger.info("Health check endpoint called")
    return {"status": "ok"}

    