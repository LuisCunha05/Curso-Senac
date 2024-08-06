class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float, peso: float, estadoCivil: str) -> None:
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.estadoCivil = estadoCivil

    def __str__(self) -> str:
        return f'Nome: {self.nome}, Idade: {self.idade}, Altura: {self.altura}, Peso: {self.peso}, Estado Civil: {self.estadoCivil}'


class Estudante(Pessoa):
    def __init__(self, nome: str, idade: int, altura: float, peso: float, estadoCivil: str, instituicao: str, turma: int) -> None:
        super().__init__(nome, idade, altura, peso, estadoCivil)
        self.instituicao = instituicao
        self.turma = turma
    
    def __str__(self) -> str:
        return super().__str__() + f', Instituição: {self.instituicao}'


doido = Estudante('Kaka', 24, 1.75, 64.5, 'Solteiro', 'Senac', 233)
print(doido)


