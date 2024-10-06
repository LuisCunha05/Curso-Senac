import tkinter as tk
from tkinter import filedialog as fd
import base64

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

import urllib.request
import time

#url = 'https://i.imgur.com/viYn8hR.png'

url = 'https://png.pngtree.com/png-clipart/20240310/original/pngtree-pink-butterfly-flying-png-image_14552374.png'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
req = urllib.request.Request(url, headers=headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read()
    #print(result)
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e.code}")

def binaryDataFromFile(path: str) -> bytes | None:
    """Convert image to binary data"""
    if(path == ''):
        return None

    with open(path, 'rb') as file:
        binaryData = file.read()

    return binaryData

def dataFromUrl(url: str) -> bytes:
    content = urllib.request.urlopen(url)
    return content.read()


root = tk.Tk()
img = tk.PhotoImage(data=result)
root.state('zoomed')

#path = select_file()

#img = tk.PhotoImage(data=binaryDataFromFile(path))
#img = tk.PhotoImage(data=base64.encodebytes(binaryDataFromFile(path)))
tk.Label(root, image=img).pack()


root.mainloop()

