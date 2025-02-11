from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return{"message":"Hello FastAPI"}

@app.get("/cars")
def get_cars():
    return {"Cars":"Cars listed by brand"}