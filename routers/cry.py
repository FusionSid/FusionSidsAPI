from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

cry = APIRouter()

@cry.get("/api/cry/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_cry_img():
    return FileResponse("file_path", media_type="image/png")