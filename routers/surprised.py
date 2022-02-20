from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

surprised = APIRouter()

@surprised.get("/api/surprised/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_surprised_img():
    return FileResponse("file_path", media_type="image/png")