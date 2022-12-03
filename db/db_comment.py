from fastapi import HTTPException, status
from router.schemas import CommentRequestSchema
from sqlalchemy.orm.session import Session
from sqlalchemy import func, exc
from sqlalchemy.exc import IntegrityError

from db.models import DbComment


def create(db: Session, request: CommentRequestSchema) -> DbComment:
    new_comment = DbComment(
        person_id=request.person_id,
        person_name=request.person_name,
        comment=request.comment,
        card_id=request.card_id,
    )
    try:
        db.add(new_comment)
        db.commit()
        db.refresh(new_comment)
        return new_comment
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"{exc}".split('\n')[0])


def get_all(db: Session) -> list[DbComment]:
    comment = db.query(DbComment).all()
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'comment not found')
    return comment


def get_comment_by_id(comment_id: int, db: Session) -> DbComment:
    comment = db.query(DbComment).filter(DbComment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Comment with id = {comment_id} not found')
    return comment

