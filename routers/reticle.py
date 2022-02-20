from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

reticle = APIRouter()

@reticle.get("/api/reticle/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_reticle_img():
    return FileResponse("file_path", media_type="image/png")