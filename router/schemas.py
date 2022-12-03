from pydantic import BaseModel, validator, EmailStr
from typing import List

class CardRequestSchema(BaseModel):
    title: str
    author: str
    content: str
    description: str
    like_point: int
    comment_point: int
    # owner_id: int


class CardResponseSchema(CardRequestSchema):
    id: int
    # owner_id: int

    class Config:
        orm_mode = True


# class CardResponseWithUserSchema(CardRequestSchema):
#     id: int

#     class Config:
#         orm_mode = True


# -------------------------------------------

class UserBase(BaseModel):
    username: str
    email: EmailStr
    is_admin: bool


class UserRequestSchema(UserBase):
    password1: str
    password2: str

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v

    @validator("password1")
    def password_must_have_6_digits(cls, v):
        if len(v) < 6:
            raise ValueError("Password must have at least 6 digits")
        return v


class UserResponseSchema(UserBase):
    id: int

    class Config:
        orm_mode = True

class CardResponseWithUserSchema(CardRequestSchema):
    id: int
    # owner_id: int
    # owner: UserResponseSchema

    class Config:
        orm_mode = True


class UserResponseWithProductsSchema(UserBase):
    id: int
    created_products: List[CardResponseSchema] = []

    class Config:
        orm_mode = True

# -------------------------------------------
class LikeRequestSchema(BaseModel):
    person_id: int
    person_name: str
    resume: str
    card_id: int

class LikeResponseSchema(LikeRequestSchema):
    id: int
    card_id: int
    # clicked_likes: CardResponseSchema

    class Config:
        orm_mode = True


class LikeResponseWithCardSchema(LikeRequestSchema):
    id: int
    card_id: int
    clicked_likes: CardResponseSchema

    class Config:
        orm_mode = True


# class CardResponseWithLikesSchema(CardRequestSchema):
#     id: int
#     # card_id: int
#     liker: List[LikeResponseSchema] = []

#     class Config:
#         orm_mode = True


# -------------------------------------------
class CommentRequestSchema(BaseModel):
    person_id: int
    person_name: str
    comment: str
    card_id: int

class CommentResponseSchema(CommentRequestSchema):
    id: int
    card_id: int
    # clicked_likes: CardResponseSchema

    class Config:
        orm_mode = True


class CommentResponseWithCardSchema(CommentRequestSchema):
    id: int
    card_id: int
    clicked_comment: CardResponseSchema

    class Config:
        orm_mode = True


class CardResponseWithLikesCommentSchema(CardRequestSchema):
    id: int
    # card_id: int
    liker: List[LikeResponseSchema] = []
    commentby: List[CommentResponseSchema] = []

    class Config:
        orm_mode = True
