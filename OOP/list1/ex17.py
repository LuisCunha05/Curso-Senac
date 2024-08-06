try:
    n = int(input('Digite um inteiro para verificar: '))
    if(n <= 0):
        raise ValueError
except ValueError:
    print('Valor precisa ser um inteiro positivo!')

print(f'A soma dos números pares até {n} é: {sum(range(2, n + 1, 2))}')
