from fastapi import FastAPI
from app.api import internal_routes

app = FastAPI(title="Requirement Service API")

app.include_router(internal_routes.router)
