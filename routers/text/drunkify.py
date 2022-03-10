from fastapi import APIRouter
from utils import update_db
import random

tags_metadata = [
    {
        "name": "Drunkify Text"
    }
]

drunkify = APIRouter(tags=tags_metadata)

@drunkify.get("/api/drunkify")
async def generate_drunk(text : str):
    update_db("drunkify")

    lst = [str.lower, str.upper]
    drunkified = ''.join(random.choice(lst)(c) for c in text)

    return {
        "text" : drunkified
    }