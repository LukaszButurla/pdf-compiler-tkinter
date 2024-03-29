import customtkinter
from tkinter import StringVar, END
from functools import partial
from PyPDF2 import PdfReader
from logic.split import Split

class SplitPage:

    def __init__(self, frame, files, color, secondColor, textColor, open_home_page, app, open_error_window):
        self.files = files
        self.windowColor = color
        self.textColor = textColor
        self.secondColor = secondColor
        self.split = Split(files, app, open_error_window)
        self.create_widgets(frame, open_home_page)
        self.mode = "one"
        
    def on_open(self):
        file = self.files.allFiles[0]
        self.selectedFileLabel.configure(text="Wybrany plik: {}".format(file))
        
        fileRead = open(self.files.allFiles[0], "rb")
        read = PdfReader(fileRead)
        pages = len(read.pages)
        
        if pages <= 1:
            return False
        else:       
            self.amountOfFilesSlider.configure(to=pages, number_of_steps = pages-1)
            self.create_boxes(pages)
            self.reset_values()
            return True

    def create_widgets(self, frame, open_home_page):
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
        self.selectedFileLabel = customtkinter.CTkLabel(self.splitFrame, text = "Wybrany plik:", text_color=self.textColor, anchor="w")
        self.selectedFileLabel.grid(row = 0, column = 0, columnspan = 2, sticky = "NSWE", padx = 15, pady = 5)
        selectionMode = StringVar()

        self.oneCheck = customtkinter.CTkRadioButton(leftFrame, text = "Dziel po stronie", value="disabled", command=partial(self.disable_enable_widgets, selectionMode), variable=selectionMode, text_color=self.textColor)
        self.oneCheck.grid(row = 0, column = 0, sticky = "NSWE", padx = 15, pady = (0, 15))

        multipleCheck = customtkinter.CTkRadioButton(leftFrame, text = "Dziel niestandardowo", value="normal", command=partial(self.disable_enable_widgets, selectionMode), variable=selectionMode, text_color=self.textColor)
        multipleCheck.grid(row = 0, column = 1, sticky = "NSWE", padx = 15, pady = (0, 15))

        self.amountInfoLabel = customtkinter.CTkLabel(leftFrame, text = "Ile plików chcesz stworzyć: {}".format(1), text_color=self.textColor, anchor="w")
        self.amountInfoLabel.grid(row = 1, column = 0, columnspan = 2, sticky = "NSWE", padx = 15)

        self.amountOfFilesSlider = customtkinter.CTkSlider(leftFrame, width=250, from_=1, to=amountOfPages, number_of_steps=amountOfPages - 1)
        self.amountOfFilesSlider.grid(row = 2, column = 0, columnspan = 2, sticky = "WE", padx = 15)
        self.amountOfFilesSlider.bind("<ButtonRelease-1>", self.update_slider)

        self.newFilesList = customtkinter.CTkScrollableFrame(rightFrame, width=350, height=275, fg_color=self.windowColor)
        self.newFilesList.grid(row = 0, column = 0, sticky = "NSWE", padx = 15, pady = 15)
        

        btnCancel = customtkinter.CTkButton(self.splitFrame, text = "Anuluj", command=open_home_page)
        btnCancel.grid(row = 7, column = 0, sticky = "NSWE", padx = 100, pady = 15)

        btnAccept = customtkinter.CTkButton(self.splitFrame, text = "Potwierdź", command=self.split_click)
        btnAccept.grid(row = 7, column = 1, sticky = "NSWE", padx = 100, pady = 15)
                    
        
    def split_click(self):
    
        try:
            configList = []

            for child in self.newFilesList.winfo_children():
                for c in child.winfo_children():
                    if isinstance(c, customtkinter.CTkEntry):
                        configList.append(c.get())

            amount = self.amountOfFilesSlider.get()
            self.split.split_file(self.mode, amount, configList)
        except Exception as e:
            self.split.open_error_window("Coś poszło nie tak")
            print(e)
        
    def create_boxes(self, amountOfPages):
        
        for i in range(amountOfPages):
            box = customtkinter.CTkFrame(self.newFilesList, fg_color=self.secondColor, height=50, border_color="black", border_width=1)
            box.pack(fill="x")
            
            box.columnconfigure((1,2,3,4,5), weight=1)
            box.rowconfigure(0, weight=1)

            numberLabel = customtkinter.CTkLabel(box, text = i+1, font=("Arial", 18), width=50, text_color=self.textColor)
            numberLabel.grid(row = 0, column = 0, sticky="NSWE", pady=15, padx = 15)

            selectedFilesText = customtkinter.CTkEntry(box, width=250, height=50)
            selectedFilesText.grid(row = 0, column = 1, columnspan = 5, sticky="NSWE", pady=15, padx = 15)
        
    def disable_enable_widgets(self, stat):
        
        if stat != "disabled" and stat != "normal":
            stat = stat.get()

        if stat == "disabled":
            self.mode = "one"
        elif stat == "normal":
            self.mode = "multiple"

        self.amountInfoLabel.configure(state = stat)
        self.amountOfFilesSlider.configure(state = stat)
        for child in self.newFilesList.winfo_children():
            for c in child.winfo_children():
                c.configure(state = stat)
            
    def update_frame(self, number):
        l = 0
        for i in self.newFilesList.winfo_children():
            l += 1
            if l <= number:
                i.pack(fill="x")
            else:
                i.pack_forget()                
                for child in i.winfo_children():
                    if isinstance(child, customtkinter.CTkEntry):
                        child.delete(0, END)
                        
                
    def update_slider(self, event):
        amount = self.amountOfFilesSlider.get()
        self.amountInfoLabel.configure(text = "Ile plików chcesz stworzyć: {}".format(str(amount)[:-2]))
        self.update_frame(amount)
        
    def reset_values(self):
        for i in self.newFilesList.winfo_children():
            for child in i.winfo_children():
                if isinstance(child, customtkinter.CTkEntry):
                    child.delete(0, END)
                    
        self.disable_enable_widgets("disabled")
        self.oneCheck.select()
        self.amountOfFilesSlider.set(1)
        self.amountInfoLabel.configure(text = "Ile plików chcesz stworzyć: {}".format(1))
        self.update_frame(1)
        
                        