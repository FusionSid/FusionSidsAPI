import hashlib

from fastapi import APIRouter

from utils import update_stats

tags_metadata = [
    {
        "name": "Encrypt Text",
    }
]

async def text_encrypt(text : str) -> str:
    text = text.encode()
    encrypted = hashlib.sha256(text)
    text = encrypted.hexdigest()

    return text

encrypt = APIRouter(tags=tags_metadata)

@encrypt.get("/api/encrypt")
@update_stats(name="encrypt")
async def encrypt_text(text : str):
    """Hashes text"""

    encrypted = await text_encrypt(text)

    return {
        "encrypted" : encrypted
    }