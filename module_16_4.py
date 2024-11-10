from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
users_db = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
def get_all_users() -> List[User]:
    return users_db


@app.get(path="/user/{user_id}")
def get_message(user_id: int) -> User:
    for us in users_db:
        if us.id == user_id:
            return us
    raise HTTPException(status_code=404, detail="User was not found")


@app.post("/user/{username}/{age}")
def create_user(username: str, age: int, create_user: User) -> str:
    if len(users_db) == 0:
        current_index = 1
    else:
        max = users_db[0].id
        for us in users_db:
            if us.id > max:
                max = us.id
        current_index = max + 1
    create_user.id = current_index
    create_user.username = username
    create_user.age = age
    users_db.append(create_user)
    return f"User created!"


@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: int, username: str, age: int) -> str:
    for us in users_db:
        if us.id == user_id:
            us.username = username
            us.age = age
            return f"User updated!"
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
def delete_message(user_id: int) -> str:
    index_del = 0
    for us in users_db:
        if us.id == user_id:
            users_db.pop(index_del)
            return f"User ID={user_id} deleted!"
        index_del += 1
    raise HTTPException(status_code=404, detail="User was not found")

# python -m uvicorn module_16_4:app --reload
