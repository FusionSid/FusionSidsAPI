from fastapi import APIRouter
import random
import json

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
    with open('./files/compliment.json') as f:
        compliment_list = json.load(f)
    return {
        "compliment" : random.choice(compliment_list)
    }
