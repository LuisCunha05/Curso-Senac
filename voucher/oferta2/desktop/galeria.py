import tkinter as tk
from tkinter import PhotoImage



def addDesc(label: tk.Label, entry: tk.Entry, uText: str)-> None:
    label.configure(text=uText)
    entry.delete(0, 'end')
    root.focus()

root = tk.Tk()
root.geometry('1280x720')
root.title('Galeria')

catList = [
    PhotoImage(file='c1.png').zoom(10).subsample(25),
    PhotoImage(file='c2.png').zoom(10).subsample(25),
    PhotoImage(file='c3.png').zoom(10).subsample(25),
    PhotoImage(file='c4.png').zoom(10).subsample(25),
    PhotoImage(file='c5.png').zoom(10).subsample(25)
]

container = tk.Frame(root, background='gray')
canvas = tk.Canvas(container)
scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollFrame = tk.Frame(canvas, padx=10)

scrollFrame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollFrame, anchor="center")

canvas.configure(yscrollcommand=scrollbar.set)


cat1 = tk.Label(scrollFrame,image=catList[0])
c1Label = tk.Label(scrollFrame, text='Adicione uma descrição:', font=('Helvetica', 14))
c1Entry = tk.Entry(scrollFrame, font=('Helvetica', 14))
c1B = tk.Button(scrollFrame, font=('Helvetica', 12), text='Adicionar descrição', command= lambda: addDesc(c1Label, c1Entry, c1Entry.get()))
cat1.pack()
c1Label.pack()
c1Entry.pack()
c1B.pack()

cat2 = tk.Label(scrollFrame,image=catList[1])
c2Label = tk.Label(scrollFrame, text='Adicione uma descrição:', font=('Helvetica', 14))
c2Entry = tk.Entry(scrollFrame, font=('Helvetica', 14))
c2B = tk.Button(scrollFrame, font=('Helvetica', 12), text='Adicionar descrição', command= lambda: addDesc(c2Label, c2Entry, c2Entry.get()))
cat2.pack()
c2Label.pack()
c2Entry.pack()
c2B.pack()

cat3 = tk.Label(scrollFrame,image=catList[2])
c3Label = tk.Label(scrollFrame, text='Adicione uma descrição:', font=('Helvetica', 14))
c3Entry = tk.Entry(scrollFrame, font=('Helvetica', 14))
c3B = tk.Button(scrollFrame, font=('Helvetica', 12), text='Adicionar descrição', command= lambda: addDesc(c3Label, c3Entry, c3Entry.get()))
cat3.pack()
c3Label.pack()
c3Entry.pack()
c3B.pack()

cat4 = tk.Label(scrollFrame,image=catList[3])
c4Label = tk.Label(scrollFrame, text='Adicione uma descrição:', font=('Helvetica', 14))
c4Entry = tk.Entry(scrollFrame, font=('Helvetica', 14))
c4B = tk.Button(scrollFrame, font=('Helvetica', 12), text='Adicionar descrição', command= lambda: addDesc(c4Label, c4Entry, c4Entry.get()))
cat4.pack()
c4Label.pack()
c4Entry.pack()
c4B.pack()

cat5 = tk.Label(scrollFrame,image=catList[4])
c5Label = tk.Label(scrollFrame, text='Adicione uma descrição:', font=('Helvetica', 14))
c5Entry = tk.Entry(scrollFrame, font=('Helvetica', 14))
c5B = tk.Button(scrollFrame, font=('Helvetica', 12), text='Adicionar descrição', command= lambda: addDesc(c5Label, c5Entry, c5Entry.get()))
cat5.pack()
c5Label.pack()
c5Entry.pack()
c5B.pack()

container.pack(padx=10, pady=10, fill='both', expand=True)
canvas.pack(side="left", fill="both", expand=True, padx=300)
scrollbar.pack(side="right", fill="y")

root.mainloop()