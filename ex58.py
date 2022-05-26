from random import randint
from time import sleep
s = 1
conter = 0
while s != 0:
    valor = randint(0, 10)
    print()
    print('-=' * 20)
    print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
    print('-=' * 20)

    number = int(input('\nQual número eu escolhi?  '))

    print('PROCESSANDO', end=' ')
    sleep(0.5)
    print('.', end=' ')
    sleep(0.5)
    print('.', end=' ')
    sleep(0.5)
    print('.', end=' ')
    sleep(0.5)

    conter += 1

    if valor != number:
        print(f'\nVocê errou, eu escolhi {valor} e você {number}')
    else:
        s = 0
print(f'\nVocê acertou, eu escolhi {valor} e você {number}')
print(f'Você precisou de {conter} tentativas')