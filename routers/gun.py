from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

gun = APIRouter()

@gun.get("/api/gun/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_gun_img():
    return FileResponse("file_path", media_type="image/png")