def menor(a: float, b: float, c: float) -> float:
    return sorted([a, b, c])[0]

def maior(a, b, c):
    return sorted([a, b, c])[2]

a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))

print(f'{a}, {b} e {c}:\nMaior: {maior(a, b, c)}\nMenor: {menor(a, b, c)}')