from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

excuseme = APIRouter()

@excuseme.get("/api/excuseme/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_excuseme_img():
    return FileResponse("file_path", media_type="image/png")