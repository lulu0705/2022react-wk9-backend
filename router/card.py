from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
# from router.schemas import ProductRequestSchema, ProductResponseSchema, ProductResponseWithUserSchema  , CardResponseWithUserSchema

from router.schemas import CardRequestSchema, CardResponseSchema, CardResponseWithLikesCommentSchema

from db.database import get_db
from db import db_card
from typing import List

router = APIRouter(
    prefix='/api/v1/cards',
    tags=['cards']
)


# @router.post('', response_model=CardResponseSchema)
# def create(request: CardRequestSchema, db: Session = Depends(get_db)):
#     return db_card.create(db=db, request=request)

# @router.get('/feed', response_model=List[CardResponseSchema])
# def feed_initial_cards(db: Session = Depends(get_db)):
#     return db_card.db_feed(db)

# @router.get('/all', response_model=List[CardResponseSchema])
# def get_all_cards(db: Session = Depends(get_db)):
#     return db_card.get_all(db)

# @router.get('/id/{card_id}', response_model=CardResponseWithUserSchema)
# def get_card_by_id(card_id: int, db: Session = Depends(get_db)):
#     return db_card.get_card_by_id(card_id=card_id, db=db)





# ------------------------------------------------

# @router.get('/id/{card_id}', response_model=CardResponseSchema)
# def get_card_by_id(card_id: int, db: Session = Depends(get_db)):
#     return db_card.get_card_by_id(card_id, db)



# @router.get('/id/{card_id}', response_model=CardResponseWithUserSchema)
# def get_card_by_id(card_id: int, db: Session = Depends(get_db)):
#     return db_card.get_card_by_id(card_id=id, db=db)


# @router.get("/{category}", response_model=List[ProductResponseSchema])
# def get_product_by_category(category: str, db: Session = Depends(get_db)):
#     return db_product.get_product_by_category(category=category, db=db)


@router.post('')
async def create(request: CardRequestSchema, db: Session = Depends(get_db)):
    return db_card.create(db=db, request=request)


@router.get('/all', response_model=List[CardResponseSchema])
def get_all_cards(db: Session = Depends(get_db)):
    return db_card.get_all(db)


@router.get('/id/{card_id}', response_model=CardResponseWithLikesCommentSchema)
def get_card_by_id(card_id: int, db: Session = Depends(get_db)):
    return db_card.get_card_by_id(card_id=card_id, db=db)