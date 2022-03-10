from fastapi import APIRouter
from utils import update_db
import random

tags_metadata = [
    {
        "name": "Reverse Text"
    }
]

reverse = APIRouter(tags=tags_metadata)

@reverse.get("/api/reverse")
async def generate_reverse(text : str):
    update_db("reverse")

    reversed_text = text[::-1]

    return {
        "text" : reversed_text
    }