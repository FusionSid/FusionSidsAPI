from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

ban = APIRouter()

@ban.get("/api/ban/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_ban_img():
    return FileResponse("file_path", media_type="image/png")