from bioclass.genero import Genero

class Especie(Genero):
    def __init__(self, reino: str = ' ', nutricao: str = ' ', organizacao: str = ' ', respiracao: str = ' ', filo: str = ' ', caract_filo: str = ' ', classe: str = ' ',
                 caract_classe: str = ' ', ordem: str = ' ', caract_ordem: str = ' ', familia: str = ' ', caract_familia: str = ' ', genero: str = ' ', caract_genero: str = ' ',
                 especie: str = ' ', nome_popular: str = ' ') -> None:
        super().__init__(reino, nutricao, organizacao, respiracao, filo, caract_filo, classe, caract_classe, ordem, caract_ordem, familia, caract_familia, genero, caract_genero)
        self.especie = especie
        self.nome_popular = nome_popular
    def __str__(self) -> str:
        return super().__str__() + f', Espécie: {self.especie}, Nome Popular: {self.nome_popular}'
    def addGenero(self, arg: Genero):
        self.reino = arg.reino
        self.nutricao = arg.nutricao
        self.organizacao = arg.organizacao
        self.respiracao = arg.respiracao
        self.filo = arg.filo
        self.caracterisca_filo = arg.caracterisca_filo
        self.classe = arg.classe
        self.caracterisca_classe = arg.caracterisca_classe
        self.ordem = arg.ordem
        self.caracterisca_ordem = arg.caracterisca_ordem
        self.familia = arg.familia
        self.caracterisca_familia = arg.caracterisca_familia
        self.genero = arg.genero
        self.caracterisca_genero = arg.caracterisca_genero