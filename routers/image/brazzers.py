import os
from io import BytesIO

from PIL import Image
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from utils import update_stats, get_url_image

tags_metadata = [
    {
        "name": "Brazzers Meme",
    }
]

brazzers = APIRouter(tags=tags_metadata)



async def generate_image(image_url : str):
    profile_image = await get_url_image(image_url)
    profile = BytesIO(profile_image)
    profile.seek(0)
    size = (750, 750)
    avatar = Image.open(profile).resize(size)


    cwd = os.getcwd()
    img = Image.open(f"{cwd}/assets/brazzers.bmp").resize((285,59))
    avatar.paste(img, (16, 675))

    d = BytesIO()
    d.seek(0)
    avatar.save(d, "PNG")
    d.seek(0)
    return d


@brazzers.get("/api/brazzers/", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
@update_stats(name="brazzers")
async def gen_brazzers_img(image_url):

    file = await generate_image(image_url)

    return StreamingResponse(file, media_type="image/png")




