class Reino:
    def __init__(self, reino: str = ' ', nutricao: str = ' ', organizacao: str = ' ', respiracao: str = ' ') -> None:
        """ 
        Argumentos:
        -   nutricao: Autotrófico | Heterotrófico
        -   organizacao: Unicelular | Multicelular
        -   respiracao: Aeróbico | Anaeróbico
        """
        self.reino = reino
        self.nutricao = nutricao
        self.organizacao = organizacao
        self.respiracao = respiracao
    def __str__(self) -> str:
        return f'Reino: {self.reino}'
    

