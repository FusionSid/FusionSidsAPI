from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

boo = APIRouter()

@boo.get("/api/boo/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_boo_img():
    return FileResponse("file_path", media_type="image/png")