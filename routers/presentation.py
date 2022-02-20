from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

presentation = APIRouter()

@presentation.get("/api/presentation/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_presentation_img():
    return FileResponse("file_path", media_type="image/png")