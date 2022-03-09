from fastapi import APIRouter
from utils import update_db
from datetime import datetime
import json

async def get_word():
    date_format = "%d/%m/%y"

    start_day = "07/03/22"
    today = datetime.now().strftime(date_format)

    a, b = datetime.strptime(start_day, date_format), datetime.strptime(today, date_format)

    delta = b - a

    with open('./utils/datafiles/words.json') as f:
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
async def get_wordle():
    await update_db("wordle")
    word = await get_word()
    return {
        "wordle" : word
    }
