def reverse(something):
    algo = str(something)
    
    for i in range(-1, -(len(algo) + 1), -1):
        print(algo[i], end='')

a = input('Digite um número: ')

print('Seu número: ' + a)
reverse(a)