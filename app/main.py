from random import randrange
from fastapi import FastAPI, status, HTTPException, Response, Depends
from typing import Optional, List
from . import models, schemas
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello World"}

@app.get("/posts", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

@app.get("/posts/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id:{id} not found.")
    return post

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

@app.post("/post", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(payload : schemas.PostCreate, db: Session = Depends(get_db)):
    new_post = models.Post(**payload.model_dump())
    db.add(new_post)
    db.commit()
    return new_post

@app.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    if post_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found.")
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/post/{id}")
def update_post(id: int, payLoad: schemas.PostCreate, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found.")
    post_query.update(payLoad.model_dump(), synchronize_session=False)
    db.commit()
    return {"message": "post updated successfully"}

@app.post("/signup", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(payload : schemas.CreateUser, db: Session = Depends(get_db)):
    new_user = models.User(**payload.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(new_user)
    return new_user