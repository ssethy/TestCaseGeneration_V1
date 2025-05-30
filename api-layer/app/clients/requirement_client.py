import os
import requests
from typing import List
from app.schemas.response_models import RequirementSummary, RequirementDetails
from app.schemas.request_models import ParsedSection


REQUIREMENT_SERVICE_URL = os.getenv("REQUIREMENT_SERVICE_URL", "http://requirement-service:8030")


def fetch_all_requirements() -> List[RequirementSummary]:
    try:
        response = requests.get(f"{REQUIREMENT_SERVICE_URL}/internal/requirements", timeout=10)
        response.raise_for_status()
        return [RequirementSummary(**item) for item in response.json()]
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch requirements: {str(e)}")


def fetch_requirement_by_id(requirement_id: str) -> RequirementDetails:
    try:
        response = requests.get(f"{REQUIREMENT_SERVICE_URL}/internal/requirements/{requirement_id}", timeout=10)
        response.raise_for_status()
        return RequirementDetails(**response.json())
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch requirement: {str(e)}")


def post_internal_requirement(sections: List[ParsedSection], raw_text: str) -> RequirementDetails:
    payload = {
        "sections": [section.dict() for section in sections],
        "raw_text": raw_text
    }
    try:
        response = requests.post(f"{REQUIREMENT_SERVICE_URL}/internal/requirements", json=payload, timeout=10)
        response.raise_for_status()
        return RequirementDetails(**response.json())
    except requests.RequestException as e:
        raise Exception(f"Failed to create requirement: {str(e)}")
