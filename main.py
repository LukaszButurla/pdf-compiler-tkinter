import tkinter
from tkinter import Frame
import customtkinter
from logic.compiler import Compiler
from logic.edit import Edit

class MainWindow:
    
    def __init__(self):     
        self.open_app()

    def open_app(self):
        app = customtkinter.CTk()
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        app.geometry("600x400")

        self.labelListOfFiles = customtkinter.CTkLabel(app, text="Lista plików:", justify="left")
        self.labelListOfFiles.place(relx=0.02, rely=0.15)

        self.compiler = Compiler(self.labelListOfFiles, app)
        self.edit = Edit(app, self.compiler)

        buttonAdd = customtkinter.CTkButton(master=app, text="Dodaj", command=self.compiler.open_select_file_window)
        buttonAdd.place(relx=0.02, rely=0.05)

        buttonEdit = customtkinter.CTkButton(master=app, text="Usuń", command=self.edit_window)
        buttonEdit.place(relx=0.35, rely=0.05)

        buttonCompile = customtkinter.CTkButton(master=app, text="Łącz", command=self.compiler.mergePdf)
        buttonCompile.place(relx=0.67, rely=0.05)
        app.mainloop()

    def edit_window(self):
        self.edit.open_edit_window()
        


if __name__ == "__main__":
    MainWindow()
