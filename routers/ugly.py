from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

ugly = APIRouter()

@ugly.get("/api/ugly/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_ugly_img():
    return FileResponse("file_path", media_type="image/png")