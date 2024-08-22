def fibo(num: int):
    array = [0, 1]
    
    if(num > 2):
        for i in range(2, num + 1):
            array.append(array[i - 2] + array[i - 1])

    for i in range(num):
            print(array[i], end=' ')

try:
    n = int(input('Digite um inteiro: '))
    if(n <= 0):
        raise ValueError
except ValueError:
    print('Valor precisa ser um inteiro positivo!')

fibo(n)