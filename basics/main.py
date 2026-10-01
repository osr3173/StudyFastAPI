from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    name: str
    age: int


@app.get("/")
def root():
    return {'message': "HI"}

@app.get("/hello")
def hello():
    return {'message': "Hello"}

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return user

@app.get("/users")
def get_users():
    return users