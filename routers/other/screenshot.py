from io import BytesIO
import os

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from utils import update_stats
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import dotenv

dotenv.load_dotenv()

option = webdriver.ChromeOptions()
option.binary_location = os.environ['GOOGLE_CHROME_BIN']
option.add_argument("--headless")
option.add_argument('--disable-gpu')
option.add_argument('--no-sandbox')
driver= webdriver.Chrome(executable_path=os.environ['CHROME_EXECUTABLE_PATH'], options=option)

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
