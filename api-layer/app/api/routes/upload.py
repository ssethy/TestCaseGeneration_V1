from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
import os
import tempfile
import shutil

from app.clients.document_client import preprocess_document
from app.clients.requirement_client import post_internal_requirement
from app.schemas.response_models import UploadResponse
from app.schemas.request_models import ParsedSection

router = APIRouter()


@router.post("/upload", response_model=UploadResponse)
def upload_document(file: UploadFile = File(...)):
    try:
        file_ext = file.filename.split('.')[-1].lower()

        print(f"Before ile name: {file.filename}")
        print(f"Before file ext: {file_ext}")
        
        parsed = preprocess_document(file, file_ext)

        print(f"Parsed sections: {parsed}")

        print(f"AFter file name: {file.filename}")
        print(f"After file ext: {file_ext}")

        created_requirement = post_internal_requirement(
            sections=parsed["sections"],
            raw_text=parsed["raw_text"]
        )
        if not created_requirement:
            raise HTTPException(status_code=500, detail="Failed to create requirement")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        return UploadResponse(
            requirement_id=created_requirement.requirement_id,
            title=created_requirement.title,
            version=created_requirement.version,
            testcase_generation_status=created_requirement.testcase_generation_status,
            sections=created_requirement.sections
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

