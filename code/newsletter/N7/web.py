import pathlib
import uuid

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

TEMPLATE = pathlib.Path(__file__).parent.joinpath("templates/web")
template = Jinja2Templates(directory=TEMPLATE)

users = [
    dict(id=uuid.uuid4(), name="Steve Jobs"),
    dict(id=uuid.uuid4(), name="Bill Gates"),
    dict(id=uuid.uuid4(), name="Sundar Pichai"),
    dict(id=uuid.uuid4(), name="Jeff Bezos"),
    dict(id=uuid.uuid4(), name="100gle"),
]


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    ctx = dict(request=request)
    return template.TemplateResponse("index.html", context=ctx)


@app.get("/users/", response_class=HTMLResponse)
async def get_users(request: Request):
    ctx = dict(request=request, users=users)
    return template.TemplateResponse("user.html", context=ctx)


@app.get("/users/{name}", response_class=HTMLResponse)
async def add_user(name: str):
    users.append(dict(id=uuid.uuid4(), name=name))
    return RedirectResponse("/users")


if __name__ == '__main__':
    uvicorn.run(app)
