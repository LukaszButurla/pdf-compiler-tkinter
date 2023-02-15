class Split:
    def __init__(self, files):
        self.files = files

    def split_file(self):
        if len(self.files.allFiles) == 1:
            print("split")
        else:
            print("Wybierz tylko jeden plik")