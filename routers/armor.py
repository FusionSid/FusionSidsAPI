from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

armor = APIRouter()

@armor.get("/api/armor/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_armor_img():
    return FileResponse("file_path", media_type="image/png")