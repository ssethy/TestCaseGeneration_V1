# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router as preprocess_router

app = FastAPI(
    title="Document Preprocessor Service",
    description="Parses and structures requirement documents (PDF, DOCX, Images) for test case generation.",
    version="1.0.0"
)

# Optional: Configure CORS (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(preprocess_router, prefix="/preprocess", tags=["Document Parsing"])

@app.get("/")
def read_root():
    return {"message": "Document Preprocessor Service is running."}
