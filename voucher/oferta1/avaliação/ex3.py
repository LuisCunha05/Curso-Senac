n = [-1, -1, -1]

for i in range(3):
    while(n[i] < 0 or n[i] > 10):
        n[i] = float(input(f'N{i}: '))

N = 3
X = 4
sum = 0

for i in range(N):
    sum += 1 / (n[i] + X)

mediaAmortizada = N / (sum) - X

if(mediaAmortizada >= 5):
    print(f'Você passou, sua média é {mediaAmortizada:.1f}')
else:
    print(f'Você não passou, sua média é {mediaAmortizada:.1f}')
