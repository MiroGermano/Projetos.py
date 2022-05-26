# calculando IMC

peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))

imc = peso / altura**2

if imc < 18.5:
    print('seu IMC deu \033[1;32m{:.2f}\033[m, Você está abaixo do peso! '.format(imc))
elif 18.5 <= imc < 25:
    print('seu IMC deu \033[1;33m{:.2f}\033[m, Você está com o peso ideal! '.format(imc))
elif 25 <= imc < 30:
    print('seu IMC deu \033[1;34m{:.2f}\033[m, Você está com sobrepeso!'.format(imc))
elif 30 <= imc < 40:
    print('seu IMC deu \033[1;31m{:.2f}\033[m, Você está obeso!'.format(imc))
else:
    print('seu IMC deu \033[1;31m{:.2f}\033[m, Você está com obesidade móbida! '.format(imc))