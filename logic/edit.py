import customtkinter
from tkinter import Frame, ttk, END, Scrollbar

class Edit:
    def __init__(self, mainFrame, files, color, secondColor, textColor, open_home_page):
        self.files = files
        self.color = color
        self.secondColor = secondColor
        self.textColor = textColor
        self.create_widgets(mainFrame, open_home_page)

    def create_widgets(self, mainFrame, open_home_page):
#-------------------create frames-----------------------------
        editFrame = customtkinter.CTkFrame(mainFrame, fg_color=self.color)

#------------------configure frames--------------------------
        editFrame.rowconfigure((0,1), weight=1)
        editFrame.rowconfigure(1, weight=1)
        editFrame.columnconfigure((0,1,2), weight=1)

#------------------create widgets----------------------------
        infoLabel = customtkinter.CTkLabel(self.editWindow, text="Wybierz pliki do usunięcia z listy", text_color=self.textColor)
        infoLabel.grid(row = 0, column = 0, columnspan = 3, sticky = "NSWE")

    def open_edit_window(self):
        self.editWindow = Frame(self.window, background=self.color)
        self.editWindow.pack(fill="both", side="bottom", expand=True)
        self.add_widgets()
        self.add_column(self.files.allFiles)

    def add_widgets(self):
        buttonCancel = customtkinter.CTkButton(self.editWindow, text="Anuluj", command=self.close_window, bg_color=self.color)
        buttonCancel.place(relx=0.65, rely=0.85)

        buttonAgree = customtkinter.CTkButton(self.editWindow, text="Potwierdź", command=self.save_changes, bg_color=self.color)
        buttonAgree.place(relx=0.4, rely=0.85)

        buttonDelete = customtkinter.CTkButton(self.editWindow, text="Usuń", bg_color=self.color)
        buttonDelete.place(relx=0.15, rely=0.85)

        

        self.create_table()

    def delete_row(self):
        row = self.table.selection()
        for r in row:
            self.table.delete(r)

    def save_changes(self):
        selectedFiles = []
        for row in self.table.get_children():
            selectedFiles.append(self.table.item(row)["values"][0])

        self.files.allFiles = selectedFiles
        self.files.add_files_to_tree()

        self.close_window()
    
    def create_table(self):
        tableFrame = Frame(self.editWindow)
        tableFrame.place(relx=0.02, rely=0.13, width=960, height=330)

        tableScroll = Scrollbar(tableFrame)
        tableScroll.pack(side="right", fill="y")

        self.table = ttk.Treeview(tableFrame, columns="Nazwa", show="headings", yscrollcommand=tableScroll.set)
        tableScroll.config(command=self.table.yview)
        self.table.heading("#1",text="Nazwa")
        self.table.place(width=940, height=330)

    def close_window(self):
        self.editWindow.destroy()
        

    def add_column(self, files):
        print(self.files.allFiles)
        for f in files:
            f = f.replace(" ", "_")
            self.table.insert("", END, values=f)

    
