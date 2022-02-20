from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

violence = APIRouter()

@violence.get("/api/violence/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_violence_img():
    return FileResponse("file_path", media_type="image/png")