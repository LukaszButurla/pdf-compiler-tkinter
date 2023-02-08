from tkinter import Toplevel
import customtkinter
from functools import partial

class WindowAskSameFile:

    def __init__(self, files):
        self.files = files
        self.filesToSelect = []

    def open_window(self, app, file):
        self.filesToSelect = file
        self.selected = []
        self.windowAsk = Toplevel(app, background="#242424")
        self.windowAsk.geometry("500x250")
        self.add_widgets_to_window()
        

    def add_widgets_to_window(self):
        self.labelInfo = customtkinter.CTkLabel(master=self.windowAsk, wraplength=400, justify="center", text_color="white", text="Plik o nazwie \"{}\" jest juz dodany. Czy chcesz dodać ponownie?".format(self.filesToSelect[0]))
        self.labelInfo.place(relx = 0.01, rely=0.3)

        buttonAgree = customtkinter.CTkButton(master=self.windowAsk, text="Tak",command=partial(self.select_if_add, True))
        buttonAgree.place(relx=0.1, rely=0.7)

        buttonDecline = customtkinter.CTkButton(master=self.windowAsk, text="Nie", command=partial(self.select_if_add, False))
        buttonDecline.place(relx=0.55, rely=0.7)

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
            