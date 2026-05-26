FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_SYSTEM_PYTHON=1
ENV UV_COMPILE_BYTECODE=1

WORKDIR /app

COPY pyproject.toml uv.lock ./

COPY BackEnd/ ./BackEnd
COPY database/ ./database
COPY FrontEnd/ ./FrontEnd
COPY main.py ./

RUN uv sync --frozen --no-dev

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

