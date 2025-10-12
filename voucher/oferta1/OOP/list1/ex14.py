def vogaisCount(word: str) -> int:
    count = 0
    
    for char in word:
        if(char.upper() in 'AEIOU'):
            count += 1
    return count

entrada = input('Digite uma palavra ou frase: ')

print(f'A frase:\n"{entrada}"\nContém {vogaisCount(entrada)} vogais!')