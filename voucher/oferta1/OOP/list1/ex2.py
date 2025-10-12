def isTriangle(a: float, b: float, c: float) -> bool:
    nums = sorted([a, b, c])
    return nums[0] + nums[1] > nums[2]

a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))
print(isTriangle(a, b, c))
print(f'{a}, {b} e {c} é um triângulo: {'Sim' if isTriangle(a, b, c) else 'Não'}')