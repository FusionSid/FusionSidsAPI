from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

emergencymeeting = APIRouter()

@emergencymeeting.get("/api/emergencymeeting/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_emergencymeeting_img():
    return FileResponse("file_path", media_type="image/png")