from fastapi import APIRouter
import os
import random
from fastapi.responses import FileResponse, Response, StreamingResponse
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from io import BytesIO
import string

abandon = APIRouter()

def generate_image(text):
    cwd = os.getcwd()
    print(cwd)
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
def gen_abandon_img(text : str):
    file = generate_image(text)
    
    return StreamingResponse(file, media_type="image/png")
