from bioclass.classe import Classe

class Ordem(Classe):
    def __init__(self, reino: str = ' ', nutricao: str = ' ', organizacao: str = ' ', respiracao: str = ' ', filo: str = ' ', caract_filo: str = ' ', classe: str = ' ',
                 caract_classe: str = ' ', ordem: str = ' ', caract_ordem: str = ' ') -> None:
        super().__init__(reino, nutricao, organizacao, respiracao, filo, caract_filo, classe, caract_classe)
        self.ordem = ordem
        self.caracterisca_ordem = caract_ordem
    def __str__(self) -> str:
        return super().__str__() + f', Ordem: {self.ordem}'
    def addClasse(self, arg: Classe):
        self.reino = arg.reino
        self.nutricao = arg.nutricao
        self.organizacao = arg.organizacao
        self.respiracao = arg.respiracao
        self.filo = arg.filo
        self.caracterisca_filo = arg.caracterisca_filo
        self.classe = arg.classe
        self.caracterisca_classe = arg.caracterisca_classe
