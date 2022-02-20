from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

confusedcat = APIRouter()

@confusedcat.get("/api/confusedcat/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_confusedcat_img():
    return FileResponse("file_path", media_type="image/png")