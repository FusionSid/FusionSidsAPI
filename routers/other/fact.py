import json
import random

from fastapi import APIRouter

from utils import update_stats

# Title for docs
tags_metadata = [
    {
        "name": "Random Fact",
    }
]

fact = APIRouter(tags=tags_metadata)

@fact.get("/api/fact/")
@update_stats(name="fact")
async def gen_fact():
    with open('./files/facts.json') as f:
        fact_list = json.load(f)
    return {
        "fact" : random.choice(fact_list)
    }
