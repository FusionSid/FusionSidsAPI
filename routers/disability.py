from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

disability = APIRouter()

@disability.get("/api/disability/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_disability_img():
    return FileResponse("file_path", media_type="image/png")