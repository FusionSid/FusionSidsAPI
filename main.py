from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routers import *
from utils import update_stats

__version__ = "1.0.0"

# Description for api docs
description = """
### Made by FusionSid

[My Github](https://github.com/FusionSid)

This api mostly generates memes but it can also do roasts, 8ball qrcodes and more

#### Source Code:
[https://github.com/FusionSid/FusionSidsAPI](https://github.com/FusionSid/FusionSidsAPI)

#### Contact:
Discord: FusionSid#3645

#### LICENCE:
"""


# Creates an instance of the FastAPI class
app = FastAPI(
    title="FusionSidsAPI",
    description=description,
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)


async def endpoint_list():
    url_list = [route.path for route in app.routes]

    url_list.remove("/openapi.json")
    url_list.remove("/docs/oauth2-redirect")
    url_list.remove("/redoc")
    url_list.remove("/")
    url_list.remove("/api")

    return url_list


@app.get("/")
@update_stats()
async def home():
    """
    The home page, Redirects to docs
    """
    return RedirectResponse("/docs")


@app.get("/api")
@update_stats()
async def api():
    """
    The api endpoint, Gives a list of endpoints
    """
    url_list = await endpoint_list()

    return {
        "docs_url": "https://fusionsidapi.herokuapp.com/docs",
        "endpoints": url_list,
    }


# Including all the endpoints:

# Stats
app.include_router(stats)


# Other Endpoints
app.include_router(router=roast)
app.include_router(router=qrcode)
app.include_router(router=wordle)
app.include_router(router=eightball)
app.include_router(router=meme)
app.include_router(router=compliment)
app.include_router(router=fact)
app.include_router(router=truth_or_dare)
app.include_router(router=searchreddit)
app.include_router(router=get_colors)
app.include_router(router=mcskin)
app.include_router(router=balloon)
app.include_router(router=changemymind)
app.include_router(router=brain)
app.include_router(router=boo)
app.include_router(router=expandingwwe)

# Text
app.include_router(router=fontconvert)
app.include_router(router=password)
app.include_router(router=drunkify)
app.include_router(router=expand)
app.include_router(router=binary)
app.include_router(router=hex)
app.include_router(router=reverse)
app.include_router(router=encrypt)


# Image Endpoints
app.include_router(router=armor)
app.include_router(router=brazzers)
app.include_router(router=gun)
app.include_router(router=affect)
app.include_router(router=violence)
app.include_router(router=wanted)
app.include_router(router=trash)
app.include_router(router=aborted)
app.include_router(router=bongocat)
app.include_router(router=surprised)
app.include_router(router=abandon)


# Filters
app.include_router(router=greyscale)
app.include_router(router=blur)
app.include_router(router=color)