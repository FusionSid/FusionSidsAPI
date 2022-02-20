from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

affect = APIRouter()

@affect.get("/api/affect/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_affect_img():
    return FileResponse("file_path", media_type="image/png")