from fastapi import APIRouter
from utils import update_db
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
    await update_db('compliment')
    with open('./utils/datafiles/compliment.json') as f:
        compliment_list = json.load(f)
    return {
        "compliment" : random.choice(compliment_list)
    }
