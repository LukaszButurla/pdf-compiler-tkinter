from tkinter import ttk, END

class Table:
    def __init__(self):
        pass

    def create_table(self, frame):
        self.table = ttk.Treeview(frame, columns="Nazwa", show="headings")
        self.table.heading("#1",text="Ścieżka do pliku")

    def add_files_to_tree(self, files):
        self.clear_tree()
        for file in files:
            self.add_row_to_tree(file)
    
    def add_row_to_tree(self, value):
        self.table.insert("", END, values=value.replace(" ", "_"))

    def delete_row(self):
        row = self.table.selection()
        for r in row:
            self.table.delete(r)

    def clear_tree(self):
        for i in self.table.get_children():
            self.table.delete(i)
