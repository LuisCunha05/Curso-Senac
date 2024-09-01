"""O desafio consiste em criar uma (ou mais telas) para um sistemas de pedido do restaurante do Ederson.
Para começar o sistema, é solicitado que ele digite um usuário e uma senha, a senha deve ser confirmada em um campo com confirmação de senha e deve seguir as mesmas normas do exercício anterior.
Depois do login deve ser possível ao usuário entrar na tela inicial onde ele pode começar o processo para fazer seus pedidos, na tela inicial deve conter a mensagem "Olá, {nome_usuário}" e abaixo as opções do restaurante, as opções possíveis são: entradas, pratos principais, bebidas, bebidas alcoólicas, sobremesas, menu do chef.
Cada botão que a pessoa clicar deve redirecionar a tela para o campo com opções variadas de produtos (no mínimo 5) para ser selecionada pelo usuário, a pessoa pode adicionar tudo no pedido dela clicando em um botão para adicionar ao pedido (use a criatividade para criar esse botão) e ao final da tela deve ter a opção de finalizar o pedido para que a pessoa possa visualizar tudo o que foi colocado no carrinho até agora e confirme se está tudo certo, caso esteja ela envia o pedido a cozinha, e finaliza o sistema com uma imagem divertida, caso não ela deve ter a opção de acrescentar mais itens ao pedido ou retirar os mesmos que já estejam lá."""

import tkinter as tk
from assets import Assets
from tkinter import messagebox
#from collections import abc as t
from typing import Tuple



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

def addLabelP(origin: tk.Frame, l_kwargs: dict = {}, pl_kwargs: dict = {}) -> tk.Label:
    label = tk.Label(origin, **l_kwargs)
    label.place(**pl_kwargs)
    return label

def addEntry(origin: tk.Frame, e_kwargs: dict = {}, p_kwargs: dict = {}) -> tk.Entry:
    entry = tk.Entry(origin, **e_kwargs)
    entry.pack(**p_kwargs)
    return entry

def forgetChildren(object: tk.Tk | tk.Frame):
    for child in object.winfo_children():
        child.pack_forget()

def addProdFrame(frame: tk.Tk | tk.Frame, name: str, price:float, img: tk.PhotoImage, cart: tk.PhotoImage, kargs :dict= {}) -> Tuple[tk.Frame, tk.Label, tk.Label]:
    pFrame = tk.Frame(frame, width=389, height=314, background='white')
    pFrame.pack(**kargs)

    pImgFrame = tk.Frame(pFrame)
    pImgFrame.pack(anchor='n')

    pImg = tk.Label(pImgFrame, image=img, borderwidth=0)
    pImg.pack()

    pTextFrame = tk.Frame(pFrame, background='white')
    pTextFrame.pack(fill='x', padx=4, pady=4)

    pName = tk.Label(pTextFrame, text=name, font=Assets.FONT_S, background='white', foreground=Assets.COLOR['text'], justify='left', anchor='w', wraplength=205)
    pName.pack(side='left', fill='x', anchor='w', expand=1)

    pAddCart = tk.Label(pTextFrame, image=cart, borderwidth=0)
    pAddCart.pack(side='right')

    pPrice = tk.Label(pTextFrame, text=f'R${price:.2f}', font=Assets.FONT_M, background='white', foreground=Assets.COLOR['text'], justify='right')
    pPrice.pack(side='right')

    return (pFrame, pImg, pAddCart)


class Cardapio:
    
    def __init__(self) -> None:
        self.root = tk.Tk()
        setGeometry(self.root, width=1920, height=1000)
        self.root.minsize(width=1920, height=1000)
        self.root.title('The Menu')
        self.root.state('zoomed')
        #self.root.configure(background='#edb3b0')

        #Loading Assets
        self.__assets = {
            'login':{
                'imgHouse':tk.PhotoImage(file=Assets.LOGIN['house']),
                'imgBanner':tk.PhotoImage(file=Assets.LOGIN['banner']),
                'imgCart':tk.PhotoImage(file=Assets.LOGIN['cartI']),
                'imgFeijoada':tk.PhotoImage(file=Assets.LOGIN['feijoada']),
            }
        }

        #Header config
        self._header = addFrame(self.root, {'background':Assets.COLOR['nav']}, { 'fill':'x', 'anchor':'n'})
        self._homeB = addLabel(self._header, {'image':self.__assets['login']['imgHouse'], 'borderwidth':0}, {'padx':(150,0), 'side':'left'})
        self._homeB.pack_forget()
        self._banner = addLabel(self._header, {'image':self.__assets['login']['imgBanner'], 'borderwidth':0, 'background':'#f2c6c4'}, {'fill':'x', 'side':'left', 'anchor':'n', 'expand':True})
        self._cartB = addLabel(self._header, {'image':self.__assets['login']['imgCart'], 'borderwidth':0}, {'padx':(0,150), 'side':'right', 'anchor':'e'})
        self._cartB.pack_forget()
        self.content = addFrame(self.root, {'background':'#edb3b0'}, {'fill':'both', 'expand':True })

        self.login()
        self.root.mainloop()

    def entrada(self):
        forgetChildren(self.content)

        addLabel(self.content, {'font':Assets.FONT_G, 'text':f'Olá, {self.user} e abaixo as opções de entrada:', 'background':'#edb3b0', 'fg':'#626262'},
                                {'fill':'x', 'padx':150, 'anchor':'center'})
        
        self.e_assets = Assets.getPhotoImagesFromCat(category='entrada')

        self.pT1 = self.e_assets[Assets.ENTRADA[0]['name']]
        self.pTC = tk.PhotoImage(file=Assets.CART)#'Texto de Teste Grande e Maior que deveria' Assets.ENTRADA[0]['name']
        self.pTestF, self.pTestL, self.PTestC = addProdFrame(self.content, Assets.ENTRADA[0]['name'], Assets.ENTRADA[0]['price'], self.pT1, self.pTC, {'anchor':'center'})
        #hEntrada = addFrame(self.content, {'background':'#F9B97D', 'width':1267, 'height':668}, {'anchor':'n', 'pady':20})
#
        #linha1 = addFrame(hEntrada, {'background':'#F9B97D'}, {'fill':'x', 'pady':(10,0)})
        #linha1.columnconfigure(0, weight=1)
        #linha1.columnconfigure(1, weight=1)
        #linha1.columnconfigure(2, weight=1)
#
        #self._mg1 = tk.Label(linha1, image=Assets.HOME['entrada'], borderwidth=0)
        #self._mg1.grid(column=0, row=0, padx=(10,0))
        #self._mg1.bind("<Button-1>", lambda e: self.entrada())
        #tk.Label(linha1, text='Entrada', font=('Helvetica', 18), fg=Assets.COLOR['text'] ).grid(column=0, row=1, padx=(10,0), sticky='we')
#
        #self._mg2 = tk.Label(linha1, image=Assets.HOME['entrada'], borderwidth=0)
        #self._mg2.grid(column=1, row=0, padx=40)
        #self._mg2.bind("<Button-1>", lambda e: print('yo2'))
        #tk.Label(linha1, text='Prato Principal', font=('Helvetica', 18), fg=Assets.COLOR['text'] ).grid(column=1, row=1, padx=40, sticky='we')
#
        #self._mg3 = tk.Label(linha1, image=Assets.HOME['entrada'], borderwidth=0)
        #self._mg3.grid(column=2, row=0, padx=(0,10))
        #self._mg3.bind("<Button-1>", lambda e: print('yo3'))
        #tk.Label(linha1, text='Bebidas', font=('Helvetica', 18), fg=Assets.COLOR['text'] ).grid(column=2, row=1, padx=(0,10), sticky='we')
#
        #linha2 = addFrame(hEntrada, {'background':'#F9B97D'}, {'fill':'x', 'pady':(20,10)})
        #linha2.columnconfigure(0, weight=1)
        #linha2.columnconfigure(1, weight=1)
        #linha2.columnconfigure(2, weight=1)
#
        #self._mg4 = tk.Label(linha2, image=Assets.HOME['entrada'], borderwidth=0, text='text' )
        #self._mg4.grid(column=0, row=0, padx=(10,0))
        #self._mg4.bind("<Button-1>", lambda e: print('yo4'))
        #tk.Label(linha2, text='Bebidas Alcoólicas', font=('Helvetica', 18), fg=Assets.COLOR['text'] ).grid(column=0, row=1, padx=(10,0), sticky='we')

        #self._mg5 = tk.Label(linha2, image=Assets.HOME['entrada'], borderwidth=0)
        #self._mg5.grid(column=1, row=0, padx=40)
        #self._mg5.bind("<Button-1>", lambda e: print('yo5'))
        #tk.Label(linha2, text='Sobremesas', font=('Helvetica', 18), fg=Assets.COLOR['text'] ).grid(column=1, row=1, padx=40, sticky='we')
#
        #self._mg6 = tk.Label(linha2, image=Assets.HOME['entrada'], borderwidth=0)
        #self._mg6.grid(column=2, row=0, padx=(0,10))
        #self._mg6.bind("<Button-1>", lambda e: print('yo6'))
        #tk.Label(linha2, text='Menu do Chef', font=('Helvetica', 18), fg=Assets.COLOR['text'] ).grid(column=2, row=1, padx=(0,10), sticky='we')

    def home(self):
        #Loading Assets

        self.__assets.update({
            'home':{
                'entrada':tk.PhotoImage(file=Assets.HOME['entrada']),
                'bebidas':tk.PhotoImage(file=Assets.HOME['bebidas']),
                'alcool':tk.PhotoImage(file=Assets.HOME['alcool']),
                'pp':tk.PhotoImage(file=Assets.HOME['pp']),
                'sobremesa':tk.PhotoImage(file=Assets.HOME['sobremesa']),
                'chef':tk.PhotoImage(file=Assets.HOME['chef'])
            }
        })

        #Repack the header in correct order
        if(not self._homeB.winfo_viewable()):
            self._homeB.pack(padx=(150,0), side='left')
            self._homeB.bind('<Button-1>', lambda e: self.home())
            self._banner.pack(fill='x', side='left', anchor='n', expand=True)
            self._cartB.pack(padx=(0,150), side='right', anchor='e')

        #Forget all elements inside content 
        forgetChildren(self.content)

        #Add new elements
        addLabel(self.content, {'font':Assets.FONT_G, 'text':f'Olá, {self.user} e abaixo as opções do restaurante, as opções possíveis são:', 'background':'#edb3b0', 'fg':'#626262'},
                  {'fill':'x', 'padx':150, 'anchor':'center'})
        holderHome = addFrame(self.content, {'background':'#F9B97D', 'width':1267, 'height':618}, {'anchor':'n', 'pady':20})
        holderHome.columnconfigure(0, weight=1)
        holderHome.columnconfigure(1, weight=1)
        holderHome.columnconfigure(2, weight=1)
        holderHome.rowconfigure(0, weight=1)
        holderHome.rowconfigure(1, weight=1)

        linha1 = addFrame(holderHome, {'background':'#F9B97D'}, {'fill':'x', 'pady':(10,0)})
        linha1.columnconfigure(0, weight=1)
        linha1.columnconfigure(1, weight=1)
        linha1.columnconfigure(2, weight=1)

        self._mg1 = tk.Label(linha1, image=self.__assets['home']['entrada'], borderwidth=0)
        self._mg1.grid(column=0, row=0, padx=(10,0))
        self._mg1.bind("<Button-1>", lambda e: self.entrada())

        tk.Label(linha1, text='Entrada', font=('Helvetica', 18), fg='#626262' ).grid(column=0, row=1, padx=(10,0), sticky='we')

        self._mg2 = tk.Label(linha1, image=self.__assets['home']['pp'], borderwidth=0)
        self._mg2.grid(column=1, row=0, padx=40)
        self._mg2.bind("<Button-1>", lambda e: print('yo2'))
        tk.Label(linha1, text='Prato Principal', font=('Helvetica', 18), fg='#626262' ).grid(column=1, row=1, padx=40, sticky='we')

        self._mg3 = tk.Label(linha1, image=self.__assets['home']['bebidas'], borderwidth=0)
        self._mg3.grid(column=2, row=0, padx=(0,10))
        self._mg3.bind("<Button-1>", lambda e: print('yo3'))
        tk.Label(linha1, text='Bebidas', font=('Helvetica', 18), fg='#626262' ).grid(column=2, row=1, padx=(0,10), sticky='we')

        linha2 = addFrame(holderHome, {'background':'#F9B97D'}, {'fill':'x', 'pady':(20,10)})
        linha2.columnconfigure(0, weight=1)
        linha2.columnconfigure(1, weight=1)
        linha2.columnconfigure(2, weight=1)

        self._mg4 = tk.Label(linha2, image=self.__assets['home']['alcool'], borderwidth=0, text='text' )
        self._mg4.grid(column=0, row=0, padx=(10,0))
        self._mg4.bind("<Button-1>", lambda e: print('yo4'))
        tk.Label(linha2, text='Bebidas Alcoólicas', font=('Helvetica', 18), fg='#626262' ).grid(column=0, row=1, padx=(10,0), sticky='we')

        self._mg5 = tk.Label(linha2, image=self.__assets['home']['sobremesa'], borderwidth=0)
        self._mg5.grid(column=1, row=0, padx=40)
        self._mg5.bind("<Button-1>", lambda e: print('yo5'))
        tk.Label(linha2, text='Sobremesas', font=('Helvetica', 18), fg='#626262' ).grid(column=1, row=1, padx=40, sticky='we')

        self._mg6 = tk.Label(linha2, image=self.__assets['home']['chef'], borderwidth=0)
        self._mg6.grid(column=2, row=0, padx=(0,10))
        self._mg6.bind("<Button-1>", lambda e: print('yo6'))
        tk.Label(linha2, text='Menu do Chef', font=('Helvetica', 18), fg='#626262' ).grid(column=2, row=1, padx=(0,10), sticky='we')


    def login(self):
        #Left Image
        addLabel(self.content, {'image':self.__assets['login']['imgFeijoada'], 'borderwidth':0}, {'padx':(150,0), 'side':'left'})

        #login elements
        holderLogin = addFrame(self.content, {'background':'white', 'width':400}, {'padx':(0,150), 'side':'right', 'anchor':'e'})#Frame
        addLabel(holderLogin, {'background':'white', 'text':'Usuário', 'font':Assets.FONT_G, 'anchor':'w', 'justify':'left'}, {'padx':15, 'pady':(15,0), 'fill':'x'})#Label User
        self.uEntry = addEntry(holderLogin, {'font':Assets.FONT_G}, {'padx':15, 'fill':'x'})#Entry User
        addLabel(holderLogin, {'background':'white', 'text':'Senha', 'font':Assets.FONT_G, 'anchor':'w', 'justify':'left'}, {'padx':15, 'pady':(20,0), 'fill':'x'})#Label Password
        self.pEntry = addEntry(holderLogin, {'font':Assets.FONT_G}, {'padx':15, 'fill':'x'})#Entry Password
        self.pEntry.config(show='*')
        addLabel(holderLogin, {'background':'white', 'text':'Confirmar Senha', 'font':Assets.FONT_G, 'anchor':'w', 'justify':'left'}, {'padx':15,'pady':(20,0), 'fill':'x'})#Label Password Confirmation
        self.cpEntry = addEntry(holderLogin, {'font':Assets.FONT_G}, {'padx':15, 'fill':'x'})#Entry Password Confirmation
        self.cpEntry.config(show='*')
        addButton(holderLogin, {'text':'Entrar', 'font':Assets.FONT_G,'fg':'white', 'background':Assets.COLOR['green'],'relief':'groove', 'border':0,
                                'command': lambda: validateCad(self, self.uEntry, self.pEntry, self.cpEntry)}, {'pady': (40,15)})
        #tk.Entry(borderwidth=)

def validateCad(object: Cardapio, uEntry:tk.Entry, pEntry:tk.Entry, cpEntry:tk.Entry):
    object.user = uEntry.get()
    user = uEntry.get()
    password = pEntry.get()
    cpassword = cpEntry.get()

    #if(user == '' or len(user) < 5):
    #    messagebox.showerror('Login Incorreto!', 'O login é muito curto!')
    #    return
    #elif(password == '' or len(password) < 6):
    #    messagebox.showerror('Senha Invalida!', 'A senha é muito curta!')
    #    return
    #elif(user == password):
    #    messagebox.showwarning('Senha Invalida!', 'A senha não pode ser igual ao login!')
    #    return
    #elif(password != cpassword):
    #    messagebox.showerror('Senha Incorreta!', 'As senhas são diferentes!')
    #    return

    uEntry.delete(0, 'end')
    pEntry.delete(0, 'end')
    cpEntry.delete(0, 'end')
    object.root.focus()
    object._banner.pack_forget()
    object.home()
    #messagebox.showinfo('Cadastrado', 'Cadrastro realizado com sucesso!')

if __name__ == '__main__':
    Cardapio()

