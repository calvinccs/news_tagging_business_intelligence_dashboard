# News Tagging Demo

A local AI-powered financial news tagging demo application.

## Overview

This project demonstrates a pipeline for:

1. Ingesting financial/news articles
2. Using a local LLM to identify companies/entities mentioned in each article
3. Storing articles and AI-generated tags
4. Allowing users to rate tagging quality (1-5)
5. Supporting company-level views
6. Providing analytics dashboards
7. Enabling RAG/semantic search

## Planned Architecture

```
Article Ingestion  ->  Entity Tagging (LLM)  ->  Storage (SQLite)
      ->  Feedback Collection  ->  Analytics Dashboard  ->  RAG Search
```

## Phase 1 — What's Implemented

- **FastAPI backend** with RESTful API
- **SQLite database** with SQLAlchemy ORM
- **Database models**: Article, Company, ArticleCompany, Feedback
- **Pydantic schemas** for request/response validation
- **25 synthetic articles** covering 10 companies (ground-truth data)
- **API endpoints**:
  - `GET /api/v1/articles/health` — health check
  - `GET /api/v1/articles/` — list articles
  - `GET /api/v1/articles/{id}` — get article
  - `POST /api/v1/articles/` — create article
  - `DELETE /api/v1/articles/{id}` — delete article
  - `GET /api/v1/companies/` — list companies
  - `GET /api/v1/companies/{id}` — get company
  - `POST /api/v1/companies/` — create company
  - `DELETE /api/v1/companies/{id}` — delete company
  - `GET /api/v1/companies/{id}/articles` — get company's articles
  - `POST /api/v1/feedback/` — submit feedback
  - `GET /api/v1/feedback/article/{id}` — get article feedback
- **pytest test suite** covering database and API operations

## Setup

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (>= 0.12)

### Create the environment

```bash
uv sync
```

This reads `pyproject.toml` and installs all dependencies, then creates a virtual environment.

### Configure

```bash
cp .env.example .env
```

Edit `.env` if you need to change any settings.

### Initialise the database

```bash
uv run python -c "
from app.database.database import engine, SessionLocal
from app.database.models import Base
Base.metadata.create_all(engine)
print('Database tables created.')
"
```

### Load sample data

```bash
uv run python -c "
from app.database.database import engine, SessionLocal
from app.database.models import Base
from data.sample_data import load_sample_data

Base.metadata.create_all(engine)
db = SessionLocal()
result = load_sample_data(db)
db.close()
print(f'Loaded: {result}')
"
```

### Run the FastAPI application

```bash
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`.

Visit `http://localhost:8000/docs` for the interactive Swagger UI.

### Run the tests

```bash
uv run pytest tests/ -v
```

## Future Phases

- **Phase 2**: LM Studio / local LLM integration
- **Phase 3**: AI company/entity tagging
- **Phase 4**: Company normalisation
- **Phase 5**: Web UI
- **Phase 6**: Human feedback integration
- **Phase 7**: Embeddings and RAG
- **Phase 8**: Evaluation framework
- **Phase 9**: L1/L2/L3 analytics dashboard

## Project Structure

```
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── config.py            # Settings (env vars)
│   ├── database/
│   │   ├── __init__.py
│   │   ├── database.py      # Engine & session
│   │   └── models.py        # SQLAlchemy models
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── articles.py  # Article endpoints
│   │       ├── companies.py # Company endpoints
│   │       └── feedback.py  # Feedback endpoints
│   ├── ingestion/           # (Phase 3)
│   ├── llm/                 # (Phase 3)
│   ├── rag/                 # (Phase 7)
│   └── schemas.py           # Pydantic schemas
├── data/
│   ├── raw/                 # (Phase 3)
│   └── processed/           # (Phase 3)
│   └── sample_data.py       # Synthetic dataset
├── tests/
│   ├── conftest.py          # Test fixtures
│   ├── test_database.py     # DB tests
│   └── test_api.py          # API tests
├── .env.example
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## License

MIT — see [LICENSE](LICENSE) for details.
