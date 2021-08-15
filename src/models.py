import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String, nullable=False)
    _password=Column(String, nullable=False)
    biography = Column(String, nullable=True)
    register_date = Column(Date, nullable=False)
    username = Column(String, unique=True)
    profile_photo = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)

class Posts(Base):
    __tablename__ = 'Posts'
    Post_id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('user.id'))
    Description = Column(String, nullable = True)

class Media(Base):
    __tablename__ = 'Media'
  
    Media_id = Column(Integer, primary_key=True)
    Post_id = Column(Integer, ForeignKey('Posts.Post_id'))
    Source_Media = Column(String)
    Type_Media = Column(Enum)  

class Followers(Base):
    __tablename__ = 'followers'
      
    Followers_id = Column(Integer, primary_key=True)
    User_From_id = Column(Integer, ForeignKey('user.id'))
    User_To_id = Column(Integer, ForeignKey('user.id'))

class Dms(Base):
    __tablename__ = 'Dms'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    text = Column(String, nullable = True)



class Comment(Base):
    __tablename__ = 'Comment'
    Comment_id = Column(Integer, primary_key=True)
    Post_id = Column(Integer, ForeignKey('Posts.Post_id'))
    User_id = Column(Integer, ForeignKey('user.id'))
    Comment = Column(String)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e