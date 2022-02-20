from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

whothisis = APIRouter()

@whothisis.get("/api/whothisis/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_whothisis_img():
    return FileResponse("file_path", media_type="image/png")