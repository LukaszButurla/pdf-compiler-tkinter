import customtkinter
from tkinter import Frame, ttk, END, Scrollbar

class Edit:
    def __init__(self, files):
        self.files = files


    def save_changes(self):
        selectedFiles = []
        for row in self.table.get_children():
            selectedFiles.append(self.table.item(row)["values"][0])

        self.files.allFiles = selectedFiles
        self.files.add_files_to_tree()

        self.close_window()

    def add_column(self, files):
        print(self.files.allFiles)
        for f in files:
            f = f.replace(" ", "_")
            self.table.insert("", END, values=f)

    
