import os
import textwrap
from io import BytesIO

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from utils import update_stats

tags_metadata = [
    {
        "name": "Boo Meme",
    }
]

boo = APIRouter(tags=tags_metadata)


async def generate_image(text_1 : str, text_2 : str):
    cwd = os.getcwd()

    img = Image.open(f"{cwd}/assets/boo.bmp")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(f"{cwd}/fonts/roboto-medium.ttf", 15)

    w, h = 200, 42
    lines = textwrap.wrap(text_1, width=15)
    y_text = h
    for line in lines:
        width, height = font.getsize(line)
        draw.text(
            ((w - width) / 2, y_text), line, font=font, fill="black", align="center"
        )
        y_text += height


    w, h = 680, 42
    lines = textwrap.wrap(text_2, width=15)
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


@boo.get(
    "/api/boo/",
    responses={200: {"content": {"image/png": {}}}},
    response_class=StreamingResponse,
)
@update_stats(name="boo")
async def gen_boo_img(text_1: str, text_2: str):
    """Generates the boo meme"""

    file = await generate_image(text_1, text_2)

    return StreamingResponse(file, media_type="image/png")
