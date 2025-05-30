FROM python:3.11-slim

WORKDIR /app

# Copy source code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables (can be overridden by K8s)
ENV PYTHONUNBUFFERED=1

# Expose FastAPI app on port 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
