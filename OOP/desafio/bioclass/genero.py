from bioclass.familia import Familia

class Genero(Familia):
    def __init__(self, reino: str = ' ', nutricao: str = ' ', organizacao: str = ' ', respiracao: str = ' ', filo: str = ' ', caract_filo: str = ' ', classe: str = ' ',
                 caract_classe: str = ' ', ordem: str = ' ', caract_ordem: str = ' ', familia: str = ' ', caract_familia: str = ' ', genero: str = ' ', caract_genero: str = ' ') -> None:
        super().__init__(reino, nutricao, organizacao, respiracao, filo, caract_filo, classe, caract_classe, ordem, caract_ordem, familia, caract_familia)
        self.genero = genero
        self.caracterisca_genero = caract_genero
    def __str__(self) -> str:
        return super().__str__() + f', Género: {self.genero}'
    def addFamilia(self, arg: Familia):
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