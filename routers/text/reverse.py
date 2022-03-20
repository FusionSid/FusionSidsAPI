import random

from fastapi import APIRouter

from utils import update_stats

tags_metadata = [
    {
        "name": "Reverse Text"
    }
]

reverse = APIRouter(tags=tags_metadata)

@reverse.get("/api/reverse")
@update_stats(name="reverse")
async def generate_reverse(text : str):

    reversed_text = text[::-1]

    return {
        "text" : reversed_text
    }