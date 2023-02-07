import tkinter
from tkinter import Frame
import customtkinter
from logic.compiler import Compiler
from logic.edit import Edit
from tkinter import Scrollbar
from tkinter import ttk
from tkinter import END

class MainWindow:
    
    def __init__(self):     
        self.open_app()

    def open_app(self):
        app = customtkinter.CTk()
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        app.geometry("600x400")

        filesLabelFrame = Frame(app)
        filesLabelFrame.place(relx=0.02, rely=0.25, width=720, height=350)

        filesListScroll = Scrollbar(filesLabelFrame)
        filesListScroll.pack(side="right", fill="y")


        labelListOfFiles = customtkinter.CTkLabel(app, text="Lista plików:", justify="left")
        labelListOfFiles.place(relx=0.02, rely=0.15)

        self.treeListOfFiles = ttk.Treeview(filesLabelFrame, columns="File", show="headings", yscrollcommand=filesListScroll.set, selectmode="none")
        self.treeListOfFiles.heading("#1", text="Ścieżka do pliku")
        self.treeListOfFiles.column("#1", minwidth=700)
        self.treeListOfFiles.place(width=700, height=350)

        filesListScroll.config(command=self.treeListOfFiles.yview)
        self.compiler = Compiler(app, self.treeListOfFiles)
        self.edit = Edit(app, self.compiler)

        self.style_tree()

        buttonAdd = customtkinter.CTkButton(master=app, text="Dodaj", command=self.compiler.open_select_file_window)
        buttonAdd.place(relx=0.02, rely=0.05)

        buttonEdit = customtkinter.CTkButton(master=app, text="Usuń", command=self.edit_window)
        buttonEdit.place(relx=0.35, rely=0.05)

        buttonCompile = customtkinter.CTkButton(master=app, text="Łącz", command=self.compiler.mergePdf)
        buttonCompile.place(relx=0.67, rely=0.05)
        app.mainloop()

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
