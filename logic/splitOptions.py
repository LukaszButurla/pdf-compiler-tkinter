from tkinter import Frame, StringVar
import customtkinter
from functools import partial

class SplitOptions:

    def __init__(self, app, color, secondColor, textColor, splitFunc):
        self.app = app
        self.windowColor = color
        self.secondColor = secondColor
        self.textColor = textColor
        self.mode = "one"
        self.split_file = splitFunc

    def open_settings(self, amountOfPages, file):

        self.settingsFrame = Frame(self.app, background=self.windowColor)
        self.settingsFrame.pack(fill="both", expand=True)

        self.add_widgets(amountOfPages, file)

    def add_widgets(self, amountOfPages, file):
        selectedFileLabel = customtkinter.CTkLabel(self.settingsFrame, text = "Wybrany plik: {}".format(file), text_color=self.textColor)
        selectedFileLabel.place(relx = 0.025, rely = 0.025)

        selectionMode = StringVar()

        oneCheck = customtkinter.CTkRadioButton(self.settingsFrame, text = "Dziel po stronie", command=partial(self.disable_enable_widgets, selectionMode), value="disabled", variable=selectionMode, text_color=self.textColor)
        oneCheck.place(relx = 0.025, rely = 0.125)

        multipleCheck = customtkinter.CTkRadioButton(self.settingsFrame, text = "Dziel niestandardowo", command=partial(self.disable_enable_widgets, selectionMode), value="normal", variable=selectionMode, text_color=self.textColor)
        multipleCheck.place(relx = 0.2, rely = 0.125)

        self.amountInfoLabel = customtkinter.CTkLabel(self.settingsFrame, text = "Ile plików chcesz stworzyć:", text_color=self.textColor)
        self.amountInfoLabel.place(relx = 0.025, rely = 0.225)

        self.amountOfFilesSlider = customtkinter.CTkSlider(self.settingsFrame, width=250, from_=1, to=amountOfPages, number_of_steps=amountOfPages - 1)
        self.amountOfFilesSlider.place(relx = 0.025, rely = 0.3)
        self.amountOfFilesSlider.bind("<ButtonRelease-1>", self.update_slider)

        self.amountOfFilesLabel = customtkinter.CTkLabel(self.settingsFrame, text = "2", text_color=self.textColor)
        self.amountOfFilesLabel.place(relx = 0.35, rely = 0.285)

        self.newFilesList = customtkinter.CTkScrollableFrame(self.settingsFrame, width=350, height=275, fg_color=self.windowColor)
        self.newFilesList.place(relx = 0.5, rely = 0.1)

        btnCancel = customtkinter.CTkButton(self.settingsFrame, text = "Anuluj", command=self.close_frame)
        btnCancel.place(relx = 0.3, rely = 0.9)

        btnAccept = customtkinter.CTkButton(self.settingsFrame, text = "Potwierdź", command=self.split_click)
        btnAccept.place(relx = 0.55, rely = 0.9)

        for i in range(amountOfPages):
            box = Frame(self.newFilesList, bg=self.secondColor, height=100, highlightbackground="black", highlightthickness=1)
            box.pack(fill="x")

            numberLabel = customtkinter.CTkLabel(box, text = i+1, font=("Arial", 18), text_color=self.textColor)
            numberLabel.place(relx = 0.05, rely = 0.3)

            selectedFilesText = customtkinter.CTkEntry(box, width=250, height=30)
            selectedFilesText.place(relx = 0.2, rely = 0.3)

        self.amountOfFilesSlider.set(2)
        self.update_frame(2)
        self.disable_enable_widgets("disabled")
        oneCheck.select()

    def close_frame(self):
        self.settingsFrame.destroy()

    def split_click(self):
        configList = []

        for child in self.newFilesList.winfo_children():
            for c in child.winfo_children():
                if isinstance(c, customtkinter.CTkEntry):
                    configList.append(c.get())

        amount = self.amountOfFilesSlider.get()
        self.split_file(self.mode, amount, configList)

    def disable_enable_widgets(self, stat):
        
        if stat != "disabled" and stat != "normal":
            stat = stat.get()

        if stat == "disabled":
            self.mode = "one"
        elif stat == "normal":
            self.mode = "multiple"

        self.amountInfoLabel.configure(state = stat)
        self.amountOfFilesSlider.configure(state = stat)
        self.amountOfFilesLabel.configure(state = stat)
        for child in self.newFilesList.winfo_children():
            for c in child.winfo_children():
                c.configure(state = stat)


    def update_slider(self, event):
        amount = self.amountOfFilesSlider.get()
        self.amountOfFilesLabel.configure(text = str(amount)[:-2])
        self.update_frame(amount)

    def update_frame(self, number):
        l = 0
        for i in self.newFilesList.winfo_children():
            l += 1
            if l <= number:
                i.pack(fill="x")
            else:
                i.pack_forget()
            

            
