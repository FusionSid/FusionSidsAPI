from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

balloon = APIRouter()

@balloon.get("/api/balloon/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_balloon_img():
    return FileResponse("file_path", media_type="image/png")