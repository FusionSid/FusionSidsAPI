from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

ipad = APIRouter()

@ipad.get("/api/ipad/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_ipad_img():
    return FileResponse("file_path", media_type="image/png")