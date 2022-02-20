from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

corporate = APIRouter()

@corporate.get("/api/corporate/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_corporate_img():
    return FileResponse("file_path", media_type="image/png")