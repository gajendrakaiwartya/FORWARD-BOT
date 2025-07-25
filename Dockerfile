FROM python:3.10.8-slim-bullseye

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /VJ-Forward-Bot
COPY . .

EXPOSE 8000

CMD gunicorn app:app --bind 0.0.0.0:8000 & python3 main.py
