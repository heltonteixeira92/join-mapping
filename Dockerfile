FROM python:3.7-slim-buster

#ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt update -y \
    && apt install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    wait-for-it \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install -U pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

#COPY contrib/env-sample .env

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]