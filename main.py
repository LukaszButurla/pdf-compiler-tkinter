import tkinter
import customtkinter

class MainWindow:
    
    def __init__(self):      
        self.open_app()

    def open_app(self):
        app = customtkinter.CTk()
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        app.geometry("400x400")

        buttonAdd = customtkinter.CTkButton(master=app, text="Dodaj")
        buttonAdd.place(relx=0.02, rely=0.05)
        labelListOfFiles = customtkinter.CTkLabel(master=app, text="Lista plików:")
        labelListOfFiles.place(relx=0.02, rely=0.15)
        app.mainloop()

if __name__ == "__main__":
    MainWindow()
