nome = str(input('Digite o seu nome completo: ')).strip()
#transforma todas as letras em maiúsculas:

print('O seu nome em maiúsculas é {} '.format(nome.upper()))

#transforma todas as letras em minúsculas:

print('O seu nome em maiúsculas é {} '.format(nome.lower()))

#mostra quantas letras tem ao todo (sem considerar os espaços)

print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

#mostra quantas letras tem o primeiro nome:
firstname = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(firstname[0], len(firstname[0])))