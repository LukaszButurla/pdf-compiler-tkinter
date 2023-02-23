from tkinter import Frame, Scrollbar, ttk
import customtkinter
from logic.compiler import Compiler
from logic.split import Split
from logic.edit import Edit
from logic.files import Files
from gui.ui import Ui

class MainWindow:
    
    def __init__(self):     
        self.open_app()
        self.ui = Ui(self.app)
        

    def open_app(self):

        self.app = customtkinter.CTk()
        self.app.title("Łącznik pdf")
        self.app.geometry("800x400")
        self.app.resizable(True, True)    
             
        self.app.columnconfigure(0, weight=1)
        self.app.rowconfigure(0, weight=1)

if __name__ == "__main__":
    MainWindow()
