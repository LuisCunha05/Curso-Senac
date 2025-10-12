def isPrimeNumber(number: int) -> bool:
    if(not(number & 1)):
        if(number == 2):
            return True
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if(number % i == 0):
            return False
        
    return True

try:
    n = int(input('Digite um inteiro para verificar: '))
except ValueError:
    print('Valor precisa ser um inteiro!')

print(f'O número {n} é primo: {'Sim' if isPrimeNumber(n) else 'Não'}')


