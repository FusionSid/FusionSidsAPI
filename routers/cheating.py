from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

cheating = APIRouter()

@cheating.get("/api/cheating/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_cheating_img():
    return FileResponse("file_path", media_type="image/png")