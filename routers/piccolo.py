from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

piccolo = APIRouter()

@piccolo.get("/api/piccolo/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_piccolo_img():
    return FileResponse("file_path", media_type="image/png")