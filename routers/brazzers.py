from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

brazzers = APIRouter()

@brazzers.get("/api/brazzers/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_brazzers_img():
    return FileResponse("file_path", media_type="image/png")