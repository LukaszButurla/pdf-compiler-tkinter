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

        self.amountOfFilesLabel = customtkinter.CTkLabel(self.settingsFrame, text = "2", text_color=self.textColor)
        self.amountOfFilesLabel.place(relx = 0.35, rely = 0.185)

        self.newFilesList = customtkinter.CTkScrollableFrame(self.settingsFrame, width=350, height=275, fg_color=self.windowColor)
        self.newFilesList.place(relx = 0.5, rely = 0.1)
        
        for i in range(amountOfPages):
            box = Frame(self.newFilesList, bg=self.secondColor, height=100, highlightbackground="black", highlightthickness=1)
            box.pack(fill="x")

            numberLabel = customtkinter.CTkLabel(box, text = i+1, font=("Arial", 18), text_color=self.textColor)
            numberLabel.place(relx = 0.05, rely = 0.3)

            selectedFilesText = customtkinter.CTkEntry(box, width=250, height=30)
            selectedFilesText.place(relx = 0.2, rely = 0.3)

        self.amountOfFilesSlider.set(2)
        self.update_frame(2)


    def update_slider(self, event):
        amount = self.amountOfFilesSlider.get()
        self.amountOfFilesLabel.configure(text = str(amount)[:-2])
        self.update_frame(amount)

    def update_frame(self, number):
        l = 0
        for i in self.newFilesList.winfo_children():
            l += 1
            if l > number:
                i.pack_forget()

            elif l >= number:
                i.pack(fill="x")
