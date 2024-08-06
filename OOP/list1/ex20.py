def firstVerifier(num: str) -> int:
    new = [int(num[i]) * (10 - i) for i in range(9)]
    return sum(new)

def secondVerifier(num: str) -> int:
    new = [int(num[i]) * (11 - i) for i in range(9)]
    new.append(firstVerifier(num))
    return sum(new)

def isCpfValid(cpf: str) -> bool:
    first = firstVerifier(cpf)
    second = secondVerifier(cpf)
    #First test
    if(first % 11 < 2 and not(cpf[-2] == '0')):
        return False
    else:
        if(not(cpf[-2] == str(11 - (first % 11)))):
            return False
    #Second test
    if(second % 11 < 2 and not(cpf[-2] == 0)):
        return False
    else:
        if(not(cpf[-1] == str(11 - (second % 11)))):
            return False
    return True




cpf = ''
while(not cpf.isdecimal()):
    cpf = input('Digite seu CPF, somente os números: ')

print(isCpfValid(cpf))