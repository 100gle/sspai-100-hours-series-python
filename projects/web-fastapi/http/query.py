import uvicorn
from fastapi import FastAPI

app = FastAPI()
fake_data = {
    1: {"name": "100gle", "age": 18},
    2: {"name": "Jenny", "age": 28},
    3: {"name": "Peter", "age": 25},
}

# just change this part:
# ===============
@app.get("/user")
def get_user_by_id(id: int):
    data = fake_data.get(id, None)
    if not data:
        return {"message": "User not found"}
    return data


# ==============

if __name__ == '__main__':
    uvicorn.run("query:app")
