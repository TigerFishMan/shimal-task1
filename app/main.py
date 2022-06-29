from fastapi import FastAPI
from pydantic import BaseModel, validator
from datetime import date
import typing

app = FastAPI(title="Task 1")

class User(BaseModel):
    username: str
    email: str
    number: str
    dob: date

    @property
    def age(self) -> int:
        return date.today().year - self.dob.year


@app.get("/")
def home():
    return {"hello": "world"}

@app.post("/users/")
def get_details(user: User):
    result = {
        'username': user.username,
        'email': user.email,
        'number': user.number,
        'dob': user.dob,
        'age': user.age,
    }
    return result
