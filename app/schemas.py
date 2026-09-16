"""Pydantic schemas for request/response validation."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Article schemas
# ---------------------------------------------------------------------------


class ArticleBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=1024)
    source: str = Field(..., min_length=1, max_length=255)
    url: Optional[str] = Field(None, max_length=2048)
    published_at: Optional[datetime] = None
    content: Optional[str] = None


class ArticleCreate(ArticleBase):
    """Schema for creating a new article."""


class ArticleOut(ArticleBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}


class ArticleWithCompanies(ArticleOut):
    companies: list["CompanyOut"] = []


# ---------------------------------------------------------------------------
# Company schemas
# ---------------------------------------------------------------------------


class CompanyBase(BaseModel):
    canonical_name: str = Field(..., min_length=1, max_length=255)
    ticker: Optional[str] = Field(None, max_length=20)
    aliases: Optional[str] = None


class CompanyCreate(CompanyBase):
    """Schema for creating a new company."""


class CompanyOut(CompanyBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}


class CompanyWithArticles(CompanyOut):
    articles: list["ArticleCompanyOut"] = []


# ---------------------------------------------------------------------------
# ArticleCompany schemas
# ---------------------------------------------------------------------------


class ArticleCompanyCreate(BaseModel):
    company_id: int
    tagging_method: str = "manual"
    confidence: Optional[float] = None
    evidence: Optional[str] = None


class ArticleCompanyOut(BaseModel):
    id: int
    article_id: int
    company_id: int
    tagging_method: str
    confidence: Optional[float] = None
    evidence: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Feedback schemas
# ---------------------------------------------------------------------------


class FeedbackCreate(BaseModel):
    article_id: int
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = None


class FeedbackOut(BaseModel):
    id: int
    article_id: int
    rating: int
    comment: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Health / misc
# ---------------------------------------------------------------------------


class HealthResponse(BaseModel):
    status: str
    app_name: str
    version: str


# ---------------------------------------------------------------------------
# Re-exports for type hints above
# ---------------------------------------------------------------------------

CompanyOut.model_rebuild()
CompanyWithArticles.model_rebuild()
ArticleWithCompanies.model_rebuild()
