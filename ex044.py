print('\033[1;34m-=-\033[m'*20)
print('Miradão Story')
print('\033[1;34m-=-\033[m'*20)

valor = float(input('Preço das compras: '))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão\n''')

num = int(input('Qual é a opção? '))

if num == 1:
    s = valor - valor*(10/100)
elif num == 2:
    s = valor - valor*(5/100)
elif num == 3:
    s = valor
    parcela = valor/2
    print('Sua compra será parcelada em 2x de RS{} SEM JUROS'.format(parcela))
elif num == 4:
    parcela = int(input('Em quantas vezes? '))
    s = valor + valor*(20/100)
    print('Você irá parcelar em {}x de R${} COM JUROS'.format(parcela, s/parcela))
else:
    s = valor
    print('Opção inválida de Pagamento. tente novamente!')

print('Sua compra de R${} irá custar R${} no final'.format(valor, s))

