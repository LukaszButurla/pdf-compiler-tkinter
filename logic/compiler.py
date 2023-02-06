from tkinter import filedialog as fd
from logic.windowAskSameFile import WindowAskSameFile
import PyPDF2

class Compiler:
    def __init__(self, labelFileList, window):
        self.allFiles = []
        self.window = window
        self.labelFileList = labelFileList
        self.windowAskSameFile = WindowAskSameFile(self)

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

        self.set_label_name()

    def set_label_name(self):
        txt = "Lista plików:\n"
        for file in self.allFiles:
            txt += "{}\n".format(file)

        self.labelFileList.configure(text=txt)

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
        self.set_label_name()


    