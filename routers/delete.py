from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

delete = APIRouter()

@delete.get("/api/delete/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_delete_img():
    return FileResponse("file_path", media_type="image/png")