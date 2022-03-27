from fastapi import APIRouter

from utils import update_stats

tags_metadata = [{"name": "Binary"}]

binary = APIRouter(tags=tags_metadata)


@binary.get("/api/texttobinary")
@update_stats(name="texttobinary")
async def texttobinary(text: str):
    """Converts text to binary"""

    result = " ".join(format(ord(x), "b") for x in text)

    return {"binary": result}


@binary.get("/api/binarytotext")
@update_stats(name="binarytotext")
async def binarytotext(binary_text: str):
    """Converts binary to text"""

    result = "".join([chr(int(s, 2)) for s in binary_text.split()])

    return {"text": result}
