word = ''
word = input('Digite uma palavra: ')

for letter in word:
    if letter.upper() in ['A', 'E', 'I', 'O', 'U']:
        print(letter, end=' ')

