import random

from fastapi import APIRouter

from utils import update_stats

tags_metadata = [
    {
        "name": "Drunkify Text"
    }
]

drunkify = APIRouter(tags=tags_metadata)

@drunkify.get("/api/drunkify")
@update_stats(name="drunkify")
async def generate_drunk(text : str):

    lst = [str.lower, str.upper]
    drunkified = ''.join(random.choice(lst)(c) for c in text)

    return {
        "text" : drunkified
    }