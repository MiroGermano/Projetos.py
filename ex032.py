#faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date
from time import sleep
ano = int(input('Que ano quer analisar? coloque 0 para analisar o ano atual:  '))
print('\033[34mAnalisando {}\033[m'.format(ano), end=' ')
sleep(0.5)
print('.', end=' ')
sleep(0.5)
print('.', end=' ')
sleep(0.5)
print('.')
sleep(0.5)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print('{} é um no bissexto.'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))
