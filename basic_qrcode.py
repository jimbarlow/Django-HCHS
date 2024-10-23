# basic_qrcode.py

import segno

qrcode = segno.make_qr("https://pokerrun.harthumane.org")
qrcode.save(
    "pokerrun.png", 
    scale=6,
)

