from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

cancer = APIRouter()

@cancer.get("/api/cancer/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_cancer_img():
    return FileResponse("file_path", media_type="image/png")