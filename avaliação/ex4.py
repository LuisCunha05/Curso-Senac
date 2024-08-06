num = []

for i in range(10):
    num.append(int(input(f'Digite o valor do elemento {i + 1}: ')))

print(num)

num = [i for i in num if i != 8]

print(num)