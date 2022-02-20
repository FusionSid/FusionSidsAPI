from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

floor = APIRouter()

@floor.get("/api/floor/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_floor_img():
    return FileResponse("file_path", media_type="image/png")