import customtkinter
from tkinter import StringVar
from functools import partial

class SplitPage:

    def __init__(self, frame, files, color, secondColor, textColor, open_home_page):
        self.files = files
        self.windowColor = color
        self.textColor = textColor
        self.secondColor = secondColor
        self.create_widgets(frame)

    def create_widgets(self, frame):
        self.splitFrame = customtkinter.CTkFrame(frame, fg_color=self.windowColor)
        self.settingsFrame = customtkinter.CTkFrame(self.splitFrame)

        leftFrame = customtkinter.CTkFrame(self.splitFrame, fg_color=self.windowColor)
        leftFrame.grid(row = 1, column = 0, rowspan = 6, sticky = "NSWE", pady = 15)

        rightFrame = customtkinter.CTkFrame(self.splitFrame, fg_color=self.windowColor)
        rightFrame.grid(row = 1, column = 1, rowspan = 6, sticky = "NSWE")

        self.splitFrame.columnconfigure((0, 1), weight=1)
        self.splitFrame.rowconfigure((1,2,3,4,5,6), weight=3)
        self.splitFrame.rowconfigure(7, weight=1)

        leftFrame.rowconfigure((3,4,5,6), weight=1)
        leftFrame.columnconfigure((0, 1), weight=1)

        rightFrame.rowconfigure(0, weight=1)
        rightFrame.columnconfigure(0, weight=1)


        amountOfPages = 4
        selectedFileLabel = customtkinter.CTkLabel(self.splitFrame, text = "Wybrany plik:", text_color=self.textColor, anchor="w")
        selectedFileLabel.grid(row = 0, column = 0, columnspan = 2, sticky = "NSWE", padx = 15, pady = 5)

        selectionMode = StringVar()

        oneCheck = customtkinter.CTkRadioButton(leftFrame, text = "Dziel po stronie", value="disabled", variable=selectionMode, text_color=self.textColor)
        oneCheck.grid(row = 0, column = 0, sticky = "NSWE", padx = 15, pady = (0, 15))

        multipleCheck = customtkinter.CTkRadioButton(leftFrame, text = "Dziel niestandardowo", value="normal", variable=selectionMode, text_color=self.textColor)
        multipleCheck.grid(row = 0, column = 1, sticky = "NSWE", padx = 15, pady = (0, 15))

        self.amountInfoLabel = customtkinter.CTkLabel(leftFrame, text = "Ile plików chcesz stworzyć:", text_color=self.textColor, anchor="w")
        self.amountInfoLabel.grid(row = 1, column = 0, columnspan = 2, sticky = "NSWE", padx = 15)

        self.amountOfFilesSlider = customtkinter.CTkSlider(leftFrame, width=250, from_=1, to=amountOfPages, number_of_steps=amountOfPages - 1)
        self.amountOfFilesSlider.grid(row = 2, column = 0, columnspan = 2, sticky = "WE", padx = 15)
        # self.amountOfFilesSlider.bind("<ButtonRelease-1>", self.update_slider)

        self.newFilesList = customtkinter.CTkScrollableFrame(rightFrame, width=350, height=275, fg_color=self.windowColor)
        self.newFilesList.grid(row = 0, column = 0, sticky = "NSWE", padx = 15, pady = 15)

        btnCancel = customtkinter.CTkButton(self.splitFrame, text = "Anuluj")
        btnCancel.grid(row = 7, column = 0, sticky = "NSWE", padx = 100, pady = 15)

        btnAccept = customtkinter.CTkButton(self.splitFrame, text = "Potwierdź")
        btnAccept.grid(row = 7, column = 1, sticky = "NSWE", padx = 100, pady = 15)
        

        for i in range(amountOfPages):
            box = customtkinter.CTkFrame(self.newFilesList, fg_color=self.secondColor, height=50, border_color="black", border_width=1)
            box.pack(fill="x")
            
            box.columnconfigure((1,2,3,4,5), weight=1)
            box.rowconfigure(0, weight=1)

            numberLabel = customtkinter.CTkLabel(box, text = i+1, font=("Arial", 18), width=50, text_color=self.textColor)
            numberLabel.grid(row = 0, column = 0, sticky="NSWE", pady=15, padx = 15)

            selectedFilesText = customtkinter.CTkEntry(box, width=250, height=50)
            selectedFilesText.grid(row = 0, column = 1, columnspan = 5, sticky="NSWE", pady=15, padx = 15)