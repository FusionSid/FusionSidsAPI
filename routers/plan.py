from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

plan = APIRouter()

@plan.get("/api/plan/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_plan_img():
    return FileResponse("file_path", media_type="image/png")