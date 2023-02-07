from tkinter import Frame
import customtkinter
from tkinter import LEFT

class InfoPage:

    def __init__(self, window):
        self.window = window

    def open_page(self):
        self.page = Frame(self.window, background="#242124")
        self.page.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):

        labelCompany = customtkinter.CTkLabel(self.page,
                                              text="Informacje firmy\nKancelaria Doradcy Podatkowego Super Nowa\nPiotr, Monika Maciejewski\nStrona internetowa: https://www.doradcy.net.pl\nE-mail: maciejewski@doradcy.net.pl\nNr tel. (32) 476 36 13",
                                             justify = LEFT, font=("Arial", 18))
        labelCompany.place(relx = 0.05, rely=0.05)

        btnExit = customtkinter.CTkButton(self.page, text="Wyjdź", command=self.close_page)
        btnExit.place(relx=0.4, rely=0.85)

        labelVersion = customtkinter.CTkLabel(self.page,
                                              text="Wersja programu: 1.1",
                                              justify = LEFT,
                                              font=("Arial", 12))
        labelVersion.place(relx = 0.05, rely = 0.9)

    def close_page(self):
        self.page.destroy()