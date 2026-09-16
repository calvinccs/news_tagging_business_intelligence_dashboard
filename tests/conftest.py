"""Shared test fixtures."""

import os
import tempfile
from typing import Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.database.database import Base, get_db
from app.database.models import Article, Company, ArticleCompany, Feedback


@pytest.fixture(autouse=True)
def _setup_test_db(tmp_path):
    """Use a temp-file SQLite DB for all tests."""
    db_file = tmp_path / "test_news_tagging.db"
    db_url = f"sqlite:///{db_file}"
    os.environ["DATABASE_URL"] = db_url

    # Create tables in the app's engine
    engine = create_engine(db_url, connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)

    yield db_file

    Base.metadata.drop_all(engine)


@pytest.fixture()
def db_session(_setup_test_db) -> Generator[Session, None, None]:
    """Provide a transactional database session."""
    db_file = _setup_test_db
    db_url = f"sqlite:///{db_file}"
    engine = create_engine(db_url, connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, class_=Session)
    session = SessionLocal()

    yield session

    session.close()


@pytest.fixture()
def sample_company(db_session: Session) -> Company:
    """Create a sample company."""
    company = Company(canonical_name="Test Corp", ticker="TEST", aliases='["Test Corp Inc"]')
    db_session.add(company)
    db_session.commit()
    db_session.refresh(company)
    return company


@pytest.fixture()
def sample_article(db_session: Session) -> Article:
    """Create a sample article."""
    article = Article(
        title="Test Article",
        source="Test Source",
        url="https://example.com/test",
        content="Test content",
    )
    db_session.add(article)
    db_session.commit()
    db_session.refresh(article)
    return article


@pytest.fixture()
def article_with_company(db_session: Session, sample_article: Article, sample_company: Company) -> Article:
    """Create an article linked to a company."""
    link = ArticleCompany(
        article_id=sample_article.id,
        company_id=sample_company.id,
        tagging_method="manual",
        confidence=0.95,
        evidence="Test link",
    )
    db_session.add(link)
    db_session.commit()
    db_session.refresh(sample_article)
    return sample_article
