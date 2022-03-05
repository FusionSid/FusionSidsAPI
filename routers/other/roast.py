from fastapi import APIRouter
import random
import json

# Title for docs
tags_metadata = [
    {
        "name": "Roast",
    }
]

roast = APIRouter(tags=tags_metadata)

@roast.get("/api/roast/")
async def gen_roast():
    with open('./utils/roastlist.json') as f:
        roast_list = json.load(f)
    return {
        "roast" : random.choice(roast_list)
    }
