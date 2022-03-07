from fastapi import APIRouter
from utils import update_db
import random
import json

# Title for docs
tags_metadata = [
    {
        "name": "Truth Or Dare",
    }
]

truth_or_dare = APIRouter(tags=tags_metadata)

@truth_or_dare.get("/api/truthordare/")
async def gen_truth_or_dare():
    await update_db('truthordare')
    with open('./utils/datafiles/truths.json') as f:
        truths_list = json.load(f)
    with open("./utils/datafiles/dares.json") as f:
        dares_list = json.load(f)

    return {
        "truth" : random.choice(truths_list),
        "dare" : random.choice(dares_list),
        "computers_choice" : random.choice(["truth", "dare"])
    }
