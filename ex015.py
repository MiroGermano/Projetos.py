km = float(input('Quantos km foram pecorridos? '))
days = float(input('Quantidade de dias que ele foi alugado: '))
s = days*60 + km*0.15
print('Total que irá pagar pelo aluguel: R${:.2f}'.format(s))
