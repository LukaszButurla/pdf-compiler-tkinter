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

        self.add_widgets(amountOfPages)

    def add_widgets(self, amountOfPages):
        self.amountOfFilesSlider = customtkinter.CTkSlider(self.settingsFrame, command=self.update_slider, width=250, from_=1, to=amountOfPages, number_of_steps=amountOfPages - 1)
        self.amountOfFilesSlider.place(relx = 0.025, rely = 0.3)

        self.amountOfFilesLabel = customtkinter.CTkLabel(self.settingsFrame, text = self.amountOfFilesSlider.get(), text_color=self.textColor)
        self.amountOfFilesLabel.place(relx = 0.35, rely = 0.285)

    def update_slider(self, event):
        amount = self.amountOfFilesSlider.get()
        self.amountOfFilesLabel.configure(text = amount)