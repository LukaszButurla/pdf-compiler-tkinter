from tkinter import filedialog as fd
from logic.windowAskSameFile import WindowAskSameFile
import PyPDF2
from tkinter import END

class Compiler:
    def __init__(self, window, filesTree):
        self.allFiles = []
        self.window = window
        self.windowAskSameFile = WindowAskSameFile(self)
        self.tree = filesTree

    def open_select_file_window(self):
        selectedFiles = fd.askopenfilenames()
        sameFiles = []
        for file in selectedFiles:
            if file not in self.allFiles:
                self.allFiles.append(file)
            else:
                sameFiles.append(file) 

        if len(sameFiles) > 0:                
            self.windowAskSameFile.open_window(self.window, sameFiles)

        self.add_files_to_tree()


    def add_files_to_tree(self):
        self.clear_tree()
        for file in self.allFiles:
            self.add_row_to_tree(file)

    def add_row_to_tree(self, value):
        self.tree.insert("", END, values=value)

    def clear_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

    def mergePdf(self):
        pdfMerger = PyPDF2.PdfMerger()
        for pdf in self.allFiles:
            pdfMerger.append(pdf)

        saveDir = r"C:\Users\praktykant\Desktop\program\pdf\test.pdf"

        with open(saveDir, "wb") as fSave:
            pdfMerger.write(fSave)

    def add_file_from_window(self, file):
        for f in file:
            self.allFiles.append(f)
        self.add_files_to_tree()


    