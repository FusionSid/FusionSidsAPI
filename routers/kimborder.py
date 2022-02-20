from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

kimborder = APIRouter()

@kimborder.get("/api/kimborder/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_kimborder_img():
    return FileResponse("file_path", media_type="image/png")