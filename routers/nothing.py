from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

nothing = APIRouter()

@nothing.get("/api/nothing/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_nothing_img():
    return FileResponse("file_path", media_type="image/png")