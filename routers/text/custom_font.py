import os
from io import BytesIO

from fastapi import APIRouter
from PIL import Image, ImageFont, ImageDraw
from fastapi.responses import StreamingResponse

from utils import update_stats

tags_metadata = [
    {
        "name": "Convert text to any font",
    }
]


async def convert(text: str, font_name: str, max_line_width: int, color: str):
    fonts_dict = {}
    for i in os.listdir("fonts/"):
        fonts_dict[i[:-4]] = i

    try:
        the_font = fonts_dict[font_name]
    except KeyError:
        return None

    file_name = f"{os.getcwd()}/fonts/{the_font}"

    font = ImageFont.truetype(file_name, 50)

    a, d = font.getmetrics()

    height = (font.getmask(text).getbbox()[3] + d) + 2
    width = (font.getmask(text).getbbox()[2]) + 2

    size = (width, height)

    # todo
    # if width is more than 50cha make a new line

    image = Image.new("RGBA", size, color=(255, 255, 255, 0))

    draw = ImageDraw.Draw(image)

    try:
        draw.text((1, 1), text, fill=color, font=font)
    except ValueError:
        draw.text((1, 1), text, fill="black", font=font)

    d = BytesIO()
    d.seek(0)
    image.save(d, "PNG")
    d.seek(0)
    return d


fontconvert = APIRouter(tags=tags_metadata)


@fontconvert.get("/api/fontconvert")
@update_stats(name="fontconvert")
async def convert_text_to_font(
    text: str, font: str, text_color: str = "black", max_line: int = 50
):
    """Converts text to any font you want, They are 1969 fonts to choose from"""
    image = await convert(text, font, max_line, text_color)
    if image is None:
        return (
            "Error, Font not found. Go to /api/fontconvert/list to get a list of them"
        )

    return StreamingResponse(image, media_type="image/png")


@fontconvert.get("/api/fontconvert/list")
@update_stats(name="fontconvert")
async def list_fonts():
    """A list of the 1969 fonts you can choose from"""
    files = os.listdir("fonts/")
    files = [file[:-4] for file in files]
    return {"Font_List": files}
