from pydantic import BaseModel
from typing import List
class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase): 
    class Config:
        orm_mode = True

class Users(BaseModel):
    name: str
    email: str
    password: str

class ShowUsers(BaseModel):
    name: str
    email: str
    blogs : List[Blog] = []
    class Config:
        orm_mode = True

class ShowBlog(Blog):
    title: str
    body: str
    creator: ShowUsers
    class Config:
        orm_mode = True
