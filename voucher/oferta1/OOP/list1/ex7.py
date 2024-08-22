from random import random as rng

def coinThrow():
    if(rng() > 0.5):
        return 'Cara'
    else:
        return 'Coroa'
    
def doXCoinThrows(num: int) -> list[str]:
    coins = []
    for _ in range(num):
        coins.append(coinThrow())
    return coins

n = int(input('Digite a quantidade de lançamento: '))

moedas = doXCoinThrows(n)

caras = coroas = 0
for i in range(len(moedas)):
    if(moedas[i] == 'Cara'):
        caras += 1
    else:
        coroas += 1

print(f'Quantidade de Caras: {caras}, Porcentagem: {caras/n:.2f}')
print(f'Quantidade de Coroas: {coroas}, Porcentagem: {coroas/n:.2f}')


