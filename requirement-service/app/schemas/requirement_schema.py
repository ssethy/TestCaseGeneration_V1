from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# === Metadata and Flowchart ===

class Metadata(BaseModel):
    file_name: str
    upload_time: str
    file_type: str
    detected_language: Optional[str] = None
    total_sections: int

class Flowchart(BaseModel):
    flow_id: str
    nodes: list
    edges: list
    raw_image_path: str

# === Core Models ===

class CreateRequirementRequest(BaseModel):
    raw_text: str
    requirement_label: str
    metadata: Metadata
    flowcharts: Optional[List[Flowchart]] = []

class RequirementResponse(BaseModel):
    requirement_id: str
    version: str
    testcase_generation_status: str

class RequirementDetailResponse(BaseModel):
    requirement_id: str
    requirement_label: str
    raw_text: str
    metadata: Metadata
    flowcharts: Optional[List[Flowchart]]
    version: str
    testcase_generation_status: str
    uploaded_at: datetime

class RequirementSummary(BaseModel):
    requirement_id: str
    requirement_label: str
    version: str
    testcase_generation_status: str
    uploaded_at: datetime

class RequirementListResponse(BaseModel):
    __root__: List[RequirementSummary]

class UpdateStatusRequest(BaseModel):
    testcase_generation_status: str

class UpdateStatusResponse(BaseModel):
    requirement_id: str
    updated: bool
