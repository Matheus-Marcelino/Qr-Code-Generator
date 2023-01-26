"""Criador de Qr Code"""
from qrcode.main import QRCode
from os import mkdir


def creat_qrcode(text: str, check: int) -> None:
    """Cria o Qr Code

    Args:
        text (str): Texto que será inserido do Qr Code
        check (int): 1 -> mostra a imagem na tela
    """
    qr = QRCode()
    qr.add_data(text)

    im = qr.make_image()
    try:
        im.save(f'output/{text}.png')
        if check == 1:
            im.show()  # mostra o Qr code na tela
    except FileNotFoundError:
        mkdir('output')
        creat_qrcode(text)


if __name__ == '__main__':
    creat_qrcode('Test', 1)
