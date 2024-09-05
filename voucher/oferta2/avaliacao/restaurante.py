"""O desafio consiste em criar uma (ou mais telas) para um sistemas de pedido do restaurante do Ederson.
Para começar o sistema, é solicitado que ele digite um usuário e uma senha, a senha deve ser confirmada em um campo com confirmação de senha e deve seguir as mesmas normas do exercício anterior.
Depois do login deve ser possível ao usuário entrar na tela inicial onde ele pode começar o processo para fazer seus pedidos, na tela inicial deve conter a mensagem "Olá, {nome_usuário}" e abaixo as opções do restaurante, as opções possíveis são: entradas, pratos principais, bebidas, bebidas alcoólicas, sobremesas, menu do chef.
Cada botão que a pessoa clicar deve redirecionar a tela para o campo com opções variadas de produtos (no mínimo 5) para ser selecionada pelo usuário, a pessoa pode adicionar tudo no pedido dela clicando em um botão para adicionar ao pedido (use a criatividade para criar esse botão) e ao final da tela deve ter a opção de finalizar o pedido para que a pessoa possa visualizar tudo o que foi colocado no carrinho até agora e confirme se está tudo certo, caso esteja ela envia o pedido a cozinha, e finaliza o sistema com uma imagem divertida, caso não ela deve ter a opção de acrescentar mais itens ao pedido ou retirar os mesmos que já estejam lá."""

import tkinter as tk
from assets import Assets
from cart import Cart
from scrollableframe import VerticalScrolledFrame
from tkinter import messagebox





def setGeometry(master:tk.Tk, scale:float = 0.7, width:int = None, height:int = None,x:int = None, y:int = None, resizable:bool = True):
    """Sets the window size and put it at center of the screen, by default uses 70% of the screen.
    If WIDTH or HEIGHT were given than uses this values instead."""
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

class Cardapio:
    
    def __init__(self) -> None:
        self.root = tk.Tk()
        setGeometry(self.root, width=1920, height=1000)
        self.root.minsize(width=1920, height=1000)
        self.root.title('The Menu')
        self.root.state('zoomed')
        self.root.configure(background='purple')

        self.start()

        self.root.mainloop()

    #-----------------------------------------------------------------------------------------------#
    #                                             Methods                                           #
    #-----------------------------------------------------------------------------------------------#
    def raiseFrame(self, key1: str, key2: str) -> bool:
        """Tries to Raise the Frame into view if already exists, otherwise catches the exception"""
        try:
            if(self.__assets[key1][key2]):
                self.__assets[key1][key2].tkraise()
            return True
        except KeyError as e:
            print(f'Gracefully handled {e}')
            return False
        
    def start(self):
        #remove old stuff
        for child in self.root.winfo_children():
            child.destroy()
        try:
            if(self.__assets):
                del self.__assets
                del self.cart
        except AttributeError as e:
            print(f'yo {e}')

        self.__assets = {
            'login':{
                'iHouse':tk.PhotoImage(file=Assets.LOGIN['house']),
                'iBanner':tk.PhotoImage(file=Assets.LOGIN['banner']),
                'iCart':tk.PhotoImage(file=Assets.LOGIN['cartI']),
                'iFeijoada':tk.PhotoImage(file=Assets.LOGIN['feijoada']),
            },
            'cart':{
                'addCart':tk.PhotoImage(file=Assets.CART['add_cart'])
            }
        }

        self.cart = Cart()

        self.addOrRepackHeader()

        self.content = addFrame(self.root, {'background':Assets.COLOR['bg']}, {'fill':'both', 'expand':True })
        self.content.columnconfigure(0, weight=1)
        self.content.rowconfigure(0, weight=1)
        self.login()

    def addOrRepackHeader(self):
        try:
            if(self.__assets['login']['lHome'] and self.__assets['login']['lCart']):
                self.__assets['login']['lBanner'].pack_forget()
                self.__assets['login']['lHome'].pack(padx=(150,0), side='left')
                self.__assets['login']['lHome'].bind('<Button-1>', lambda e: self.home())
                self.__assets['login']['lBanner'].pack(fill='x', side='left', anchor='n', expand=True)
                self.__assets['login']['lCart'].pack(padx=(0,150), side='right', anchor='e')
                self.__assets['login']['lCart'].bind('<Button-1>', lambda e: self.shoppingCart())
                self.__assets['login']['lCartQuant'].pack(side='right', anchor='e')
                return
        except KeyError as e:
            print(f'Gracefully handled {e}')
            pass

        self.__assets['login']['fHeader'] = addFrame(self.root, {'background':Assets.COLOR['nav']}, { 'fill':'x', 'anchor':'n'})
        self.__assets['login']['lHome'] = addLabel(self.__assets['login']['fHeader'], {'image':self.__assets['login']['iHouse'], 'borderwidth':0, 'cursor':'cross'}, {'padx':(150,0), 'side':'left'})
        self.__assets['login']['lBanner'] = addLabel(self.__assets['login']['fHeader'], {'image':self.__assets['login']['iBanner'], 'borderwidth':0, 'background':'#f2c6c4'}, {'fill':'x', 'side':'left', 'anchor':'n', 'expand':True})
        self.__assets['login']['lCart'] = addLabel(self.__assets['login']['fHeader'], {'image':self.__assets['login']['iCart'], 'borderwidth':0}, {'padx':(0,150), 'side':'right', 'anchor':'e'})
        self.__assets['login']['lCartQuant'] = addLabel(self.__assets['login']['fHeader'], {'text':self.cart.getTotalAmount(), 'width':2,'borderwidth':0, 'font':Assets.FONT_G, 'background':Assets.COLOR['nav']}, {'side':'right', 'anchor':'e', 'after':self.__assets['login']['lCart']})
        self.__assets['login']['lHome'].pack_forget()
        self.__assets['login']['lCart'].pack_forget()
        self.__assets['login']['lCartQuant'].pack_forget()

    def addProdFrame(self, frame: tk.Tk | tk.Frame, name: str, price:float, img: tk.PhotoImage, cart: tk.PhotoImage, kargs :dict= {}) -> tk.Label:
        """Adds the Product frame and it contents. Returns the 'add to cart' Label for later binding"""
        pFrame = tk.Frame(frame, width=389, height=314, background='white')
        pFrame.grid(**kargs)

        pImgFrame = tk.Frame(pFrame)
        pImgFrame.pack(anchor='n')

        tk.Label(pImgFrame, image=img, borderwidth=0).pack()

        pTextFrame = tk.Frame(pFrame, background='white')
        pTextFrame.pack(fill='x', padx=4, pady=4)

        tk.Label(pTextFrame, text=name, font=Assets.FONT_S, background='white', foreground=Assets.COLOR['text'], justify='left', anchor='w', wraplength=205).pack(side='left', fill='x', anchor='w', expand=1)

        pAddCart = tk.Label(pTextFrame, image=cart, borderwidth=0, cursor='plus')
        pAddCart.pack(side='right')

        pAddCart.bind('<Button-1>', lambda e: [self.cart.add(name, 1, price), self.updateCartAmount()] )

        tk.Label(pTextFrame, text=f'R${price:.2f}', font=Assets.FONT_S, background='white', foreground=Assets.COLOR['text'], justify='right').pack(side='right')

    def updateCartAmount(self):
        self.__assets['login']['lCartQuant'].configure(text=self.cart.getTotalAmount())

    def addProdCart(self, frame:tk.Frame, name: str, quantity:int, price:float) -> tk.Label:
        def increase():
            """Increases the product's Label amount and updates the total cart amount"""
            nonlocal name, price

            amount = self.cart.add(name, 1)
            priceL.configure(text=f'R${price * amount:6.2f}')
            amountL.configure(text=f'QTD: {amount:2}')
            self.updateCartAmount()
            self.updateTotalCart()

        def decrease():
            """Decreases the product's Label amount and updates the total cart amount"""
            nonlocal name, price

            amount = self.cart.sub(name, 1)
            if(amount == 0):
                linha.destroy()
                self.updateCartAmount()
                self.updateTotalCart()
                return
            priceL.configure(text=f'R${price * amount:6.2f}')
            amountL.configure(text=f'QTD: {amount:2}')
            self.updateCartAmount()
            self.updateTotalCart()


        linha = tk.Frame(frame, background='white', height=50, borderwidth=0, highlightthickness=2, highlightcolor='black')
        linha.pack(fill='x', pady=5, padx=10)

        nameL = tk.Label(linha, text=name, background='white', foreground=Assets.COLOR['text'], font=Assets.FONT_M, anchor='w')
        nameL.pack(side='left', fill='x')

        priceL = tk.Label(linha, text=f'R${price:6.2f}', font=Assets.FONT_M, background='white', width=9, foreground=Assets.COLOR['text'])
        priceL.pack(side='right', after=nameL)

        plusL = tk.Label(linha, image=self.__assets['cart']['plus'], border=0)
        plusL.pack(side='right', after=priceL)
        plusL.bind('<Button-1>', lambda e: increase())

        amountL = tk.Label(linha, text=f'QTD: {quantity:2}', font=Assets.FONT_M, background='white', width=7, foreground=Assets.COLOR['text'])
        amountL.pack(side='right', after=plusL)

        minusL = tk.Label(linha, image=self.__assets['cart']['minus'], border=0)
        minusL.pack(side='right', after=amountL)
        minusL.bind('<Button-1>', lambda e: decrease())

    def addCartTotal(self, frame:tk.Frame) -> tk.Label:
        linha = tk.Frame(frame, background='white', height=50, borderwidth=0, highlightthickness=2, highlightcolor='black')
        linha.pack(anchor='n', fill='x',pady=10, padx=500)

        totalL = tk.Label(linha, text='Total de Produtos', background='white', foreground=Assets.COLOR['text'], font=Assets.FONT_M, anchor='w')
        totalL.pack(side='left', fill='x')

        self.__assets['cart']['lAmount'] = tk.Label(linha, text=f'QTD: {self.cart.getTotalAmount():2}', font=Assets.FONT_M, background='white', width=7, foreground=Assets.COLOR['text'])
        self.__assets['cart']['lPrice'] = tk.Label(linha, text=f'Total: R${self.cart.getTotalValue():8.2f}', font=Assets.FONT_M, background='white', width=15, foreground=Assets.COLOR['text'])
        
        self.__assets['cart']['lAmount'].pack(side='right', after=totalL)
        self.__assets['cart']['lPrice'].pack(side='right', after=self.__assets['cart']['lAmount'])

    def updateTotalCart(self):
        self.__assets['cart']['lPrice'].configure(text=f'Total: R${self.cart.getTotalValue():8.2f}')
        self.__assets['cart']['lAmount'].configure(text=f'QTD: {self.cart.getTotalAmount():2}')

    def shoppingCart(self):
        if(self.raiseFrame('cart', 'fCart')):
            for child in self.__assets['cart']['fLista'].interior.winfo_children(): #Detroy all children inside the list
                child.destroy()
            for item in self.cart.data: #Recreate list of products to add new ones
                self.addProdCart(self.__assets['cart']['fLista'].interior, item, self.cart.data[item]['quantity'], self.cart.data[item]['price'])
            return

        self.__assets['cart']['plus'] = tk.PhotoImage(file=Assets.CART['plus'])
        self.__assets['cart']['minus'] = tk.PhotoImage(file=Assets.CART['minus'])

        self.__assets['cart']['fCart'] = tk.Frame(self.content, background=Assets.COLOR['bg'])
        self.__assets['cart']['fCart'].grid(column=0, row=0, sticky='nsew')

        addLabel(self.__assets['cart']['fCart'], {'font':Assets.FONT_G, 'text':f'Olá, {self.user} aqui estão os produtos escolhidos:', 'background':Assets.COLOR['bg'], 'fg':Assets.COLOR['text']},
                                {'fill':'x', 'padx':150, 'anchor':'center'})

        self.__assets['cart']['fLista'] = VerticalScrolledFrame(self.__assets['cart']['fCart'], height=900)
        self.__assets['cart']['fLista'].pack(anchor='n', fill='x', padx=500)
        #addFrame(self.__assets['cart']['fCart'], {'background':Assets.COLOR['gray']}, {'anchor':'n', 'fill':'x', 'padx':500})

        for item in self.cart.data:
            self.addProdCart(self.__assets['cart']['fLista'].interior, item, self.cart.data[item]['quantity'], self.cart.data[item]['price'])
        
        self.addCartTotal(self.__assets['cart']['fCart']) #adds the total amount line

        tk.Button( self.__assets['cart']['fCart'], text='Finalizar Compra', font=Assets.FONT_G, foreground='white', background=Assets.COLOR['green'], relief='groove', border=0, command=self.obrigado).pack(pady=20)

    def obrigado(self):
        self.__assets.update({'obrigado':{}})

        self.__assets['obrigado']['gif'] = [tk.PhotoImage(file='assets\\obrigado.gif',format = f'gif -index {i}') for i in range(33)]

        for child in self.root.winfo_children():
            child.pack_forget()

        self.__assets['obrigado']['fObrigado'] = tk.Frame(self.root, background=Assets.COLOR['bg'])
        self.__assets['obrigado']['fObrigado'].pack(fill='both', expand=True)

        self.__assets['obrigado']['counter'] = 0
        self.__assets['obrigado']['lGif'] = []
        for index, img in enumerate(self.__assets['obrigado']['gif']):
            self.__assets['obrigado']['lGif'].append(tk.Label(self.__assets['obrigado']['fObrigado'], image=img, border=0))
            self.__assets['obrigado']['lGif'][index].place(relx=0.5, rely=0.6, anchor='s')

        self.__assets['obrigado']['lGif'][0].tkraise()
        self.__assets['obrigado']['lGif'][0].after(30, self.runGif)
        tk.Button( self.__assets['obrigado']['fObrigado'], text='Ir para Login', font=Assets.FONT_G, foreground='white', background=Assets.COLOR['green'], relief='groove', border=0, command= self.start).place(relx=0.5, rely=0.7, anchor='n')

    def runGif(self):
        count = self.__assets['obrigado']['counter']
        self.__assets['obrigado']['lGif'][count].tkraise()
        self.__assets['obrigado']['lGif'][count].after(30, self.runGif)
        self.__assets['obrigado']['counter'] += 1
        if count == 32:
            self.__assets['obrigado']['counter'] = 0

    def entrada(self):
        if(self.raiseFrame('entrada', 'fEntrada')):
            return

        self.__assets.update({'entrada':{}})
        self.__assets['entrada']['fEntrada'] = tk.Frame(self.content, background=Assets.COLOR['bg'])
        self.__assets['entrada']['fEntrada'].grid(column=0, row=0, sticky='nsew')

        addLabel(self.__assets['entrada']['fEntrada'], {'font':Assets.FONT_G, 'text':f'Olá, {self.user} e abaixo as opções de Entrada:', 'background':Assets.COLOR['bg'], 'fg':Assets.COLOR['text']},
                                {'fill':'x', 'padx':150, 'anchor':'center'})
        
        self.__assets['entrada'].update(Assets.getPhotoImagesFromCat(category='entrada'))

        productF = addFrame(self.__assets['entrada']['fEntrada'], {'background':Assets.COLOR['orange']}, {'anchor':'n', 'pady':20})

        linha1 = addFrame(productF, {'background':Assets.COLOR['orange']}, {'fill':'x', 'pady':10, 'padx':10})
        linha1.columnconfigure(0, weight=1)
        linha1.columnconfigure(1, weight=1)
        linha1.columnconfigure(2, weight=1)

        linha2 = addFrame(productF, {'background':Assets.COLOR['orange']}, {'fill':'x', 'pady':10, 'padx':10})
        linha2.columnconfigure(0, weight=1)
        linha2.columnconfigure(1, weight=1)
        linha2.columnconfigure(2, weight=1)

        index = -1
        for i in range(3):
            index += 1
            nameA = Assets.ENTRADA[index]['name']
            padding = 40 if i == 1 else 0

            self.addProdFrame(linha1, nameA, Assets.ENTRADA[index]['price'], self.__assets['entrada'][nameA], self.__assets['cart']['addCart'], {'column':i, 'row':0,'padx':padding})

            index += 1
            nameB = Assets.ENTRADA[index]['name']
            self.addProdFrame(linha2, nameB, Assets.ENTRADA[index]['price'], self.__assets['entrada'][nameB], self.__assets['cart']['addCart'], {'column':i, 'row':0,'padx':padding})

    def bebidas(self):
        if(self.raiseFrame('bebidas', 'fBebidas')):
            return

        self.__assets.update({'bebidas':{}})

        self.__assets['bebidas']['fBebidas'] = tk.Frame(self.content, background=Assets.COLOR['bg'])
        self.__assets['bebidas']['fBebidas'].grid(column=0, row=0, sticky='nsew')

        addLabel(self.__assets['bebidas']['fBebidas'], {'font':Assets.FONT_G, 'text':f'Olá, {self.user} e abaixo as opções de Bebidas:', 'background':Assets.COLOR['bg'], 'fg':Assets.COLOR['text']},
                                {'fill':'x', 'padx':150, 'anchor':'center'})
        
        self.__assets['bebidas'].update(Assets.getPhotoImagesFromCat(category='bebidas'))

        productF = addFrame(self.__assets['bebidas']['fBebidas'], {'background':Assets.COLOR['orange']}, {'anchor':'n', 'pady':20})

        linha1 = addFrame(productF, {'background':Assets.COLOR['orange']}, {'fill':'x', 'pady':10, 'padx':10})
        linha1.columnconfigure(0, weight=1)
        linha1.columnconfigure(1, weight=1)
        linha1.columnconfigure(2, weight=1)

        linha2 = addFrame(productF, {'background':Assets.COLOR['orange']}, {'fill':'x', 'pady':10, 'padx':10})
        linha2.columnconfigure(0, weight=1)
        linha2.columnconfigure(1, weight=1)
        linha2.columnconfigure(2, weight=1)

        index = -1
        for i in range(3):
            index += 1
            nameA = Assets.BEBIDAS[index]['name']
            padding = 40 if i == 1 else 0

            self.addProdFrame(linha1, nameA, Assets.BEBIDAS[index]['price'], self.__assets['bebidas'][nameA], self.__assets['cart']['addCart'], {'column':i, 'row':0,'padx':padding})

            index += 1
            nameB = Assets.BEBIDAS[index]['name']
            self.addProdFrame(linha2, nameB, Assets.BEBIDAS[index]['price'], self.__assets['bebidas'][nameB], self.__assets['cart']['addCart'], {'column':i, 'row':0,'padx':padding})

    def prato_principal(self):
        if(self.raiseFrame('prato_principal', 'fPrato_principal')):
            return

        self.__assets.update({'prato_principal':{}})

        self.__assets['prato_principal']['fPrato_principal'] = tk.Frame(self.content, background=Assets.COLOR['bg'])
        self.__assets['prato_principal']['fPrato_principal'].grid(column=0, row=0, sticky='nsew')

        addLabel(self.__assets['prato_principal']['fPrato_principal'], {'font':Assets.FONT_G, 'text':f'Olá, {self.user} e abaixo as opções de Pratos Principal:', 'background':Assets.COLOR['bg'], 'fg':Assets.COLOR['text']},
                                {'fill':'x', 'padx':150, 'anchor':'center'})
        
        self.__assets['prato_principal'].update(Assets.getPhotoImagesFromCat(category='principal'))

        productF = addFrame(self.__assets['prato_principal']['fPrato_principal'], {'background':Assets.COLOR['orange']}, {'anchor':'n', 'pady':20})

        linha1 = addFrame(productF, {'background':Assets.COLOR['orange']}, {'fill':'x', 'pady':10, 'padx':10})
        linha1.columnconfigure(0, weight=1)
        linha1.columnconfigure(1, weight=1)
        linha1.columnconfigure(2, weight=1)

        linha2 = addFrame(productF, {'background':Assets.COLOR['orange']}, {'fill':'x', 'pady':10, 'padx':10})
        linha2.columnconfigure(0, weight=1)
        linha2.columnconfigure(1, weight=1)
        linha2.columnconfigure(2, weight=1)

        index = -1
        for i in range(3):
            index += 1
            nameA = Assets.PRINCIPAL[index]['name']
            padding = 40 if i == 1 else 0

            self.addProdFrame(linha1, nameA, Assets.PRINCIPAL[index]['price'], self.__assets['prato_principal'][nameA], self.__assets['cart']['addCart'], {'column':i, 'row':0,'padx':padding})

            index += 1
            nameB = Assets.PRINCIPAL[index]['name']
            self.addProdFrame(linha2, nameB, Assets.PRINCIPAL[index]['price'], self.__assets['prato_principal'][nameB], self.__assets['cart']['addCart'], {'column':i, 'row':0,'padx':padding})

    def alcool(self):
        if(self.raiseFrame('alcool', 'fAlcool')):
            return

        self.__assets.update({'alcool':{}})

        self.__assets['alcool']['fAlcool'] = tk.Frame(self.content, background=Assets.COLOR['bg'])
        self.__assets['alcool']['fAlcool'].grid(column=0, row=0, sticky='nsew')

        addLabel(self.__assets['alcool']['fAlcool'], {'font':Assets.FONT_G, 'text':f'Olá, {self.user} e abaixo as opções de Bebidas Alcoólicas:', 'background':Assets.COLOR['bg'], 'fg':Assets.COLOR['text']},
                                {'fill':'x', 'padx':150, 'anchor':'center'})
        
        self.__assets['alcool'].update(Assets.getPhotoImagesFromCat(category='alcool'))

        productF = addFrame(self.__assets['alcool']['fAlcool'], {'background':Assets.COLOR['orange']}, {'anchor':'n', 'pady':20})

        linha1 = addFrame(productF, {'background':Assets.COLOR['orange']}, {'fill':'x', 'pady':10, 'padx':10})
        linha1.columnconfigure(0, weight=1)
        linha1.columnconfigure(1, weight=1)
        linha1.columnconfigure(2, weight=1)

        linha2 = addFrame(productF, {'background':Assets.COLOR['orange']}, {'fill':'x', 'pady':10, 'padx':10})
        linha2.columnconfigure(0, weight=1)
        linha2.columnconfigure(1, weight=1)
        linha2.columnconfigure(2, weight=1)

        index = -1
        for i in range(3):
            index += 1
            nameA = Assets.ALCOOL[index]['name']
            padding = 40 if i == 1 else 0

            self.addProdFrame(linha1, nameA, Assets.ALCOOL[index]['price'], self.__assets['alcool'][nameA], self.__assets['cart']['addCart'], {'column':i, 'row':0,'padx':padding})

            index += 1
            nameB = Assets.ALCOOL[index]['name']
            self.addProdFrame(linha2, nameB, Assets.ALCOOL[index]['price'], self.__assets['alcool'][nameB], self.__assets['cart']['addCart'], {'column':i, 'row':0,'padx':padding})

    def sobremesa(self):
        if(self.raiseFrame('sobremesa', 'fSobremesa')):
            return

        self.__assets.update({'sobremesa':{}})

        self.__assets['sobremesa']['fSobremesa'] = tk.Frame(self.content, background=Assets.COLOR['bg'])
        self.__assets['sobremesa']['fSobremesa'].grid(column=0, row=0, sticky='nsew')

        addLabel(self.__assets['sobremesa']['fSobremesa'], {'font':Assets.FONT_G, 'text':f'Olá, {self.user} e abaixo as opções de Bebidas Alcoólicas:', 'background':Assets.COLOR['bg'], 'fg':Assets.COLOR['text']},
                                {'fill':'x', 'padx':150, 'anchor':'center'})
        
        self.__assets['sobremesa'].update(Assets.getPhotoImagesFromCat(category='sobremesa'))

        productF = addFrame(self.__assets['sobremesa']['fSobremesa'], {'background':Assets.COLOR['orange']}, {'anchor':'n', 'pady':20})

        linha1 = addFrame(productF, {'background':Assets.COLOR['orange']}, {'fill':'x', 'pady':10, 'padx':10})
        linha1.columnconfigure(0, weight=1)
        linha1.columnconfigure(1, weight=1)
        linha1.columnconfigure(2, weight=1)

        linha2 = addFrame(productF, {'background':Assets.COLOR['orange']}, {'fill':'x', 'pady':10, 'padx':10})
        linha2.columnconfigure(0, weight=1)
        linha2.columnconfigure(1, weight=1)
        linha2.columnconfigure(2, weight=1)

        index = -1
        for i in range(3):
            index += 1
            nameA = Assets.SOBREMESA[index]['name']
            padding = 40 if i == 1 else 0

            self.addProdFrame(linha1, nameA, Assets.SOBREMESA[index]['price'], self.__assets['sobremesa'][nameA], self.__assets['cart']['addCart'], {'column':i, 'row':0,'padx':padding})

            index += 1
            nameB = Assets.SOBREMESA[index]['name']
            self.addProdFrame(linha2, nameB, Assets.SOBREMESA[index]['price'], self.__assets['sobremesa'][nameB], self.__assets['cart']['addCart'], {'column':i, 'row':0,'padx':padding})

    def chef(self):
        if(self.raiseFrame('chef', 'fChef')):
            return

        self.__assets.update({'chef':{}})

        self.__assets['chef']['fChef'] = tk.Frame(self.content, background=Assets.COLOR['bg'])
        self.__assets['chef']['fChef'].grid(column=0, row=0, sticky='nsew')

        addLabel(self.__assets['chef']['fChef'], {'font':Assets.FONT_G, 'text':f'Olá, {self.user} e abaixo as opções do Menu do Chef:', 'background':Assets.COLOR['bg'], 'fg':Assets.COLOR['text']},
                                {'fill':'x', 'padx':150, 'anchor':'center'})
        
        self.__assets['chef'].update(Assets.getPhotoImagesFromCat(category='chef'))

        productF = addFrame(self.__assets['chef']['fChef'], {'background':Assets.COLOR['orange'] }, {'anchor':'n', 'pady':20})#'width':1267, 'height':618

        linha1 = addFrame(productF, {'background':Assets.COLOR['orange']}, {'fill':'x', 'pady':10, 'padx':10})
        linha1.columnconfigure(0, weight=1)
        linha1.columnconfigure(1, weight=1)
        linha1.columnconfigure(2, weight=1)

        linha2 = addFrame(productF, {'background':Assets.COLOR['orange']}, {'fill':'x', 'pady':10, 'padx':10})
        linha2.columnconfigure(0, weight=1)
        linha2.columnconfigure(1, weight=1)
        linha2.columnconfigure(2, weight=1)

        index = -1
        for i in range(3):
            index += 1
            nameA = Assets.CHEF[index]['name']
            padding = 40 if i == 1 else 0

            self.addProdFrame(linha1, nameA, Assets.CHEF[index]['price'], self.__assets['chef'][nameA], self.__assets['cart']['addCart'], {'column':i, 'row':0,'padx':padding})

            index += 1
            nameB = Assets.CHEF[index]['name']
            self.addProdFrame(linha2, nameB, Assets.CHEF[index]['price'], self.__assets['chef'][nameB], self.__assets['cart']['addCart'], {'column':i, 'row':0,'padx':padding})

    def home(self):
        if(self.raiseFrame('home', 'fHome')):
            self.cart.show()
            return

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

        self.addOrRepackHeader() #Repack header to add Home button and Cart icon

        self.__assets['home']['fHome'] = tk.Frame(self.content, background=Assets.COLOR['bg'])
        self.__assets['home']['fHome'].grid(column=0, row=0, sticky='nsew')

        #Add new elements
        addLabel(self.__assets['home']['fHome'], {'font':Assets.FONT_G, 'text':f'Olá, {self.user} e abaixo as opções do restaurante, as opções possíveis são:', 'background':Assets.COLOR['bg'], 'fg':Assets.COLOR['text']}, {'fill':'x', 'padx':150, 'anchor':'center'})

        homeF = addFrame(self.__assets['home']['fHome'], {'background':Assets.COLOR['orange']}, {'anchor':'n', 'pady':20})

        linha1 = addFrame(homeF, {'background':Assets.COLOR['orange']}, {'fill':'x', 'pady':(10,0)})
        linha1.columnconfigure(0, weight=1)
        linha1.columnconfigure(1, weight=1)
        linha1.columnconfigure(2, weight=1)

        entrada = tk.Label(linha1, image=self.__assets['home']['entrada'], borderwidth=0)
        entrada.grid(column=0, row=0, padx=(10,0))
        entrada.bind("<Button-1>", lambda e: self.entrada())

        tk.Label(linha1, text='Entrada', font=('Helvetica', 18), fg=Assets.COLOR['text'] ).grid(column=0, row=1, padx=(10,0), sticky='we')

        pagina_principal = tk.Label(linha1, image=self.__assets['home']['pp'], borderwidth=0)
        pagina_principal.grid(column=1, row=0, padx=40)
        pagina_principal.bind("<Button-1>", lambda e: self.prato_principal())
        tk.Label(linha1, text='Prato Principal', font=('Helvetica', 18), fg=Assets.COLOR['text'] ).grid(column=1, row=1, padx=40, sticky='we')

        bebidas = tk.Label(linha1, image=self.__assets['home']['bebidas'], borderwidth=0)
        bebidas.grid(column=2, row=0, padx=(0,10))
        bebidas.bind("<Button-1>", lambda e: self.bebidas())
        tk.Label(linha1, text='Bebidas', font=('Helvetica', 18), fg=Assets.COLOR['text'] ).grid(column=2, row=1, padx=(0,10), sticky='we')

        linha2 = addFrame(homeF, {'background':Assets.COLOR['orange']}, {'fill':'x', 'pady':(20,10)})
        linha2.columnconfigure(0, weight=1)
        linha2.columnconfigure(1, weight=1)
        linha2.columnconfigure(2, weight=1)

        alcool = tk.Label(linha2, image=self.__assets['home']['alcool'], borderwidth=0, text='text' )
        alcool.grid(column=0, row=0, padx=(10,0))
        alcool.bind("<Button-1>", lambda e: self.alcool())
        tk.Label(linha2, text='Bebidas Alcoólicas', font=('Helvetica', 18), fg=Assets.COLOR['text'] ).grid(column=0, row=1, padx=(10,0), sticky='we')

        sobremesa = tk.Label(linha2, image=self.__assets['home']['sobremesa'], borderwidth=0)
        sobremesa.grid(column=1, row=0, padx=40)
        sobremesa.bind("<Button-1>", lambda e: self.sobremesa())
        tk.Label(linha2, text='Sobremesas', font=('Helvetica', 18), fg=Assets.COLOR['text'] ).grid(column=1, row=1, padx=40, sticky='we')

        chef = tk.Label(linha2, image=self.__assets['home']['chef'], borderwidth=0)
        chef.grid(column=2, row=0, padx=(0,10))
        chef.bind("<Button-1>", lambda e: self.chef())
        tk.Label(linha2, text='Menu do Chef', font=('Helvetica', 18), fg=Assets.COLOR['text'] ).grid(column=2, row=1, padx=(0,10), sticky='we')

    def login(self):
        if(self.raiseFrame('login', 'fLogin')):
            return

        self.__assets['login']['fLogin'] = tk.Frame(self.content, background=Assets.COLOR['bg'])
        self.__assets['login']['fLogin'].grid(column=0, row=0, sticky='nsew')
        addLabel(self.__assets['login']['fLogin'], {'image':self.__assets['login']['iFeijoada'], 'borderwidth':0}, {'padx':(150,0), 'side':'left'})

        #login elements
        fLogin = addFrame(self.__assets['login']['fLogin'], {'background':'white', 'width':400}, {'padx':(0,150), 'side':'right', 'anchor':'e'})

        addLabel(fLogin, {'background':'white', 'text':'Usuário', 'font':Assets.FONT_G, 'anchor':'w', 'justify':'left'}, {'padx':15, 'pady':(15,0), 'fill':'x'})#Label User
        user = addEntry(fLogin, {'font':Assets.FONT_G}, {'padx':15, 'fill':'x'})#Entry User

        addLabel(fLogin, {'background':'white', 'text':'Senha', 'font':Assets.FONT_G, 'anchor':'w', 'justify':'left'}, {'padx':15, 'pady':(20,0), 'fill':'x'})#Label Password
        password = addEntry(fLogin, {'font':Assets.FONT_G}, {'padx':15, 'fill':'x'})#Entry Password
        password.config(show='*')

        addLabel(fLogin, {'background':'white', 'text':'Confirmar Senha', 'font':Assets.FONT_G, 'anchor':'w', 'justify':'left'}, {'padx':15,'pady':(20,0), 'fill':'x'})#Label Password Confirmation
        confirmP = addEntry(fLogin, {'font':Assets.FONT_G}, {'padx':15, 'fill':'x'})#Entry Password Confirmation
        confirmP.config(show='*')

        addButton(fLogin, {'text':'Entrar', 'font':Assets.FONT_G,'fg':'white', 'background':Assets.COLOR['green'],'relief':'groove', 'border':0,
                            'command': lambda: validateCad(self, user, password, confirmP)}, {'pady': (40,15)})


def validateCad(object: Cardapio, uEntry:tk.Entry, pEntry:tk.Entry, cpEntry:tk.Entry):
    object.user = uEntry.get()
    user = uEntry.get()
    password = pEntry.get()
    cpassword = cpEntry.get()

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
    object.home()
    #messagebox.showinfo('Cadastrado', 'Cadrastro realizado com sucesso!')

if __name__ == '__main__':
    Cardapio()