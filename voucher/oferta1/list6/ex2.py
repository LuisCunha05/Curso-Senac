children: dict[str,list[float]] = {'Cadu':[9.55, 8.55, 7.55, 9.55],
                                   'Requis':[9.556, 8.556, 7.556, 9.556],
                                   'Isas':[9.557, 8.557, 7.557, 9.557],
                                   'João':[9.558, 8.558, 7.558, 9.558],
                                   'Luis N.':[9.554, 8.554, 7.554, 9.554]
                                  }

def media(notas: float):
    """Retorna a média dos valores de uma lista"""
    return round(sum(notas)/len(notas), 2)

for key in children.keys():
    print(f'Aluno: {key:7}; Média: {media(children[key])}')

