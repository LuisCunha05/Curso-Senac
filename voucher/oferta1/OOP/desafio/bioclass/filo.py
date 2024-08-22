from bioclass.reino import Reino

class Filo(Reino):
    def __init__(self, reino: str = ' ', nutricao: str = ' ', organizacao: str = ' ', respiracao: str = ' ', filo: str = ' ', caract_filo: str = ' ') -> None:
        super().__init__(reino, nutricao, organizacao, respiracao)
        self.filo = filo
        self.caracterisca_filo = caract_filo

    def __str__(self) -> str:
        return super().__str__() + f', Filo: {self.filo}'
    
    def addReino(self, arg: Reino):
        self.reino = arg.reino
        self.nutricao = arg.nutricao
        self.organizacao = arg.organizacao
        self.respiracao = arg.respiracao

