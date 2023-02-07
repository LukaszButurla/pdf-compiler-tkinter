from tkinter import Frame

class InfoPage:

    def __init__(self, window):
        self.window = window

    def open_page(self):
        self.page = Frame(self.window, background="#242124")
        self.page.pack(fill="both", expand=True)