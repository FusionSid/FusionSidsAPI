from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

hitler = APIRouter()

@hitler.get("/api/hitler/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_hitler_img():
    return FileResponse("file_path", media_type="image/png")