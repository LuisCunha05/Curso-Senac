from random import random as rng
from math import floor


def dado():
    cubo = [1, 2, 3, 4, 5, 6]
    return cubo[floor(6 * rng())]
    
def doXDado(num: int) -> list[str]:
    dados = []
    for _ in range(num):
        dados.append(dado())
    return dados

n = int(input('Digite a quantidade de lançamento: '))

dados = doXDado(n)

quantidade = {k:0 for k in range(1,7)}

for i in range(len(dados)):
    match(dados[i]):
        case 1:
            quantidade[1] += 1
        case 2:
            quantidade[2] += 1
        case 3:
            quantidade[3] += 1
        case 4:
            quantidade[4] += 1
        case 5:
            quantidade[5] += 1
        case 6:
            quantidade[6] += 1

for key, value in quantidade.items():
    print(f'Quantidade da face {key}: {value}, Porcentagem: {value/n:.3f}')


