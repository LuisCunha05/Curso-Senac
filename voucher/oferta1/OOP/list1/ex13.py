def isPalindromo(word: str) -> bool:
    for i in range(len(word)//2):
        if(new[i].upper() != new[-(i + 1)].upper()):
            return False
    return True

entrada = input('Digite uma palavra ou frase: ')

new = ''.join(entrada.split(' '))

print(f'{'É' if isPalindromo(new) else 'Não é'} palíndromo!')
