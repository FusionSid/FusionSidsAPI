from fastapi import APIRouter
from utils import update_db
from io import BytesIO
from fastapi.responses import StreamingResponse
import qrcode as qrc

# Title for docs
tags_metadata = [
    {
        "name": "Qr Code",
    }
]

qrcode = APIRouter(tags=tags_metadata)

async def generate_qrcode(url):
    qr = qrc.QRCode(
        version=1,
        error_correction=qrc.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(str(url))
    qr.make(fit=True)
    img = qr.make_image(fill_color="black",
                        back_color="white").convert('RGB')
    d = BytesIO()
    d.seek(0)
    img.save(d, "PNG")
    d.seek(0)
    return d


@qrcode.get("/api/qrcode/")
async def gen_qrcode(link : str):
    await update_db('qrcode')
    file = await generate_qrcode(link)

    return StreamingResponse(file, media_type="image/png")
