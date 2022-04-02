import os
from io import BytesIO

from fastapi import APIRouter
from PIL import Image, ImageFilter
from fastapi.responses import StreamingResponse

from utils import update_stats, get_url_image

tags_metadata = [
    {
        "name": "Color Filter",
    }
]

color = APIRouter(tags=tags_metadata)


async def red(r, g, b):
    r = r
    g = 0
    b = 0
    return (r, g, b)

async def blue(r, g, b):
    r = 0
    g = 0
    b = b
    return (r, g, b)

async def green(r, g, b):
    r = 0
    g = g
    b = 0
    return (r, g, b)


async def purple(r, g, b):
    r = r
    g = g
    b = r
    return (r, g, b)


async def pink(r, g, b):
    r = g
    g = b
    b = r
    return (r, g, b)


async def yellow(r, g, b):
    r = g
    g = r
    b = b
    return (r, g, b)


async def grey(r, g, b):
    r = (r + g + b) // 3
    g = (r + g + b) // 3
    b = (r + g + b) // 3
    return (r, g, b)


async def sepia(r, g, b):
    r = int((r * 0.396) + (g * 0.769) + (b * 0.189))
    g = int((r * 0.349) + (g * 0.686) + (b * 0.168))
    b = int((r * 0.272) + (g * 0.534) + (b * 0.131))
    return (r, g, b)


colors = {
    "red": red,
    "green": green,
    "blue": blue,
    "sepia": sepia,
    "yellow": yellow,
    "grey": grey,
    "pink": pink,
    "purple": purple,
}


async def generate_image(color, image_url):
    colors_list = []
    for key, value in colors.items():
        colors_list.append(key)
    if color not in colors_list:
        return {
            "error": "Color doesnt exists", 
            "colors": ", ".join(colors_list)
        }
    photo = await get_url_image(image_url)

    photo = Image.open(BytesIO(photo)).convert("RGB")

    width, height = photo.size

    pixels = photo.load()

    for height_px in range(height):
        for width_px in range(width):
            r, g, b = photo.getpixel((width_px, height_px))
            func = colors[color]
            pixels[width_px, height_px] = await func(r, g, b)

    return_img = BytesIO()
    photo.save(return_img, "PNG")
    return_img.seek(0)

    return return_img


@color.get(
    "/api/filter/color",
)
@update_stats(name="color_filter")
async def gen_color_filter(color: str, image_url: str):
    """
    Puts a color filter on an image
    """
    file = await generate_image(color, image_url)
    if type(file) == dict:
        return file
    return StreamingResponse(file, media_type="image/png")
