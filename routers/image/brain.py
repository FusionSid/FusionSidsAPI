import os
import textwrap
from io import BytesIO

from fastapi import APIRouter
from PIL import Image, ImageDraw, ImageFont
from fastapi.responses import StreamingResponse

from utils import update_stats, get_url_image

tags_metadata = [
    {
        "name": "Brain Meme",
    }
]

brain = APIRouter(tags=tags_metadata)


async def generate_image(text_1: str, text_2: str, text_3: str, text_4: str):
    cwd = os.getcwd()
    img = Image.open(f"{cwd}/assets/brain.bmp")
    font = ImageFont.truetype(f"{cwd}/fonts/roboto-medium.ttf", 20)
    draw = ImageDraw.Draw(img)

    w, h = 250, 10
    lines = textwrap.wrap(text_1, width=18)
    y_text = h
    for line in lines:
        width, height = font.getsize(line)
        draw.text(
            ((w - width) / 2, y_text), line, font=font, fill="black", align="center"
        )
        y_text += height

    w, h = 250, 205
    lines = textwrap.wrap(text_2, width=18)
    y_text = h
    for line in lines:
        width, height = font.getsize(line)
        draw.text(
            ((w - width) / 2, y_text), line, font=font, fill="black", align="center"
        )
        y_text += height

    w, h = 250, 400
    lines = textwrap.wrap(text_3, width=18)
    y_text = h
    for line in lines:
        width, height = font.getsize(line)
        draw.text(
            ((w - width) / 2, y_text), line, font=font, fill="black", align="center"
        )
        y_text += height

    w, h = 250, 580
    lines = textwrap.wrap(text_4, width=18)
    y_text = h
    for line in lines:
        width, height = font.getsize(line)
        draw.text(
            ((w - width) / 2, y_text), line, font=font, fill="black", align="center"
        )
        y_text += height

    d = BytesIO()
    d.seek(0)
    img.save(d, "PNG")
    d.seek(0)
    return d


@brain.get(
    "/api/brain/",
    responses={200: {"content": {"image/png": {}}}},
    response_class=StreamingResponse,
)
@update_stats(name="brain")
async def gen_brain_img(text_1: str, text_2: str, text_3: str, text_4: str):
    """Generates the brain meme"""

    file = await generate_image(text_1, text_2, text_3, text_4)

    return StreamingResponse(file, media_type="image/png")
