import tkinter
from tkinter import Frame
import customtkinter
from logic.compiler import Compiler
from logic.edit import Edit
from tkinter import Scrollbar
from tkinter import ttk
from tkinter import END

class MainWindow:
    
    def __init__(self):     
        self.open_app()

    def open_app(self):
        app = customtkinter.CTk()
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        app.geometry("600x400")

        filesLabelFrame = Frame(app)
        filesLabelFrame.place(relx=0.02, rely=0.25, width=720, height=350)

        filesListScroll = Scrollbar(filesLabelFrame)
        filesListScroll.pack(side="right", fill="y")


        self.labelListOfFiles = customtkinter.CTkLabel(app, text="Lista plików:", justify="left")
        self.labelListOfFiles.place(relx=0.02, rely=0.15)

        self.treeListOfFiles = ttk.Treeview(filesLabelFrame, columns="File", show="headings", yscrollcommand=filesListScroll.set)
        self.treeListOfFiles.heading("#1", text="File")
        self.treeListOfFiles.place(width=720, height=350)

        filesListScroll.config(command=self.treeListOfFiles.yview)
        self.compiler = Compiler(self.labelListOfFiles, app)
        self.edit = Edit(app, self.compiler)

        self.treeListOfFiles.insert('', END, values = "dsadasdasdasdasdasda")
        self.treeListOfFiles.insert('', END, values = "dsadasdasdsadasdasdasda")
        self.treeListOfFiles.insert('', END, values = "dsadasdasddsaasdasdasda")
        self.treeListOfFiles.insert('', END, values = "dsadasdgasdasdasdasda")
        self.treeListOfFiles.insert('', END, values = "dsadasasddasdasdasdasda")
        self.treeListOfFiles.insert('', END, values = "dsadadassdasdasdasdasda")


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
