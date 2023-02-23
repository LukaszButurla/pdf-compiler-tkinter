from tkinter import Toplevel, filedialog
from logic.splitOptions import SplitOptions
import customtkinter
from PyPDF2 import PdfReader, PdfWriter
from os import path

class Split:
    def __init__(self, app, files, windowColor, secondColor, textColor):
        self.files = files
        self.app = app
        self.splitOptions = SplitOptions(self.app, windowColor, secondColor, textColor, self.split_file, self.open_error_window)

    def open_split_file(self):
        if len(self.files.allFiles) == 1:
            file = open(self.files.allFiles[0], "rb")
            read = PdfReader(file)
            pages = len(read.pages)

            if pages >= 2:
                self.splitOptions.open_settings(pages, self.files.allFiles[0])
            else:
                self.open_error_window("Wybrany plik ma tylko 1 stronę")
        else:
            self.open_error_window("Wybierz tylko jeden plik")

    def open_error_window(self, text):

        self.errorWindow = Toplevel(self.app, background="#072d5e")
        self.errorWindow.geometry("350x150")

        btnAccept = customtkinter.CTkButton(self.errorWindow, text = "Ok", command=self.close_error_window, width= 70)
        btnAccept.place(relx = 0.35, rely= 0.6)

        labelInfo = customtkinter.CTkLabel(self.errorWindow, text = text, text_color="white", width=250, font=("Arial", 14))
        labelInfo.place(relx = 0.05, rely = 0.2)

    def close_error_window(self):
        self.errorWindow.destroy()

    def split_file(self, mode, amount, configList):

        folderToSave = filedialog.askdirectory()
        name = path.basename(self.files.allFiles[0])
        success = True

        if folderToSave != "":

            match mode:
                case "one":
                    try:
                        file = open(self.files.allFiles[0], "rb")
                        read = PdfReader(file)
                        pages = read.pages
                        i = 1
                        for p in pages:
                            with open(r"{}\{}_{}.pdf".format(folderToSave, name, i), "wb") as fSave:
                                toSave = PdfWriter()
                                toSave.add_page(p)
                                toSave.write(fSave)
                                i+=1                        
                    except:
                        self.open_error_window("Coś poszło nie tak")
                        success = False
                    
                    if success:
                        file.close()
                        self.open_error_window("Dzielenie powiodło się")

                case "multiple":

#--------------set readable syntax--------------------
                    number = 1
                    for i in range(int(amount)):
                        config = configList[i]
                        if config.replace(" ", "") == "":
                            self.open_error_window("Wypełnij wszystkie pola")
                            success = False
                            break

                        config = config.replace(" ", ",")
                        config = config.replace(";", ",")
                        config = config.split(",")
                        tmp = []

#--------------get pages with "-"---------------------
                        for c in config:
                            if "-" in c:
                                t = c.split("-")

                                try:

                                    if int(t[0]) > int(t[1]):
                                        t1 = t[0]
                                        t[0] = int(t[1])
                                        t[1] = int(t1) 

                                        for i in range(t[0], t[1]+1):
                                            tmp.append(i)

                                        else:
                                            tmp.reverse() 
                                    else:                             
                                    
                                        for i in range(int(t[0]), int(t[1])+1):
                                            tmp.append(i)

                                except:
                                    self.open_error_window("Coś poszło nie tak")
                                    success = False
                                                               
                            else:
                                tmp.append(int(c))

#--------------add selected pages---------------------
                        fRead = PdfReader(self.files.allFiles[0])
                        fSave = PdfWriter()
                        amountOfPages = len(fRead.pages)

                        if int(max(tmp)) <= int(amountOfPages):
                            for t in tmp:
                                t = int(t)
                                fSave.add_page(fRead.pages[t-1])

                            else:
                                with open(r"{}\{}_{}.pdf".format(folderToSave, name, number), "wb") as finalFile:
                                    fSave.write(finalFile)
                                number += 1
#----------------problem with inputs----------------------
                        else:
                            self.open_error_window("Podaj popawne liczby")
                            success = False
#----------------spliting ended succesflly-------------------
                    if success:
                        self.open_error_window("Dzielenie powiodło się")

                