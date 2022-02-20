from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

bongocat = APIRouter()

@bongocat.get("/api/bongocat/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_bongocat_img():
    return FileResponse("file_path", media_type="image/png")