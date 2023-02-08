from tkinter import filedialog as fd
import PyPDF2
from tkinter import END

class Compiler:
    def __init__(self, files):
        self.files = files


    def mergePdf(self):
        pdfMerger = PyPDF2.PdfMerger()

        try:
            for pdf in self.files.allFiles:
                pdfMerger.append(pdf)

            saveDir = fd.asksaveasfilename(filetypes=[("PDF", ".pdf")], title="Zapisz")

            if saveDir != "":
                if not saveDir.endswith(".pdf"):
                    saveDir = "{}.pdf".format(saveDir)

                with open(saveDir, "wb") as fSave:
                    pdfMerger.write(fSave)
        except:
            print("Error save")

    


    