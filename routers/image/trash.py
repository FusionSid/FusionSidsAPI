from fastapi import APIRouter
from io import BytesIO
from fastapi.responses import StreamingResponse
from utils import get_url_image
from PIL import Image
import os

from utils import update_stats

tags_metadata = [
    {
        "name": "Trash Meme",
    }
]

trash = APIRouter(tags=tags_metadata)

async def generate_image(image_url : str):
    profile_image = await get_url_image(image_url)
    profile = BytesIO(profile_image)
    profile.seek(0)
    size = (480, 485)
    avatar = Image.open(profile).resize(size)


    cwd = os.getcwd()
    img = Image.open(f"{cwd}/assets/trash.bmp")
    img.paste(avatar, (480, 0))

    d = BytesIO()
    d.seek(0)
    img.save(d, "PNG")
    d.seek(0)
    return d


@trash.get("/api/trash/", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
@update_stats(name="trash")
async def gen_trash_img(image_url : str):
    
    file = await generate_image(image_url)

    return StreamingResponse(file, media_type="image/png")