import customtkinter
from gui.home import HomePage
from gui.info import InfoPage

class Ui:
    def __init__(self, app):
        windowColor = "#072d5e"
        secondColor = "#0f4b99"
        textColor = "white"
        self.create_main_frame(app, windowColor)
        self.homePage = HomePage(self.mainFrame, windowColor, secondColor, textColor, self.open_info_page)
        self.infoPage = InfoPage(self.mainFrame, windowColor, secondColor, textColor, self.open_home_page)
        app.mainloop()

    def create_main_frame(self, app, windowColor):
        self.mainFrame = customtkinter.CTkFrame(app, fg_color=windowColor, bg_color=windowColor)
        self.mainFrame.grid(sticky = "NSWE")

        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.rowconfigure(0, weight=1)

    def open_info_page(self):
        self.homePage.homeFrame.grid_forget()
        self.infoPage.infoFrame.grid(row = 0, column = 0, sticky = "NSWE")

    def open_home_page(self):
        self.homePage.homeFrame.grid_forget()
        self.infoPage.infoFrame.grid_forget()
        self.homePage.homeFrame.grid(sticky = "NSWE")

    # def open_home_page(self):
    #     self.mainFrame = 