salario = float(input('Digite seu sálario para calcularmos o valor do seu aumento: '))

if salario > 1250:
    s1 = (salario * 10)/100
    print('Seu novo salário com o acréscimo de 10% é RS{}.'.format(s1 + salario))

else:
    s2 = (salario * 15) / 100
    print('Seu novo salário com o acréscimo de 15% é RS{}.'.format(s2 + salario))
