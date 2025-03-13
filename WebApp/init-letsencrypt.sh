#!/bin/bash

# Устанавливаем настройки
DOMAIN="gos-bot.duckdns.org"
EMAIL="polytex@internet.ru"
DOCKER_COMPOSE_FILE="docker-compose2.yml"

# Останавливаем контейнеры, если они уже запущены
docker-compose -f $DOCKER_COMPOSE_FILE down

# Строим и запускаем контейнеры
docker-compose -f $DOCKER_COMPOSE_FILE up --build -d nginx bot

# Ждём, пока Nginx и Certbot будут готовы
echo "Waiting for Nginx to start..."
sleep 5

# Получаем сертификат
docker-compose -f $DOCKER_COMPOSE_FILE run --rm certbot certonly \
  --webroot -w /var/www/certbot \
  -d $DOMAIN \
  --email $EMAIL \
  --agree-tos \
  --no-eff-email

# Перезапускаем все контейнеры с реальными сертификатами
docker-compose -f $DOCKER_COMPOSE_FILE down
docker-compose -f $DOCKER_COMPOSE_FILE up --build -d

