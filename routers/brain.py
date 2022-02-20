from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

brain = APIRouter()

@brain.get("/api/brain/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_brain_img():
    return FileResponse("file_path", media_type="image/png")