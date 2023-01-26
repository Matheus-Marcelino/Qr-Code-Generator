from qrcode.main import QRCode
from os import mkdir

def creat_qrcode(text: str, check: int) -> None:
    qr = QRCode()
    qr.add_data(text)

    im = qr.make_image()
    try:
        im.save(f'output/placa-{text}.png')
        if check == 1:
            im.show()
    except FileNotFoundError:
        mkdir('output')
        creat_qrcode(text)
