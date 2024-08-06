class Pessoa:
    nome = 'Sem Nome'
    idade = 0
    peso = .0
    altura = .0
    otaku = False

    def setNome(self, name: str) -> str:
        self.nome = name
        return self.nome
    def setIdade(self, age: int) -> int:
        self.idade = age
        return self.idade
    def setWeight(self, weight: float) -> float:
        self.peso = weight
        return self.peso
    def setHeight(self, height: float) -> float:
        self.altura = height
        return self.altura
    def isOtaku(self) -> str:
        return 'Sim, é otaku!' if self.otaku else 'Não é otaku!'
    def __str__(self) -> str:
        return f'Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso}, Altura: {self.altura} e È otaku? {self.isOtaku()}'
    

class Estudante(Pessoa):
    instituicao = ''
    bolsa = 'Nenhuma'

    def setInstituicao(self, nome: str) -> str:
        self.instituicao = nome
        return self.instituicao
    def setBolsa(self, tipo: str) -> str:
        self.bolsa = tipo
        return self.bolsa
    
class Trabalhador(Pessoa):
    cargo = 'Nenhum'
    empresa = 'Nenhum'

    def setCargo(self, cargo: str) -> str:
        self.cargo = cargo
        return self.cargo
    def setEmpresa(self, nome: str) -> str:
        self.empresa = nome
        return self.empresa
    
doido = Estudante()
doido.setNome(input('Digite seu nome: '))
doido.setInstituicao(input('Digite a instituição: '))

print(doido.nome, doido.instituicao)

ferrado = Trabalhador()
ferrado.setNome(input('Digite o nome do ferrado: '))
ferrado.setCargo(input('Digite seu cargo: '))

print(ferrado.nome, ferrado.cargo)
