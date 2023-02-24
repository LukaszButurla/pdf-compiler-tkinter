from tkinter import filedialog as fd, END
from logic.windowAskSameFile import WindowAskSameFile

class Files:

    def __init__(self):
        self.allFiles = []
        # self.windowAskSameFile = WindowAskSameFile(self, color, textColor)


    def open_select_file_window(self, table):
        selectedFiles = fd.askopenfilenames(filetypes=[("PDF", ".pdf")])
        sameFiles = []
        for file in selectedFiles:
            if file not in self.allFiles:
                self.allFiles.append(file)
            else:
                sameFiles.append(file) 
        table.add_files_to_tree(self.allFiles)

        # if len(sameFiles) > 0:                
            # self.windowAskSameFile.open_window(self.window, sameFiles)


    def update_files(self, files):
        self.allFiles = files.copy()