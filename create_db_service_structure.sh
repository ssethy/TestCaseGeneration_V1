#!/bin/bash

# Base directory
BASE_DIR="testcase-db-service"

echo "📁 Creating database service structure..."

# Create application directories
mkdir -p $BASE_DIR/app/models
mkdir -p $BASE_DIR/app/crud
mkdir -p $BASE_DIR/app/schemas
mkdir -p $BASE_DIR/migrations/versions
mkdir -p $BASE_DIR/k8s

# Create base code and metadata files
touch $BASE_DIR/app/__init__.py
touch $BASE_DIR/app/config.py
touch $BASE_DIR/app/database.py
touch $BASE_DIR/app/main.py
touch $BASE_DIR/app/models/__init__.py
touch $BASE_DIR/app/crud/__init__.py
touch $BASE_DIR/app/schemas/__init__.py
touch $BASE_DIR/.env
touch $BASE_DIR/README.md
touch $BASE_DIR/requirements.txt

# Create Docker and script files
touch $BASE_DIR/Dockerfile
touch $BASE_DIR/docker-compose.yml
touch $BASE_DIR/wait-for-postgres.sh
touch $BASE_DIR/init_db.sh
touch $BASE_DIR/entrypoint.sh

# Create Kubernetes YAML placeholders
touch $BASE_DIR/k8s/postgres-deployment.yaml
touch $BASE_DIR/k8s/postgres-service.yaml
touch $BASE_DIR/k8s/db-service-deployment.yaml
touch $BASE_DIR/k8s/db-service-service.yaml

# Make relevant shell scripts executable
chmod +x $BASE_DIR/*.sh

echo "✅ Directory structure and empty files created in $BASE_DIR"
