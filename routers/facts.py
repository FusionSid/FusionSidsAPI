from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

facts = APIRouter()

@facts.get("/api/facts/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_facts_img():
    return FileResponse("file_path", media_type="image/png")