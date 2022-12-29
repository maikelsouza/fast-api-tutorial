from enum import Enum

from fastapi import FastAPI

app = FastAPI()


@app.get('/users')
async def get_users():
    return {"message": "list users route"}


@app.get('/user/me')
async def get_current_user():
    return {"message": "This is the current user"}


@app.get('/user/{user_id}')
async def get_user(user_id: str):
    return {"user_id": user_id}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you are healthy"}

    if food_name.value == "fruits":
        return {"food_name": food_name, "message": "you are still healthy, but like sweet things"}

    return {"food_name": food_name, "message": "I like chocolate milk"}