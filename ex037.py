num = int(input('Digite um número inteiro: '))
print("""Escolha uma das bases para conversão: 
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL """)

opçao = int(input('Sua opção: '))

if opçao == 1:
    print(f'{num} convertido para Binário é igual a {bin(num)[2:]}')
elif opçao == 2:
    print(f'{num} convertido para Octal é igual a {oct(num)[2:]} ')
elif opçao == 3:
    print(f'{num} convertido para Hexadecimal é igual a {hex(num)[2:]}')
else:
    print('Digite uma opção válida')

