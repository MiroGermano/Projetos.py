#print('\033[1;33;40m-=\033[m'*20)
color = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m'}

print('{}-='.format(color['amarelo'])*20)
print('Analisador de triângulos')
print('-='*20)
a = float(input('\033[mDigite um valor de reta: '))
b = float(input('Digite outro valor de reta: '))
c = float(input('Digite outro valor de reta: '))

if a < b + c and b < a + c and c < b + a:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÂO PODEM FORMAR triângulo!')