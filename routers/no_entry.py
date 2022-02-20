from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

no_entry = APIRouter()

@no_entry.get("/api/no_entry/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_no_entry_img():
    return FileResponse("file_path", media_type="image/png")