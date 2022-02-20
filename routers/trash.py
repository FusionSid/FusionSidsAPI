from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

trash = APIRouter()

@trash.get("/api/trash/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_trash_img():
    return FileResponse("file_path", media_type="image/png")