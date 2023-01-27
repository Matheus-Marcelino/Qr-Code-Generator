"""Criador de Qr Code"""
from os import mkdir
from os.path import dirname, realpath
from webbrowser import open
from qrcode.main import QRCode


def creat_qrcode(text: str, check: int) -> None:
    """Cria o Qr Code

    Args:
        text (str): Texto que será inserido do Qr Code
        check (int): 1 -> mostra a imagem na tela
    """
    qr = QRCode()
    qr.add_data(text)

    text: str = text + '.png'
    FILE: str = dirname(realpath(__file__)) + '/output/'

    im = qr.make_image()
    try:
        im.save(f'output/{text}')
        if check == 1:
            open(FILE+text)  # mostra o Qr code na tela
    except FileNotFoundError:
        mkdir('output')
        creat_qrcode(text)


if __name__ == '__main__':
    creat_qrcode('Test', 1)
