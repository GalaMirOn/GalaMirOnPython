from fastapi import FastAPI

app = FastAPI()

@app.get("/user/admin")
async def get_admin_page() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def get_user_number(user_id:int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/{age}")
async def get_user_info(username: str = "Синица", age: int = 23) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

@app.get("/")
async def get_main_page():
    return {"message": "Главная страница"}

if __name__ == "__main__":
    user_id = 123456
    pass
# python -m uvicorn module_16_1:app --reload