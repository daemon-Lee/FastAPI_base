from typing import List, Optional
from pydantic import BaseModel, ValidationError

# to gen a string key run command:
# openssl rand -hex 32
SECRET_KEY = "08e97a024497d80060cb868c5517f4aa9382d5e84298367e56a3c37220d6fd68"
ALOGITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token: str
    token_type: str


class Token(BaseModel):
    username: Optional[str] = None
    scopes: List[str] = []


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[str] = None

