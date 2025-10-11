"""
Solicite ao usuário que digite um número natural qualquer (inteiro e positivo).
Implemente uma função recursiva que seja capaz de somar todos os números até o número que foi digitado pelo usuário.
Importante: não utilize nenhum laço (estrutura de repetição) no programa!
Exiba em tela o resultado da soma desses números.
"""

def recursiveSum(num: int) -> int:
    if(num == 1):return 1
    if(num <= 0):return 0

    return num + recursiveSum(num - 1)

entrada: int = -1
while(entrada < 0):
    try:
        entrada = int(input('Digite um número inteiro positivo: '))
        if(entrada < 0):
            print('Número precisa ser maior ou igual a Zero')
    except ValueError:
        print('Entrada inválida\n')
        entrada = -1

print(f"Soma dos {entrada} números naturais: {recursiveSum(entrada)}")