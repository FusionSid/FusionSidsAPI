from io import BytesIO
import os

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from utils import update_stats
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

op = webdriver.ChromeOptions()
op.add_argument('headless')
cwd = os.getcwd()
print(cwd)
driver = webdriver.Chrome(executable_path=f"{cwd}/chromedriver", options=op)

# Title for docs
tags_metadata = [
    {
        "name": "Screenshot Page",
    }
]

screenshot = APIRouter(tags=tags_metadata)


async def generate_screenshot(url:str):
    driver.get(url)
    driver.fullscreen_window()
    driver.execute_script("document.body.style.zoom='75%'")
    
    img = BytesIO(bytes(driver.get_screenshot_as_png()))
    img.seek(0)
    return img


@screenshot.get("/api/screenshot/")
@update_stats(name="screenshot")
async def gen_screenshot(link: str):
    """Screenshots a page"""
    file = await generate_screenshot(link)

    return StreamingResponse(file, media_type="image/png")
