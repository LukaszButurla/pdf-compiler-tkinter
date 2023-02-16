from tkinter import Frame
import customtkinter

class SplitOptions:

    def __init__(self, app, color, secondColor, textColor):
        self.app = app
        self.windowColor = color
        self.secondColor = secondColor
        self.textColor = textColor

    def open_settings(self, amountOfPages):

        self.settingsFrame = Frame(self.app, background=self.windowColor)
        self.settingsFrame.pack(fill="both", expand=True)

