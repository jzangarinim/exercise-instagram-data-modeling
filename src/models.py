import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    bio = Column(String(250), nullable=True)
    password = Column(String, nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    created_at = Column(DateTime(timezone=False))
    profile_img_url = Column(String, nullable=True)

class Following(Base):
    __tablename__ = 'following'
    id = Column(Integer, primary_key=True)
    id_of_following = Column(Integer, ForeignKey('users.id'))

class Follower(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    id_of_follower = Column(Integer, ForeignKey('users.id'))

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    description = Column(String(250), nullable=True)
    media_url = Column(String, nullable=False)

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    commentator_id = Column(Integer, ForeignKey('users.id'))
    commentator_img_url = Column(String, nullable=True)
    comment_text = Column(String, nullable=False)

class Story(Base):
    __tablename__ = 'stories'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    story_url = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=True)
    post = relationship("Post", uselist=False)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
