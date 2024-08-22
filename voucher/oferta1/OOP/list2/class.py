class Empresa:
    nomeOficial = ''
    cnpj = ''
    tempoDeAtividade = 0

    def setName(self, name: str) -> str:
        self.nomeOficial = name
        return self.nomeOficial
    def setTempoAtividade(self, year: int) -> int:
        self.tempoDeAtividade = year
        return self.tempoDeAtividade
    def setCNPJ(self, cnpj: str) -> str:
        self.cnpj = cnpj
        return self.cnpj
    def __str__(self) -> str:
        return f'Nome Oficial: {self.nomeOficial}, CNPJ: {self.cnpj} e Tempo de atividade: {self.tempoDeAtividade}.'
    

empress = Empresa()

empress.setName(input('Digite o nome da empresa: '))
empress.setCNPJ(input('Digite o CNPJ da empresa: '))
empress.setTempoAtividade(input('Digite o tempo de atividade da empresa: '))

print(empress)

empress2 = Empresa()

print(empress2)