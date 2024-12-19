import tkinter as tk
from tkinter import filedialog

class File:
    def __init__(self):
        self.filePath = None

    def saveFile(self):
        """
        Opens a save file dialog that allows the user to select a directory and enter a file name
        """
        root = tk.Tk()
        root.withdraw()

        options = {
            'defaultextension': '.png',
            'filetypes': [('image files', '*.png')],
            'initialdir': 'C:\\',
            'title': 'Save as...'
        }

        self.filePath = filedialog.asksaveasfilename(**options)

        if not self.filePath:
            print("No file was selected.")
            return
        
        try:
            with open(self.filePath, 'w') as file:
                pass
            print(f"File saved: {self.filePath}")
        except Exception as e:
            print(f"Failed ot save the file: {e}")