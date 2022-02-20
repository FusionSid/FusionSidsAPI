from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

failure = APIRouter()

@failure.get("/api/failure/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_failure_img():
    return FileResponse("file_path", media_type="image/png")