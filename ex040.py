nota1 = float(input('Qual é a sua primeira nota? '))
nota2 = float(input('Qual é a sua segunda nota? '))

s = (nota1 + nota2)/2

if s <= 0:
    print('Valor invalido, digite números positivos')
elif s < 5:
    print(f'Sua nota foi {s:.2f}, você está \033[1;31mREPROVADO!!!')
elif s >= 7:
    print(f'Sua nota foi {s:.2f}, Parabéns pela \033[1;32mAPROVAÇÃO!!!')
else:
    print(f'sua nota foi {s:.2f}, Você está na \033[1;35mRECUPERAÇÃO!')