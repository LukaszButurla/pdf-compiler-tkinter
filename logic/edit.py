import customtkinter
from tkinter import Frame
from tkinter import ttk
from tkinter import END
from tkinter import Scrollbar

class Edit:
    def __init__(self, app, compiler):
        self.compiler = compiler
        self.window = app

    def open_edit_window(self):
        self.editWindow = Frame(self.window, background="#242124")
        self.editWindow.pack(fill="both", side="bottom", expand=True)
        self.add_widgets()
        self.add_column(self.compiler.allFiles)

    def add_widgets(self):
        buttonCancel = customtkinter.CTkButton(self.editWindow, text="Anuluj", command=self.close_window)
        buttonCancel.place(relx=0.68, rely=0.85)

        buttonAgree = customtkinter.CTkButton(self.editWindow, text="Potwierdź", command=self.save_changes)
        buttonAgree.place(relx=0.38, rely=0.85)

        buttonDelete = customtkinter.CTkButton(self.editWindow, text="Usuń", command=self.delete_row)
        buttonDelete.place(relx=0.08, rely=0.85)

        infoLabel = customtkinter.CTkLabel(self.editWindow, text="Wybierz pliki do usunięcia z listy")
        infoLabel.place(relx=0.04, rely=0.03)

        self.create_table(1)

    def delete_row(self):
        row = self.table.selection()
        for r in row:
            self.table.delete(r)

    def save_changes(self):
        files = []
        for row in self.table.get_children():
            files.append(self.table.item(row)["values"][0])

        self.compiler.allFiles = files
        self.compiler.add_files_to_tree()

        self.close_window()
    
    def create_table(self, files):
        tableFrame = Frame(self.editWindow)
        tableFrame.place(relx=0.04, rely=0.13, width=690, height=330)

        tableScroll = Scrollbar(tableFrame)
        tableScroll.pack(side="right", fill="y")

        self.table = ttk.Treeview(tableFrame, columns="Nazwa", show="headings", yscrollcommand=tableScroll.set)
        tableScroll.config(command=self.table.yview)
        self.table.heading("#1",text="Nazwa")
        self.table.place(width=670, height=330)

    def close_window(self):
        self.editWindow.destroy()
        

    def add_column(self, files):
        files.reverse()
        for f in files:
            f = f.replace(" ", "_")
            self.table.insert("", END, values=f)

    
