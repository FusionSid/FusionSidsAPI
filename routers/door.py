from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

door = APIRouter()

@door.get("/api/door/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_door_img():
    return FileResponse("file_path", media_type="image/png")