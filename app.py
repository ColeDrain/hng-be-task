'''
Minimal example using fastAPI.
'''
from fastapi import FastAPI
from typing import List
from models import User

db: List[User] = [
    User(
        slackUsername = "anonymous",
        backend = True,
        age = 23,
        bio = "I dey everywhere, more like Vinci of Tech.."
    )
]

app = FastAPI()

@app.get("/")
async def fetch_user():
    return db[0];
