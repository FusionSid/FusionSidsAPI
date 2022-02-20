from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

unpopular = APIRouter()

@unpopular.get("/api/unpopular/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_unpopular_img():
    return FileResponse("file_path", media_type="image/png")