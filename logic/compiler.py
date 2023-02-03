from tkinter import filedialog as fd

class Compiler:
    def __init__(self):
        self.allFiles = []

    def open_select_file_window(self):
        selectedFiles = fd.askopenfilenames()
        for file in selectedFiles:
            self.allFiles.append(file)
        print(self.allFiles)
        print(selectedFiles)