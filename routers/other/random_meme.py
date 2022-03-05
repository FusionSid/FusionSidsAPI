import asyncpraw
from io import BytesIO
from utils import get_url_image
import os
import random
from fastapi import APIRouter
from utils import update_db
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv

load_dotenv()

# Title for docs
tags_metadata = [
    {
        "name": "Random Meme",
    }
]

async def reddit_client():
    client = asyncpraw.Reddit(
        client_id=os.environ['CLIENT_ID'],
        client_secret=os.environ['CLIENT_SECRET'],
        user_agent="memes-fastapi"
    )
    return client

meme = APIRouter(tags=tags_metadata)


async def generate_meme(reddit_info):
    reddit = await reddit_client()
    subreddit = await reddit.subreddit("memes")
    hot = subreddit.hot(limit=50)
    urls = []
    async for i in hot:
        urls.append(i)
    ran_sub = random.choice(urls)
    name = ran_sub.title
    url = ran_sub.url
    ups = ran_sub.ups
    author = ran_sub.author
    

    if reddit_info:
        return {
            "url" : url,
            "title" : name,
            "author" : str(author.name),
            "upvotes" : ups,
        }
    else:
        file = await get_url_image(url)
        file = BytesIO(file)
        file.seek(0)
        return file

@meme.get("/api/meme/")
async def gen_meme(reddit_json_info : bool = False):
    await update_db('meme')
    reddit_meme = await generate_meme(reddit_json_info)

    if reddit_json_info:
        return reddit_meme
    else:
        return StreamingResponse(reddit_meme, media_type="image/png")
