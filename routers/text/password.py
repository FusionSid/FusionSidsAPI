from fastapi import APIRouter
from utils import update_db
import string
import random

tags_metadata = [
    {
        "name": "Generate Password",
    }
]

password = APIRouter(tags=tags_metadata)

@password.get("/api/password")
async def generate_password(length : int = 8):
    update_db("password")
    letters = list(string.ascii_letters + string.digits + string.punctuation)

    pswd = ""
    for i in range(length):
        pswd += random.choice(letters)

    return {
        "password" : pswd
    }