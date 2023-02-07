import tkinter
from tkinter import Frame
import customtkinter
from logic.compiler import Compiler
from logic.edit import Edit
from Ui.info import InfoPage
from tkinter import Scrollbar
from tkinter import ttk
from tkinter import END

class MainWindow:
    
    def __init__(self):     
        self.open_app()

    def open_app(self):

        windowColor = "#072d5e"
        secondColor = "#0f4b99"
        textColor = "white"
        self.app = customtkinter.CTk()
        # customtkinter.set_appearance_mode("dark")
        # customtkinter.set_default_color_theme("blue")
        self.app.geometry("600x400")
        self.app.config(bg=windowColor)

        filesLabelFrame = Frame(self.app)
        filesLabelFrame.place(relx=0.02, rely=0.25, width=720, height=350)

        filesListScroll = Scrollbar(filesLabelFrame)
        filesListScroll.pack(side="right", fill="y")


        labelListOfFiles = customtkinter.CTkLabel(self.app, text="Lista plików:", justify="left", text_color="white", bg_color=windowColor)
        labelListOfFiles.place(relx=0.02, rely=0.15)

        self.treeListOfFiles = ttk.Treeview(filesLabelFrame, columns="File", show="headings", yscrollcommand=filesListScroll.set, selectmode="none")
        self.treeListOfFiles.heading("#1", text="Ścieżka do pliku")
        self.treeListOfFiles.column("#1", minwidth=700)
        self.treeListOfFiles.place(width=700, height=350)

        filesListScroll.config(command=self.treeListOfFiles.yview)
        self.compiler = Compiler(self.app, self.treeListOfFiles, labelListOfFiles)
        self.edit = Edit(self.app, self.compiler, windowColor, secondColor, textColor)
        self.infoPage = InfoPage(self.app, windowColor, secondColor, textColor)

        self.style_tree()

        buttonAdd = customtkinter.CTkButton(master=self.app, text="Dodaj", command=self.compiler.open_select_file_window, width=120, bg_color=windowColor)
        buttonAdd.place(relx=0.02, rely=0.05)

        buttonEdit = customtkinter.CTkButton(master=self.app, text="Usuń", command=self.edit_window, width=120, bg_color=windowColor)
        buttonEdit.place(relx=0.27, rely=0.05)

        buttonCompile = customtkinter.CTkButton(master=self.app, text="Łącz", command=self.compiler.mergePdf, width=120, bg_color=windowColor)
        buttonCompile.place(relx=0.52, rely=0.05)

        buttonInfo = customtkinter.CTkButton(master=self.app, text="O programie", command=self.infoPage.open_page, width=120, bg_color=windowColor)
        buttonInfo.place(relx = 0.77, rely = 0.05)
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
