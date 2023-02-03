from tkinter import Toplevel
import customtkinter

class WindowAskSameFile:

    def __init__(self):
        pass

    def open_window(self, app):
        self.windowAsk = Toplevel(app, background="#242424")
        self.windowAsk.geometry("500x250")
        self.add_widgets_to_window()

    def add_widgets_to_window(self):
        labelInfo = customtkinter.CTkLabel(master=self.windowAsk, justify="center", text="Plik o podanej nazwie jest juz dodany. Czy chcesz dodać ponownie?")
        labelInfo.place(relx = 0.01, rely=0.3)

        buttonAgree = customtkinter.CTkButton(master=self.windowAsk, text="Tak")
        buttonAgree.place(relx=0.1, rely=0.7)

        buttonDecline = customtkinter.CTkButton(master=self.windowAsk, text="Nie")
        buttonDecline.place(relx=0.55, rely=0.7)