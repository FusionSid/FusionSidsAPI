from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

aborted = APIRouter()

@aborted.get("/api/aborted/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_aborted_img():
    return FileResponse("file_path", media_type="image/png")