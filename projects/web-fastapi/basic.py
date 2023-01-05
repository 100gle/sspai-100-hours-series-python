import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def index():
    response = """
    <div style="text-align: center;">
        <h1>Hello, World</h1>
        <p>you got it!</p>
    </div>
    """
    return HTMLResponse(content=response)


router = APIRouter(prefix="/api")


@router.get("/users")
def get_users():
    ...


@router.post("/users/create")
def create_user():
    ...


@router.put("/users/update/{user_id}")
def update_user(user_id):
    ...


@router.delete("/users/delete/{user_id}")
def delete_user(user_id):
    ...


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("basic:app")
