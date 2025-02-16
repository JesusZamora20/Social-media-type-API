from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return{"message":"Hello FastAPI"}

@app.get("/posts")
def get_cars():
    return {"data":"This is your post"}