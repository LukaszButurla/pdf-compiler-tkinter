from tkinter import Frame
import customtkinter

class SplitOptions:

    def __init__(self, app, color, secondColor, textColor):
        self.app = app
        self.windowColor = color
        self.secondColor = secondColor
        self.textColor = textColor

    def open_settings(self, amountOfPages, file):

        self.settingsFrame = Frame(self.app, background=self.windowColor)
        self.settingsFrame.pack(fill="both", expand=True)

        self.add_widgets(amountOfPages, file)

    def add_widgets(self, amountOfPages, file):
        selectedFileLabel = customtkinter.CTkLabel(self.settingsFrame, text = "Wybrany plik: {}".format(file), text_color=self.textColor)
        selectedFileLabel.place(relx = 0.025, rely = 0.025)

        amountInfoLabel = customtkinter.CTkLabel(self.settingsFrame, text = "Ile plików chcesz stworzyć:", text_color=self.textColor)
        amountInfoLabel.place(relx = 0.025, rely = 0.125)

        self.amountOfFilesSlider = customtkinter.CTkSlider(self.settingsFrame, command=self.update_slider, width=250, from_=1, to=amountOfPages, number_of_steps=amountOfPages - 1)
        self.amountOfFilesSlider.place(relx = 0.025, rely = 0.2)

        self.amountOfFilesLabel = customtkinter.CTkLabel(self.settingsFrame, text = self.amountOfFilesSlider.get(), text_color=self.textColor)
        self.amountOfFilesLabel.place(relx = 0.35, rely = 0.185)


    def update_slider(self, event):
        amount = self.amountOfFilesSlider.get()
        self.amountOfFilesLabel.configure(text = amount)