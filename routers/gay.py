from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

gay = APIRouter()

@gay.get("/api/gay/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_gay_img():
    return FileResponse("file_path", media_type="image/png")