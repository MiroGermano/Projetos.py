#city = str(input('Digite o nome de uma cidade: ')).strip()
#valor = city.split()
#s = valor[0]
#lista = ['santo', 'Santo']

#if s in lista:
    #print('Está cidade começa com "Santo"')
#else:
    #print('Está cidade não começa com "Santo"')

city = str(input('Em qual cidade você nasceu? ')).strip()
print(city[:5].upper() == 'SANTO')
