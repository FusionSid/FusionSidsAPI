import os
import textwrap
from io import BytesIO

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from utils import update_stats

# Title for docs
tags_metadata = [
    {
        "name": "Surprised Meme",
    }
]

surprised = APIRouter(tags=tags_metadata)

# Image generate function
async def generate_image(text):
    """
    This function generate an `surprised` Meme

    Args:
        text (str) : The text to put on the meme

    Returns:
        BytesIO image
    """
    cwd = os.getcwd()

    img = Image.open(f"{cwd}/assets/surprised.bmp")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(f"{cwd}/fonts/roboto-medium.ttf", 40)

    w, h = 675, 50
    lines = textwrap.wrap(text, width=18)
    y_text = h
    for line in lines:
        width, height = font.getsize(line)
        draw.text(
            ((w - width) / 2, y_text), line, font=font, fill="white", align="center"
        )
        y_text += height

    d = BytesIO()
    d.seek(0)
    img.save(d, "PNG")
    d.seek(0)
    return d


@surprised.get(
    "/api/surprised/",
    responses={200: {"content": {"image/png": {}}}},
    response_class=StreamingResponse,
)
@update_stats(name="surprised")
async def gen_surprised_img(text: str):
    """Generates the surprised meme"""
    file = await generate_image(text)

    return StreamingResponse(file, media_type="image/png")
