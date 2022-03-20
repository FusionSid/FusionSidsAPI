import os
from io import BytesIO

from PIL import Image
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from utils import update_stats, get_url_image

tags_metadata = [
    {
        "name": "Wanted Image",
    }
]

wanted = APIRouter(tags=tags_metadata)

async def generate_image(image_url : str):
    profile_image = await get_url_image(image_url)
    profile = BytesIO(profile_image)
    profile.seek(0)
    size = (500, 500)
    avatar = Image.open(profile).resize(size)


    cwd = os.getcwd()
    img = Image.open(f"{cwd}/assets/wanted.bmp")
    img.paste(avatar, (115, 265))

    d = BytesIO()
    d.seek(0)
    img.save(d, "PNG")
    d.seek(0)
    return d


@wanted.get("/api/wanted/", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
@update_stats(name="wanted")
async def gen_wanted_img(image_url : str):
    file = await generate_image(image_url)

    return StreamingResponse(file, media_type="image/png")

