def celsiusToFahrenheit(cel: float) -> float:
    return 1.8 * cel + 32

try:
    temp = float(input('Digite a temperatura em celsius: '))
except ValueError:
    print('Temperatura precisa ser um número!')

print(f'{temp} °C equivale a {celsiusToFahrenheit(temp)} °F')