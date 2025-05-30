# app/routes.py

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.models.response import PreprocessResponse
from app.service.processor import process_uploaded_document

router = APIRouter()

@router.post("/", response_model=PreprocessResponse)
async def preprocess_document(
    file: UploadFile = File(...),
    file_type: str = Form(...)
):
    try:
        result = process_uploaded_document(file, file_type)
        return result
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
