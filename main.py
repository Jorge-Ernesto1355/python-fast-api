
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class User(BaseModel): 
    id: int
    name: str
    age: int
    email: str

users_list = [User(name = "jorge", age = 24, email = "jorge@j.com", id=1), User(name = "said", age = 24, email = "jorge@j.com", id= 2)]


@app.get('/users')
def get_users(): 
    return {"users": users_list}

@app.get('/users/{user_id}')
def get_user(user_id: int):
    user = next((user for user in users_list if user.id == user_id), None)
    if user is None:
        return {"message": "User not found"}
    return {"user": user}