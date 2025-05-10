FROM python:3.13.3-slim-bullseye

WORKDIR /app

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev build-essential postgresql-client && \
    rm -rf /var/lib/apt/lists/*

# Создаём юзера
ARG HOST_UID=1000
ARG HOST_GID=1000

RUN groupadd -g $HOST_GID django && \
    useradd -m -u $HOST_UID -g $HOST_GID django

# Копируем зависимости и устанавливаем от root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальное с правильными правами
COPY --chown=django:django . .

# Переключаемся на пользователя
USER django

# Готовим entrypoint
RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]