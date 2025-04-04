from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    name: str
    id: int
    age: int 
    email: str

users_list = [User(name="John", age=30, email="john@example.com", id=1), User(name="Jane", age=25, email="jane@example.com", id=2)]

@app.get('/')
async def root(): 
    return {"message": "Hello World"}

@app.get("/users")
async def get_users():
    return users_list

@app.get("/users/{id}")
async def get_user(id: int):
    try:
        user = filter(lambda user: user.id == id, users_list)
        return list(user    )[0]
    except: 
        return  {"message": "User not found"}

