import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class LoginData(BaseModel):
    username: str
    password: str


@app.post("/login")
def login(data: LoginData):
    response = dict(message="Succeed", token="user-token")
    if data.username == "admin":
        response["token"] = "superuser-token"
    elif data.username != "user":
        invalid = dict(
            message="Login failed. Invalid credentials",
            token=None,
        )
        response.update(invalid)

    return response


if __name__ == '__main__':
    uvicorn.run("body:app")
