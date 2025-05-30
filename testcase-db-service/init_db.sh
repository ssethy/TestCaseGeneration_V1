#!/bin/bash

set -e

echo "🔄 Starting DB initialization..."

# Ensure required env vars are set
: "${DB_HOST:?Need to set DB_HOST}"
: "${DB_PORT:?Need to set DB_PORT}"
: "${DB_USER:?Need to set DB_USER}"
: "${DB_PASSWORD:?Need to set DB_PASSWORD}"
: "${DB_NAME:?Need to set DB_NAME}"

export PGPASSWORD=$DB_PASSWORD

echo "📡 Connecting to PostgreSQL at $DB_HOST:$DB_PORT..."

psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d "$DB_NAME" <<'SQL'

-- Drop existing tables (for dev rebuild)
DROP TABLE IF EXISTS testcases CASCADE;
DROP TABLE IF EXISTS requirements CASCADE;
DROP TABLE IF EXISTS requirement_labels CASCADE;

-- requirement_labels
CREATE TABLE requirement_labels (
    label_id SERIAL PRIMARY KEY,
    requirement_label TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- requirements
CREATE TABLE requirements (
    requirement_id UUID PRIMARY KEY,
    label_id INTEGER NOT NULL REFERENCES requirement_labels(label_id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    version TEXT NOT NULL,
    requirement_detail JSON NOT NULL,
    testcase_generation_status TEXT CHECK (testcase_generation_status IN ('NOT_STARTED', 'IN_PROGRESS', 'COMPLETED', 'FAILED')) NOT NULL,
    meta_info JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- testcases
CREATE TABLE testcases (
    testcase_id UUID PRIMARY KEY,
    requirement_id UUID NOT NULL REFERENCES requirements(requirement_id) ON DELETE CASCADE,
    version TEXT NOT NULL,
    content JSON NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX idx_label_name ON requirement_labels(requirement_label);
CREATE INDEX idx_requirements_label_id ON requirements(label_id);
CREATE INDEX idx_testcases_requirement_id ON testcases(requirement_id);

SQL

echo "✅ Database schema created successfully."
