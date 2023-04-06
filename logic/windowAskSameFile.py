from tkinter import Toplevel
import customtkinter
from functools import partial

class WindowAskSameFile:

    def __init__(self, files):
        self.files = files
        self.filesToSelect = []
        self.color = "#072d5e"
        self.textColor = "white"

    def open_window(self, app, file, table):
        self.filesToSelect = file
        self.selected = []
        self.windowAsk = Toplevel(app, background=self.color)
        self.windowAsk.geometry("500x250")
        self.add_widgets_to_window()

        x = app.winfo_x()
        y = app.winfo_y()
        self.windowAsk.geometry("+%d+%d" %(x+200,y+200))
        self.windowAsk.wm_transient(app)
        

    def add_widgets_to_window(self):
        self.labelInfo = customtkinter.CTkLabel(master=self.windowAsk, wraplength=400, justify="center", text_color="white", text="Plik o nazwie \"{}\" jest juz dodany. Czy chcesz dodać ponownie?".format(self.filesToSelect[0]))
        self.labelInfo.grid(row = 0, column = 0, rowspan = 2, columnspan = 2, sticky = "NSWE")

        buttonAgree = customtkinter.CTkButton(master=self.windowAsk, text="Tak",command=partial(self.select_if_add, True))
        buttonAgree.grid(row = 2, column = 0, sticky = "NSWE", padx = 25, pady = 45)

        buttonDecline = customtkinter.CTkButton(master=self.windowAsk, text="Nie", command=partial(self.select_if_add, False))
        buttonDecline.grid(row = 2, column = 1, sticky = "NSWE", padx = 25, pady = 45)
        
        self.windowAsk.rowconfigure((0,1,2), weight=1)
        self.windowAsk.columnconfigure((0,1), weight=1)
        self.windowAsk.minsize(500,250)

    def select_if_add(self, state):
        if state == False:
            self.filesToSelect.remove(self.filesToSelect[0])
            self.check_list()

        elif state == True:
            self.selected.append(self.filesToSelect[0])
            self.filesToSelect.remove(self.filesToSelect[0])
            self.check_list()
            

    def check_list(self):
        if len(self.filesToSelect) == 0:
            self.close_window(self.selected)

        if len(self.filesToSelect) > 0:
            self.change_label_text(self.filesToSelect[-1])


    def close_window(self, file):
        self.windowAsk.destroy()
        self.files.add_file_from_window(file)

    def change_label_text(self, fileName):
        self.labelInfo.configure(text="Plik o nazwie \"{}\" jest juz dodany. Czy chcesz dodać ponownie?".format(self.filesToSelect[0]))
            