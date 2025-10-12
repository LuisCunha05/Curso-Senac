import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry('500x350')
root.title('Cadastrar Algo')
root.configure(background='#282828')

cFrame = tk.Frame(root, padx=20, pady=20, background='#8e8e8e')
cFrame.columnconfigure(0, weight=1)
cFrame.columnconfigure(1, weight=2)
cFrame.columnconfigure(2, weight=1)

def validateCad():
    user = uEntry.get()
    password = pEntry.get()
    cpassword = cpEntry.get()
    #print(user, password, cpassword)
    if(user == '' or len(user) < 5):
        messagebox.showerror('Login Incorreto!', 'O login é muito curto!')
        return
    elif(password == '' or len(password) < 6):
        messagebox.showerror('Senha Invalida!', 'A senha é muito curta!')
        return
    elif(user == password):
        messagebox.showwarning('Senha Invalida!', 'A senha não pode ser igual ao login!')
        return
    elif(password != cpassword):
        messagebox.showerror('Senha Incorreta!', 'As senhas são diferentes!')
        return
    uEntry.delete(0, 'end')
    pEntry.delete(0, 'end')
    cpEntry.delete(0, 'end')
    root.focus()
    messagebox.showinfo('Cadastrado', 'Cadrastro realizado com sucesso!')

#Labels
uLabel = tk.Label(
    cFrame,
    text='Usuário',
    font=("helvitaca", 16),
    justify='left',
    anchor='w',
    background='#8e8e8e'
)
pLabel = tk.Label(
    cFrame,
    text='Senha',
    font=("helvitaca", 16),
    justify='left',
    anchor='w',
    background='#8e8e8e'
)
cpLabel = tk.Label(
    cFrame,
    text='Confirmar Senha',
    font=("helvitaca", 16),
    justify='left',
    anchor='w',
    background='#8e8e8e'
)
uLabel.grid(column=1, row=0, sticky='we')
pLabel.grid(column=1, row=2, sticky='we', pady=(10,0))
cpLabel.grid(column=1, row=4, sticky='we', pady=(10,0))

#Entries
uEntry = tk.Entry(cFrame ,font=("helvitaca", 14))
pEntry = tk.Entry(cFrame ,font=("helvitaca", 14))
cpEntry = tk.Entry(cFrame ,font=("helvitaca", 14))
uEntry.grid(column=1, row=1, sticky='we')
pEntry.grid(column=1, row=3, sticky='we')
cpEntry.grid(column=1, row=5, sticky='we')

#Button
cButton = tk.Button(cFrame, text='Cadastrar', font=("helvitaca", 16), command=validateCad)
cButton.grid(column=1, row=6, pady=20)

cFrame.pack(fill='both', anchor='center', expand=True)

root.mainloop()