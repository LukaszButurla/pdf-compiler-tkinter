# from tkinter import Toplevel

# class Edit:
#     def __init__(self, app, compiler):
#         self.compiler = compiler
#         self.window = app

#     def open_edit_window(self):
#         self.editWindow = Toplevel(self.window, background="#242424")
#         self.editWindow.geometry("600x400")

from tkinter import Frame

class Edit:
    def __init__(self, app, compiler):
        self.compiler = compiler
        self.window = app

    def open_edit_window(self):
        self.editWindow = Frame(self.window, background="#242124")
        # self.editWindow.geometry("600x400")
        self.editWindow.pack(fill="both", side="bottom", expand=True)
        print("pack")