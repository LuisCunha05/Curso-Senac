from bioclass.especie import Especie


class Individuo(Especie):
    def __init__(self, reino: object, filo: object, classe: object, ordem: object, familia: object, genero: object, especie: object, nome: str) -> None:
        super().__init__(reino, filo, classe, ordem, familia, genero, especie)
        self.nome = nome
    def __str__(self) -> str:
        return super().__str__() + f', Nome: {self.nome}'


