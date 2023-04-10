from tkinter import filedialog as fd
import PyPDF2

class Compiler:
    def __init__(self, files, errorWindow):
        self.files = files
        self.errorWindow = errorWindow


    def mergePdf(self):
        pdfMerger = PyPDF2.PdfMerger()

        try:
            if len(self.files.allFiles) >= 2:            
                for pdf in self.files.allFiles:
                    pdfMerger.append(pdf)

                saveDir = fd.asksaveasfilename(filetypes=[("PDF", ".pdf")], title="Zapisz")

                if saveDir != "":
                    if not saveDir.endswith(".pdf"):
                        saveDir = "{}.pdf".format(saveDir)

                    with open(saveDir, "wb") as fSave:
                        pdfMerger.write(fSave)
                
                    self.errorWindow.open_error_window("Łączenie przebiegło pomyślnie")
            
            elif len(self.files.allFiles) < 2:
                self.errorWindow.open_error_window("Wybierz minimum 2 pliki") 
                
            
        except:
            self.errorWindow.open_error_window("Coś poszło nie tak")
    


    