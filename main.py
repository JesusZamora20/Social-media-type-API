from fastapi import FastAPI, Body
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return{"message":"Hello FastAPI"}

@app.get("/posts")
def get_posts():
    return {"data":"This is your post"}

@app.post("/created")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"newpost": f"{payload['title']}"}