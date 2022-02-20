from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

inator = APIRouter()

@inator.get("/api/inator/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_inator_img():
    return FileResponse("file_path", media_type="image/png")