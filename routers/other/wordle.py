from datetime import datetime

import aiohttp
from fastapi import APIRouter

from utils import update_stats


async def get_word():
    url = "https://www.nytimes.com/games/wordle/main.3d28ac0c.js"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            resp = await response.text()

    resp = resp.split("var Ma=")[1].split("]")[0]+"]"

    date_format = "%d/%m/%y"

    start_day = "11/04/22"
    today = datetime.now().strftime(date_format)

    a, b = datetime.strptime(start_day, date_format), datetime.strptime(today, date_format)

    delta = b - a

    data = eval(resp)
    data = data[297:]

    answer = data[delta.days-1]

    return answer

# Title for docs
tags_metadata = [
    {
        "name": "Wordle Answer",
    }
]

wordle = APIRouter(tags=tags_metadata)


@wordle.get("/api/wordle/")
@update_stats(name="wordle")
async def get_wordle():
    """Gets the wordle answer, This might be yesterdays answer depending on you timezone"""
    word = await get_word()
    return {"wordle": word}
