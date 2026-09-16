"""Tests for API endpoints."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/api/v1/articles/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "app_name" in data
    assert "version" in data


def test_list_articles_empty(db_session):
    """Test listing articles when none exist."""
    response = client.get("/api/v1/articles/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_and_get_article(db_session):
    """Test creating and retrieving an article."""
    # Create
    response = client.post(
        "/api/v1/articles/",
        json={
            "title": "API Test Article",
            "source": "API Source",
            "url": "https://example.com/api-test",
            "content": "API test content",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "API Test Article"
    assert data["source"] == "API Source"
    article_id = data["id"]

    # Retrieve
    response = client.get(f"/api/v1/articles/{article_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "API Test Article"


def test_get_article_not_found():
    """Test retrieving a non-existent article."""
    response = client.get("/api/v1/articles/9999")
    assert response.status_code == 404


def test_list_companies_empty(db_session):
    """Test listing companies when none exist."""
    response = client.get("/api/v1/companies/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_and_get_company(db_session):
    """Test creating and retrieving a company."""
    # Create
    response = client.post(
        "/api/v1/companies/",
        params={"canonical_name": "API Company", "ticker": "API"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["canonical_name"] == "API Company"
    assert data["ticker"] == "API"
    company_id = data["id"]

    # Retrieve
    response = client.get(f"/api/v1/companies/{company_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["canonical_name"] == "API Company"


def test_get_company_not_found():
    """Test retrieving a non-existent company."""
    response = client.get("/api/v1/companies/9999")
    assert response.status_code == 404


def test_submit_feedback(db_session, sample_article):
    """Test submitting feedback."""
    response = client.post(
        "/api/v1/feedback/",
        json={
            "article_id": sample_article.id,
            "rating": 5,
            "comment": "Excellent tagging",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["rating"] == 5
    assert data["comment"] == "Excellent tagging"


def test_submit_feedback_invalid_article():
    """Test submitting feedback for non-existent article."""
    response = client.post(
        "/api/v1/feedback/",
        json={
            "article_id": 9999,
            "rating": 3,
        },
    )
    assert response.status_code == 404


def test_submit_feedback_invalid_rating():
    """Test submitting feedback with invalid rating."""
    response = client.post(
        "/api/v1/feedback/",
        json={
            "article_id": 1,
            "rating": 6,  # Out of range
        },
    )
    assert response.status_code == 422

