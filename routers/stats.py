from fastapi import APIRouter
from utils import get_db

# Title for docs
tags_metadata = [
    {
        "name": "Stats",
    }
]

stats = APIRouter(tags=tags_metadata)

@stats.get("/stats/")
async def get_stats():
    data = await get_db()
    return {
        "stats" : data
    }
