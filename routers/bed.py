from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

bed = APIRouter()

@bed.get("/api/bed/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_bed_img():
    return FileResponse("file_path", media_type="image/png")