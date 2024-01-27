# Base
FROM python:3.11-slim AS base

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y libpq5

# Development
FROM base AS development

ENV PYTHONDONTWRITEBYTECODE 1

ENV POETRY_HOME=/opt/poetry

WORKDIR /app

RUN python -m venv $POETRY_HOME && \
    $POETRY_HOME/bin/pip install poetry~=1.7 && \
    ln -s $POETRY_HOME/bin/poetry /usr/local/bin/poetry && \
    poetry self add poethepoet[poetry_plugin]~=0.24 poetry-bumpversion~=0.3

# Builder
FROM development AS builder

RUN apt-get update && \
    apt-get install -y gcc libpq-dev

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt -E c -E gunicorn | pip install --prefix /env/ -r /dev/stdin

COPY . .

RUN pip install --no-deps --prefix /env/ .

# Production
FROM base AS production

ENV STATIC_ROOT=/static

RUN addgroup --system app \
    && adduser --system --ingroup app app \
    && mkdir -p $STATIC_ROOT \
    && chmod 755 -R $STATIC_ROOT \
    && chown app:app -R $STATIC_ROOT

COPY --from=builder /env/ /usr/local/

USER app

EXPOSE 8000

CMD gunicorn django_htmx_todo.wsgi:application -w ${WORKERS:-4} --bind 0.0.0.0:8000
