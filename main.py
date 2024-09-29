
from typing import List

import strawberry
from fastapi import FastAPI, HTTPException
from strawberry.fastapi import GraphQLRouter

from database import SessionLocal
from models import Post, User

app=FastAPI()


@strawberry.type
class PostType:
    id:int
    title:str
    description:str

@strawberry.type
class UserType:
    id:int
    name:str
    email:str
    role:str
    posts: List[PostType]


@strawberry.type
class QueryResolvers:
    @strawberry.field
    def getUsers(self,id:int) -> UserType:
          session = SessionLocal()
          user=session.get(User,id)
          if not user:
              raise HTTPException(status_code=400,detail="User Not Found")
          return UserType(id=user.id,name=user.name,email=user.email,role=user.role,posts=user.posts)
        
    @strawberry.field
    def getPost(self,id:int)->PostType:
            session = SessionLocal()
            post=session.get(Post,id)
            if not post:
                raise HTTPException(status_code=400,detail="Post are not found")
            return PostType(id=post.id,title=post.title,description=post.description)
        

@strawberry.type
class Mutation:

    @strawberry.mutation
    def createUser(self,name:str,email:str,role:str) -> UserType:
          session = SessionLocal()
          new_user=User(name=name,email=email,role=role)
          session.add(new_user)
          session.commit()
          session.refresh(new_user)
          return UserType(id=new_user.id,name=new_user.name,email=new_user.email,role=new_user.role,posts=[])
        
    @strawberry.mutation
    def createPost(self,title:str,description:str,author_id:int) -> PostType:
            session = SessionLocal()
            new_post=Post(Title=title,Description=description,author_id=author_id)
            session.add(new_post)
            session.commit()
            session.refresh(new_post)
            return PostType(id=new_post.id,title=new_post.title,description=new_post.description)
        

schema=strawberry.Schema(query=QueryResolvers,mutation=Mutation)

graphql_app=GraphQLRouter(schema)

app.include_router(graphql_app,prefix='/graph')

