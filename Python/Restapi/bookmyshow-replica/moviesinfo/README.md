# Movies Info Service

FastAPI microservice for movie information with PostgreSQL and async support.

## Quick Start

```bash
docker-compose up --build
```

## API Endpoints

- `GET /` - Health check
- `GET /items/{item_id}` - Get item by ID
- `GET /docs` - API documentation

## Access

- Application: http://localhost:18000
- API Docs: http://localhost:18000/docs

## Environment

- `MOVIES_SVC_PORT=18000`
- `POSTGRES_DB=movies_info`
- `DATABASE_URL=postgresql://user:password@postgres:5432/movies_info`