def factorial(num: int) -> int:
    mult = 1
    for i in range(1, num + 1):
        mult *= i
    return mult

n = int(input('Digite um inteiro: '))

print(f'Fatorial de {n} é: {factorial(n)} ')