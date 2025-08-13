# Dockerfile for OpsAI
# Docker container setup for AI-powered operations platform
#
# Author: Ayush
# GitHub: https://github.com/pheonix-19
# Copyright (c) 2025

FROM python:3.11-slim

# set a working directory
WORKDIR /app

# install system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
 && rm -rf /var/lib/apt/lists/*

# upgrade pip and install with better timeout settings
RUN pip install --upgrade pip

# copy only requirements first (for caching)
COPY requirements.txt .

# install pip deps with increased timeout and retries
RUN pip install --no-cache-dir \
    --timeout 1000 \
    --retries 5 \
    --default-timeout=1000 \
    -r requirements.txt

# copy source
COPY src/ src/
COPY .env .

# expose port
EXPOSE 8000

# default command
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
