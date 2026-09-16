"""Database engine and session management."""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


class Base(DeclarativeBase):
    """Base class for SQLAlchemy models."""

    pass


def _get_engine():
    """Create engine from current DATABASE_URL env var."""
    db_url = os.environ.get("DATABASE_URL", "sqlite:///./data/news_tagging.db")
    return create_engine(
        db_url,
        connect_args={"check_same_thread": False} if "sqlite" in db_url else {},
    )


def get_db():
    """Yield a database session; closes it on exit.

    Creates a fresh engine each time to support test overrides via
    the DATABASE_URL environment variable.
    """
    engine = _get_engine()
    SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, class_=Session)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    """Create all tables in the database."""
    engine = _get_engine()
    Base.metadata.create_all(engine)


# Module-level sessionmaker for direct DB access (e.g., loading sample data)
SessionLocal = sessionmaker(
    bind=_get_engine(),
    autocommit=False,
    autoflush=False,
    class_=Session,
)
