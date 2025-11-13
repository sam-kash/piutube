from fastapi import FastAPI

app = FastAPI()

@app.get("/hello-world")
def hello_world():
    return {"message" : "Hello-world"}

@app.get("/")
def first():
    return {"message" : "write the url as piutube"}

@app.get("/piutube")
def piutube():
    return {"message" : "welcome to piutube"}