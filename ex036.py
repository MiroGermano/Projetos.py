casa = float(input('Qual o valor da casa que deseja comprar ? '))
salario = float(input('Qual é o seu salário? '))
anos = float(input('Em quantos anos pretende pagar? '))

s = salario * 30/100
prestação = (casa/anos)/12

if prestação > s:
    print('\n\033[31mEmpréstimo negado!!\033[m A prestação R${:.2f} seria maior que 30% do seu salário'.format(prestação))
elif prestação < s:
    print('\n\033[32mEmpréstimo aceito,\033[m o senhor(a) irá pagar R${} mensais durante {} anos '.format(prestação, anos))


