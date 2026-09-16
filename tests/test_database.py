"""Tests for database models and operations."""

from app.database.models import Article, Company, ArticleCompany, Feedback


def test_database_tables_created(db_session):
    """Verify tables can be created."""
    from app.database.database import Base
    Base.metadata.create_all(db_session.get_bind())
    inspector = db_session.get_bind()
    # Just ensure no exception is raised
    assert inspector is not None


def test_insert_article(db_session):
    """Test inserting an article."""
    article = Article(
        title="DB Test Article",
        source="Test Source",
        url="https://example.com/db-test",
        content="DB test content",
    )
    db_session.add(article)
    db_session.commit()
    db_session.refresh(article)

    assert article.id is not None
    assert article.title == "DB Test Article"
    assert article.source == "Test Source"


def test_retrieve_article(db_session):
    """Test retrieving an article."""
    article = Article(
        title="Retrieve Test",
        source="Test Source",
        content="Content",
    )
    db_session.add(article)
    db_session.commit()
    db_session.refresh(article)

    found = db_session.query(Article).filter(Article.id == article.id).first()
    assert found is not None
    assert found.title == "Retrieve Test"


def test_insert_company(db_session):
    """Test inserting a company."""
    company = Company(canonical_name="Test Company", ticker="TC")
    db_session.add(company)
    db_session.commit()
    db_session.refresh(company)

    assert company.id is not None
    assert company.canonical_name == "Test Company"
    assert company.ticker == "TC"


def test_article_company_relationship(db_session, sample_article, sample_company):
    """Test article-company many-to-many relationship."""
    link = ArticleCompany(
        article_id=sample_article.id,
        company_id=sample_company.id,
        tagging_method="manual",
        confidence=0.95,
        evidence="Test evidence",
    )
    db_session.add(link)
    db_session.commit()

    # Verify link exists
    found_link = db_session.query(ArticleCompany).filter_by(
        article_id=sample_article.id,
        company_id=sample_company.id,
    ).first()
    assert found_link is not None
    assert found_link.confidence == 0.95

    # Verify reverse lookup
    company_links = (
        db_session.query(ArticleCompany)
        .filter(ArticleCompany.article_id == sample_article.id)
        .all()
    )
    assert len(company_links) == 1


def test_submit_feedback(db_session, sample_article):
    """Test submitting feedback."""
    feedback = Feedback(
        article_id=sample_article.id,
        rating=4,
        comment="Good tagging",
    )
    db_session.add(feedback)
    db_session.commit()
    db_session.refresh(feedback)

    assert feedback.id is not None
    assert feedback.rating == 4
    assert feedback.comment == "Good tagging"

    # Retrieve feedback
    feedbacks = db_session.query(Feedback).filter_by(article_id=sample_article.id).all()
    assert len(feedbacks) == 1
    assert feedbacks[0].rating == 4
