from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

mom = APIRouter()

@mom.get("/api/mom/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_mom_img():
    return FileResponse("file_path", media_type="image/png")