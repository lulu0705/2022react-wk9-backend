from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from router.schemas import CommentRequestSchema, CommentResponseSchema, CommentResponseWithCardSchema
from db.database import get_db
from db import db_comment
from typing import List

router = APIRouter(
    prefix='/api/v1/comment',
    tags=['comment']
)


@router.post('', response_model=CommentResponseSchema)
async def create(request: CommentRequestSchema, db: Session = Depends(get_db)):
    return db_comment.create(db=db, request=request)


@router.get('/all', response_model=List[CommentResponseSchema])
def get_all_like(db: Session = Depends(get_db)):
    return db_comment.get_all(db)


@router.get('/id/{comment_id}', response_model=CommentResponseWithCardSchema)
def get_comment_by_id(comment_id: int, db: Session = Depends(get_db)):
    return db_comment.get_comment_by_id(comment_id=comment_id, db=db)


# @router.get('/{user_email}', response_model=UserResponseWithProductsSchema)
# def get_user_by_email(user_email: str, db: Session = Depends(get_db)):
#     return db_user.get_user_by_email(user_email=user_email, db=db)
