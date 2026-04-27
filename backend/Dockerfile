FROM dhi.io/python:3.12-dev

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_NO_DEV=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

COPY --from=ghcr.io/astral-sh/uv:0.10.0 /uv /uvx /bin/

COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-install-project

COPY --chown=1000:1000 . .
RUN uv sync --locked

COPY --chown=1000:1000 entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER 1000:1000

ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 8000
CMD ["uv", "run", "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
