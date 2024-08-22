from random import random as rng

escolha = ''

while(not(escolha == '1' or escolha == '0')):
    escolha = input('Digite 1 ou 0: ')

num = int(escolha) + round(10 * rng())

print(f'Seu número é {num}, esse número é {'Par' if not(num & 1) else 'Ímpar'}')
