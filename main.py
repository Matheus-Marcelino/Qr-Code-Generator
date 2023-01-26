from os import mkdir
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
