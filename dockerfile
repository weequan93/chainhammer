FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

ENV SECP256K1_BUILD_TESTS=0
ENV PIP_INDEX_URL=https://mirrors.aliyun.com/pypi/simple/

# Install build dependencies
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends gcc build-essential libffi-dev && \
#     rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        build-essential \
        libffi-dev \
        python3-dev \
        pkg-config \
        libfreetype6-dev \
        libpng-dev \
        libc-dev \
        libssl-dev \
        autoconf \
        automake \
        libtool \
        wget \
    && rm -rf /var/lib/apt/lists/*

RUN wget -O /usr/local/bin/solc https://github.com/ethereum/solidity/releases/download/v0.4.21/solc-static-linux && \
    chmod +x /usr/local/bin/solc


RUN python -m pip install --upgrade pip setuptools wheel
RUN python -m pip install --no-cache-dir pycparser cffi pytest-runner==2.7

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

WORKDIR /app/hammer

# Command to run the application
CMD ["python", "/app/hammer/tps.py"]



