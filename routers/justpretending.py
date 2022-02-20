from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

justpretending = APIRouter()

@justpretending.get("/api/justpretending/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_justpretending_img():
    return FileResponse("file_path", media_type="image/png")