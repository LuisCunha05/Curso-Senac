def digitSum(number: str) -> int:
    return sum(int(num) for num in number)

entrada = ''

while(not entrada.isdecimal()):
    entrada = input('Digite um número inteiro: ')

print(f'A soma dos digitos de {entrada} é: {digitSum(entrada)}')