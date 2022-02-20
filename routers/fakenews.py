from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

fakenews = APIRouter()

@fakenews.get("/api/fakenews/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_fakenews_img():
    return FileResponse("file_path", media_type="image/png")