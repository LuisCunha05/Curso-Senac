agenda : dict[str, str] = {'Maria':'993459942', 'João':'995434444'}

def validateName() -> str:
    name = ''
    while(True):
        name = input('Digite o nome: ')
        if(name.isalpha()):
            break



while(True):
    print(f'Agenda Digital:\n',
           '1 - Adicionar contato\n',
           '2 - Buscar contato\n',
           '3 - Remover contato\n',
           '0 - Sair')
    option = ''
    while(option not in '0123' or len(option) != 1):
        option = input('Digite o número da opção desejada: ')
    
    match(option):
        case '0':
            print('Até logo!')
            break
        case '1':
            name = ''
            while(True):
                name = input('Digite o nome que deseja buscar: ')
                if(name.isalpha()):
                    break
            
        case '2':
            pass
        case '0':
            break

