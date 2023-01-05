import pathlib

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from popup_api.api import router
from popup_api.models import init_db
from popup_api.settings import settings

app = FastAPI(
    title=settings.SITE_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    docs_url=None,
    redoc_url=None,
)
ROOT = pathlib.Path(__file__).parent
templates = Jinja2Templates(directory=ROOT.joinpath("templates"))


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})


@app.post("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})


@app.get("/docs", include_in_schema=False)
def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/js/swagger-ui-bundle.js",
        swagger_css_url="/static/css/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/js/redoc.standalone.js",
    )


@app.on_event("startup")
def startup():
    init_db()
    print("initialization for app")


app.include_router(router, prefix="/api")
app.mount("/static", StaticFiles(directory=ROOT.joinpath("static")), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
