dudes = []

nome = ''
preco = -1
meia = ''
carteirinha = ''

while(True):
    while( not(nome == '0') and len(nome) <= 4):
        nome = input('Digite o seu nome ou 0 para finalizar: ')

    if(nome == '0'):
            break
    while(preco <= 0):
        try:
            preco = float(input('Digite o valor do ingresso: '))
        except ValueError:
            print('Valor precisa ser um número!')
    while(True):
        meia = input('É  meia entrada? digite sim ou não: ')
        if(meia.lower() == 'sim'):
            meia = True
            break
        elif(meia.lower() == 'não'):
            meia = False
            break
    if(meia):
        while(len(carteirinha) <= 4):
            carteirinha = input('Digite o código da sua carteirinha: ')
    dudes.append(
        {
            'name': nome, 'price': preco, 'meia': meia, 'card': carteirinha
        }
    )
    nome = ''
    preco = -1
    meia = ''
    carteirinha = ''
    total = 0
for i in dudes:
    total += i['price']

print(f'Valor total de todos os ingressos: R$ {total:.2f}')
print('Ingressos comprados: ')
for i in dudes:
    print(f'    Comprador: {i['name']}, Tipo de ingresso: {'Meia' if i['meia'] else 'Inteira'}')

