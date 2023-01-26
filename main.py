from qr import creat_qrcode
from PIL import Image, ImageTk
from os.path import dirname, realpath
from tkinter import (Tk, TclError, IntVar, PhotoImage, FALSE, END,
                     SUNKEN, Button, Entry, Checkbutton, Label)
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

        def clear_entry() -> None:
            self.__text_entry.delete(0, END)
            self.__text_verify.delete(0, END)

        data_entry_1: str = self.__text_entry.get()
        data_entry_verify: str = self.__text_verify.get()

        if data_entry_verify == data_entry_1 and data_entry_verify != '':
            upload_image('sucesso.png')
            self.__button_verify.configure(image=self.__WINDOW.button_image)
            creat_qrcode(data_entry_verify, self.__check)
        elif data_entry_verify != data_entry_1:
            upload_image('invalido.png')
            self.__button_verify.configure(image=self.__WINDOW.button_image)

        if self.__check_2 == 1:
            clear_entry()

    def __object_screen(self) -> None:
        def configurate_image() -> None:
            self.__WINDOW.button_verify_image_lower = ImageTk.PhotoImage(Image.open(
                f"{self.__path_image}" + "/verify.png".replace(' ', '')))

            self.__WINDOW.button_verify_image_upper = ImageTk.PhotoImage(Image.open(
                f"{self.__path_image}" + "/verify_handler.png"))

            self.__WINDOW.button_copy_upper = ImageTk.PhotoImage(Image.open(
                f'{self.__path_image}' + '/button_copy_upper.png'))

            self.__WINDOW.button_copy_normal = ImageTk.PhotoImage(Image.open(
                f'{self.__path_image}' + '/button_copy_normal.png'))

        def transfer_text() -> None:  # Copia o texto da entry 1 para entry verify
            data: str = self.__text_entry.get()
            self.__text_verify.delete(0, END)
            self.__text_verify.insert(END, data)

        def on_enter(button: Button, image: any, x: int, y: int) -> None:
            button.config(image=image)
            button.place(x=x, y=y)

        def on_leave(button: Button, image: any, x: int, y: int) -> None:
            button.config(image=image)
            button.place(x=x, y=y)

        # titulo do programa
        self.__title = Label(self.__WINDOW, text='Gerador de Qr Code', fg='white',
                             bg=self.__COLOR_BASIC, font=f'{self.__FONT_BASIC} 15 bold')
        self.__title.place(x=160, y=50)

                # configuração da entrada de texto
        self.__text_entry = Entry(self.__WINDOW, bg='white',
                                  fg='black', width=50)
        self.__text_entry.place(x=100, y=150)

        self.__text_verify = Entry(self.__WINDOW, bg='white',
                                   fg='black', width=50)
        self.__text_verify.place(x=100, y=220)

        # configuração das Checkboxs e dos seus Labels
        lb_cb_visu = Label(self.__WINDOW, text='Visualização do Qr Code',
                           fg='white', bg=self.__COLOR_BASIC)
        lb_cb_visu.place(x=270, y=263)
        cb_visualization = Checkbutton(self.__WINDOW, bg=self.__COLOR_BASIC,
                                       variable=self.__check, onvalue=1, offvalue=0)
        cb_visualization.place(x=245, y=260)

        lb_cb_clear = Label(self.__WINDOW, text='Clear on enter',
                            fg='white', bg=self.__COLOR_BASIC)
        lb_cb_clear.place(x=125, y=262)
        cb_clear = Checkbutton(self.__WINDOW, bg=self.__COLOR_BASIC,
                               variable=self.__check_2, onvalue=1, offvalue=0)
        cb_clear.place(x=100, y=260)

        # setando o botão de copiar
        configurate_image()
        button_copy = Button(self.__WINDOW, image=self.__WINDOW.button_copy_normal,
                             bg=self.__COLOR_BASIC, activebackground=self.__COLOR_BASIC,
                             bd=0, relief=SUNKEN, command=transfer_text)
        button_copy.place(x=205, y=180)

        # configuração do botão
        self.__button_verify = Button(self.__WINDOW, image=self.__WINDOW.button_verify_image_lower,
                                      bg=self.__COLOR_BASIC, activebackground=self.__COLOR_BASIC,
                                      command=self.__verify, bd=0, relief=SUNKEN)
        self.__button_verify.place(x=200, y=300)

        self.__button_verify.bind('<Enter>',
                                  lambda e: on_enter(self.__button_verify,
                                                     image=self.__WINDOW.button_verify_image_upper,
                                                     x=198, y=298))
        self.__button_verify.bind('<Leave>',
                                  lambda e: on_leave(self.__button_verify,
                                                     image=self.__WINDOW.button_verify_image_lower,
                                                     x=200, y=300))

        button_copy.bind('<Enter>',
                         lambda e: on_enter(button_copy,
                                            image=self.__WINDOW.button_copy_upper,
                                            x=203, y=178))
        button_copy.bind('<Leave>',
                         lambda e: on_leave(button_copy,
                                            image=self.__WINDOW.button_copy_normal,
                                            x=205, y=180))
