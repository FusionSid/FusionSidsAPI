from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

vr = APIRouter()

@vr.get("/api/vr/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_vr_img():
    return FileResponse("file_path", media_type="image/png")