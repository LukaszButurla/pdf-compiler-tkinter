from tkinter import filedialog as fd

class Compiler:
    def __init__(self):
        pass

    def open_select_file_window(self):
        selectedFiles = fd.askopenfilenames()
        print(selectedFiles)