from typing import Literal

class Habilitacao:
    __des = {'A': 'Permite conduzir veículos com duas ou três rodas, ou seja, motos, motonetas e triciclos',
     'B': 'Permite a condução de veículos de 4 rodas (carros) com peso total de 35,5 toneladas',
     'C': 'Permite dirigir veículos de carga (como caminhões e tratores) e veículos agrícolas com mais de 3,5 toneladas e que não passem de 6 toneladas em conjunto, além de todos os descritos na categoria B',
     'D': 'Permite dirigir todos os veículos dos grupos B e C, além de ônibus, vans e micro-ônibus',
     'E': 'Permite dirigir todos os tipos de veículos das outras categorias, exceto da A, além de autorizar que seja acoplada uma carga superior a 6 toneladas, como um veículo com dois reboques, por exemplo',
     'Nenhuma': 'Permite dirigir os veículos não possuem aceleração nem variação manual de potência, bem como potência nominal máxima de 350 Watts. O motor só poderá funcionar para manutenção da velocidade, que não pode ultrapassar 25 km/h'}
    def __init__(self, tipo: Literal['A', 'B', 'C', 'D', 'E', 'Nenhuma']) -> None:
        self.tipo = tipo
    def getDescricao(self) -> str:
        return self.__des[self.tipo]

class Veiculo:
    def __init__(self, propulsao: Literal['Automotor', 'Elétrico', 'Humana', 'Animal', 'Reboque'],
                 especie: Literal['Passageiros', 'Carga', 'Misto', 'Competição', 'Tração', 'Especial', 'Coleção'],
                 categoria: Literal['Particular', 'Oficial', 'Repre. Diplomática', 'Aluguel', 'Aprendizagem'],
                 nome: str, marca: str, tipoHabilitacao: Literal['A', 'B', 'C', 'D', 'E', 'Nenhuma']  ) -> None:
        self.propulsao = propulsao
        self.especie = especie
        self.categoria = categoria
        self.nome = nome
        self.marca = marca
        self.habilitacao = tipoHabilitacao
    def __str__(self) -> str:
        return f'Nome: {self.nome}, Marca: {self.marca}, Habilitação Neces.: {self.habilitacao}, Tração: {self.propulsao}, Categoria: {self.categoria}, Espécie: {self.especie}, '
    def isHabilitacaoValida(self, hab: Habilitacao) -> bool:
        match self.habilitacao:
            case 'A':
                return hab.tipo == 'A'
            case 'B':
                return hab.tipo in ['B', 'C', 'D', 'E']
            case 'C':
                return hab.tipo in ['C', 'D', 'E']
            case 'D':
                return hab.tipo in ['D', 'E']
            case 'E':
                return hab.tipo == 'E'
            case 'Nenhuma':
                return True

class Passageiros(Veiculo):
    def __init__(self, propulsao: Literal['Automotor', 'Elétrico', 'Humana', 'Animal', 'Reboque'],
                 categoria: Literal['Particular', 'Oficial', 'Repre. Diplomática', 'Aluguel', 'Aprendizagem'],
                 nome: str, marca: str, tipoHabilitacao: Literal['A', 'B', 'C', 'D', 'E', 'Nenhuma'], quantPassageiros: int ) -> None:
        super().__init__(propulsao, 'Passageiros', categoria, nome, marca, tipoHabilitacao)
        self.capacidadePassageiros = quantPassageiros
    def __str__(self) -> str:
        return super().__str__() + f'Capacidade de Pessoas: {self.capacidadePassageiros}'

class Carga(Veiculo):
    def __init__(self, propulsao: Literal['Automotor', 'Elétrico', 'Humana', 'Animal', 'Reboque'],
                 categoria: Literal['Particular', 'Oficial', 'Repre. Diplomática', 'Aluguel', 'Aprendizagem'],
                 nome: str, marca: str, tipoHabilitacao: Literal['A', 'B', 'C', 'D', 'E', 'Nenhuma'], quantCarga: int ) -> None:
        super().__init__(propulsao, 'Carga', categoria, nome, marca, tipoHabilitacao)
        self.capacidadeCarga = quantCarga
    def __str__(self) -> str:
        return super().__str__() + f'Capacidade de carga: {self.capacidadeCarga} Kg'

class Misto(Veiculo):
    def __init__(self, propulsao: Literal['Automotor', 'Elétrico', 'Humana', 'Animal', 'Reboque'],
                 categoria: Literal['Particular', 'Oficial', 'Repre. Diplomática', 'Aluguel', 'Aprendizagem'],
                 nome: str, marca: str, tipoHabilitacao: Literal['A', 'B', 'C', 'D', 'E', 'Nenhuma'], quantPassageiros: int, quantCarga: int ) -> None:
        super().__init__(propulsao, 'Misto', categoria, nome, marca, tipoHabilitacao)
        self.capacidadePassageiros = quantPassageiros
        self.capacidadeCarga = quantCarga
    def __str__(self) -> str:
        return super().__str__() + f'Capacidade de Pessoas: {self.capacidadePassageiros}, Capacidade de carga: {self.capacidadeCarga} Kg'

class Competicao(Veiculo):
    def __init__(self, propulsao: Literal['Automotor', 'Elétrico', 'Humana', 'Animal', 'Reboque'],
                 categoria: Literal['Particular', 'Oficial', 'Repre. Diplomática', 'Aluguel', 'Aprendizagem'],
                 nome: str, marca: str, tipoHabilitacao: Literal['A', 'B', 'C', 'D', 'E', 'Nenhuma'], catCompeticao: str) -> None:
        super().__init__(propulsao, 'Competição', categoria, nome, marca, tipoHabilitacao)
        self.competicao = catCompeticao
    def __str__(self) -> str:
        return super().__str__() + f'Competição: {self.competicao}'

class Tracao(Veiculo):
    def __init__(self, propulsao: Literal['Automotor', 'Elétrico', 'Humana', 'Animal', 'Reboque'],
                 categoria: Literal['Particular', 'Oficial', 'Repre. Diplomática', 'Aluguel', 'Aprendizagem'],
                 nome: str, marca: str, tipoHabilitacao: Literal['A', 'B', 'C', 'D', 'E', 'Nenhuma'],
                 tipo: Literal['Trator de rodas', 'Trator de esteiras', 'Caminhão-trator', 'Trator misto'] ) -> None:
        super().__init__(propulsao, 'Tração', categoria, nome, marca, tipoHabilitacao)
        self.tipoT = tipo
    def __str__(self) -> str:
        return super().__str__() + f'Tipo: {self.tipoT}'
    
        
class Especial(Veiculo):
    def __init__(self, propulsao: Literal['Automotor', 'Elétrico', 'Humana', 'Animal', 'Reboque'],
                 categoria: Literal['Particular', 'Oficial', 'Repre. Diplomática', 'Aluguel', 'Aprendizagem'],
                 nome: str, marca: str, tipoHabilitacao: Literal['A', 'B', 'C', 'D', 'E', 'Nenhuma'],
                 tipo: Literal['Guindastes', 'Caminhões munck', 'Viaturas', 'Carros funerários', 'Ambulâncias', 'Caminhões de bombeiro', 'Food trucks', 'Bases móveis',
                               'Subestações móveis', 'Máquinas perfuratrizes']) -> None:
        super().__init__(propulsao, 'Especial', categoria, nome, marca, tipoHabilitacao)
        self.tipoE = tipo
    def __str__(self) -> str:
        return super().__str__() + f'Tipo: {self.tipoE}'


class Veiculos:
    bicicleta = Passageiros('Humana', 'Particular', 'GTSM1 ARO 29', 'SHIMANO', 'Nenhuma', 1)
    bombeiro = Especial('Automotor', 'Particular', '270', 'Volkswagen', 'C', 'Caminhões de bombeiro')
    ambulancia = Especial('Automotor', 'Particular', 'L1H1', 'Renault', 'D', 'Ambulâncias')
    tesla = Passageiros('Elétrico', 'Particular', 'Model 3', 'Tesla', 'B', 5)
    carro = Passageiros('Automotor', 'Particular', 'Versa 1.6 16V FLEX ADVANCE XTRONIC', 'Nissan', 'B', 5)
    moto = Passageiros('Automotor', 'Particular', 'CB 300F Twister', 'Honda', 'A', 2)
    caminhao = Carga('Automotor', 'Particular', 'Atego', 'Mercedes Benz', 'E', 25000)
    caminhaoEletrico = Carga('Elétrico', 'Particular', 'eT18 21.250', 'Byd', 'E', 21000)
    camioneta = Misto('Automotor', 'Particular', 'Hilux Cabine Simples 2024', 'Toyota', 'C', 2, 6500)
    f1 = Competicao('Automotor', 'Particular', 'AMR23', 'Aston Martin Team', 'B', 'Formula 1')
    #Segunda
    rali = Competicao('Automotor', 'Particular', 'Polo R WRC', 'Volkswagen', 'B', 'Rally')
    celtaEscola = Passageiros('Automotor', 'Aprendizagem', 'Celta', 'Chevrolet', 'B', 5)
    trator = Tracao('Automotor', 'Particular', '814', 'Cat', 'C', 'Trator de rodas')
    esteira = Tracao('Automotor', 'Particular', '814', 'Cat', 'C', 'Trator de esteiras')
    strada = Misto('Automotor', 'Particular', 'Strada', 'Fiat', 'C', 5, 720)
    spin = Passageiros('Automotor', 'Particular', 'Spin', 'Chevrolet', 'B', 7)
    kombi = Passageiros('Automotor', 'Particular', 'Kombi', 'Volkswageb', 'B', 9)
    ex90 = Passageiros('Elétrico', 'Particular', 'EX90', 'Volvo', 'B', 7)
    limo = Passageiros('Automotor', 'Particular', 'Grand Blazer', 'Chevrolet', 'C', 11)
    guindaste = Especial('Automotor', 'Particular', 'ATF90G-4', 'Tadano', 'D', 'Guindastes')
    carroca = Passageiros('Animal', 'Particular', 'Carroça', 'Ipê Roxo', 'Nenhuma', 3)

classDict = {'Passageiros': Passageiros, 'Carga': Carga, 'Misto': Misto, 'Competição': Competicao, 'Tração': Tracao, 'Especial': Especial}

mobile = [value for key, value in Veiculos.__dict__.items() if not key.startswith('__')]


##### Quiz #####
def inputFromList(text: str, cat: list[str]) -> str:
    var = ''
    while var not in cat:
        var = input(text)
    return var

def inputFromRange(text: str, min: int, max: int)-> int:
    num = 9999999
    while not(min <= num <= max):
        try:
            num = int(input(text))
        except ValueError as e:
            print('Valor precisa ser um número inteiro.', e)
    return num


def deleteInvalido(array: list[Veiculo], attName: str, value: str | int) -> list[Veiculo] | None:
    selec = []
    try:
        for element in array:
            if(hasattr(element, attName)):
                if(type(value) == str and  getattr(element, attName) == value):
                    selec.append(element)
                elif(type(value) == int and getattr(element, attName) >= value):
                    selec.append(element)
    except TypeError as e:
        print(f'Nenhum veículo com as opções seleciondas! {e}')
        exit()
    return selec if len(selec) != 0 else None

userInput = inputFromList('Digite qual tipo de veículo vc deseja: Passageiros, Carga, Misto(Carga e passageiros), Competição ou Tração ou Especial:\n',
                           ['Passageiros', 'Carga', 'Misto', 'Competição', 'Tração', 'Especial'])
userCat = userInput #Salvar categoria para usar depois

potencial = []
for element in mobile:
    if(isinstance(element, classDict[userInput])):
        potencial.append(element)

userInput = inputFromList('Digite qual categoria de veículo você deseja: Particular, Oficial, Repre. Diplomática, Aluguel ou Aprendizagem:\n',
                           ['Particular', 'Oficial', 'Repre. Diplomática', 'Aluguel', 'Aprendizagem'])
potencial = deleteInvalido(potencial, 'categoria', userInput)


userInput = inputFromList('Digite qual tipo tração deseja: Automotor, Elétrico, Humana, Animal ou Reboque:\n', ['Automotor', 'Elétrico', 'Humana', 'Animal', 'Reboque'])
potencial = deleteInvalido(potencial, 'propulsao', userInput)


match userCat:
    case 'Passageiros':
        userInput = inputFromList('Digite quantos passageiros você deseja levar(incluindo o motorista)? Min:1 e Max: 12\n', [str(x) for x in range(1, 12)])
        potencial = deleteInvalido(potencial, 'capacidadePassageiros', int(userInput))
    case 'Carga':
        userInput = inputFromRange('Digite qual a quantidade de carga que deseja levar em Kg? Min:1 e Max: 25000\n', 1, 25000)
        potencial = deleteInvalido(potencial, 'capacidadeCarga', userInput)
    case 'Misto':
        userInput = inputFromList('Digite quantos passageiros você deseja levar(incluindo o motorista)? Min:1 e Max: 12\n', [str(x) for x in range(1, 12)])
        potencial = deleteInvalido(potencial, 'capacidadePassageiros', int(userInput))
        userInput = inputFromRange('Digite qual a quantidade de carga que deseja levar em Kg? Min:1 e Max: 25000\n', 1, 25000)
        potencial = deleteInvalido(potencial, 'capacidadeCarga', userInput)
    case 'Competição':
        userInput = inputFromList('Digite para qual competição? Formula 1 ou Rally\n', ['Formula 1', 'Rally'])
        potencial = deleteInvalido(potencial, 'competicao', userInput)
    case 'Tração':
        userInput = inputFromList('Digite qual tipo de veículo de tração você deseja? Trator de rodas, Trator de esteiras, Caminhão-trator ou Trator misto\n', ['Trator de rodas', 'Trator de esteiras', 'Caminhão-trator', 'Trator misto'])
        potencial = deleteInvalido(potencial, 'tipoT', userInput)
    case 'Especial':
        userInput = inputFromList('Digite qual tipo de veículo especial você deseja? Guindastes, Caminhões munck, Viaturas, Carros funerários, Ambulâncias, Caminhões de bombeiro, Food trucks, Bases móveis,\
                                   Subestações móveis, Máquinas perfuratrizes\n', ['Guindastes', 'Caminhões munck', 'Viaturas', 'Carros funerários', 'Ambulâncias',
                                  'Caminhões de bombeiro', 'Food trucks', 'Bases móveis', 'Subestações móveis', 'Máquinas perfuratrizes'])
        potencial = deleteInvalido(potencial, 'tipoE', userInput)

userHab = inputFromList('Digite qual habilitação você possui. Digite A, B, C, D, E ou Nenhuma\n', ['A', 'B', 'C', 'D', 'E', 'Nenhuma'])
userHab = Habilitacao(userHab)

try:
    print('Lista de Veículos disponiveis:\n')
    for idx, item in enumerate(potencial):
        print(f'{idx} - Nome: {item.nome}')
except TypeError as e:
    print('Nenhum veículo com as caracteristicas seleciondas!')
    exit(0)
except:
    print('Algo deu errado. lol!')

while True:
    choice = ''
    choice = inputFromRange('Digite qual veículo você deseja: ', 0, len(potencial) - 1)
    print(f'Veículo selecionado:\n{potencial[choice]}\n')

    if(potencial[choice].isHabilitacaoValida(userHab)):
        print('Habilitação compativel com veículo!')
    else:
        print(f'Habilitação inválida para o veículo selecionado!')
        continue

    confirm = inputFromList('Deseja confirmar a sua escolha? Digite sim ou não\n', ['sim', 'não'])
    print()
    
    if(confirm == 'sim'):
        print(f'Veículo escolhido:\n{potencial[choice]}\n')
        break
    print(f'Selecione um novo veículo.\n')



