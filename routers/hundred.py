from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

hundred = APIRouter()

@hundred.get("/api/hundred/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_hundred_img():
    return FileResponse("file_path", media_type="image/png")