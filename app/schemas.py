from pydantic import BaseModel, EmailStr

class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    
    class config:
        orm_mode = True

class CreateUser(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr

    class config:
        orm_mode = True