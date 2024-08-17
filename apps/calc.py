from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry('500x700')
root.title('Pyculator')
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()