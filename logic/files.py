from tkinter import filedialog as fd
from logic.windowAskSameFile import WindowAskSameFile

class Files:

    def __init__(self, app):
        self.allFiles = []
        self.window = app
        self.windowAskSameFile = WindowAskSameFile(self)


    def open_select_file_window(self, table):
        self.table = table
        selectedFiles = fd.askopenfilenames(filetypes=[("PDF", ".pdf")])
        sameFiles = []
        for file in selectedFiles:
            if file not in self.allFiles:
                self.allFiles.append(file)
            else:
                sameFiles.append(file) 
        table.add_files_to_tree(self.allFiles)

        if len(sameFiles) > 0:                
            self.windowAskSameFile.open_window(self.window, sameFiles, table)


    def update_files(self, files):
        self.allFiles = files.copy()
        
    def add_file_from_window(self, files):
        for file in files:
            self.allFiles.append(file)
        
        self.table.add_files_to_tree(self.allFiles)