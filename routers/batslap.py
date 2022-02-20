from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

batslap = APIRouter()

@batslap.get("/api/batslap/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_batslap_img():
    return FileResponse("file_path", media_type="image/png")