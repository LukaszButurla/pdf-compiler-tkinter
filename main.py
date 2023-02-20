import tkinter
from tkinter import Frame
import customtkinter
from logic.compiler import Compiler
from logic.split import Split
from logic.edit import Edit
from logic.files import Files
from Ui.info import InfoPage
from tkinter import Scrollbar
from tkinter import ttk
from tkinter import END
from functools import partial

class MainWindow:
    
    def __init__(self):     
        self.open_app()

    def open_app(self):

        windowColor = "#072d5e"
        secondColor = "#0f4b99"
        textColor = "white"
        self.app = customtkinter.CTk()
        self.app.title("Łącznik pdf")
        # customtkinter.set_appearance_mode("dark")
        # customtkinter.set_default_color_theme("blue")
        self.app.geometry("800x400")
        self.app.config(bg=windowColor)
        self.app.resizable(False, False)

        filesLabelFrame = Frame(self.app)
        filesLabelFrame.place(relx=0.02, rely=0.25, width=960, height=350)

        filesListScroll = Scrollbar(filesLabelFrame)
        filesListScroll.pack(side="right", fill="y")


        labelListOfFiles = customtkinter.CTkLabel(self.app, text="Lista plików:", justify="left", text_color="white", bg_color=windowColor)
        labelListOfFiles.place(relx=0.02, rely=0.15)

        self.treeListOfFiles = ttk.Treeview(filesLabelFrame, columns="File", show="headings", yscrollcommand=filesListScroll.set, selectmode="none")
        self.treeListOfFiles.heading("#1", text="Ścieżka do pliku")
        self.treeListOfFiles.column("#1", minwidth=940)
        self.treeListOfFiles.place(width=940, height=350)

        filesListScroll.config(command=self.treeListOfFiles.yview)
        self.infoPage = InfoPage(self.app, windowColor, secondColor, textColor)
        self.files = Files(self.app, self.treeListOfFiles, labelListOfFiles, windowColor, textColor)
        self.split = Split(self.app, self.files, windowColor, secondColor, textColor)
        self.compiler = Compiler(self.files)
        self.edit = Edit(self.app, self.files, windowColor, secondColor, textColor)

        self.style_tree()

        buttonAdd = customtkinter.CTkButton(master=self.app, text="Dodaj", command=self.files.open_select_file_window, width=120, bg_color=windowColor)
        buttonAdd.place(relx=0.02, rely=0.05)

        buttonEdit = customtkinter.CTkButton(master=self.app, text="Usuń", command=self.edit_window, width=120, bg_color=windowColor)
        buttonEdit.place(relx=0.22, rely=0.05)

        buttonCompile = customtkinter.CTkButton(master=self.app, text="Łącz", command = self.compiler.mergePdf, width=120, bg_color=windowColor)
        buttonCompile.place(relx=0.42, rely=0.05)

        buttonSplit = customtkinter.CTkButton(master=self.app, text="Dziel", command=self.split.open_split_file, width=120, bg_color=windowColor)
        buttonSplit.place(relx=0.62, rely=0.05)

        buttonInfo = customtkinter.CTkButton(master=self.app, text="O programie", command=self.infoPage.open_page, width=120, bg_color=windowColor)
        buttonInfo.place(relx = 0.82, rely = 0.05)


        self.app.mainloop()

    def style_tree(self):
        s = ttk.Style()
        s.theme_use("clam")
        s.configure("Treeview",
                    font = (None, 15),
                    rowheight = 35)      
        s.configure("Treeview.Heading", font=(None, 14))
        

    def edit_window(self):
        self.edit.open_edit_window()

    
    

if __name__ == "__main__":
    MainWindow()
