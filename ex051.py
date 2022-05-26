print('='*30)
print('10 termos de uma P.A')
print('='*30)
i = int(input('Digite o valor inicial da P.A.: '))
r = int(input('Digite a razão: '))
d = i + (10-1) * r
for c in range(i, d + r, r):
    print(f'{c}', end='->')
print('acabou')
