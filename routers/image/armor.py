from fastapi import APIRouter
from utils import update_stats
import os
from fastapi.responses import StreamingResponse
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from io import BytesIO
import textwrap

tags_metadata = [
    {
        "name": "Armor Meme",
    }
]

armor = APIRouter(tags=tags_metadata)

async def generate_image(text):
    cwd = os.getcwd()

    img = Image.open(f"{cwd}/assets/armor.bmp")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(f"{cwd}/fonts/roboto-medium.ttf", 20)

    w, h = 270, 360
    lines = textwrap.wrap(text, width=18)
    y_text = h
    for line in lines:
        width, height = font.getsize(line)
        draw.text(((w - width) / 2, y_text), line, font=font, fill="black", align="center")
        y_text += height

    d = BytesIO()
    d.seek(0)
    img.save(d, "PNG")
    d.seek(0)
    return d

@armor.get("/api/armor/", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
@update_stats(name="armor")
async def gen_armor_img(text : str):

    file = await generate_image(text)

    return StreamingResponse(file, media_type="image/png")

