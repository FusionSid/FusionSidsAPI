from fastapi import APIRouter
from utils import update_db
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
    await update_db("roast")
    with open('./utils/datafiles/roastlist.json') as f:
        roast_list = json.load(f)
    return {
        "roast" : random.choice(roast_list)
    }
