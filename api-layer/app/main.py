from fastapi import FastAPI

from app.api.routes import upload, requirements, test_cases

app = FastAPI(
    title="Test Case Generation Platform – API Layer",
    version="1.0.0"
)

# Register API route groups with base path prefix
app.include_router(upload.router, prefix="/api", tags=["Upload"])
app.include_router(requirements.router, prefix="/api/requirements", tags=["Requirements"])
app.include_router(test_cases.router, prefix="/api", tags=["Test Cases"])

# Optional health check endpoint
@app.get("/healthz", tags=["Health"])
def health_check():
    return {"status": "ok"}
