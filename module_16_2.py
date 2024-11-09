from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

@app.get("/user/{username}/{age}")
async def get_user_info(username: Annotated[str, Path(min_length=5, max_length=20,description='Enter username', example='UrbanUser')],
                        age:Annotated[int, Path(ge=18, le=120, description= 'Enter age', example='24')]) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

@app.get("/user/{user_id}")
async def get_user_number(user_id:int = Path(ge=1, le=100, description= 'Enter User ID', example='17')) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


if __name__ == "__main__":
    pass
# python -m uvicorn module_16_2:app --reload