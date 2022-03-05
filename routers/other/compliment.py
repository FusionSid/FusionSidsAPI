from fastapi import APIRouter
import random
import json

# Title for docs
tags_metadata = [
    {
        "name": "Compliment",
    }
]

compliment = APIRouter(tags=tags_metadata)

@compliment.get("/api/compliment/")
async def gen_compliment():
    with open('./utils/compliment.json') as f:
        compliment_list = json.load(f)
    return {
        "compliment" : random.choice(compliment_list)
    }
