n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
s = (n1+n2)/2
print('\nsua média é {}!'.format(s), end=' ')
if s >= 7:
    print('\033[32mParabéns você foi aprovado!')
else:
    print('\033[31mVocê REPROVOU!')

