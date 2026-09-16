"""Feedback API endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.models import Feedback
from app.schemas import FeedbackCreate, FeedbackOut

router = APIRouter(prefix="/feedback", tags=["feedback"])


@router.post("/", response_model=FeedbackOut, status_code=status.HTTP_201_CREATED)
def submit_feedback(
    payload: FeedbackCreate,
    db: Session = Depends(get_db),
) -> Feedback:
    """Submit user feedback on an article's tagging quality."""
    # Verify the article exists
    from app.database.models import Article

    article = db.query(Article).filter(Article.id == payload.article_id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article not found",
        )

    feedback = Feedback(
        article_id=payload.article_id,
        rating=payload.rating,
        comment=payload.comment,
    )
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback


@router.get("/article/{article_id}", response_model=list[FeedbackOut])
def get_feedback_for_article(
    article_id: int,
    db: Session = Depends(get_db),
) -> list[Feedback]:
    """Return all feedback for a given article."""
    feedbacks = (
        db.query(Feedback)
        .filter(Feedback.article_id == article_id)
        .all()
    )
    return feedbacks
