# Dockerfile

FROM python:3.10-slim

WORKDIR /app

# Install PostgreSQL client and netcat
RUN apt-get update && \
    apt-get install -y postgresql-client netcat-openbsd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project source (app code + shell scripts)
COPY . .

# Make startup scripts executable
RUN chmod +x ./wait-for-postgres.sh ./init_db.sh ./entrypoint.sh

# Run entrypoint that waits for DB and then starts the app
CMD ["./entrypoint.sh"]
