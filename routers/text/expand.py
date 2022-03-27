from fastapi import APIRouter

from utils import update_stats

tags_metadata = [{"name": "Expand Text"}]

expand = APIRouter(tags=tags_metadata)


@expand.get("/api/expand")
@update_stats(name="expand")
async def generate_expand(text: str, space: int = 5):
    """Expands T e x t"""

    spacing = ""
    for i in range(space):
        spacing += " "
    result = spacing.join(text)

    return {"text": result}
