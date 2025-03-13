# app/Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Установка зависимостей
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Создаем папку для загрузок
RUN mkdir -p /app/uploads

EXPOSE 8000

CMD ["waitress-serve", "--host=0.0.0.0", "--port=8000", "app:app"]


