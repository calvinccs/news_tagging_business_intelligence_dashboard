"""Article API endpoints."""

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.models import Article, ArticleCompany, Company
from app.schemas import (
    ArticleCreate,
    ArticleOut,
    ArticleWithCompanies,
    CompanyOut,
    HealthResponse,
)

router = APIRouter(prefix="/articles", tags=["articles"])


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Simple health check endpoint."""
    from app.config import get_settings

    settings = get_settings()
    return HealthResponse(
        status="ok",
        app_name=settings.app_name,
        version=settings.app_version,
    )


@router.get("/", response_model=list[ArticleOut])
def list_articles(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> list[ArticleOut]:
    """Return all articles (paginated)."""
    articles = db.query(Article).offset(skip).limit(limit).all()
    return articles


@router.get("/{article_id}", response_model=ArticleWithCompanies)
def get_article(
    article_id: int,
    db: Session = Depends(get_db),
) -> ArticleWithCompanies:
    """Retrieve a single article by ID."""
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
    return article


@router.post("/", response_model=ArticleOut, status_code=status.HTTP_201_CREATED)
def create_article(
    payload: ArticleCreate,
    db: Session = Depends(get_db),
) -> Article:
    """Create a new article."""
    article = Article(**payload.model_dump())
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


@router.delete("/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_article(
    article_id: int,
    db: Session = Depends(get_db),
) -> None:
    """Delete an article by ID."""
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
    db.delete(article)
    db.commit()
