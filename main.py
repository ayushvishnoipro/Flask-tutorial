from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/blog")
def index(limit = 10,published: Optional[bool] = True, sort: Optional[str] = None): 
    if published:
        return {"data": f'{limit} blog published'}
    else:
        return {"data": f'{limit} blog unpublished'}
    

@app.get("/blog/unpublished")
def unpublished():
    return {"data": 'all blog unpublished'}

@app.get("/blog/{id}")
def show(id:int):
    return {"data": id}



@app.get("/blog/comments/{id}")
def comment(id,limit:int = 10): 
    return {"data": {'1','2','3'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = True

@app.post("/blog")
def create_blog(request: Blog):
    return {"data": f'blog is created with title as {request.title} '}