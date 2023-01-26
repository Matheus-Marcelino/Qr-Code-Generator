from qr import creat_qrcode
from PIL import Image, ImageTk
from os.path import dirname, realpath
from tkinter import (Tk, TclError, IntVar, PhotoImage, FALSE, END,
                     SUNKEN, Button, Entry, CHECKBUTTON, Label)
from tkinter.messagebox import showerror


class App(object):
    def __init__(self) -> None:
        self.__file_main: str = dirname(realpath(__file__))
        self.__path_image: str = self.__file_main + '/buttons'
        self.__COLOR_BASIC: str = '#282828'
        self.__FONT_BASIC: str = 'Bahnschrift'
        self.__WINDOW = Tk()
        self.__check = IntVar(self.__WINDOW)
        self.__check_2 = IntVar(self.__WINDOW)
        try:
            self.__screen_settings()
        except TclError:
            self.__WINDOW.state('icon')
            showerror('Arquivo não encontrado',
                      'A pasta "icon" não foi encontrada ou arquivo não encontrado\n'
                      'porfavor restaure ela!')
            self.__WINDOW.destroy()

        try:
            self.__object_screen()
        except (FileNotFoundError, TclError):
            showerror('Pasta de imagens não encontrada',
                      'A pasta "buttons" não foi encontrada ou arquivo não encontrado,\n'
                      'porfavor restaure ela!')
            self.__WINDOW.destroy()
        self.__WINDOW.mainloop()

    def __screen_settings(self) -> None:
        """Contém todas as definições da tela"""
        self.__WINDOW["bg"] = self.__COLOR_BASIC
        self.__WINDOW.resizable(width=FALSE, height=FALSE)
        self.__WINDOW.title('Gerador de Qr Code')

        # Centralizando a janela no monitor
        HEIGHT = int(400)
        WIDTH = int(500)
        X: int = self.__WINDOW.winfo_screenwidth() // 2 - (WIDTH + 2) // 2
        Y: int = self.__WINDOW.winfo_screenheight() // 2 - HEIGHT // 2
        self.__WINDOW.geometry(f'{WIDTH}x{HEIGHT}+{X}+{Y}')

        # Carregando icon da janela
        self.__WINDOW.call('wm', 'iconphoto', self.__WINDOW._w,
                           PhotoImage(file='icon/qr.png'))

    def __verify(self) -> None:
        def upload_image(image: str) -> None:
            self.__WINDOW.button_image = ImageTk.PhotoImage(
                Image.open(f'{self.__path_image}' + f'/ {image}'.replace(' ', ''))) # Carrega a imagem desejada
            if image == 'sucesso.png':
                self.__title['fg'] = 'green'
                self.__button_verify.place(x=197, y=298)
            else:
                self.__title['fg'] = 'red'
                self.__button_verify.place(x=198, y=298)