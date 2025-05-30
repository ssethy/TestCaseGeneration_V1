#!/bin/bash

mkdir -p requirement-service/app/api
mkdir -p requirement-service/app/models
mkdir -p requirement-service/app/db
mkdir -p requirement-service/app/schemas
mkdir -p requirement-service/app/services
mkdir -p requirement-service/app/utils
mkdir -p requirement-service/tests
mkdir -p requirement-service/k8s

# Touch __init__.py for Python packages
touch requirement-service/app/__init__.py
touch requirement-service/app/api/__init__.py
touch requirement-service/app/models/__init__.py
touch requirement-service/app/db/__init__.py
touch requirement-service/app/schemas/__init__.py
touch requirement-service/app/services/__init__.py
touch requirement-service/app/utils/__init__.py
touch requirement-service/tests/__init__.py

# Core files
touch requirement-service/app/main.py
touch requirement-service/app/api/internal_routes.py
touch requirement-service/app/models/requirement.py
touch requirement-service/app/models/enums.py
touch requirement-service/app/db/database.py
touch requirement-service/app/db/repository.py
touch requirement-service/app/schemas/requirement_schema.py
touch requirement-service/app/services/requirement_logic.py
touch requirement-service/app/utils/logger.py
touch requirement-service/tests/test_requirement.py

# Deployment and configuration
touch requirement-service/k8s/deployment.yaml
touch requirement-service/k8s/service.yaml
touch requirement-service/Dockerfile
touch requirement-service/.dockerignore
touch requirement-service/requirements.txt
touch requirement-service/README.md

