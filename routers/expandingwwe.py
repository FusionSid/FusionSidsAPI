from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

expandingwwe = APIRouter()

@expandingwwe.get("/api/expandingwwe/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_expandingwwe_img():
    return FileResponse("file_path", media_type="image/png")