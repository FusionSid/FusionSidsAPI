from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

farmer = APIRouter()

@farmer.get("/api/farmer/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_farmer_img():
    return FileResponse("file_path", media_type="image/png")