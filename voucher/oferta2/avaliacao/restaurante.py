"""O desafio consiste em criar uma (ou mais telas) para um sistemas de pedido do restaurante do Ederson.
Para começar o sistema, é solicitado que ele digite um usuário e uma senha, a senha deve ser confirmada em um campo com confirmação de senha e deve seguir as mesmas normas do exercício anterior.
Depois do login deve ser possível ao usuário entrar na tela inicial onde ele pode começar o processo para fazer seus pedidos, na tela inicial deve conter a mensagem "Olá, {nome_usuário}" e abaixo as opções do restaurante, as opções possíveis são: entradas, pratos principais, bebidas, bebidas alcoólicas, sobremesas, menu do chef.
Cada botão que a pessoa clicar deve redirecionar a tela para o campo com opções variadas de produtos (no mínimo 5) para ser selecionada pelo usuário, a pessoa pode adicionar tudo no pedido dela clicando em um botão para adicionar ao pedido (use a criatividade para criar esse botão) e ao final da tela deve ter a opção de finalizar o pedido para que a pessoa possa visualizar tudo o que foi colocado no carrinho até agora e confirme se está tudo certo, caso esteja ela envia o pedido a cozinha, e finaliza o sistema com uma imagem divertida, caso não ela deve ter a opção de acrescentar mais itens ao pedido ou retirar os mesmos que já estejam lá."""

import tkinter as tk

def setGeometry(master: tk.Tk, scale: float = 0.7, width: int = None, height: int = None, resizable: bool = True):
    """Sets the window size and put it at center of the screen, by default uses 70% of the screen.
    If WIDTH or HEIGHT are given than uses this values instead."""
    width = width if width else int(master.winfo_screenwidth() * scale)
    height = height if height else int(master.winfo_screenheight() * scale)
    x = int((master.winfo_screenwidth() - width) / 2)
    y = int((master.winfo_screenheight() - height) / 2)

    master.geometry(f'{width}x{height}+{x}+{y}')
    master.resizable(resizable, resizable)

def addButton(origin: tk.Frame, b_kwargs: dict = {}, p_kwargs: dict = {}) -> tk.Button:
    button =  tk.Button(origin, **b_kwargs)
    button.pack(**p_kwargs)
    return button

def addFrame(origin: tk.Frame, f_kwargs: dict = {}, p_kwargs: dict = {}) -> tk.Button:
    frame =  tk.Frame(origin, **f_kwargs)
    frame.pack(**p_kwargs)
    return frame

def deleteChildren(object: tk.Tk | tk.Frame):
    for child in object.winfo_children():
        child.destroy()

class Cardapio:
    def __init__(self) -> None:
        self.root = tk.Tk()
        setGeometry(self.root, resizable=False)
        self.root.title('The Menu')
        self.login()
        
        self.root.mainloop()

    def login(self):
        mainF = addFrame(self.root, {'background':'#e5cb5f'}, {'padx':5, 'pady':5, 'fill':'both', 'expand':True})
        addButton(mainF, {'text':'Teste', 'background':'cyan', 'command':lambda: deleteChildren(mainF)})


if __name__ == '__main__':
    Cardapio()

