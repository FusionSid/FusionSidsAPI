import os
from io import BytesIO

from fastapi import APIRouter
from PIL import Image, ImageOps
from fastapi.responses import StreamingResponse

from utils import update_stats, get_url_image

tags_metadata = [
    {
        "name": "Greyscale Filters",

    }
]

greyscale = APIRouter(tags=tags_metadata)

async def generate_image(image_url):
    image = await get_url_image(image_url)
    image = BytesIO(image)

    image = Image.open(image)

    gray_image = ImageOps.grayscale(image)

    img = BytesIO()
    gray_image.save(img, "PNG")
    img.seek(0)

    return img

@greyscale.get("/api/filters/greyscale",responses={200: {"content": {"image/png": {}}}},response_class=StreamingResponse,)
@update_stats(name="greyscale_filter")
async def gen_grey_filter(image_url: str):

    file = await generate_image(image_url)

    return StreamingResponse(file, media_type="image/png")