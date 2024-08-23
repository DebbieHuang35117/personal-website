FROM nvidia/cuda:12.4.0-base-ubuntu22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    git \
    python3-pip \
    python3-dev 
# Install any python packages you need
COPY requirements.txt requirements.txt

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Install PyTorch and torchvision
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

# Install other python packages
RUN python3 -m pip install -r requirements.txt

# Set the working directory
WORKDIR /app

# Set the entrypoint
ENTRYPOINT [ "python-torch-gpu" ]
