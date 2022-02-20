from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

changemymind = APIRouter()

@changemymind.get("/api/changemymind/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_changemymind_img():
    return FileResponse("file_path", media_type="image/png")