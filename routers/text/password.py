import string
import random

from fastapi import APIRouter

from utils import update_stats

tags_metadata = [
    {
        "name": "Generate Password",
    }
]

password = APIRouter(tags=tags_metadata)

@password.get("/api/password")
@update_stats(name="password")
async def generate_password(length : int = 8):
    """Generates a password"""
    letters = list(string.ascii_letters + string.digits + string.punctuation)

    pswd = ""
    for i in range(length):
        pswd += random.choice(letters)

    return {
        "password" : pswd
    }