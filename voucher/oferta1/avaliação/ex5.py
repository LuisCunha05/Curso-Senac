salt = float(input('Digite o valor do sálario: '))

tax = 0

if(salt <= 2000.):
    print('Isento')
else:
    if(salt <= 3000.):
        tax = (salt - 2000.) * 0.08
    elif(salt <= 4500.):
        tax = 80. + (salt - 3000.) * 0.18
    else:
        tax = 80 + 270 + (salt - 4500) * 0.28
    print(f'R$ {tax:.2f}')
