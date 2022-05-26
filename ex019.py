from random import choice
nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')
print('{} irá comer um traveco'.format(choice([nome1, nome2, nome3, nome4])))