#somando dois números
print('\033[33m-=-'*13, '\033[m')
print('\033[1;33;107mPrograma que soma dois números...', '\033[m')
print('\033[33m-=-'*13, '\033[m')
color = {
    'azul': '\033[1;34m',
    'limpar': '\033[m',
    'amarelo': '\033[1;33m'}
v1 = float(input('Primeiro valor: '))
v2 = float(input('segundo valor: '))
s = v1+v2
print('A soma de {}{}{}'.format(color['azul'], v1, color['limpar']), end=' ')
print('mais {}{}{}'.format(color['azul'], v2, color['limpar']), end=' ')
print('é igual a {}{}{}!!'.format(color['amarelo'], s, color['limpar']))
