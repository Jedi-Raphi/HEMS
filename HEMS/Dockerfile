From python:3.14

run apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

run pip install --upgrade pip
run pip install flask paho-mqtt 
run pip install simple_pid

COPY . /app
WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["python", "HEMS.py"]