#!/bin/bash

mkdir -p api-layer/{app/{api/routes,services,schemas,clients,config,middleware,utils},tests/{test_routes,test_services},kube}

touch api-layer/app/main.py

# API routes
touch api-layer/app/api/routes/{requirements.py,upload.py,test_cases.py}
touch api-layer/app/api/__init__.py

# Services
touch api-layer/app/services/{requirement_service.py,document_service.py,test_case_service.py,llm_queue_service.py,__init__.py}

# Schemas
touch api-layer/app/schemas/{request_models.py,response_models.py,__init__.py}

# Clients
touch api-layer/app/clients/{requirement_client.py,test_case_client.py,document_client.py}

# Config
touch api-layer/app/config/{settings.py,__init__.py}

# Middleware
touch api-layer/app/middleware/{error_handler.py,logging_middleware.py,__init__.py}

# Utils
touch api-layer/app/utils/id_generator.py

# Tests
touch api-layer/tests/test_routes/{test_requirements.py,test_upload.py,test_test_cases.py}
touch api-layer/tests/test_services/{test_requirement_service.py,test_document_service.py,test_test_case_service.py}
touch api-layer/tests/conftest.py

# K8s deployment files
touch api-layer/kube/{api-deployment.yaml,api-service.yaml,ingress.yaml}

# Project root files
touch api-layer/{Dockerfile,requirements.txt,.env,README.md}

echo "✅ API Layer directory structure created successfully."

