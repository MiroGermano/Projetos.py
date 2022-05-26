nome = str(input('Digite seu nome: ')).strip()

lista = nome.split()

print(nome)
print('primeiro: {} '.format(lista[0]))
print('último: {}'.format(lista[-1]))
