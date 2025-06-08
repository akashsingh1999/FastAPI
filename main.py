from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": "these are all my posts"}

@app.post("/createpost")
def create_post():
    return {"message": "post successfully created."}