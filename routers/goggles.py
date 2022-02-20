from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

goggles = APIRouter()

@goggles.get("/api/goggles/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_goggles_img():
    return FileResponse("file_path", media_type="image/png")