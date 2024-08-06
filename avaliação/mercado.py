
produtosCat = ['Higiene', 'Alimento']
subHiegene = ['Pessoal', 'Carro']
subAlimento = ['Carnes', 'Legumes']

pessoalProdutos = ['Creme dental', 'Sabonete']
pessoalPreco = [4.55, 2.33]
pessoalDesc = 'Tipo: Higiene, Subtipo: Pessoal'
pessoalCod = ['101', '102']

carroProdutos = ['Aromatizante', 'Aspirado de Pó']
carroPreco = [15.22, 233.98]
carroDesc = 'Tipo: Higiene, Subtipo: Carro'
carroCod = ['201', '202']

carneProdutos = ['Costela', 'Bistéca']
carnePreco = [25.74, 17.34]
carneDesc = 'Tipo: Alimento, Subtipo: Carnes'
carneCod = ['301', '302']

legumeProdutos = ['Beterraba', 'Cenoura']
legumePreco = [4.77, 6.44]
legumeDesc = 'Tipo: Alimento, Subtipo: Legumes'
legumeCod = ['401', '402']


print('Bem vindo a SuperLoja!')

##____Validação Nome____##
nome = ''
while(len(nome) <= 3):
    nome = input('Digite seu nome: ')

##____Validação CPF____##
cpf = ''
cpfNotOK = True
while(len(cpf) < 11 or cpfNotOK):
    cpfNotOK = False
    cpf = input('Digite seu CPF: ')
    for char in cpf:
        if(char not in '0123456789'):
            cpfNotOK = True
            break
matricula = ''
bornDate = ''

carrinho = []
preco = []

while(True):
    isFuncionario = ''
    while(not(isFuncionario == 'sim' or isFuncionario == 'não' or isFuncionario == 'sair')):
        isFuncionario = input('Você é um funcionário da loja? Digite sim, não ou sair para finalizar ')
    if(isFuncionario == 'sair'):
        break
    ##____Area do Funcionario____##
    if(isFuncionario == 'sim'):

    ##____Validação da Matricula____##
        while(len(matricula) < 4):
            matricula = input('Digite a sua matricula: ')

    ##____Validação da data____##
        bornDateNotOK = True
        while(len(bornDate) < 10 or bornDateNotOK):
            bornDateNotOK = False
            bornDate = input('Digite sua data de nascimento no formato DD/MM/AAAA: ')
            for char in bornDate:
                if(char not in '/0123456789'):
                    bornDateNotOK = True
                    break
            if(bornDate[0] not in '0123'):
                bornDateNotOK = True
            elif(bornDate[0] == '0' and bornDate[1] == '0'):
                bornDateNotOK = True
            elif(bornDate[0] == '3' and bornDate[1] not in '01'):
                bornDateNotOK = True
            elif(not(bornDate[2] == '/')):
                bornDateNotOK = True
            elif(bornDate[3] not in '01'):
                bornDateNotOK = True
            elif(bornDate[3] == '0' and bornDate[4] == '0'):
                bornDateNotOK = True
            elif(bornDate[3] == '1' and bornDate[4] not in '012'):
                bornDateNotOK = True
            elif(bornDate[4] not in '0123456789'):
                bornDateNotOK = True
            elif(not(bornDate[5] == '/')):
                bornDateNotOK = True
            elif(bornDate[6] not in '12'):
                bornDateNotOK = True
            elif(bornDate[7] not in '09'):
                bornDateNotOK = True
            elif(bornDate[6] == '1' and bornDate[7] == '0'):
                bornDateNotOK = True
            elif(bornDate[7] == '9' and bornDate[8] in '01'):
                bornDateNotOK = True
            elif(bornDate[6] == '2' and not(bornDate[7] == '0')):
                bornDateNotOK = True
            elif(bornDate[6] == '2' and bornDate[8] not in '012'):
                bornDateNotOK = True
            elif(bornDate[6] == '2' and bornDate[8] == '2' and bornDate[9] not  in '01234'):
                bornDateNotOK = True
            elif(bornDate[8] not in '0123456789'):
                bornDateNotOK = True
            elif(bornDate[9] not in '0123456789'):
                bornDateNotOK = True


        while(True):
            option = 'x'
            print('\nDigite o número da opção que deseja acessar:',
                  '\n1 - Exibir Estoque',
                  '\n2 - Atualizar Estoque,',
                  '\n3 - Adicionar ao Estoque',
                  '\n0 - Sair')
            while(option not in '0123' or len(option) != 1):
                option = input('Digite a opção: ')
            if(option == '1'):
                for prod in produtosCat:
                    print('\nCategoria:', prod)
                    if prod == 'Higiene':
                        for prodHi in subHiegene:
                            if(prodHi == 'Pessoal'):
                                for i in range(len(pessoalProdutos)):
                                    print('\nNome do produto: ' + pessoalProdutos[i],
                                          '\nPreço: R$ ' + str(pessoalPreco[i]),
                                          '\nDescrição: ' + pessoalDesc,
                                          '\nCódigo do produto: ' + pessoalCod[i])
                            else:
                                for i in range(len(carroProdutos)):
                                    print('\nNome do produto: ' + carroProdutos[i],
                                          '\nPreço: R$ ' + str(carroPreco[i]),
                                          '\nDescrição: ' + carroDesc,
                                          '\nCódigo do produto: ' + carroCod[i])
                    else:
                        for prodAl in subAlimento:
                            if(prodAl == 'Carnes'):
                                for i in range(len(carneProdutos)):
                                    print('\nNome do produto: ' + carneProdutos[i],
                                          '\nPreço: R$ ' + str(carnePreco[i]),
                                          '\nDescrição: ' + carneDesc,
                                          '\nCódigo do produto: ' + carneCod[i])
                            else:
                                for i in range(len(legumeProdutos)):
                                    print('\nNome do produto: ' + legumeProdutos[i],
                                          '\nPreço: R$ ' + str(legumePreco[i]),
                                          '\nDescrição: ' + legumeDesc,
                                          '\nCódigo do produto: ' + legumeCod[i])                                 
            elif(option == '2'):
                ##____Encontrar Categoria____##
                novaEntrada = 'x'
                print('\nCategorias:',
                      '\n1 - ' + produtosCat[0],
                      '\n2 - ' + produtosCat[1])
                while(novaEntrada not in '12' or len(novaEntrada) != 1):
                    novaEntrada = input('Digite em qual catergoria deseja entrar: ')
                if(novaEntrada == '1'):
                    ##____Encontrar Subcategoria____##
                    novaEntrada = 'x'
                    print('\nSubcategorias:',
                      '\n1 - ' + subHiegene[0],
                      '\n2 - ' + subHiegene[1])
                    while(novaEntrada not in '12' or len(novaEntrada) != 1):
                        novaEntrada = input('Digite em qual subcatergoria deseja entrar: ')
                    ##____Higiene Pessoal____##
                    if(novaEntrada == '1'):
                        listIndexString = ''
                        for i in range(len(pessoalProdutos)):
                            print(str(i) + ' - Nome: ' + pessoalProdutos[i] + ', Preço: R$ ' + str(pessoalPreco[i]))
                            listIndexString += str(i)
                        novaEntrada = 'x'
                        print(listIndexString)
                        while(novaEntrada not in listIndexString):
                            novaEntrada = input('Digite qual produto deseja alterar o preço: ')
                        print('Produto selecionado: ' + pessoalProdutos[int(novaEntrada)])
                        novoPreco = 'x'
                        precoNotOk = True
                        while(precoNotOk):
                            precoNotOk = False
                            dotCounter = 0
                            novoPreco = input('Digite o novo preço do produto:')
                            for char in novoPreco:
                                if(char not in '0123456789.'):
                                    precoNotOk = True
                                    break
                                if(char == '.'):
                                    dotCounter += 1
                            if(dotCounter > 1):
                                precoNotOk = True
                        pessoalPreco[int(novaEntrada)] = float(novoPreco)
                        print('Valor atualizado: Nome: ' + pessoalProdutos[int(novaEntrada)] + ', Preço: R$ ' + str(pessoalPreco[int(novaEntrada)]))
                    else:
                        ##____Higiene Carro____##
                        listIndexString = ''
                        for i in range(len(carroProdutos)):
                            print(str(i) + ' - Nome: ' + carroProdutos[i] + ', Preço: R$ ' + str(carroPreco[i]))
                            listIndexString += str(i)
                        novaEntrada = 'x'
                        print(listIndexString)
                        while(novaEntrada not in listIndexString):
                            novaEntrada = input('Digite qual produto deseja alterar o preço: ')
                        print('Produto selecionado: ' + carroProdutos[int(novaEntrada)])
                        novoPreco = 'x'
                        precoNotOk = True
                        while(precoNotOk):
                            precoNotOk = False
                            dotCounter = 0
                            novoPreco = input('Digite o novo preço do produto:')
                            for char in novoPreco:
                                if(char not in '0123456789.'):
                                    precoNotOk = True
                                    break
                                if(char == '.'):
                                    dotCounter += 1
                            if(dotCounter > 1):
                                precoNotOk = True
                        carroPreco[int(novaEntrada)] = float(novoPreco)
                        print('Valor atualizado: Nome: ' + carroProdutos[int(novaEntrada)] + ', Preço: R$ ' + str(carroPreco[int(novaEntrada)]))
                else:
                    ##____Encontrar Subcategoria____##
                    novaEntrada = 'x'
                    print('\nSubcategorias:',
                      '\n1 - ' + subAlimento[0],
                      '\n2 - ' + subAlimento[1])
                    while(novaEntrada not in '12' or len(novaEntrada) != 1):
                        novaEntrada = input('Digite em qual subcatergoria deseja entrar: ')
                    ##____Alimento Carne____##
                    if(novaEntrada == '1'):
                        listIndexString = ''
                        for i in range(len(carneProdutos)):
                            print(str(i) + ' - Nome: ' + carneProdutos[i] + ', Preço: R$ ' + str(carnePreco[i]))
                            listIndexString += str(i)
                        novaEntrada = 'x'
                        print(listIndexString)
                        while(novaEntrada not in listIndexString):
                            novaEntrada = input('Digite qual produto deseja alterar o preço: ')
                        print('Produto selecionado: ' + carneProdutos[int(novaEntrada)])
                        novoPreco = 'x'
                        precoNotOk = True
                        while(precoNotOk):
                            precoNotOk = False
                            dotCounter = 0
                            novoPreco = input('Digite o novo preço do produto:')
                            for char in novoPreco:
                                if(char not in '0123456789.'):
                                    precoNotOk = True
                                    break
                                if(char == '.'):
                                    dotCounter += 1
                            if(dotCounter > 1):
                                precoNotOk = True
                        carnePreco[int(novaEntrada)] = float(novoPreco)
                        print('Valor atualizado: Nome: ' + carneProdutos[int(novaEntrada)] + ', Preço: R$ ' + str(carnePreco[int(novaEntrada)]))
                    else:
                        ##____Alimento Legume____##
                        listIndexString = ''
                        for i in range(len(legumeProdutos)):
                            print(str(i) + ' - Nome: ' + legumeProdutos[i] + ', Preço: R$ ' + str(legumePreco[i]))
                            listIndexString += str(i)
                        novaEntrada = 'x'
                        print(listIndexString)
                        while(novaEntrada not in listIndexString):
                            novaEntrada = input('Digite qual produto deseja alterar o preço: ')
                        print('Produto selecionado: ' + legumeProdutos[int(novaEntrada)])
                        novoPreco = 'x'
                        precoNotOk = True
                        while(precoNotOk):
                            precoNotOk = False
                            dotCounter = 0
                            novoPreco = input('Digite o novo preço do produto:')
                            for char in novoPreco:
                                if(char not in '0123456789.'):
                                    precoNotOk = True
                                    break
                                if(char == '.'):
                                    dotCounter += 1
                            if(dotCounter > 1):
                                precoNotOk = True
                        legumePreco[int(novaEntrada)] = float(novoPreco)
                        print('Valor atualizado: Nome: ' + legumeProdutos[int(novaEntrada)] + ', Preço: R$ ' + str(legumePreco[int(novaEntrada)]))           
            elif(option == '3'):
                enterOp = 'x'
                print('\nCategorias:',
                      '\n' + produtosCat[0],
                      '\nSubcategorias:',
                      '\n\t1 - ' + subHiegene[0],
                      '\n\t2 - ' + subHiegene[1],
                      '\n' + produtosCat[1],
                      '\nSubcategorias:',
                      '\n\t3 - ' + subAlimento[0],
                      '\n\t4 - ' + subAlimento[1])
                while(enterOp not in '1234' or len(enterOp) != 1):
                        enterOp = input('Digite em qual catergoria deseja entrar: ')
                novoNome = ''
                while(len(novoNome) <= 3):
                    novoNome = input('Digite o nome do novo produto: ')
                novoCod = ''
                codNotOk = True
                while(codNotOk):
                    codNotOk = False
                    novoCod = input('Digite o código do novo produto:')
                    for char in novoCod:
                        if(char not in '0123456789'):
                            codNotOk = True
                            break
                        if(len(novoCod) <= 2):
                            codNotOk = True
                novoPrice = 'x'
                priceNotOk = True
                while(priceNotOk):
                    priceNotOk = False
                    dotCounter = 0
                    novoPrice = input('Digite o preço do novo produto:')
                    for char in novoPrice:
                        if(char not in '0123456789.'):
                            priceNotOk = True
                            break
                        if(char == '.'):
                            dotCounter += 1
                    if(dotCounter > 1):
                        priceNotOk = True

                if(enterOp == '1'):
                    pessoalProdutos.append(novoNome)
                    pessoalCod.append(novoCod)
                    pessoalPreco.append(float(novoPrice))
                elif(enterOp == '2'):
                    carroProdutos.append(novoNome)
                    carroCod.append(novoCod)
                    carroPreco.append(float(novoPrice))
                elif(enterOp == '3'):
                    carneProdutos.append(novoNome)
                    carneCod.append(novoCod)
                    carnePreco.append(float(novoPrice))
                else:
                    legumeProdutos.append(novoNome)
                    legumeCod.append(novoCod)
                    legumePreco.append(float(novoPrice))     

            elif(option == '0'):
                print('Até logo!.')
                
                break #Sai do menu
    else:
        ##____Area do cliente____##
        while(True):
            option = 'x'
            print('\nDigite qual ação deseja realizar:',
                  '\n1 - Adicionar produto ao carrinho',
                  '\n2 - Remover produto do carrinho',
                  '\n3 - Finalizar compra',
                  '\n0 - Sair')
            while(option not in '1230' or len(option) != 1):
                option = input('Digite o número da opção: ')

            if(option == '1'):
                ##____Adicionar Produto ao Carrinho____##
                enterOp = 'x'
                print('\nCategorias:',
                      '\n1 - ' + produtosCat[0],
                      '\n2 - ' + produtosCat[1])
                while(enterOp not in '12' or len(enterOp) != 1):
                        enterOp = input('Digite em qual catergoria deseja entrar: ')
                if(enterOp == '1'):
                    enterOp = 'x'
                    print('\nSubcategorias:',
                          '\n1 - ' + subHiegene[0],
                          '\n2 - ' + subHiegene[1])
                    while(enterOp not in '12' or len(enterOp) != 1):
                        enterOp = input('Digite em qual subcatergoria deseja entrar: ')
                    selected = 'x'
                    indexString = ''
                    if(enterOp == '1'):
                        for i in range(len(pessoalProdutos)):
                            indexString += str(i)
                            print(str(i) +' - Nome do produto: ' + pessoalProdutos[i],', Preço: R$ ' + str(pessoalPreco[i]))
                        while(selected not in indexString):
                            selected = input('Digite qual produto deseja adicionar ao carrinho: ')
                        carrinho.append(pessoalProdutos[int(selected)])
                        preco.append(pessoalPreco[int(selected)])
                    else:
                        for i in range(len(carroProdutos)):
                            indexString += str(i)
                            print(str(i) +' - Nome do produto: ' + carroProdutos[i],', Preço: R$ ' + str(carroPreco[i]))
                        while(selected not in indexString):
                            selected = input('Digite qual produto deseja adicionar ao carrinho: ')
                        carrinho.append(carroProdutos[int(selected)])
                        preco.append(carroPreco[int(selected)])
                else:
                    enterOp = 'x'
                    print('\nSubcategorias:',
                          '\n1 - ' + subAlimento[0],
                          '\n2 - ' + subAlimento[1])
                    while(enterOp not in '12' or len(enterOp) != 1):
                        enterOp = input('Digite em qual subcatergoria deseja entrar: ')
                    selected = 'x'
                    indexString = ''
                    if(enterOp == '1'):
                        for i in range(len(carneProdutos)):
                            indexString += str(i)
                            print(str(i) +' - Nome do produto: ' + carneProdutos[i],', Preço: R$ ' + str(carnePreco[i]))
                        while(selected not in indexString):
                            selected = input('Digite qual produto deseja adicionar ao carrinho: ')
                        carrinho.append(carneProdutos[int(selected)])
                        preco.append(carnePreco[int(selected)])
                    else:
                        for i in range(len(legumeProdutos)):
                            indexString += str(i)
                            print(str(i) +' - Nome do produto: ' + legumeProdutos[i],', Preço: R$ ' + str(legumePreco[i]))
                        while(selected not in indexString):
                            selected = input('Digite qual produto deseja adicionar ao carrinho: ')
                        carrinho.append(legumeProdutos[int(selected)])
                        preco.append(legumePreco[int(selected)])

            elif(option == '2'):
                ##____Remover Produto do Carrinho____##
                if(len(carrinho) == 0):
                    print('\nAdicione produtos ao carrinho primeiro!')
                    continue
                print('\nLista de produtos:')
                indexNew = ''
                toRemove = 'x'
                for i in range(len(carrinho)):
                    indexNew += str(i)
                    print(str(i),'- Nome do produto: ' + carrinho[i],', Preço: R$ ' + str(preco[i]))
                while(toRemove not in indexNew):
                    toRemove = input('Digite qual produto deseja remover do carrinho: ')
                print('\n'+ 'Produto removido:', carrinho[int(toRemove)])
                del(carrinho[int(toRemove)])
                del(preco[int(toRemove)])

            elif(option == '3'):
                while(True):

                    total = sum(preco)
                    impostoMun = total * 0.05
                    impostoEst = total * 0.08
                    impostoNac = total * 0.12
                    totalComImposto = total + impostoMun + impostoEst + impostoNac
                    print('\nProdutos no carrinho: ')
                    for i in range(len(carrinho)):
                        print(str(i),'- Nome do produto: ' + carrinho[i],', Preço: R$ ' + str(preco[i]))

                    print('\nNome do Cliente: ' + nome, 'CPF: ' + cpf)
                    print('\nValor Total com impostos a pagar: R$ ' + str(totalComImposto) + ', Total dos produtos: R$ ' + str(total) + ', Com impostos: R$ ' + str(impostoMun) +
                           '(Municipal), R$ ' + str(impostoEst) + '(Estadual), R$ ' + str(impostoNac) + '(Nacional)')
                    print('\nQual a forma de pagamento:',
                          '\n1 - Dinheiro',
                          '\n2 - Cartão',
                          '\n3 - Pix')
                    metodo = 'x'
                    while(metodo not in '123' or len(metodo) != 1):
                        metodo = input('Digite a forma de pagamento: ')

                    if(metodo == '1'):
                        ##____Validação dinheiro____##
                        cash = 'x'
                        cashNotOk = True
                        while(cashNotOk):
                            cashNotOk = False
                            dotCounter = 0
                            cash = input('Quanto você tem em dinheiro?')
                            for char in cash:
                                if(char not in '0123456789.'):
                                    cashNotOk = True
                                    break
                                if(char == '.'):
                                    dotCounter += 1
                            if(dotCounter > 1):
                                cashNotOk = True

                        if(float(cash) < totalComImposto):
                            print('Quantidade insuficiente!')
                            continue
                        else:
                            print('Compra realizada!')
                            while(len(carrinho) != 0):
                                del(carrinho[-1])
                                del(preco[-1])
                            if(float(cash) > totalComImposto):
                                print('Troco:', float(cash) - totalComImposto)
                                break
                            
                    elif(metodo == '2'):
                        ##____Validação Cartão____##
                        print('\nQual a tipo do cartão:',
                          '\n1 - Crédito',
                          '\n2 - Débito',
                          '\n3 - Voucher')
                        metodo = 'x'
                        while(metodo not in '123' or len(metodo) != 1):
                            metodo = input('Digite o tipo: ')
                        saldo = 'x'
                        saldoNotOk = True
                        while(saldoNotOk):
                            saldoNotOk = False
                            dotCounter = 0
                            saldo = input('Qual seu saldo?')
                            for char in saldo:
                                if(char not in '0123456789.'):
                                    saldoNotOk = True
                                    break
                                if(char == '.'):
                                    dotCounter += 1
                            if(dotCounter > 1):
                                saldoNotOk = True

                        if(float(saldo) < totalComImposto):
                            print('Saldo insuficiente!')
                            continue
                        else:
                            print('Compra realizada com sucesso!')
                            while(len(carrinho) != 0):
                                del(carrinho[-1])
                                del(preco[-1])
                            break
                    elif(metodo == '3'):
                        ##____Validação Pix____##
                        saldo = 'x'
                        saldoNotOk = True
                        while(saldoNotOk):
                            saldoNotOk = False
                            dotCounter = 0
                            saldo = input('Qual seu saldo?')
                            for char in saldo:
                                if(char not in '0123456789.'):
                                    saldoNotOk = True
                                    break
                                if(char == '.'):
                                    dotCounter += 1
                            if(dotCounter > 1):
                                saldoNotOk = True

                        if(float(saldo) < totalComImposto):
                            print('Saldo insuficiente!')
                        else:
                            print('Compra realizada com sucesso!')
                            while(len(carrinho) != 0):
                                del(carrinho[-1])
                                del(preco[-1])
                            break
            else:
                break