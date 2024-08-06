from random import sample
from random import randint



class Bingo:
    def __init__(self) -> None:
        self.tabela = [
            sample([x for x in range(1, 16)], 5),
            sample([x for x in range(16, 31)], 5),
            sample([x for x in range(31, 46)], 5),
            sample([x for x in range(46, 61)], 5),
            sample([x for x in range(61, 76)], 5)
        ]
        self.tabela[2][2] = 0 
        self.linhas = [
            {self.tabela[0][idx] for idx in range(5)},
            {self.tabela[1][idx] for idx in range(5)},
            {self.tabela[2][idx] for idx in range(5)},
            {self.tabela[3][idx] for idx in range(5)},
            {self.tabela[4][idx] for idx in range(5)}
        ]
        self.colunas = [
            {self.tabela[idx][0] for idx in range(5)},
            {self.tabela[idx][1] for idx in range(5)},
            {self.tabela[idx][2] for idx in range(5)},
            {self.tabela[idx][3] for idx in range(5)},
            {self.tabela[idx][4] for idx in range(5)}
        ]
        self.diagonais = [
            {self.tabela[idx][idx] for idx in range(5)},
            {self.tabela[idx][-(idx + 1)] for idx in range(5)}
        ]
    
class NumeroBingo:
    def __init__(self) -> None:
        self.__numbers = [x for x in range(1, 76)]
    def getNumber(self) -> int | None:
        #Retorna um número aleatório sem repetições ou None caso não haja mais números restantes

        if(len(self._NumeroBingo__numbers) != 0):
            idx = randint(0, len(self._NumeroBingo__numbers) - 1)
            temp = self._NumeroBingo__numbers[idx]
            del self._NumeroBingo__numbers[idx]
            return temp
        else:
            return None
    def reserBingo(self) -> None:
        self._NumeroBingo__numbers = [x for x in range(1, 76)]


bin = Bingo()

for item in bin.diagonais:
    print(item)


