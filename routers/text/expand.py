from fastapi import APIRouter
from utils import update_db

tags_metadata = [
    {
        "name": "Expand Text"
    }
]

expand = APIRouter(tags=tags_metadata)

@expand.get("/api/expand")
async def generate_expand(text : str, space : int = 5):
    update_db("expand")

    spacing = ""
    for i in range(space):
        spacing += " "
    result = spacing.join(text)

    return {
        "text" : result
    }