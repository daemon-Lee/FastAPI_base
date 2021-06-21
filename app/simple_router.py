from fastapi import APIRouter
simple = APIRouter()

@simple.get('/simple')
async def simple_page():
    return {"message": "here is simple router"}