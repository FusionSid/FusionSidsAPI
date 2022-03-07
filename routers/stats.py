import platform
from fastapi import APIRouter
import psutil
import datetime
from utils import get_db

UPTIME = datetime.datetime.now()

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
    system_data = {
    "memory" : f'{psutil.virtual_memory().percent}%',
    "running_on" : f"{platform.system()} {platform.release()}",
    "python_version" : f"{platform.python_version()}",
    "cpu" : f'{psutil.cpu_percent()}%'
    }
    
    return {
        "uptime" : time,
        "stats" : data,
        "system_stats" : system_data
    }