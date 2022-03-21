import os
from io import BytesIO

from PIL import Image
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from utils import update_stats, get_url_image

tags = [
    {
        "name" : "Gun Image"
    }
]

gun = APIRouter(tags=tags)

async def generate_image(image_url : str):
    profile_image = await get_url_image(image_url)
    profile = BytesIO(profile_image)
    profile.seek(0)
    size = (750, 750)
    avatar = Image.open(profile).resize(size)


    cwd = os.getcwd()
    img = Image.open(f"{cwd}/assets/gun.bmp").resize((750, 750))
    img = Image.alpha_composite(avatar, img)

    d = BytesIO()
    d.seek(0)
    img.save(d, "PNG")
    d.seek(0)
    return d

@gun.get("/api/gun/", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
@update_stats(name="gun")
async def gen_gun_img(image_url : str):
    """Generates the gun meme"""
    file = await generate_image(image_url)
    
    return StreamingResponse(file, media_type="image/png")