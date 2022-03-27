import json
import random

from fastapi import APIRouter

from utils import update_stats

# Title for docs
tags_metadata = [
    {
        "name": "Compliment",
    }
]

compliment = APIRouter(tags=tags_metadata)


@compliment.get("/api/compliment/")
@update_stats(name="compliment")
async def gen_compliment():
    """Gets a random compliment"""
    with open("./files/compliment.json") as f:
        compliment_list = json.load(f)
    return {"compliment": random.choice(compliment_list)}
