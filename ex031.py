km = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(km))
preço = km * 0.50 if km <= 200 else km * 0.45
print('O preço da sua passagem será de R${}'.foramt(preço))