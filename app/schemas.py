from pydantic import BaseModel

class PostCreate(BaseModel): # inherit from the base model
    title: str
    content: str

class PostResponse(BaseModel):
    title: str
    content : str