import os
from io import BytesIO

from fastapi import APIRouter
from PIL import Image, ImageFilter
from fastapi.responses import StreamingResponse

from utils import update_stats, get_url_image

tags_metadata = [
    {
        "name": "Blur Filter",

    }
]

blur = APIRouter(tags=tags_metadata)

async def generate_image(image_url, amount):
    photo = await get_url_image(image_url) 
    photo = BytesIO(photo)
    photo = Image.open(photo)

    image = photo.filter(ImageFilter.GaussianBlur(amount))

    return_img = BytesIO()
    image.save(return_img, "PNG")
    return_img.seek(0)

    return return_img

@blur.get("/api/filter/blur",responses={200: {"content": {"image/png": {}}}},response_class=StreamingResponse,)
@update_stats(name="blur_filter")
async def gen_blur_filter(image_url: str, amount : int = 5):
    """Puts a blur filter on an image"""

    file = await generate_image(image_url, amount)

    return StreamingResponse(file, media_type="image/png")