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

        boxColor = "#242424"

        boxFrame = Frame(self.page, background=boxColor)
        boxFrame.place(relx = 0.06, rely=0.08, width=660, height=325)

        labelCompanyName = customtkinter.CTkLabel(boxFrame,
                                              text="Doradcy Podatkowi Piotr Maciejewski,\n Monika Maciejewska Spółka z ograniczoną\nodpowiedzialnością",
                                              font=("Arial", 18))
        labelCompanyName.place(relx = 0, rely = 0.2, width = 660, height=100)

        labelCompanyContact = customtkinter.CTkLabel(boxFrame, text="Strona internetowa: www.doradcy.net.pl\nE-mail: maciejewski@doradcy.net.pl\nNr tel. (32) 476 36 13",
                                                     font=("Arial", 18))
        labelCompanyContact.place(relx = 0, rely = 0.5, width = 660, height=100)

        btnExit = customtkinter.CTkButton(self.page, text="Wyjdź", command=self.close_page)
        btnExit.place(relx=0.4, rely=0.85)

        labelVersion = customtkinter.CTkLabel(self.page,
                                              text="Wersja programu: 1.1",
                                              justify = LEFT,
                                              font=("Arial", 12))
        labelVersion.place(relx = 0.05, rely = 0.9)

    def close_page(self):
        self.page.destroy()