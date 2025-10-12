import tkinter as tk

def changeColor(object: tk.Frame, color: str) -> None:
    object.configure(background=color)

root = tk.Tk()
root.geometry('500x600')
root.resizable(width=False, height=False)
root.title('Rainbow Button')
root.configure(background='#282828')


rFrame = tk.Frame()#background="#e5f1f7"

rButton = tk.Button(rFrame, text='Red', font=('Helvetica', 16), background='#dc052d', fg='#ffffff', command= lambda: changeColor(root, '#dc052d'))
bButton = tk.Button(rFrame, text='Blue', font=('Helvetica', 16), background='#2432e2', fg='#ffffff', command= lambda: changeColor(root, '#2432e2'))
gButton = tk.Button(rFrame, text='Green', font=('Helvetica', 16), background='#adf705', fg='#ffffff', command= lambda: changeColor(root, '#adf705'))

rButton.pack(side='left', padx=30)
bButton.pack(side='right', padx=30)
gButton.pack(side='right', padx=30, pady=30)

rFrame.pack(padx=20,pady=20)

root.mainloop()