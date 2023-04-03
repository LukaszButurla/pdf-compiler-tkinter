import customtkinter
from tkinter import Toplevel

class ErrorWindow:
    def __init__(self, app, color, secondColor, textColor):
        self.app = app
        self.color = color
        self.secondColor = secondColor
        self.textColor = textColor
        
    def open_error_window(self, text):
    
        self.errorWindow = Toplevel(self.app, background=self.color)
        self.errorWindow.geometry("350x150")
        self.errorWindow.resizable(False, False)

        x = self.app.winfo_x()
        y = self.app.winfo_y()
        self.errorWindow.geometry("+%d+%d" %(x+200,y+200))
        self.errorWindow.wm_transient(self.app)

        btnAccept = customtkinter.CTkButton(self.errorWindow, text = "Ok", command=self.close_error_window, width= 70)
        btnAccept.grid(row = 1, column = 0, sticky="NSWE", padx = 40, pady=30)

        labelInfo = customtkinter.CTkLabel(self.errorWindow, text = text, text_color="white", width=250, font=("Arial", 14), anchor="s")
        labelInfo.grid(row = 0, column = 0, sticky="NSWE")
        
        self.errorWindow.rowconfigure((0,1), weight=1)
        self.errorWindow.columnconfigure(0, weight=1)

    def close_error_window(self):
        self.errorWindow.destroy()