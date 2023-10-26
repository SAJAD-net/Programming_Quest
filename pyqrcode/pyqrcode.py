#!/usr/bin/env python3

import sys
from datetime import datetime
import qrcode

qr = qrcode.QRCode(version=3, box_size=8, border=3,\
error_correction=qrcode.constants.ERROR_CORRECT_H)


def qr_gen(data):
    qr.add_data(data)
    qr.make(fit=True)

    ntosave = str(datetime.now().strftime("%Y.%m.%d_%H.%M.%S"))+'.png'
    img = qr.make_image(fill_color="blue", back_color="white")
    img.save(ntosave)
    print(f"QrCode saved : {ntosave}")


if da:=sys.argv[1]:
    qr_gen(da)
else:
    print("PyQrCode Usage : pyqrcode [DATA]")
