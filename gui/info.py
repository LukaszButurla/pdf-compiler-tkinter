from tkinter import Frame
import customtkinter
from tkinter import RIGHT

class InfoPage:

    def __init__(self, mainFrame, color, secondColor, textColor, open_home_page):
        self.color = color
        self.secondColor = secondColor
        self.textColor = textColor
        self.create_widgets(mainFrame, open_home_page)


    def create_widgets(self, mainFrame, open_home_page):

#---------------------create frame-------------------------
        self.infoFrame = customtkinter.CTkFrame(mainFrame, fg_color=self.color)

        self.infoFrame.rowconfigure((0, 1), weight=3)
        self.infoFrame.rowconfigure((2), weight=1)
        self.infoFrame.columnconfigure(0, weight=1)

        boxFrame = customtkinter.CTkFrame(self.infoFrame, fg_color=self.secondColor)
        boxFrame.grid(row = 0, column = 0, rowspan = 2, sticky = "NSWE", padx = 50, pady = (50, 0))
        buttonFrame = customtkinter.CTkFrame(self.infoFrame, fg_color=self.color)
        buttonFrame.grid(row = 2, column = 0, sticky = "NSWE")

#-----------------configure frames----------------------------
        boxFrame.rowconfigure((0,1,2,3), weight=4)
        boxFrame.rowconfigure(4, weight=1)
        boxFrame.columnconfigure((0,1,2), weight=1)

        buttonFrame.rowconfigure(0, weight=1)
        buttonFrame.columnconfigure((0, 1, 2), weight=1)

#-----------------create widgets------------------------------
        labelCompanyName = customtkinter.CTkLabel(boxFrame,
                                              text="Doradcy Podatkowi Piotr Maciejewski,\n Monika Maciejewska Spółka z ograniczoną\nodpowiedzialnością",                                            
                                              font=("Arial", 18),
                                              text_color=self.textColor,
                                              anchor="s")
        labelCompanyName.grid(row = 0, column = 0, rowspan = 2, columnspan = 3, sticky = "NSWE", pady = 10)

        labelCompanyContact = customtkinter.CTkLabel(boxFrame, text="Strona internetowa: www.doradcy.net.pl\nE-mail: maciejewski@doradcy.net.pl\nNr tel. (32) 476 36 13",
                                                     font=("Arial", 18),
                                                     text_color=self.textColor,
                                                     anchor="n")
        labelCompanyContact.grid(row = 2, column = 0, rowspan = 2, columnspan = 3, sticky = "NSWE")


        btnExit = customtkinter.CTkButton(buttonFrame, text="Wyjdź",command=open_home_page)
        btnExit.grid(row = 0, column = 1, sticky = "NSWE", padx = 20, pady = 25)


        labelVersion = customtkinter.CTkLabel(boxFrame,
                                              text="Wersja programu: 1.3",
                                              font=("Arial", 12),
                                              text_color=self.textColor,
                                              anchor="e")
        labelVersion.grid(row = 4, column = 2, sticky = "NSWE", padx = 15)



    def close_page(self):
        self.page.destroy()