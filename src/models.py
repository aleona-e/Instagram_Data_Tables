import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstName = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Followers(Base):
    __tablename__= 'followers'
    id = Column(Integer, primary_key=True)
    userFromId = Column(Integer, ForeignKey('user.id'), nullable=True)
    userToId = Column(Integer, ForeignKey('user.id'), nullable=True)
   

class Post(Base):
    __tablename__='post'
    id = Column(Integer, primary_key=True)
    user_id =Column(Integer, ForeignKey('user.id'))
    date = Column(String)
    

class Comment(Base):
    __tablename__='comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    length = Column(Integer)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')