from tkinter import filedialog as fd

class Compiler:
    def __init__(self, labelFileList):
        self.allFiles = []
        self.labelFileList = labelFileList
        print(self.labelFileList)

    def open_select_file_window(self):
        selectedFiles = fd.askopenfilenames()
        for file in selectedFiles:
            self.allFiles.append(file)
        self.set_label_name()
        print(self.allFiles)
        print(selectedFiles)

    def set_label_name(self):
        txt = "Lista plików:\n"
        for file in self.allFiles:
            txt += "{}\n".format(file)

        self.labelFileList.configure(text=txt)

    