import platform
from fastapi import APIRouter
import psutil
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
    system_data = {
    "memory" : f'{psutil.virtual_memory().percent}%',
    "running_on" : f"{platform.system()} {platform.release()}",
    "python_version" : f"{platform.python_version()}",
    "cpu" : f'{psutil.cpu_percent()}%'
    }
    return {
        "stats" : data,
        "system_stats" : system_data
    }