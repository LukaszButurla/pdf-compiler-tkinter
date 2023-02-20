from tkinter import filedialog as fd
from tkinter import END
from logic.windowAskSameFile import WindowAskSameFile

class Files:

    def __init__(self, window, filesTree, filesLabel, color, textColor):
        self.allFiles = []
        self.window = window
        self.tree = filesTree
        self.filesLabel = filesLabel
        self.windowAskSameFile = WindowAskSameFile(self, color, textColor)


    def open_select_file_window(self):
        selectedFiles = fd.askopenfilenames(filetypes=[("PDF", ".pdf")])
        sameFiles = []
        for file in selectedFiles:
            if file not in self.allFiles:
                self.allFiles.append(file)
            else:
                sameFiles.append(file) 

        if len(sameFiles) > 0:                
            self.windowAskSameFile.open_window(self.window, sameFiles)

        self.add_files_to_tree()


    def add_files_to_tree(self):
        self.clear_tree()
        for file in self.allFiles:
            self.add_row_to_tree(file)
        self.filesLabel.configure(text = "Lista plików: {}".format(len(self.allFiles)))

    def add_row_to_tree(self, value):
        self.tree.insert("", END, values=value.replace(" ", "_"))

    def clear_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

    def add_file_from_window(self, file):
        for f in file:
            self.allFiles.append(f)
        self.add_files_to_tree()