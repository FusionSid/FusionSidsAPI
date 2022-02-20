from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

jail = APIRouter()

@jail.get("/api/jail/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_jail_img():
    return FileResponse("file_path", media_type="image/png")