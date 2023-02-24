import customtkinter
from tkinter import Frame, ttk, END, Scrollbar
from functools import partial

class EditPage:
    def __init__(self, mainFrame, files, color, secondColor, textColor, open_home_page):
        self.files = files
        self.color = color
        self.secondColor = secondColor
        self.textColor = textColor
        self.create_widgets(mainFrame, open_home_page)

    def open_page(self):
        self.add_files_to_tree()

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

        buttonAgree = customtkinter.CTkButton(self.editFrame, text="Potwierdź", bg_color=self.color, command=partial(self.update_files, open_home_page))
        buttonAgree.grid(row = 2, column = 0, sticky = "NSWE", padx = 25, pady = 15)

        buttonDelete = customtkinter.CTkButton(self.editFrame, text="Usuń", bg_color=self.color, command = self.delete_row)
        buttonDelete.grid(row = 2, column = 1, sticky = "NSWE", padx = 25, pady = 15)

        buttonCancel = customtkinter.CTkButton(self.editFrame, text="Anuluj", command=open_home_page, bg_color=self.color)
        buttonCancel.grid(row = 2, column = 2, sticky = "NSWE", padx = 25, pady = 15)

        self.table = ttk.Treeview(tableFrame, columns="Nazwa", show="headings")
        self.table.heading("#1",text="Nazwa")
        self.table.grid(row = 0, column = 0, sticky = "NSWE", padx = 25)

    def add_files_to_tree(self):
        self.clear_tree()
        for file in self.files.allFiles:
            self.add_row_to_tree(file)
    
    def add_row_to_tree(self, value):
        self.table.insert("", END, values=value.replace(" ", "_"))

    def delete_row(self):
        row = self.table.selection()
        for r in row:
            self.table.delete(r)

    def clear_tree(self):
        for i in self.table.get_children():
            self.table.delete(i)

    def update_files(self, close):
        selectedFiles = []
        for row in self.table.get_children():
            selectedFiles.append(self.table.item(row)["values"][0])
        self.files.allFiles = selectedFiles
        close()


