from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

spank = APIRouter()

@spank.get("/api/spank/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_spank_img():
    return FileResponse("file_path", media_type="image/png")