from fastapi import APIRouter

from utils import update_stats

tags_metadata = [
    {
        "name": "Hex"
    }
]

hex = APIRouter(tags=tags_metadata)


@hex.get("/api/texttohex")
@update_stats(name="texttohex")
async def texttohex(text : str):
    
    result = " ".join("{:02x}".format(ord(c)) for c in text)

    return {
        "hex" : result
    }
    

@hex.get("/api/hextotext")
@update_stats(name="hextotext")
async def hextotext(hex_text : str):

    result = bytearray.fromhex(hex_text).decode()

    return {
        "text" : result
    }
