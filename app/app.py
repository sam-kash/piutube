from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate  
app = FastAPI()

text_posts = {1: {"title":"New Post", "content":"cool test post"} }

@app.get("/hello-world")
def hello_world():
    return {"message" : "Hello-world"}

@app.get("/")
def first():
    return {"message" : "write the url as piutube to actually start"}

@app.get("/piutube")    # From here you look at the actual code     
def piutube():
    return {"message" : "welcome to piutube"} 

@app.get("/piutube/posts")
def get_all_posts(limit: int =10):
    if limit:
        return list(text_posts.vaues())[:limit]
    return text_posts

@app.get("/piutube/posts/{id}") 
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail ="Post not found")
    
    return text_posts.get(id)

@app.post("/piutube/posts")
def create_post(post: PostCreate):  
    new_post = {"title" : post.title , "content" : post.content}
    text_posts[max(text_posts.keys())+1] = new_post
    return new_post