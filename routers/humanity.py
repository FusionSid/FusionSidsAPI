from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

humanity = APIRouter()

@humanity.get("/api/humanity/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_humanity_img():
    return FileResponse("file_path", media_type="image/png")