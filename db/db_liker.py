from fastapi import HTTPException, status
from router.schemas import LikeRequestSchema
from sqlalchemy.orm.session import Session
from sqlalchemy import func, exc
from sqlalchemy.exc import IntegrityError

from db.models import DbLike


def create(db: Session, request: LikeRequestSchema) -> DbLike:
    new_like = DbLike(
        person_id=request.person_id,
        person_name=request.person_name,
        resume=request.resume,
        card_id=request.card_id,
    )
    try:
        db.add(new_like)
        db.commit()
        db.refresh(new_like)
        return new_like
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"{exc}".split('\n')[0])


def get_all(db: Session) -> list[DbLike]:
    like = db.query(DbLike).all()
    if not like:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'like not found')
    return like


def get_like_by_id(like_id: int, db: Session) -> DbLike:
    like = db.query(DbLike).filter(DbLike.id == like_id).first()
    if not like:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Like with id = {like_id} not found')
    return like

