
valor = int(input('Digite um número inteiro para saber se é par ou impar: '))
s = valor % 2
if s == 0:
    print('{} é par'.format(valor))
else:
    print('{} é impar'.format(valor))