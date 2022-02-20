from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

abandon = APIRouter()

@abandon.get("/api/abandon/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_abandon_img():
    return FileResponse("file_path", media_type="image/png")