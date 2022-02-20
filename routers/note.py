from fastapi import APIRouter
from fastapi.responses import FileResponse, Response

note = APIRouter()

@note.get("/api/note/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)
def gen_note_img():
    return FileResponse("file_path", media_type="image/png")