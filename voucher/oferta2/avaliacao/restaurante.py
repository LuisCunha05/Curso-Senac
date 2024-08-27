"""O desafio consiste em criar uma (ou mais telas) para um sistemas de pedido do restaurante do Ederson.
Para começar o sistema, é solicitado que ele digite um usuário e uma senha, a senha deve ser confirmada em um campo com confirmação de senha e deve seguir as mesmas normas do exercício anterior.
Depois do login deve ser possível ao usuário entrar na tela inicial onde ele pode começar o processo para fazer seus pedidos, na tela inicial deve conter a mensagem "Olá, {nome_usuário}" e abaixo as opções do restaurante, as opções possíveis são: entradas, pratos principais, bebidas, bebidas alcoólicas, sobremesas, menu do chef.
Cada botão que a pessoa clicar deve redirecionar a tela para o campo com opções variadas de produtos (no mínimo 5) para ser selecionada pelo usuário, a pessoa pode adicionar tudo no pedido dela clicando em um botão para adicionar ao pedido (use a criatividade para criar esse botão) e ao final da tela deve ter a opção de finalizar o pedido para que a pessoa possa visualizar tudo o que foi colocado no carrinho até agora e confirme se está tudo certo, caso esteja ela envia o pedido a cozinha, e finaliza o sistema com uma imagem divertida, caso não ela deve ter a opção de acrescentar mais itens ao pedido ou retirar os mesmos que já estejam lá."""

import tkinter as tk
from tkinter import messagebox
from collections import abc as t


def setGeometry(master:tk.Tk, scale:float = 0.7, width:int = None, height:int = None,x:int = None, y:int = None, resizable:bool = True):
    """Sets the window size and put it at center of the screen, by default uses 70% of the screen.
    If WIDTH or HEIGHT are given than uses this values instead."""
    width = width if width else int(master.winfo_screenwidth() * scale)
    height = height if height else int(master.winfo_screenheight() * scale)
    x = x if x else int((master.winfo_screenwidth() - width) / 2)
    y = y if y else int((master.winfo_screenheight() - height) / 2)

    master.geometry(f'{width}x{height}+{x}+{y}')
    master.resizable(resizable, resizable)

def addButton(origin: tk.Frame, b_kwargs: dict = {}, p_kwargs: dict = {}) -> tk.Button:
    button = tk.Button(origin, **b_kwargs)
    button.pack(**p_kwargs)
    return button

def addFrame(origin: tk.Frame, f_kwargs: dict = {}, p_kwargs: dict = {}) -> tk.Frame:
    frame = tk.Frame(origin, **f_kwargs)
    frame.pack(**p_kwargs)
    return frame

def addLabel(origin: tk.Frame, l_kwargs: dict = {}, p_kwargs: dict = {}) -> tk.Label:
    label = tk.Label(origin, **l_kwargs)
    label.pack(**p_kwargs)
    return label

def addEntry(origin: tk.Frame, e_kwargs: dict = {}, p_kwargs: dict = {}) -> tk.Entry:
    entry = tk.Entry(origin, **e_kwargs)
    entry.pack(**p_kwargs)
    return entry

def deleteChildren(object: tk.Tk | tk.Frame):
    for child in object.winfo_children():
        child.destroy()



class Cardapio:
    def __init__(self) -> None:
        self.root = tk.Tk()
        setGeometry(self.root, width=1920, height=1000)
        self.root.minsize(width=1920, height=1000)
        self.root.title('The Menu')
        #self.root.configure(background='#edb3b0')

        #Loading Assets
        self._assets = {
        'house':tk.PhotoImage(file='assets\\house.png'),
        'banner':tk.PhotoImage(file='assets\\banner.png'),
        'cart':tk.PhotoImage(file='assets\\cart.png'),
        'entrada':tk.PhotoImage(file='assets\\entrada.png'),
        'bebidas':tk.PhotoImage(file='assets\\bebidas.png'),
        'alcool':tk.PhotoImage(file='assets\\alcool.png'),
        'pp':tk.PhotoImage(file='assets\\pp.png'),
        'sobremesa':tk.PhotoImage(file='assets\\sobremesa.png'),
        'chef':tk.PhotoImage(file='assets\\chef.png'),
        'add_cart':tk.PhotoImage(file='assets\\add_cart.png'),
        'feijoada':tk.PhotoImage(file='assets\\feijoada.png'),
        }

        #Header config
        self._header = addFrame(self.root, {'background':'#f2c6c4'}, { 'fill':'x', 'anchor':'n'})
        self._homeB = addLabel(self._header, {'image':self._assets['house'], 'borderwidth':0}, {'padx':(150,0), 'side':'left'})
        self._homeB.pack_forget()
        self._banner = addLabel(self._header, {'image':self._assets['banner'], 'borderwidth':0, 'background':'#f2c6c4'}, {'fill':'x', 'side':'left', 'anchor':'n', 'expand':True})
        self._cartB = addLabel(self._header, {'image':self._assets['cart'], 'borderwidth':0}, {'padx':(0,150), 'side':'right', 'anchor':'e'})
        self._cartB.pack_forget()
        self.content = addFrame(self.root, {'background':'#edb3b0'}, {'fill':'both', 'expand':True })

        self.login()
        self.root.mainloop()


    def home(self):
        self._homeB.pack(padx=(150,0), side='left')
        self._banner.pack(fill='x', side='left', anchor='n', expand=True)
        self._cartB.pack(padx=(0,150), side='right', anchor='e')
        deleteChildren(self.content)
        print('yyoooooooooooooooooooooooooooooooo')

    def login(self):
        #Left Image
        addLabel(self.content, {'image':self._assets['feijoada'], 'borderwidth':0}, {'padx':(150,0), 'side':'left'})

        #login elements
        holderLogin = addFrame(self.content, {'background':'white', 'width':400}, {'padx':(0,150), 'side':'right', 'anchor':'e'})#Frame
        addLabel(holderLogin, {'background':'white', 'text':'Usuário', 'font':('Helvetica', 24), 'anchor':'w', 'justify':'left'}, {'padx':15, 'pady':(15,0), 'fill':'x'})#Label User
        self.uEntry = addEntry(holderLogin, {'font':('Helvetica', 24)}, {'padx':15, 'fill':'x'})#Entry User
        addLabel(holderLogin, {'background':'white', 'text':'Senha', 'font':('Helvetica', 24), 'anchor':'w', 'justify':'left'}, {'padx':15, 'pady':(20,0), 'fill':'x'})#Label Password
        self.pEntry = addEntry(holderLogin, {'font':('Helvetica', 24)}, {'padx':15, 'fill':'x'})#Entry Password
        self.pEntry.config(show='*')
        addLabel(holderLogin, {'background':'white', 'text':'Confirmar Senha', 'font':('Helvetica', 24), 'anchor':'w', 'justify':'left'}, {'padx':15,'pady':(20,0), 'fill':'x'})#Label Password Confirmation
        self.cpEntry = addEntry(holderLogin, {'font':('Helvetica', 24)}, {'padx':15, 'fill':'x'})#Entry Password Confirmation
        self.cpEntry.config(show='*')
        addButton(holderLogin, {'text':'Entrar', 'font':('Helvetica', 24),'fg':'white', 'background':'#444444','highlightthickness':3, 'highlightbackground':'#727272',
                                'command': lambda: validateCad(self, self.uEntry, self.pEntry, self.cpEntry)}, {'pady': (40,15)})
        #tk.Entry(borderwidth=)

def validateCad(object: Cardapio, uEntry:tk.Entry, pEntry:tk.Entry, cpEntry:tk.Entry):
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
    object.root.focus()
    object._banner.pack_forget()
    object.home()
    #messagebox.showinfo('Cadastrado', 'Cadrastro realizado com sucesso!')

if __name__ == '__main__':
    Cardapio()

