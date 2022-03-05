from fastapi import APIRouter
from io import BytesIO
from fastapi.responses import StreamingResponse
from utils import get_url_image
from utils import update_db
from PIL import Image
import os

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
async def gen_aborted_img(image_url : str):
    await update_db('aborted')
    
    file = await generate_image(image_url)

    return StreamingResponse(file, media_type="image/png")

