from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

simple = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@simple.get('/simple')
async def simple_page():
    return {"message": "here is simple router"}


@simple.get('/base')
async def base_page(request: Request):

    # return HTMLResponse(content=content)
    # return "haha"
    return templates.TemplateResponse("base.html",{"request": request})
