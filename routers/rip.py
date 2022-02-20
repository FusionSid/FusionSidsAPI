from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

rip = APIRouter()

@rip.get("/api/rip/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_rip_img():
    return FileResponse("file_path", media_type="image/png")