from time import time
ini = time()
def isPerfect(num: int) -> bool:
    sum = 0
    for i in range(1, num//2 + 1):
        if(num % i == 0):
            sum += i
            print(f'i: {i:20,}{sum:20,}')
        if(sum > num):
            break
    print(sum)
    return num == sum

a = int(input('Digite um inteiro: '))

print(f'{a} é perfeito: {'Sim' if isPerfect(a) else 'Não'}')
print(time() - ini)