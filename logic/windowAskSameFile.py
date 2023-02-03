from tkinter import Toplevel
import customtkinter
from functools import partial

class WindowAskSameFile:

    def __init__(self, compiler):
        self.compiler = compiler

    def open_window(self, app, file):
        self.windowAsk = Toplevel(app, background="#242424")
        self.windowAsk.geometry("500x250")
        self.add_widgets_to_window(file)
        

    def add_widgets_to_window(self, file):
        labelInfo = customtkinter.CTkLabel(master=self.windowAsk, justify="center", text="Plik o podanej nazwie jest juz dodany. Czy chcesz dodać ponownie?")
        labelInfo.place(relx = 0.01, rely=0.3)

        buttonAgree = customtkinter.CTkButton(master=self.windowAsk, text="Tak",command=partial(self.close_window, True, file))
        buttonAgree.place(relx=0.1, rely=0.7)

        buttonDecline = customtkinter.CTkButton(master=self.windowAsk, text="Nie", command=partial(self.close_window, False, file))
        buttonDecline.place(relx=0.55, rely=0.7)

    def close_window(self, state, file):
        if state == False:
            self.windowAsk.destroy()
            
        
        elif state == True:
            self.windowAsk.destroy()
            self.compiler.add_file_from_window(file)
            