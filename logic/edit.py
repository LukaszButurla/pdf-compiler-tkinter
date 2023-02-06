# from tkinter import Toplevel

# class Edit:
#     def __init__(self, app, compiler):
#         self.compiler = compiler
#         self.window = app

#     def open_edit_window(self):
#         self.editWindow = Toplevel(self.window, background="#242424")
#         self.editWindow.geometry("600x400")
import customtkinter
from tkinter import Frame
from tkinter import ttk
from tkinter import END

class Edit:
    def __init__(self, app, compiler):
        self.compiler = compiler
        self.window = app

    def open_edit_window(self):
        self.editWindow = Frame(self.window, background="#242124")
        # self.editWindow.geometry("600x400")
        self.editWindow.pack(fill="both", side="bottom", expand=True)
        self.add_widgets()
        self.add_column(self.compiler.allFiles)

    def add_widgets(self):
        buttonCancel = customtkinter.CTkButton(self.editWindow, text="Anuluj")
        buttonCancel.place(relx=0.6, rely=0.85)

        buttonAgree = customtkinter.CTkButton(self.editWindow, text="Potwierdź")
        buttonAgree.place(relx=0.2, rely=0.85)

        infoLabel = customtkinter.CTkLabel(self.editWindow, text="Wybierz pliki do usunięcia z listy")
        infoLabel.place(relx=0.04, rely=0.03)

        self.create_table(1)
    
    def create_table(self, files):
        s = ttk.Style()
        s.theme_use("clam")
        s.configure("Treeview", rowheight=35, font=(None, 14))
        s.configure("Treeview.Heading", font=(None, 16))
        self.table = ttk.Treeview(self.editWindow, columns="Nazwa", show="headings")
        self.table.heading("#1",text="Nazwa")
        self.table.place(relx=0.04, rely=0.13, width=690, height=330)
        

    def add_column(self, files):
        files.reverse()
        for f in files:
            self.table.insert("", END, values=f)

    
