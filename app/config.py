"""Application configuration via environment variables."""

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables or .env file."""

    app_name: str = "News Tagging Demo"
    app_version: str = "0.1.0"
    debug: bool = False

    # Database
    database_url: str = "sqlite:///./data/news_tagging.db"

    # API
    api_prefix: str = "/api/v1"

    # Paths (relative to project root)
    data_dir: Path = Path("data")
    raw_articles_dir: Path = Path("data/raw")
    processed_articles_dir: Path = Path("data/processed")

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance."""
    return Settings()
