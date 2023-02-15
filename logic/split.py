from tkinter import Toplevel
import customtkinter

class Split:
    def __init__(self, app, files):
        self.files = files
        self.app = app

    def split_file(self):
        if len(self.files.allFiles) == 1:
            print("split")
        else:
            self.open_error_window()

    def open_error_window(self):

        self.errorWindow = Toplevel(self.app, background="#072d5e")
        self.errorWindow.geometry("250x150")

        btnAccept = customtkinter.CTkButton(self.errorWindow, text = "Ok", command=self.close_error_window, width= 70)
        btnAccept.place(relx = 0.35, rely= 0.6)

        labelInfo = customtkinter.CTkLabel(self.errorWindow, text = "Wybierz tylko 1 plik", text_color="white")
        labelInfo.place(relx = 0.25, rely = 0.2)

    def close_error_window(self):
        self.errorWindow.destroy()

    