from fastapi import APIRouter
from utils import update_db

tags_metadata = [
    {
        "name": "Binary"
    }
]

binary = APIRouter(tags=tags_metadata)

@binary.get("/api/texttobinary")
async def texttobinary(text : str):
    update_db("texttobinary")

    result = ' '.join(format(ord(x), 'b') for x in text)

    return {
        "binary" : result
    }
    

@binary.get("/api/binarytotext")
async def binarytotext(binary_text : str):
    update_db("binarytotext")

    result = ''.join([chr(int(s, 2)) for s in binary_text.split()])

    return {
        "text" : result
    }

