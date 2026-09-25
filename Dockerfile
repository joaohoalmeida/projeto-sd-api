FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recomends libpq-dev gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml /app/

RUN pip install --upgrade pip \
    && pip install --no-cache-dir .

COPY . /app/