from random import randint
from time import sleep
valor = randint(0, 5)
print('-='*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-='*20)

uservalor = int(input('Em que número eu pensei? '))
print('PROCESSANDO', end=' ')
sleep(0.5)
print('.', end=' ')
sleep(0.5)
print('.', end=' ')
sleep(0.5)
print('.', end=' ')
sleep(0.5)

if valor == uservalor:
    print('Parabéns! O computador escolheu {} também. '.format(valor))
else:
    print('Você perdeu! Você escolheu {} e o computador {}.'.format(uservalor, valor))


