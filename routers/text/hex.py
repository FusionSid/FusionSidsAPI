from fastapi import APIRouter
from utils import update_db

tags_metadata = [
    {
        "name": "Hex"
    }
]

hex = APIRouter(tags=tags_metadata)


@hex.get("/api/texttohex")
async def texttohex(text : str):
    update_db("texttohex")
    
    result = " ".join("{:02x}".format(ord(c)) for c in text)

    return {
        "hex" : result
    }
    

@hex.get("/api/hextotext")
async def hextotext(hex_text : str):
    update_db("hextotext")

    result = bytearray.fromhex(hex_text).decode()

    return {
        "text" : result
    }
