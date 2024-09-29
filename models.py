from dataclasses import Field
from typing import List, Optional

from sqlalchemy.engine import create_engine
from sqlmodel import Field, Relationship, SQLModel

from database import DATABASE_URL, base

db_engine = create_engine(DATABASE_URL)

class Post(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    title:str
    description:str
    author_id:int=Field(foreign_key="user.id")
    
    author:"User"=Relationship(back_populates="posts")

class User(SQLModel,table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    name:str
    email:str
    role:str
    posts:List[Post] = Relationship(back_populates="author")




SQLModel.metadata.create_all(bind=db_engine)
