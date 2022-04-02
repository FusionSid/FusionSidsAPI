import os
from io import BytesIO

from fastapi import APIRouter
from PIL import Image, ImageFilter
from fastapi.responses import StreamingResponse

from utils import update_stats, get_url_image

tags_metadata = [
    {
        "name": "Contour Filter",

    }
]

contour = APIRouter(tags=tags_metadata)

async def generate_image(image_url):
    photo = await get_url_image(image_url) 

    img = Image.open(BytesIO(photo))

    img = img.filter(ImageFilter.CONTOUR)

    return_img = BytesIO()
    img.save(return_img, "PNG")
    return_img.seek(0)

    return img


@contour.get("/api/filter/contour",responses={200: {"content": {"image/png": {}}}},response_class=StreamingResponse,)
@update_stats(name="contour_filter")
async def gen_contour_filter(image_url: str):
    """
    Puts a contour filter on an image
    """
    file = await generate_image(image_url)

    return StreamingResponse(file, media_type="image/png")