from typing import Literal
from tkinter import PhotoImage

class Assets:

    COLOR = {
        'bg':'#add8e6',#add8e6 edb3b0
        'nav':'#f2c6c4',
        'text':'#626262',
        'green':'#4CAF50',
        'orange':'#F9B97D'
    } 

    FONT_S = ('Helvetica', 13)
    FONT_M = ('Helvetica', 20)
    FONT_G = ('Helvetica', 24)

    LOGIN = {
        'house':'assets\\login\\house.png',
        'banner':'assets\\login\\banner.png',
        'cartI':'assets\\login\\cart.png',
        'feijoada':'assets\\login\\feijoada.png'
    }

    HOME = {
        'entrada':'assets\\home\\entrada.png',
        'bebidas':'assets\\home\\bebidas.png',
        'alcool':'assets\\home\\alcool.png',
        'pp':'assets\\home\\pp.png',
        'sobremesa':'assets\\home\\sobremesa.png',
        'chef':'assets\\home\\chef.png'
    }

    CART = 'assets\\cart\\add_cart.png'

    ALCOOL = [
        {'name':'Cerveja', 'price':1, 'img':'assets\\alcool\\beer.png'},
        {'name':'Jack Daniels', 'price':1, 'img':'assets\\alcool\\jack.png'},
        {'name':'Martini', 'price':1, 'img':'assets\\alcool\\liquor.png'},
        {'name':'Rúm', 'price':1, 'img':'assets\\alcool\\martini.png'},
        {'name':'Vinho', 'price':1, 'img':'assets\\alcool\\rum.png'},
        {'name':'Licor', 'price':1, 'img':'assets\\alcool\\wines.png'}
    ]

    BEBIDAS = [
        {'name':'Suco de Cenoura', 'price':1, 'img':'assets\\bebidas\\cenoura.png'},
        {'name':'Suco de Goiaba', 'price':1, 'img':'assets\\bebidas\\goiaba.png'},
        {'name':'Suco de Kiwi', 'price':1, 'img':'assets\\bebidas\\kiwi.png'},
        {'name':'Suco de Laranja', 'price':1, 'img':'assets\\bebidas\\laranja.png'},
        {'name':'Suco de Manga', 'price':1, 'img':'assets\\bebidas\\manga.png'},
        {'name':'Suco de Repolho', 'price':1, 'img':'assets\\bebidas\\repolho.png'}
    ]

    CHEF = [
        {'name':'Bacalhau', 'price':1, 'img':'assets\\chef\\bacalhau.png'},
        {'name':'Frango Frito', 'price':1, 'img':'assets\\chef\\frango.png'},
        {'name':'Lasanha', 'price':1, 'img':'assets\\chef\\lasanha.png'},
        {'name':'Nhoque', 'price':1, 'img':'assets\\chef\\nhoque.png'},
        {'name':'Ratatouille', 'price':1, 'img':'assets\\chef\\ratatouille.png'},
        {'name':'Strogonoff', 'price':1, 'img':'assets\\chef\\strogonoff.png'}
    ]

    ENTRADA = [
        {'name':'Brusquetas', 'price':1, 'img':'assets\\entrada\\brusquetas.png'},
        {'name':'Canapes', 'price':1, 'img':'assets\\entrada\\canapes.png'},
        {'name':'Ceviche', 'price':1, 'img':'assets\\entrada\\ceviche.png'},
        {'name':'Fondue', 'price':1, 'img':'assets\\entrada\\fondue.png'},
        {'name':'Guacamole', 'price':1, 'img':'assets\\entrada\\guacamole.png'},
        {'name':'Quibe', 'price':1, 'img':'assets\\entrada\\quibe.png'}
    ]

    PRINCIPAL = [
        {'name':'Steak', 'price':1, 'img':'assets\\prato_principal\\bife.png'},
        {'name':'Macarrão', 'price':1, 'img':'assets\\prato_principal\\macarrao.png'},
        {'name':'Pasta', 'price':1, 'img':'assets\\prato_principal\\pasta.png'},
        {'name':'Pizza de Calabresa', 'price':1, 'img':'assets\\prato_principal\\pizza.png'},
        {'name':'Salmão Assado', 'price':1, 'img':'assets\\prato_principal\\salmao.png'},
        {'name':'Sopa de Lentilha', 'price':1, 'img':'assets\\prato_principal\\sopa_lentilha.png'}
    ]

    SOBREMESA = [
        {'name':'Cookies', 'price':1, 'img':'assets\\sobremesa\\cookies.png'},
        {'name':'Creme Brulee', 'price':1, 'img':'assets\\sobremesa\\creme_brulee.png'},
        {'name':'Muffins', 'price':1, 'img':'assets\\sobremesa\\muffins.png'},
        {'name':'Rocambole', 'price':1, 'img':'assets\\sobremesa\\rocambole.png'},
        {'name':'Sorvete', 'price':1, 'img':'assets\\sobremesa\\sorvete.png'},
        {'name':'Torta de Maçã', 'price':1, 'img':'assets\\sobremesa\\torta_maca.png'}
    ]

    def __init__(self) -> None:
        pass
    
    @classmethod
    def getPhotoImagesFromCat(self, category:Literal['alcool', 'bebidas', 'chef', 'entrada', 'principal', 'sobremesa']) -> dict[str: PhotoImage]:
        """Returns a dictionary containing PhotoImage object from the chosen category of Assets. Format dict{ name:PhotoImage }"""
        match(category):
            case 'alcool':
                return {element['name']: PhotoImage(file=element['img']) for i, element in enumerate(self.ALCOOL)}
            case 'bebidas':
                return {element['name']: PhotoImage(file=element['img']) for i, element in enumerate(self.BEBIDAS)}
            case 'chef':
                return {element['name']: PhotoImage(file=element['img']) for i, element in enumerate(self.CHEF)}
            case 'entrada':
                return {element['name']: PhotoImage(file=element['img']) for i, element in enumerate(self.ENTRADA)}
            case 'principal':
                return {element['name']: PhotoImage(file=element['img']) for i, element in enumerate(self.PRINCIPAL)}
            case 'sobremesa':
                return {element['name']: PhotoImage(file=element['img']) for i, element in enumerate(self.SOBREMESA)}


if __name__ == '__main__':
    Assets()