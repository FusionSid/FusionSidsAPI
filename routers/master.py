from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

master = APIRouter()

@master.get("/api/master/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_master_img():
    return FileResponse("file_path", media_type="image/png")