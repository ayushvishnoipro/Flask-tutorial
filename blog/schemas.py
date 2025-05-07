from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str

class ShowBlog(Blog):
    title: str
    body: str
    class Config:
        orm_mode = True


class Users(BaseModel):
    name: str
    email: str
    password: str

class ShowUsers(BaseModel):
    name: str
    email: str
    class Config:
        orm_mode = True
