# app/services/requirement_logic.py

import httpx
import os
from fastapi import HTTPException
from app.utils.logger import logger

DB_SERVICE_BASE_URL = os.getenv("DB_SERVICE_BASE_URL", "http://testcase-db-service:8002/internal/requirement")


async def create_requirement_service(requirement_data: dict) -> dict:
    logger.info("Sending request to create new requirement via DB service")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(DB_SERVICE_BASE_URL, json=requirement_data)
            response.raise_for_status()
            logger.info("Requirement created successfully")
            return response.json()
    except httpx.RequestError as e:
        logger.error(f"Error connecting to DB service: {e}")
        raise HTTPException(status_code=500, detail="Internal DB service connection failed")
    except httpx.HTTPStatusError as e:
        logger.error(f"DB service responded with error: {e.response.status_code} - {e.response.text}")
        raise HTTPException(status_code=e.response.status_code, detail="Failed to create requirement")


async def list_requirements_service() -> list:
    logger.info("Fetching all requirements from DB service")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(DB_SERVICE_BASE_URL)
            response.raise_for_status()
            logger.info("Requirements fetched successfully")
            return response.json()
    except httpx.RequestError as e:
        logger.error(f"Error connecting to DB service: {e}")
        raise HTTPException(status_code=500, detail="Internal DB service connection failed")
    except httpx.HTTPStatusError as e:
        logger.error(f"DB service error during list fetch: {e.response.status_code} - {e.response.text}")
        raise HTTPException(status_code=e.response.status_code, detail="Failed to fetch requirements")


async def get_requirement_by_id_service(requirement_id: str) -> dict:
    logger.info(f"Fetching requirement with ID: {requirement_id}")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{DB_SERVICE_BASE_URL}/{requirement_id}")
            response.raise_for_status()
            logger.info("Requirement detail fetched successfully")
            return response.json()
    except httpx.RequestError as e:
        logger.error(f"Error connecting to DB service: {e}")
        raise HTTPException(status_code=500, detail="Internal DB service connection failed")
    except httpx.HTTPStatusError as e:
        logger.error(f"DB service error fetching requirement ID {requirement_id}: {e.response.status_code}")
        raise HTTPException(status_code=e.response.status_code, detail="Requirement not found")


async def update_requirement_status_service(requirement_id: str, status_update: dict) -> dict:
    logger.info(f"Updating test case generation status for requirement ID: {requirement_id}")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.patch(f"{DB_SERVICE_BASE_URL}/{requirement_id}/status", json=status_update)
            response.raise_for_status()
            logger.info("Requirement status updated successfully")
            return response.json()
    except httpx.RequestError as e:
        logger.error(f"Error connecting to DB service: {e}")
        raise HTTPException(status_code=500, detail="Internal DB service connection failed")
    except httpx.HTTPStatusError as e:
        logger.error(f"DB service error during status update: {e.response.status_code} - {e.response.text}")
        raise HTTPException(status_code=e.response.status_code, detail="Failed to update requirement status")
