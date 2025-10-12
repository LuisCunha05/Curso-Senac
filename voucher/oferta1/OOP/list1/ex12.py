def mediaInput():
    entrada = 1
    count = 0
    sum = 0
    print('Digite 0 para sair!')
    while(entrada != 0):    
        try:
            entrada = float(input(f'Digite o {count + 1} número: '))
        except ValueError:
            print('Valor precisa ser um número!')
        if(entrada == 0):
            break
        sum += entrada
        count += 1
    return round(sum/count, 2)



print(f'Média dos números digitados é {mediaInput():5.2f}')