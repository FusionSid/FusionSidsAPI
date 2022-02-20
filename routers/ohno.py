from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

ohno = APIRouter()

@ohno.get("/api/ohno/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_ohno_img():
    return FileResponse("file_path", media_type="image/png")