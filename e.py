import os

# for file in list(os.listdir("assets")):
#     name = file[:-4]
#     write_file = 'from fastapi import APIRouter\nfrom fastapi.responses import FileResponse, Response\n\n? = APIRouter()\n\n@?.get("/api/?/", responses = {200: {"content": {"image/png": {}}}}, response_class=Response)\ndef gen_?_img():\n    return FileResponse("file_path", media_type="image/png")'.replace("?", name)
#     write_file = str(write_file)
#     print(write_file)
#     with open(f"routers/{name}.py", 'w') as f:
#         f.write(write_file)

# for file in list(os.listdir("routers")):
#     with open("main.py", 'a') as f:
#         f.write(f"from routers.{file[:-3]} import {file[:-3]}")
#         f.write('\n')

for file in list(os.listdir("routers")):
    with open("main.py", 'a') as f:
        f.write(f"app.include_router(router={file[:-3]})")
        f.write('\n')