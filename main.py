import tkinter
import customtkinter

app = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
app.geometry("400x400")

buttonAdd = customtkinter.CTkButton(master=app, text="Dodaj")
buttonAdd.place(relx=0.5, rely=0.5)
labelListOfFiles = customtkinter.CTkLabel(master=app, text="Lista plików:")
labelListOfFiles.place(relx=0.5, rely=0.3)

app.mainloop()