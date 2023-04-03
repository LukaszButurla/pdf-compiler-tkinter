import customtkinter
from gui.home import HomePage
from gui.info import InfoPage
from gui.edit import EditPage
from gui.splitPage import SplitPage
from gui.errorWindow import ErrorWindow

class Ui:
    def __init__(self, app, files, compiler):
        self.files = files
        windowColor = "#072d5e"
        secondColor = "#0f4b99"
        textColor = "white"
        self.create_main_frame(app, windowColor)
        self.homePage = HomePage(self.mainFrame, files, compiler, windowColor, secondColor, textColor, self.open_info_page, self.open_edit_page, self.open_split_page)
        self.infoPage = InfoPage(self.mainFrame, windowColor, secondColor, textColor, self.open_home_page)
        self.editPage = EditPage(self.mainFrame, files, windowColor, secondColor, textColor, self.open_home_page)
        self.splitPage = SplitPage(self.mainFrame, files, windowColor, secondColor, textColor, self.open_home_page, app)
        self.errorWindow = ErrorWindow(app, windowColor, secondColor, textColor)
        app.mainloop()

    def create_main_frame(self, app, windowColor):
        self.mainFrame = customtkinter.CTkFrame(app, fg_color=windowColor, bg_color=windowColor)
        self.mainFrame.grid(sticky = "NSWE")

        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.rowconfigure(0, weight=1)

    def open_info_page(self):
        self.homePage.homeFrame.grid_forget()
        self.infoPage.infoFrame.grid(row = 0, column = 0, sticky = "NSWE")

    def open_edit_page(self):
        self.homePage.homeFrame.grid_forget()
        self.editPage.editFrame.grid(row = 0, column = 0, sticky = "NSWE")
        self.editPage.open_page()

    def open_split_page(self):
        if len(self.files.allFiles) == 1:
            self.splitPage.on_open()
            self.homePage.homeFrame.grid_forget()
            self.splitPage.splitFrame.grid(row= 0, column = 0, sticky = "NSWE")
        else:
            self.errorWindow.open_error_window("Wybierz dokładnie 1 plik")
        

    def open_home_page(self):
        self.infoPage.infoFrame.grid_forget()
        self.editPage.editFrame.grid_forget()
        self.splitPage.splitFrame.grid_forget()
        self.homePage.homeFrame.grid(sticky = "NSWE")
        self.homePage.table.add_files_to_tree(self.homePage.files.allFiles)

    # def open_home_page(self):
    #     self.mainFrame = 