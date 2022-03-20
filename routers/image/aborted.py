import os
from io import BytesIO

from PIL import Image
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from utils import update_stats, get_url_image

tags_metadata = [
    {
        "name": "Aborted Meme",
    }
]

aborted = APIRouter(tags=tags_metadata)

async def generate_image(image_url : str):
    profile_image = await get_url_image(image_url)
    profile = BytesIO(profile_image)
    profile.seek(0)
    size = (80, 80)
    avatar = Image.open(profile).resize(size)


    cwd = os.getcwd()
    img = Image.open(f"{cwd}/assets/aborted.bmp")
    img.paste(avatar, (400, 130))

    d = BytesIO()
    d.seek(0)
    img.save(d, "PNG")
    d.seek(0)
    return d


@aborted.get("/api/aborted/", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
@update_stats(name="aborted")
async def gen_aborted_img(image_url : str):
    
    file = await generate_image(image_url)

    return StreamingResponse(file, media_type="image/png")

