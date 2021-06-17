from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message" : "hello world + 1"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/about")
def show_about():
    return {"message": "here is about"}