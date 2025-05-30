#!/bin/bash

# Wait for PostgreSQL to be available
./wait-for-postgres.sh postgres 5432

# Run DB initialization (if needed)
./init_db.sh

# Launch the FastAPI app
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
