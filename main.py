import tkinter
from tkinter import Frame
import customtkinter
from logic.compiler import Compiler

class MainWindow:
    
    def __init__(self):
        # self.compiler = Compiler()      
        self.open_app()

    def open_app(self):
        app = customtkinter.CTk()
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        app.geometry("400x400")

        self.labelListOfFiles = customtkinter.CTkLabel(app, text="Lista plików:", justify="left")
        self.labelListOfFiles.place(relx=0.02, rely=0.15)

        self.compiler = Compiler(self.labelListOfFiles)

        buttonAdd = customtkinter.CTkButton(master=app, text="Dodaj", command=self.compiler.open_select_file_window)
        buttonAdd.place(relx=0.02, rely=0.05)
        app.mainloop()


if __name__ == "__main__":
    MainWindow()
