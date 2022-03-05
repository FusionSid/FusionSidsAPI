from fastapi import APIRouter
import os
from fastapi.responses import StreamingResponse
from PIL import Image
from PIL import ImageFont
from utils import update_db
from PIL import ImageDraw 
from io import BytesIO


# Title for docs
tags_metadata = [
    {
        "name": "Abandon Meme",
    }
]

abandon = APIRouter(tags=tags_metadata)

# Image generate function
async def generate_image(text):
    """
    This function generate an `Abandon` Meme

    Args:
        text (str) : The text to put on the meme

    Returns:
        BytesIO image
    """
    cwd = os.getcwd()

    img = Image.open(f"{cwd}/assets/abandon.bmp")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(f"{cwd}/fonts/roboto-medium.ttf", 20)

    draw.text((30, 460),text, fill="black", font=font, align='center')

    d = BytesIO()
    d.seek(0)
    img.save(d, "PNG")
    d.seek(0)
    return d

@abandon.get("/api/abandon/", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
async def gen_abandon_img(text : str):
    await update_db('abandon')
    
    file = await generate_image(text)
    
    return StreamingResponse(file, media_type="image/png")
