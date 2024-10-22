# FROM nvidia/cuda:12.4.0-base-ubuntu22.04
FROM python:3.12-slim AS base

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    git \
    python3-pip \
    python3-dev 

# Upgrade pip
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export --without-hashes --without-urls -f requirements.txt -o requirements.txt

# Install PyTorch and other dependencies
# RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/mps

# Install other python packages
RUN pip3 install -r ./requirements.txt

# Download the model
# Set the working directory

WORKDIR /app

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

FROM base AS prepare
RUN huggingface-cli download intfloat/multilingual-e5-large
ENTRYPOINT [ "python" , "prepare_database.py" ]

FROM base AS dev

ENTRYPOINT [ "/bin/bash" ]

FROM base AS serve

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]

