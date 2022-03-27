import json
from datetime import datetime

from fastapi import APIRouter

from utils import update_stats


async def get_word():
    date_format = "%d/%m/%y"

    start_day = "07/03/22"
    today = datetime.now().strftime(date_format)

    a, b = datetime.strptime(start_day, date_format), datetime.strptime(
        today, date_format
    )

    delta = b - a

    with open("./files/words.json") as f:
        data = json.load(f)

    answer = data[delta.days]

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
