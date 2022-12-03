from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from router.schemas import UserRequestSchema, UserResponseSchema, UserResponseWithProductsSchema
from db.database import get_db
from db import db_user
from typing import List

router = APIRouter(
    prefix='/api/v1/users',
    tags=['users']
)


@router.post('')
async def create(request: UserRequestSchema, db: Session = Depends(get_db)):
    return db_user.create(db=db, request=request)


@router.get('/all', response_model=List[UserResponseSchema])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all(db)


@router.get('/id/{user_id}', response_model=UserResponseWithProductsSchema)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return db_user.get_user_by_id(user_id=user_id, db=db)


@router.get('/{user_email}', response_model=UserResponseWithProductsSchema)
def get_user_by_email(user_email: str, db: Session = Depends(get_db)):
    return db_user.get_user_by_email(user_email=user_email, db=db)