from io import BytesIO

from colorthief import ColorThief
from fastapi import APIRouter, UploadFile

from utils import update_stats

# Title for docs
tags_metadata = [
    {
        "name": "Get Colors",
    }
]

get_colors = APIRouter(tags=tags_metadata)


async def get_image_colors(image, _hex):
    color_thief = ColorThief(image)
    dominant_color = list(color_thief.get_color(quality=1))
    palette = color_thief.get_palette(color_count=6)
    palette = [list(i) for i in palette]

    if _hex:
        dominant_color = ("#{:X}{:X}{:X}").format(
            dominant_color[0], dominant_color[1], dominant_color[2]
        )

        for index, color in enumerate(palette):
            palette[index] = ("#{:X}{:X}{:X}").format(color[0], color[1], color[2])

    return {"dominant_color": dominant_color, "palette": palette}


@get_colors.post("/api/get_colors/")
@update_stats(name="getcolors")
async def find_colors(image: UploadFile, show_hex: bool = True):
    """Gets the colors in an image"""
    img = await image.read()
    img = BytesIO(img)

    colors = await get_image_colors(img, show_hex)

    return colors
