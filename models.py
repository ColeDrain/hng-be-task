from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    slackUsername: str
    backend: bool
    age: int
    bio: str