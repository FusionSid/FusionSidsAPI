from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

humansgood = APIRouter()

@humansgood.get("/api/humansgood/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_humansgood_img():
    return FileResponse("file_path", media_type="image/png")