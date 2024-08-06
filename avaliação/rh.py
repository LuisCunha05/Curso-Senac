cargo = nome_completo = email = curso = ''
mensagemP = 'Parabéns você passou para a próxima fase!!'
mensagemN = 'Obrigado pela sua participação!!'
idade = 0
nota = 0.

cargos = ['ti', 'médico', 'administrador']

cursosV = {
    'ti':['engenharia de software', 'ciência da computação'],
    'médico':['medicina', 'enfermagem'],
    'administrador':['administração']
    }

print('Bem vindo ao processo seletivo automatizado!\nPor favor insira os seguintes dados:')

while(len(nome_completo) <= 5):
    nome_completo = input('Nome completo: ')
while(not('@' in email)):
    email = input('Email: ')
while(not(cargo.lower() in cargos)):
    print('Escolha um cargo para se candidatar: TI, Médico ou Administrador')
    cargo = input('Cargo: ')

print('Primeira fase: ')
while(idade <= 0):
    idade = int(input('Idade: '))
if(idade < 18):
    print(f'Email recebido em {email}: {mensagemN}')
    quit()
else:
    print(f'Email recebido em {email}: {mensagemP}')

print('Segunda fase: ')
while(len(curso) <= 4):
    curso = input('Curso: ')
if(curso.lower() in cursosV[cargo.lower()]):
    print(f'Email recebido em {email}: {mensagemP}')
else:
    print(f'Email recebido em {email}: {mensagemN}')
    quit()

print('Terceira fase: ')
acertou = 0

print('Teste de conhecimentos: ')
resposta = int(input(f'1:Quem é maior, -4 ou -7?\nResporta: '))
if(resposta == -4):
    acertou += 10
    print('yo')
resposta = input('Qual o planeta mais quente o sistema solar?\nResporta: ')
if(resposta.lower() == 'vênus'):
    acertou += 10
    print('yo')
resposta = float(input('Quantos o volume em litros de 1 mol de Hidrogênio nas CNTP: '))
if(resposta == 22.4):
    acertou += 10
    print('yo')
resposta = input('Qual nome do pigmento verde das plantas?\nResporta: ')
if(resposta.lower() == 'clorofila'):
    acertou += 10
    print('yo')

if(acertou / 4 >= 7.):
    print(f'Email recebido em {email}: {mensagemP}')
else:
    print(f'Email recebido em {email}: {mensagemN}')
    quit()




