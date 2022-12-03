from .database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

class DbComment(Base):
    __tablename__ = 'commentdata'
    id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer,unique=True,nullable=False)
    person_name = Column(String(30),unique=True,nullable=False)
    comment = Column(String(255),unique=True,nullable=False)
    card_id = Column(Integer, ForeignKey('card.id'))
    clicked_comment = relationship('DbCard',back_populates='commentby')


class DbLike(Base):
    __tablename__ = 'likedata'
    id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer,unique=True,nullable=False)
    person_name = Column(String(30),unique=True,nullable=False)
    resume = Column(String(255),unique=True,nullable=False)
    card_id = Column(Integer, ForeignKey('card.id'))
    clicked_likes = relationship('DbCard',back_populates='liker')


class DbCard(Base):
    __tablename__ = 'card'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    content = Column(String)
    description = Column(String)
    like_point = Column(Integer)
    comment_point = Column(Integer)
    owner_id = Column(Integer, ForeignKey('user.id'))
    liker = relationship('DbLike',back_populates='clicked_likes')
    commentby = relationship('DbComment',back_populates='clicked_comment')


class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30),unique=True,nullable=False)
    email = Column(String(30),unique=True,nullable=False)
    password = Column(String(255),nullable=False)
    is_admin = Column(Boolean,default=False,nullable=False)
    # created_products = relationship('DbCard',back_populates='owner')

