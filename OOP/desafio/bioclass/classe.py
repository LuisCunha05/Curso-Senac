from bioclass.filo import Filo

class Classe(Filo):
    def __init__(self, reino: str = ' ', nutricao: str = ' ', organizacao: str = ' ', respiracao: str = ' ', filo: str = ' ', caract_filo: str = ' ', classe: str = ' ',
                 caract_classe: str = ' ') -> None:
        super().__init__(reino, nutricao, organizacao, respiracao, filo, caract_filo)
        self.classe = classe
        self.caracterisca_classe = caract_classe
        
    def __str__(self) -> str:
        return super().__str__() + f', Classe: {self.classe}'
    def addFilo(self, arg: Filo):
        self.reino = arg.reino
        self.nutricao = arg.nutricao
        self.organizacao = arg.organizacao
        self.respiracao = arg.respiracao
        self.filo = arg.filo
        self.caracterisca_filo = arg.caracterisca_filo
