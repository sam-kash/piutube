from fastapi import FastAPI, HTTPException

app = FastAPI()

text_posts = {1: {"title":"New Post", "content":"cool test post"} }

@app.get("/hello-world")
def hello_world():
    return {"message" : "Hello-world"}

@app.get("/")
def first():
    return {"message" : "write the url as piutube to actually start"}

@app.get("/piutube")
def piutube():
    return {"message" : "welcome to piutube"} 

@app.get("/piutube/posts")
def get_all_posts(limit: int =10):
    if limit:
        return text_posts[:limit]
    return text_posts

@app.get("/piutube/posts/{id}") 
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detaiil ="Post not found")
    return text_posts.get(id)