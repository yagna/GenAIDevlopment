FROM python:3.13-slim

RUN pip install uv

WORKDIR /app

COPY pyproject.toml ./
#RUN uv sync

COPY . .

EXPOSE 18000

CMD ["uv", "run", "python", "main.py"]