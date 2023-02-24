import customtkinter
from tkinter import ttk, Scrollbar

class HomePage:
    def __init__(self, mainFrame, windowColor, secondColor, textColor, open_info_page):
        self.create_widgets(mainFrame, windowColor, secondColor, textColor, open_info_page)
        self.style_tree()

    def create_widgets(self, mainFrame, windowColor, secondColor, textColor, open_info_page):

#---------------------create frames----------------------------------
        self.homeFrame = customtkinter.CTkFrame(mainFrame, fg_color=windowColor)
        self.homeFrame.grid(sticky = "NSWE")

        buttonsFrame = customtkinter.CTkFrame(self.homeFrame, fg_color=windowColor)
        buttonsFrame.grid(row = 0, column = 0, rowspan = 4, sticky = "NSWE")

        filesLabelFrame = customtkinter.CTkFrame(self.homeFrame, fg_color=windowColor)
        filesLabelFrame.grid(row = 4, column = 0, sticky = "NSWE")

        treeFrame = customtkinter.CTkFrame(self.homeFrame, fg_color=windowColor)
        treeFrame.grid(row = 5, column = 0, rowspan = 20, sticky = "NSWE")

#-------------------configure frames----------------------------
        self.homeFrame.rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.homeFrame.rowconfigure((5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24), weight=2)
        self.homeFrame.columnconfigure(0, weight=1)

        buttonsFrame.columnconfigure((0, 1, 2, 3, 4), weight=1)
        buttonsFrame.rowconfigure(0, weight=1)

        filesLabelFrame.rowconfigure(0, weight=1)
        filesLabelFrame.columnconfigure(0, weight=1)

        treeFrame.rowconfigure(0, weight=1)
        treeFrame.columnconfigure(0, weight=1)



        buttonAdd = customtkinter.CTkButton(master=buttonsFrame, text="Dodaj", width=120, bg_color=windowColor)
        buttonAdd.grid(row = 0, column = 0, sticky = "NSWE", padx = 15, pady = 20)

        buttonEdit = customtkinter.CTkButton(master=buttonsFrame, text="Usuń", width=120, bg_color=windowColor)
        buttonEdit.grid(row = 0, column = 1, sticky = "NSWE", padx = 15, pady = 20)

        buttonCompile = customtkinter.CTkButton(master=buttonsFrame, text="Łącz", width=120, bg_color=windowColor)
        buttonCompile.grid(row = 0, column = 2, sticky = "NSWE", padx = 15, pady = 20)

        buttonSplit = customtkinter.CTkButton(master=buttonsFrame, text="Dziel", width=120, bg_color=windowColor)
        buttonSplit.grid(row = 0, column = 3, sticky = "NSWE", padx = 15, pady = 20)

        buttonInfo = customtkinter.CTkButton(master=buttonsFrame, text="O programie", width=120, bg_color=windowColor, command=open_info_page)
        buttonInfo.grid(row = 0, column = 4, sticky = "NSWE", padx = 15, pady = 20)

        # filesListScroll = Scrollbar(filesLabelFrame)
        # filesListScroll.pack(side="right", fill="y")

        labelListOfFiles = customtkinter.CTkLabel(filesLabelFrame, text="Lista plików:", justify="left", text_color="white", bg_color=windowColor, anchor="w", font = ("Arial", 15))
        labelListOfFiles.grid(row = 0, column = 0, sticky = "NSWE", padx =15)

        self.treeListOfFiles = ttk.Treeview(treeFrame, columns="File", show="headings", selectmode="none")
        self.treeListOfFiles.heading("#1", text="Ścieżka do pliku")
        self.treeListOfFiles.column("#1", minwidth=940)
        self.treeListOfFiles.grid(row=0, column = 0, sticky = "NSWE", padx = 15, pady = 15)

    #     filesListScroll.config(command=self.treeListOfFiles.yview)
    #     # self.infoPage = InfoPage(self.app, windowColor, secondColor, textColor)
    #     # self.files = Files(self.app, self.treeListOfFiles, labelListOfFiles, windowColor, textColor)
    #     # self.split = Split(self.app, self.files, windowColor, secondColor, textColor)
    #     # self.compiler = Compiler(self.files)
    #     # self.edit = Edit(self.app, self.files, windowColor, secondColor, textColor)



    def style_tree(self):
        s = ttk.Style()
        s.theme_use("clam")
        s.configure("Treeview",
                    font = (None, 15),
                    rowheight = 35)      
        s.configure("Treeview.Heading", font=(None, 14))