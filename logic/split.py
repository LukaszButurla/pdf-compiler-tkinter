from tkinter import Toplevel
from logic.splitOptions import SplitOptions
import customtkinter
from PyPDF2 import PdfReader, PdfWriter

class Split:
    def __init__(self, app, files, windowColor, secondColor, textColor):
        self.files = files
        self.app = app
        self.splitOptions = SplitOptions(self.app, windowColor, secondColor, textColor, self.split_file)

    def open_split_file(self):
        if len(self.files.allFiles) == 1:
            file = open(self.files.allFiles[0], "rb")
            read = PdfReader(file)
            pages = len(read.pages)

            self.splitOptions.open_settings(pages, self.files.allFiles[0])
        else:
            self.open_error_window()

    def open_error_window(self):

        self.errorWindow = Toplevel(self.app, background="#072d5e")
        self.errorWindow.geometry("250x150")

        btnAccept = customtkinter.CTkButton(self.errorWindow, text = "Ok", command=self.close_error_window, width= 70)
        btnAccept.place(relx = 0.35, rely= 0.6)

        labelInfo = customtkinter.CTkLabel(self.errorWindow, text = "Wybierz tylko 1 plik", text_color="white")
        labelInfo.place(relx = 0.25, rely = 0.2)

    def close_error_window(self):
        self.errorWindow.destroy()

    def split_file(self, mode):

        match mode:
            case "one":
                print("one")
                file = open(self.files.allFiles[0], "rb")
                read = PdfReader(file)
                pages = read.pages
                print(len(pages))
                i = 1
                for p in pages:
                    with open(r"C:\Users\praktykant\Desktop\program\pdf\test_{}.pdf".format(i), "wb") as fSave:
                        toSave = PdfWriter()
                        toSave.add_page(p)
                        toSave.write(fSave)

                        i+=1

                else:
                    file.close()




            case "multiple":
                print("multiple")



    