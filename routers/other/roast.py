from fastapi import APIRouter
import random
import json

from utils import update_stats

# Title for docs
tags_metadata = [
    {
        "name": "Roast",
    }
]

roast = APIRouter(tags=tags_metadata)

@roast.get("/api/roast/")
@update_stats(name="roast")
async def gen_roast():
    with open('./files/roastlist.json') as f:
        roast_list = json.load(f)
    return {
        "roast" : random.choice(roast_list)
    }
