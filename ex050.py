soma = 0
cont = 0
for c in range(1, 7):
    valor = int(input('Digite o {}° número: '.format(c)))
    if valor % 2 == 0:
        soma += valor
        cont += 1
print(f'Você informou {cont} números e a soma foi {soma}.')

