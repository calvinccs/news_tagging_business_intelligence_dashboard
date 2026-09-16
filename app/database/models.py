"""SQLAlchemy models for the news tagging application."""

from datetime import datetime, timezone

from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import relationship

from app.database.database import Base


def _utc_now() -> datetime:
    """Return the current UTC time."""
    return datetime.now(timezone.utc)


# ---------------------------------------------------------------------------
# Article
# ---------------------------------------------------------------------------


class Article(Base):
    """Represents a single financial/news article."""

    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(1024), nullable=False)
    source = Column(String(255), nullable=False)
    url = Column(String(2048), nullable=True)
    published_at = Column(DateTime, nullable=True)
    content = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    # Relationships
    companies = relationship(
        "ArticleCompany",
        back_populates="article",
        cascade="all, delete-orphan",
        lazy="selectin",
    )
    feedback = relationship(
        "Feedback",
        back_populates="article",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    def __repr__(self) -> str:
        return f"<Article(id={self.id}, title='{self.title[:40]}...')>"


# ---------------------------------------------------------------------------
# Company
# ---------------------------------------------------------------------------


class Company(Base):
    """Represents a company / entity mentioned in articles."""

    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    canonical_name = Column(String(255), unique=True, nullable=False, index=True)
    ticker = Column(String(20), nullable=True, index=True)
    aliases = Column(Text, nullable=True)  # JSON string of alternate names
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    # Relationships
    articles = relationship(
        "ArticleCompany",
        back_populates="company",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    def __repr__(self) -> str:
        return f"<Company(id={self.id}, name='{self.canonical_name}')>"


# ---------------------------------------------------------------------------
# ArticleCompany (many-to-many join table)
# ---------------------------------------------------------------------------


class ArticleCompany(Base):
    """Links an article to a company with tagging metadata."""

    __tablename__ = "article_companies"

    id = Column(Integer, primary_key=True, index=True)
    article_id = Column(Integer, ForeignKey("articles.id", ondelete="CASCADE"), nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="CASCADE"), nullable=False)
    tagging_method = Column(
        String(32),
        nullable=False,
        server_default="manual",
    )  # manual | llm | corrected
    confidence = Column(Float, nullable=True)  # 0.0 – 1.0
    evidence = Column(Text, nullable=True)  # short justification
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    # Relationships
    article = relationship("Article", back_populates="companies")
    company = relationship("Company", back_populates="articles")

    __table_args__ = (
        UniqueConstraint("article_id", "company_id", name="uq_article_company"),
    )

    def __repr__(self) -> str:
        return f"<ArticleCompany(article_id={self.article_id}, company_id={self.company_id}, method={self.tagging_method})>"


# ---------------------------------------------------------------------------
# Feedback
# ---------------------------------------------------------------------------


class Feedback(Base):
    """User feedback on article tagging quality."""

    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    article_id = Column(Integer, ForeignKey("articles.id", ondelete="CASCADE"), nullable=False)
    rating = Column(Integer, nullable=False)  # 1–5
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    # Relationships
    article = relationship("Article", back_populates="feedback")

    def __repr__(self) -> str:
        return f"<Feedback(id={self.id}, article_id={self.article_id}, rating={self.rating})>"
