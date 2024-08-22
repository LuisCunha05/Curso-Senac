def hip(sideA: float, sideB: float) -> float:
    return (sideA * sideA + sideB * sideB)** 0.5

a = float(input('Digite o lado A: '))
b = float(input('Digite o lado B: '))

print(f'Hipotenusa de {a:5.2f} e {b:5.2f} = {hip(a, b):5.2f}')