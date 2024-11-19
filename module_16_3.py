from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/")
async def get_all_dict() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_users(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",
                                                  example="UrbanUser")], age: int = Path(ge=18, le=120,
                                                  description="Enter age", example="24"))  -> str:
    value = f"Имя:{username}, возраст:{age}"
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = value
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_users(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",
                                                     example="UrbanUser")],
                       user_id: str = Path(ge=1, le=100, description="Enter User ID", example="25"),
                       age: int = Path(ge=18, le=120, description="Enter age", example="24")) -> str:
    value = f"Имя:{username}, возраст:{age}"
    users[user_id] = value
    return f"User {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_users(user_id: str = Path(ge=1, le=100, description="Enter User ID", example="25"),) -> str:
    for user_id in enumerate(users):
        if user_id == user_id:
            users.pop(user_id)
            return f"User {user_id} has been deleted."
