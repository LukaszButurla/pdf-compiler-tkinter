from tkinter import filedialog as fd
from logic.windowAskSameFile import WindowAskSameFile
import PyPDF2
from tkinter import END

class Compiler:
    def __init__(self, window, filesTree, filesLabel):
        self.allFiles = []
        self.window = window
        self.windowAskSameFile = WindowAskSameFile(self)
        self.tree = filesTree
        self.filesLabel = filesLabel

    def open_select_file_window(self):
        selectedFiles = fd.askopenfilenames(filetypes=[("PDF", ".pdf")])
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
        self.filesLabel.configure(text = "Lista plików: {}".format(len(self.allFiles)))

    def add_row_to_tree(self, value):
        self.tree.insert("", END, values=value)

    def clear_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

    def mergePdf(self):
        pdfMerger = PyPDF2.PdfMerger()

        try:
            for pdf in self.allFiles:
                pdfMerger.append(pdf)

<<<<<<< HEAD
            saveDir = fd.asksaveasfilename(filetypes = [("PDF", ".pdf")], title="Zapisz")
=======
            saveDir = fd.asksaveasfilename(filetypes=[("PDF", ".pdf")], title="Zapisz")
>>>>>>> main

            if not saveDir.endswith(".pdf"):
                saveDir = "{}.pdf".format(saveDir)

            with open(saveDir, "wb") as fSave:
                pdfMerger.write(fSave)
<<<<<<< HEAD

        except Exception as e:
            print("Error save: ", e)
=======
        except:
            print("Error save")
>>>>>>> main

    def add_file_from_window(self, file):
        for f in file:
            self.allFiles.append(f)
        self.add_files_to_tree()


    