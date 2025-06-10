from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title : str
    content : str

@app.get("/")
def root():
    return {"message":"Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": "these are all my posts"}

@app.post("/createpost")
def create_post(payload : Post):
    print(payload)
    return {"message": "post successfully created."}