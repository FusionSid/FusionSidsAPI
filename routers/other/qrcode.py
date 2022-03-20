from fastapi import APIRouter
from io import BytesIO
from fastapi.responses import StreamingResponse
import qrcode as qrc

from utils import update_stats

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
@update_stats(name="qrcode")
async def gen_qrcode(link : str):
    file = await generate_qrcode(link)

    return StreamingResponse(file, media_type="image/png")
