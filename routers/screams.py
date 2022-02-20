from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

screams = APIRouter()

@screams.get("/api/screams/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_screams_img():
    return FileResponse("file_path", media_type="image/png")