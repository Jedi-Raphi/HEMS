FROM python:3.14

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install flask paho-mqtt 
RUN pip install simple_pid

COPY . /app
WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["python", "HEMS.py"]