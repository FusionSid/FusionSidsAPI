import os

import asyncpraw
from fastapi import APIRouter
from dotenv import load_dotenv

from utils import update_stats

load_dotenv()

# Title for docs
tags_metadata = [
    {
        "name": "Search Reddit",
    }
]


async def reddit_client():
    client = asyncpraw.Reddit(
        client_id=os.environ["CLIENT_ID"],
        client_secret=os.environ["CLIENT_SECRET"],
        user_agent="memes-fastapi",
    )
    return client


searchreddit = APIRouter(tags=tags_metadata)


async def do_search_reddit(keyword):
    search = []
    reddit = await reddit_client()
    subreddit = await reddit.subreddit("all")
    posts = subreddit.search(keyword, limit=10)

    urls = []
    async for i in posts:
        urls.append(i)

    for ran_sub in urls:
        name = ran_sub.title
        url = ran_sub.url
        ups = ran_sub.ups
        author = ran_sub.author

        search.append(
            {
                "url": url,
                "title": name,
                "author": str(author.name),
                "upvotes": ups,
            }
        )

    return search


@searchreddit.get("/api/searchreddit/")
@update_stats(name="searchreddit")
async def search_reddit(keyword):
    """Searches reddit for a keyword"""
    search = await do_search_reddit(keyword)

    return search
