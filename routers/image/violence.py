from fastapi import APIRouter
import os
from fastapi.responses import StreamingResponse
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from io import BytesIO
from utils import update_db
import textwrap

tags_metadata = [
    {
        "name": "Violence Meme",
    }
]

violence = APIRouter(tags=tags_metadata)

async def generate_image(text):
    cwd = os.getcwd()

    img = Image.open(f"{cwd}/assets/violence.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(f"{cwd}/fonts/roboto-medium.ttf", 20)

    w, h = 960, 5
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

@violence.get("/api/violence/", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
async def gen_violence_img(text : str):
    await update_db('violence')
    file = await generate_image(text)

    return StreamingResponse(file, media_type="image/png")

