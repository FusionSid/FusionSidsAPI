import json
import random

from fastapi import APIRouter

from utils import update_stats

# Title for docs
tags_metadata = [
    {
        "name": "Truth Or Dare",
    }
]

truth_or_dare = APIRouter(tags=tags_metadata)


@truth_or_dare.get("/api/truthordare/")
@update_stats(name="truthordare")
async def gen_truth_or_dare():
    """Truth or dare"""
    with open("./files/truths.json") as f:
        truths_list = json.load(f)
    with open("./files/dares.json") as f:
        dares_list = json.load(f)

    return {
        "truth": random.choice(truths_list),
        "dare": random.choice(dares_list),
        "computers_choice": random.choice(["truth", "dare"]),
    }
