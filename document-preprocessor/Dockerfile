# Base Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies for OCR, PDF parsing, image handling
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    poppler-utils \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set PYTHONPATH so FastAPI app and imports work correctly
ENV PYTHONPATH=/app

# Copy application source code
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Default command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
