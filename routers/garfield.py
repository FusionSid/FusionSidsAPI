from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

garfield = APIRouter()

@garfield.get("/api/garfield/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_garfield_img():
    return FileResponse("file_path", media_type="image/png")