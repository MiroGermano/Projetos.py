from math import hypot, trunc
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
s = hypot(co, ca)
s1 = trunc(s)
print('A hipotenusa é igual a {}'.format(s1))
