import random
from typing import List, Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

random.seed(233)


class User(BaseModel):
    name: str
    email: Optional[str] = None
    age: int
    telephone: Optional[str] = None


app = FastAPI()
users = {
    1: User(name="John", age=42),
    2: User(name="Jane", age=36, email="jane@example.com"),
    3: User(name="Jack", age=40, telephone="555-555-5555"),
}


@app.post("/users/create/", response_model=User)
def create_user(user: User):
    user_id = random.randint(4, 100)
    users[user_id] = user
    return user


@app.get("/users", response_model=List[User])
def get_users():
    return [user for user in users.values()]


if __name__ == "__main__":
    uvicorn.run("pydantic_usage:app")
