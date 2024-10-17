# carro = {
#     "marca":"VolksWagen",
#     "modelo":"Fusca",
#     "cor":"Azul",
#     "ano":"1945"
# }

# print(carro.get("marca"))

class Veiculo:
    def __init__(self, marca: str, modelo: str, ano: int, cor: str):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__cor = cor

    def freiar(self):
        print(f'O veículo {self.modelo} freiou!')

    @property
    def marca(self):
        """Propriedade Marca"""
        return self.__marca

    @marca.setter
    def marca(self, value):
        if(type(value) != str):
            raise TypeError('Tipo incorreto! Precisa ser uma String')
        if(len(value) <= 3):
            raise ValueError('Comprimento do Marca é muito curto')

        self.__marca = value

    @marca.deleter
    def marca(self):
        self.__marca = 'Carro'

    @property
    def modelo(self):
        """Propriedade modelo"""
        return self.__modelo

    @modelo.setter
    def modelo(self, value):
        if(type(value) != str):
            raise TypeError('Tipo incorreto! Precisa ser uma String')
        if(len(value) <= 3):
            raise ValueError('Comprimento do Modelo é muito curto')

        self.__modelo = value

    @modelo.deleter
    def modelo(self):
        self.__modelo = None

    @property
    def ano(self):
        """Propriedade ano"""
        return self.__ano

    @ano.setter
    def ano(self, value):
        if(type(value) != int):
            raise TypeError('Tipo incorreto! Precisa ser uma Int')
        if(value <= 0):
            raise ValueError('Ano não pode ser menor que ou igual a Zero')
        if(value > 2025):
            raise ValueError('Ano não pode ser maior que 2025')

        self.__ano = value

    @ano.deleter
    def ano(self):
        self.__ano = None

    @property
    def cor(self):
        """Propriedade cor"""
        return self.__cor

    @cor.setter
    def cor(self, value):
        if(type(value) != str):
            raise TypeError('Tipo incorreto! Precisa ser uma String')
        if(len(value) <= 3):
            raise ValueError('Comprimento da cor é muito curto')

        self.__cor = value

    @cor.deleter
    def cor(self):
        self.__cor = None

    def __str__(self) -> str:
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.__cor}, Ano: {self.ano}'


class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, portas: int):
        super().__init__(marca, modelo, ano, cor)
        self.__portas = portas

    def freiar(self):
        print(f'O carro pisou no pedal!')

    @property
    def portas(self):
        """Propriedade Portas"""
        return self.__portas
    
    @portas.setter
    def portas(self, quant: int):
        if(type(quant) != int):
            raise TypeError('Tipo incorreto! Precisa ser uma Int')
        if(quant <= 0):
            raise ValueError('Portas não pode ser menor que ou igual a Zero')
        if(quant > 6):
            raise ValueError('Portas não pode ser maior que 6')
    
    @portas.deleter
    def portas(self):
        self.__portas = 1

    def __str__(self) -> str:
        return super().__str__() + f', Portas: {self.__portas}'


cusca = Veiculo('volkis', 'Fusção', 'Laranja', 1945)

car = Carro('Fiat', 'Uno', 2007, 'roxo', 4)

cusca.freiar()
car.freiar()
