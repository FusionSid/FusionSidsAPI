from fastapi import APIRouter
import os
import random
from fastapi.responses import FileResponse, Response
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import string

abandon = APIRouter()

def generate_image(text):
    cwd = os.getcwd()
    print(cwd)
    img = Image.open(f"{cwd}/assets/abandon.bmp")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(f"{cwd}/fonts/roboto-medium.ttf", 20)

    draw.text((30, 460),text, fill="black", font=font, align='center')
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(32))
    img.save(f"./tempstorage/{x}.png")

    return f"./tempstorage/{x}.png"

@abandon.get("/api/abandon/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_abandon_img(text : str):
    file_path = generate_image(text)
    
    return FileResponse(file_path, media_type="image/png")


cwd = os.getcwd()
print(cwd)