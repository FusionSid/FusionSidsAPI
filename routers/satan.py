from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

satan = APIRouter()

@satan.get("/api/satan/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_satan_img():
    return FileResponse("file_path", media_type="image/png")