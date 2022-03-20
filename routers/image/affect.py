
from fastapi import APIRouter
from utils import update_stats
from io import BytesIO
from fastapi.responses import StreamingResponse
from utils import get_url_image
from PIL import Image
import os

tags_metadata = [
    {
        "name": "Affect Meme",
    }
]

affect = APIRouter(tags=tags_metadata)

async def generate_image(image_url : str):
    profile_image = await get_url_image(image_url)
    profile = BytesIO(profile_image)
    profile.seek(0)
    size = (200, 170)
    avatar = Image.open(profile).resize(size)
    avatar = avatar.rotate(-1)


    cwd = os.getcwd()
    img = Image.open(f"{cwd}/assets/affect.bmp")
    img.paste(avatar, (179, 379))

    d = BytesIO()
    d.seek(0)
    img.save(d, "PNG")
    d.seek(0)
    return d


@affect.get("/api/affect/", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
@update_stats(name="affect")
async def gen_affect_img(image_url : str):
    
    file = await generate_image(image_url)

    return StreamingResponse(file, media_type="image/png")

