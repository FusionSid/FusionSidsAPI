from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

fuck = APIRouter()

@fuck.get("/api/fuck/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_fuck_img():
    return FileResponse("file_path", media_type="image/png")