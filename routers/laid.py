from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

laid = APIRouter()

@laid.get("/api/laid/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_laid_img():
    return FileResponse("file_path", media_type="image/png")