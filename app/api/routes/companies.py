"""Company API endpoints."""

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.models import Article, ArticleCompany, Company
from app.schemas import (
    ArticleCompanyCreate,
    ArticleCompanyOut,
    ArticleOut,
    CompanyOut,
    CompanyWithArticles,
)

router = APIRouter(prefix="/companies", tags=["companies"])


@router.get("/", response_model=list[CompanyOut])
def list_companies(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> list[CompanyOut]:
    """Return all companies (paginated)."""
    companies = db.query(Company).offset(skip).limit(limit).all()
    return companies


@router.get("/{company_id}", response_model=CompanyWithArticles)
def get_company(
    company_id: int,
    db: Session = Depends(get_db),
) -> Company:
    """Retrieve a single company by ID."""
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    return company


@router.post("/", response_model=CompanyOut, status_code=status.HTTP_201_CREATED)
def create_company(
    canonical_name: str,
    ticker: Optional[str] = None,
    aliases: Optional[str] = None,
    db: Session = Depends(get_db),
) -> Company:
    """Create a new company."""
    company = Company(canonical_name=canonical_name, ticker=ticker, aliases=aliases)
    db.add(company)
    db.commit()
    db.refresh(company)
    return company


@router.delete("/{company_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_company(
    company_id: int,
    db: Session = Depends(get_db),
) -> None:
    """Delete a company by ID."""
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    db.delete(company)
    db.commit()


@router.get("/{company_id}/articles", response_model=list[ArticleOut])
def get_company_articles(
    company_id: int,
    db: Session = Depends(get_db),
) -> list[Article]:
    """Return all articles associated with a company."""
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    links = (
        db.query(ArticleCompany)
        .filter(ArticleCompany.company_id == company_id)
        .all()
    )
    article_ids = [link.article_id for link in links]
    if not article_ids:
        return []
    articles = (
        db.query(Article).filter(Article.id.in_(article_ids)).all()
    )
    return articles
