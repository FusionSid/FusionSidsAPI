
from fastapi import APIRouter
import os
from fastapi.responses import StreamingResponse
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from io import BytesIO
import textwrap

tags_metadata = [
    {
        "name": "Changemymind Meme",
    }
]

changemymind = APIRouter(tags=tags_metadata)


async def generate_image(text):
    cwd = os.getcwd()

    img = Image.open(f"{cwd}/assets/changemymind.bmp")
    font = ImageFont.truetype(f"{cwd}/fonts/roboto-medium.ttf", 20)

    text_image = Image.new("RGB", (768, 568),color="WHITE")
    text_image.convert("RGBA")

    draw = ImageDraw.Draw(text_image)

    newImage = []
    for item in text_image.getdata():
        if item[:3] == (255, 255, 255):
            newImage.append((255, 255, 255, 0))
        else:
            newImage.append(item)

    text_image.putdata(newImage)

    w, h = 670, 330
    lines = textwrap.wrap(text, width=18)
    y_text = h
    for line in lines:
        width, height = font.getsize(line)
        draw.text(((w - width) / 2, y_text), line, font=font, fill="black", align="center")
        y_text += height
    
    text_image = text_image.rotate(20)
  
    text_image = Image.alpha_composite(img, text_image)

    d = BytesIO()
    d.seek(0)
    img.save(d, "PNG")
    d.seek(0)
    return d


@changemymind.get("/api/changemymind/", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
async def gen_changemymind_img(text : str):

    file = await generate_image(text)

    return StreamingResponse(file, media_type="image/png")

