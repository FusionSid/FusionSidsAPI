import random

from fastapi import APIRouter

from utils import update_stats

# Title for docs
tags_metadata = [
    {
        "name": "8ball",
    }
]

eightball = APIRouter(tags=tags_metadata)


@eightball.get("/api/8ball/")
@update_stats(name="eightball")
async def eight_ball(question: str = None):
    """Asks the magical 8ball a question"""
    _8ballans = [
        "As I see it, yes",
        "It is certain",
        "It is decidedly so",
        "Most likely",
        "Outlook good",
        "Signs point to yes",
        "Without a doubt",
        "Yes",
        "Yes - definitely",
        "You may rely on it",
        "Reply hazy, try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful",
    ]

    return {"question": question, "answer": random.choice(_8ballans)}
