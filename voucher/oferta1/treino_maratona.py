entrada = ''
users = []
while(True):
    while(True):
        try:
            entrada = input("Digite o nome completo do cliente (ou digite 'sair' para encerrar): ")
            if(entrada == 'sair'):
                break
            temp = ''.join(entrada.split(' '))
            assert temp.isalpha()
            break
        except AssertionError:
            print('A entrada deve conter apenas caracteres a-z. Digite novamente')
            entrada = ''
    if(entrada == 'sair'):
        break
    else:
        users.append(entrada)

    while(True):
        try:
            entrada = input("Digite o RG do cliente: ")
            assert entrada.isdecimal()
            break
        except AssertionError:
            print('A entrada deve conter apenas números de 0-9. Digite novamente')
            entrada = ''
    users.append(entrada)

    while(True):
        try:
            entrada = input("Digite o CPF do cliente: ")
            assert entrada.isdecimal()
            break
        except AssertionError:
            print('A entrada deve conter apenas números de 0-9. Digite novamente')
            entrada = ''
    users.append(entrada)

    while(True):
        try:
            entrada = input("Digite o telefone do cliente: ")
            assert entrada.isdecimal()
            break
        except AssertionError:
            print('A entrada deve conter apenas números de 0-9. Digite novamente')
            entrada = ''
    users.append(entrada)

print(f'Cadastro de Clientes:\n====================')

for idx in range(0, len(users), 4):
    print(f'Nome: {users[idx]}, RG: {users[idx + 1]}, CPF: {users[idx + 2]}, Telefone: {users[idx + 3]}')

