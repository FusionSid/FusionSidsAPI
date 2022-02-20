from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

wanted = APIRouter()

@wanted.get("/api/wanted/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_wanted_img():
    return FileResponse("file_path", media_type="image/png")