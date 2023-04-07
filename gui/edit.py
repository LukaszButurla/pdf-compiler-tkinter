import customtkinter
from tkinter import Frame, ttk, END, Scrollbar
from functools import partial
from gui.table import Table

class EditPage:
    def __init__(self, mainFrame, files, color, secondColor, textColor, open_home_page):
        self.files = files
        self.color = color
        self.secondColor = secondColor
        self.textColor = textColor
        self.table = Table()
        self.create_widgets(mainFrame, open_home_page)

    def open_page(self):
        self.fileToUpdate = self.files.allFiles.copy()
        self.table.add_files_to_tree(self.fileToUpdate)

    def create_widgets(self, mainFrame, open_home_page):
#-------------------create frames-----------------------------
        self.editFrame = customtkinter.CTkFrame(mainFrame, fg_color=self.color)
        tableFrame = customtkinter.CTkFrame(self.editFrame, fg_color=self.color)
        tableFrame.grid(row = 1, column = 0, columnspan=3, sticky = "NSWE")

#------------------configure frames--------------------------
        self.editFrame.rowconfigure((2), weight=1)
        self.editFrame.rowconfigure((1), weight=7)
        self.editFrame.columnconfigure((0,1,2), weight=1)
        tableFrame.rowconfigure(0, weight=1)
        tableFrame.columnconfigure(0, weight=1)

#------------------create widgets----------------------------
        infoLabel = customtkinter.CTkLabel(self.editFrame, text="Wybierz pliki do usunięcia z listy", text_color=self.textColor, anchor="w")
        infoLabel.grid(row = 0, column = 0, columnspan = 3, sticky = "NSWE", padx = 25, pady = 15)

        buttonAgree = customtkinter.CTkButton(self.editFrame, text="Potwierdź", bg_color=self.color, command=partial(self.agree, open_home_page))
        buttonAgree.grid(row = 2, column = 0, sticky = "NSWE", padx = 25, pady = 15)

        buttonDelete = customtkinter.CTkButton(self.editFrame, text="Usuń", bg_color=self.color, command = self.table.delete_row)
        buttonDelete.grid(row = 2, column = 1, sticky = "NSWE", padx = 25, pady = 15)

        buttonCancel = customtkinter.CTkButton(self.editFrame, text="Anuluj", command=open_home_page, bg_color=self.color)
        buttonCancel.grid(row = 2, column = 2, sticky = "NSWE", padx = 25, pady = 15)

        self.table.create_table(tableFrame)
        self.table.table.grid(row = 0, column = 0, sticky = "NSWE", padx = 15)

    def agree(self, close):
        selectedFiles = []
        for file in self.table.filesToEdit:
            selectedFiles.append(file)
        self.files.update_files(selectedFiles)
        close()


