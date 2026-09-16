"""FastAPI application factory."""

from fastapi import FastAPI

from app.api.routes import articles, companies, feedback
from app.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)

# Register routers
app.include_router(articles.router, prefix=settings.api_prefix)
app.include_router(companies.router, prefix=settings.api_prefix)
app.include_router(feedback.router, prefix=settings.api_prefix)
