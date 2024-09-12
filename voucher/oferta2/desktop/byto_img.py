import tkinter as tk
from tkinter import filedialog as fd
import io


def select_file():
    filetypes = (
        ('Images', '*.png'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    print(f'valor: {filename}....')
    return filename
    

def binaryDataFromFile(path: str) -> bytes | None:
    """Convert image to binary data"""
    if(path == ''):
        return None

    with open(path, 'rb') as file:
        binaryData = file.read()

    return binaryData

root = tk.Tk()

root.state('zoomed')

path = select_file()

img = tk.PhotoImage(data=binaryDataFromFile(path), format='png')

tk.Label(root, image=img).pack()

root.mainloop()

