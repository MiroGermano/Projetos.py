from random import choice
from time import sleep
color = {
    'blue': '\033[34m',
    'red': '\033[31m',
    'clean': '\033[m',
    'verde': '\033[32m',
    'amarelo': '\033[33m'}

print('{}-={}'.format(color['amarelo'], color['clean'])*20)
print('JOKENPÔ BY MIRADÃO')
print('{}-={}'.format(color['amarelo'], color['clean'])*20)

pc = choice(['pedra', 'papel', 'tesoura'])
jogador = str(input('Pedra, papel ou tesoura? ')).strip()

print('\n\033[33mJO', end='')
sleep(0.5)
print('O', end='')
sleep(0.5)
print('O', end='')
sleep(0.5)
print('KEN', end='')
sleep(0.5)
print('PÔOOOOOO\033[m')

if pc == jogador:
    print('Os dois colocaram {}. JOGUE NOVAMENTE!'.format(jogador))

elif pc == 'pedra' and jogador == 'tesoura':
    print('\033[1;31mVocê perdeu, tome uma dose!!!!')
elif pc == 'tesoura' and jogador == 'pedra':
    print('\033[1;32mVocê ganhou!!')

elif pc == 'papel' and jogador == 'tesoura':
    print('\033[1;32mVocê ganhou!!')
elif pc == 'tesoura' and jogador == 'papel':
    print('\033[1;31mVocê perdeu, tome uma dose!!')

elif pc == 'papel' and jogador == 'pedra':
    print('\033[1;31mVocê perdeu, tome uma dose!!!!')
elif pc == 'pedra' and jogador == 'papel':
    print('\033[1;32mVocê ganhou!!')

print('{}O computador jogou {} e você {}{}'.format(color['blue'], pc, jogador, color['clean']))

