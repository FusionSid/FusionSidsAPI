from fastapi import APIRouter
from utils import update_db
import random
import json

# Title for docs
tags_metadata = [
    {
        "name": "Random Fact",
    }
]

fact = APIRouter(tags=tags_metadata)

@fact.get("/api/fact/")
async def gen_fact():
    await update_db('fact')
    with open('./utils/datafiles/facts.json') as f:
        fact_list = json.load(f)
    return {
        "fact" : random.choice(fact_list)
    }
