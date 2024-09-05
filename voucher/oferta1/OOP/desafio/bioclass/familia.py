from bioclass.ordem import Ordem

class Familia(Ordem):
    def __init__(self, reino: str = ' ', nutricao: str = ' ', organizacao: str = ' ', respiracao: str = ' ', filo: str = ' ', caract_filo: str = ' ', classe: str = ' ',
                 caract_classe: str = ' ', ordem: str = ' ', caract_ordem: str = ' ', familia: str = ' ', caract_familia: str = ' ') -> None:
        super().__init__(reino, nutricao, organizacao, respiracao, filo, caract_filo, classe, caract_classe, ordem, caract_ordem)
        self.familia = familia
        self.caracterisca_familia = caract_familia
    def __str__(self) -> str:
        return super().__str__() + f', Família: {self.familia}'
    def addOrdem(self, arg: Ordem):
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