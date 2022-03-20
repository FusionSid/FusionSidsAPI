import json
import datetime

import psutil
import platform
from fastapi import APIRouter

UPTIME = datetime.datetime.now()

# Title for docs
tags_metadata = [
    {
        "name": "Stats",
    }
]

stats = APIRouter(tags=tags_metadata)

async def get_uptime():
    time_right_now = datetime.datetime.now()
    seconds = int((time_right_now - UPTIME).total_seconds())
    time = f"{seconds}s"
    if seconds > 60:
        minutes = seconds - (seconds % 60)
        seconds = seconds - minutes
        minutes = int(minutes / 60)
        time = f"{minutes}min {seconds}s"
        if minutes > 60:
            hoursglad = minutes - (minutes % 60)
            hours = int(hoursglad / 60)
            minutes = minutes - (hours*60)
            time = f"{hours}h {minutes}min {seconds}s"

    return time


@stats.get("/stats/")
async def get_stats():
    
    time = await get_uptime()

    with open("files/stats.json") as f:
        stat_data = json.load(f)    

    system_data = {
        "memory" : f'{psutil.virtual_memory().percent}%',
        "running_on" : f"{platform.system()} {platform.release()}",
        "python_version" : f"{platform.python_version()}",
        "cpu" : f'{psutil.cpu_percent()}%'
    }
    
    return {
        "uptime" : time,
        "stats" : stat_data,
        "system_stats" : system_data
    }