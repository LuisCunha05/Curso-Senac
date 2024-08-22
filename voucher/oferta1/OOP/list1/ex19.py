
def evalueteInvest(cash: float, jur: float, per: int) -> float:
    for _ in range(per):
        cash *= 1 + jur
    return cash


try:
    money = float(input('Digite o montante inicial: '))
    juros = float(input('Digite o juros: '))
    anos = int(input('Digite a quantidade de anos do rendimento: '))
    if(anos <= 0 or money <= 0 or juros <= 0):
        raise ValueError
except ValueError:
    print('Valor precisa ser um número positivo!')

print(f'Investimento de {money} com juros de {juros} por {anos} anos, resulta em: {evalueteInvest(money, juros, anos):6.2f}')