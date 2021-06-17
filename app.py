from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message" : "hello world + 1"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/about")
async def show_about():
    return {"message": "here is about"}

class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

@app.get("/users/me")
async def read_user_me():
    external_data = {
        'id': '123',
        'signup_ts': '2019-06-01 12:22',
        'friends': [1, 2, '3'],
    }
    user = User(**external_data)
    return user

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
# In that case, the URL would be: /files//home/johndoe/myfile.txt, with a double slash (//) between files and home.

