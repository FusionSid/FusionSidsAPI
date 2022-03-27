import json
import base64
from io import BytesIO

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from utils import update_stats, get_url_json, get_url_image


async def get_uuid(user: str):
    url = f"https://api.mojang.com/users/profiles/minecraft/{user}?"
    response = await get_url_json(url)
    uuid = response["id"]
    return uuid


tags = [{"name": "Gets MC Skin"}]


mcskin = APIRouter(tags=tags)


@mcskin.get("/api/mcskin")
@update_stats(name="mcskin")
async def get_minecraft_skin(username: str):
    """Gets a users minecraft skin"""

    uuid = await get_uuid(username)

    url = f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid}"
    response = await get_url_json(url)

    try:
        properties = response["properties"][0]["value"]
    except KeyError:
        return "Error"

    properties = json.loads(base64.b64decode(properties))

    try:
        skin_url = properties["textures"]["SKIN"]["url"]
    except KeyError:
        return "Error"

    skin = await get_url_image(skin_url)

    skin = BytesIO(skin)
    skin.seek(0)

    return StreamingResponse(skin, media_type="image/png")
